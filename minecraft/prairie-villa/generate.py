#!/usr/bin/env python3
"""Prairie villa for Minecraft Bedrock: one voxel model -> plans, facades, BOM, commands.

Coordinates: origin (0,0,0) = NW corner of the foundation at floor level.
X grows east, Z grows south, Y grows up. Run: python3 generate.py
Writes BLUEPRINT.md and prairie_villa.mcfunction next to this file and
fails loudly if any self-check does not pass.
"""
import math
import os
from collections import defaultdict, deque

HERE = os.path.dirname(os.path.abspath(__file__))

LX = range(-3, 20)   # lot 23 x 23
LZ = range(-3, 20)
LY = range(-1, 13)   # foundation .. chimney cap

# ---------------------------------------------------------------- palette
# key -> (bedrock id, block states for commands, 2-char code, legend)
DIRS = {"^": 3, "v": 2, ">": 0, "<": 1}   # weirdo_direction: side the stair rises to
P = {
    "grass": ("grass_block", "", "Gr", "трава (участок)"),
    "andesite": ("polished_andesite", "", "An", "полированный андезит"),
    "smooth_stone": ("smooth_stone", "", "Ss", "гладкий камень"),
    "tuff": ("polished_tuff", "", "Tu", "полированный туф (полосы)"),
    "calcite": ("calcite", "", "Ca", "кальцит (пилоны, труба)"),
    "sandstone": ("smooth_sandstone", "", "Sa", "гладкий песчаник (цоколь, пояс)"),
    "diorite": ("polished_diorite", "", "Di", "полированный диорит (кашпо)"),
    "brick": ("brick_block", "", "Br", "кирпич"),
    "mud": ("mud_bricks", "", "Mu", "кирпич из грязи"),
    "glass": ("gray_stained_glass_pane", "", "Gl", "серая стеклянная панель"),
    "lintel": ("dark_oak_trapdoor", '["upside_down_bit"=true,"open_bit"=false]', "Td",
               "люк тёмного дуба, верхний, закрыт (рама-перемычка)"),
    "door_l": ("dark_oak_door", None, "Dr", "дверь тёмного дуба (низ)"),
    "door_u": ("dark_oak_door", None, "Dr", "дверь тёмного дуба (верх)"),
    "planks": ("spruce_planks", "", "Sp", "еловые доски"),
    "log_x": ("stripped_spruce_log", '["pillar_axis"="x"]', "L-", "обтёсанное еловое бревно, ось X"),
    "log_z": ("stripped_spruce_log", '["pillar_axis"="z"]', "L|", "обтёсанное еловое бревно, ось Z"),
    "froglight": ("ochre_froglight", "", "Fr", "охровая жаболампа"),
    "lantern_h": ("lantern", '["hanging"=true]', "Ln", "фонарь подвесной"),
    "lantern": ("lantern", '["hanging"=false]', "ln", "фонарь стоячий"),
    "tiles": ("deepslate_tiles", "", "Dt", "глубинносланцевая плитка (полный блок)"),
    "tslab": ("deepslate_tile_slab", '["minecraft:vertical_half"="bottom"]', "Ds",
              "плиточный слэб, нижний"),
    "sslab_b": ("spruce_slab", '["minecraft:vertical_half"="bottom"]', "wb", "еловый слэб, нижний"),
    "sslab_t": ("spruce_slab", '["minecraft:vertical_half"="top"]', "wt", "еловый слэб, верхний"),
    "stslab": ("smooth_stone_slab", '["minecraft:vertical_half"="bottom"]', "Sb",
               "слэб гладкого камня (ступень)"),
    "fence": ("dark_oak_fence", "", "Fe", "забор тёмного дуба (перила)"),
    "moss": ("moss_block", "", "Mo", "блок мха"),
    "az": ("azalea_leaves", '["persistent_bit"=true]', "Az", "листва азалии"),
    "azf": ("azalea_leaves_flowered", '["persistent_bit"=true]', "Af", "цветущая листва азалии"),
    "oak": ("oak_log", '["pillar_axis"="y"]', "Lo", "дубовое бревно (ствол)"),
    "campfire": ("campfire", "", "Cf", "костёр (огонь камина)"),
    "cauldron": ("cauldron", "", "Ku", "котёл (ванна, раковина)"),
    "smoker": ("smoker", "", "Sm", "коптильня (плита)"),
    "barrel": ("barrel", "", "Ba", "бочка (шкаф, тумба)"),
    "bookshelf": ("bookshelf", "", "Bk", "книжная полка"),
    "hopper": ("hopper", "", "Ho", "воронка (унитаз)"),
    "bed_h": ("bed", None, "Bd", "кровать (изголовье)"),
    "bed_f": ("bed", None, "Bd", "кровать (изножье)"),
}
for a, d in DIRS.items():
    P["tst" + a] = ("deepslate_tile_stairs",
                    '["weirdo_direction"=%d,"upside_down_bit"=false]' % d, "R" + a,
                    "плиточная ступень, подъём на %s" % {"^": "север", "v": "юг", ">": "восток", "<": "запад"}[a])
    P["sst" + a] = ("spruce_stairs",
                    '["weirdo_direction"=%d,"upside_down_bit"=false]' % d, "C" + a,
                    "еловая ступень, спинка/подъём на %s" % {"^": "север", "v": "юг", ">": "восток", "<": "запад"}[a])
MANUAL = {"door_l", "door_u", "bed_h", "bed_f"}   # placed by hand, not by command

PHASES = [
    "0. Подготовка участка", "1. Фундамент (Y=-1)", "2. Полы и террасы (Y=0)",
    "3. Стены 1-го этажа", "4. Перекрытие и нижние свесы (Y=4)", "5. Стены 2-го этажа и балкон",
    "6. Потолок 2-го этажа и верхние свесы (Y=8)", "7. Окна и рамы", "8. Нижняя крыша (Y=5..6)",
    "9. Верхняя крыша (Y=9..10)", "10. Каминная труба", "11. Интерьер и свет", "12. Ландшафт",
]

M = {}          # (x,y,z) -> key
PH = {}         # (x,y,z) -> phase index
TREE = set()    # tree cells (hidden on facades)


def put(x, y, z, key, ph):
    assert key in P, key
    M[(x, y, z)] = key
    PH[(x, y, z)] = ph


def clear(x, y, z):
    M.pop((x, y, z), None)
    PH.pop((x, y, z), None)


def rect(x0, x1, z0, z1):
    return {(x, z) for x in range(x0, x1 + 1) for z in range(z0, z1 + 1)}


# ---------------------------------------------------------------- volumes
FOOT = rect(0, 14, 0, 14)                       # 15 x 15 base
E1 = rect(0, 9, 0, 14) | rect(10, 14, 0, 9)     # enclosed ground floor (L)
LOGGIA = rect(10, 14, 10, 14)                   # covered terrace under the low roof
U = rect(0, 9, 0, 11)                           # upper storey
BAL = rect(0, 9, 12, 14)                        # balcony on the ground-floor slab
CHIM = rect(-1, 0, 9, 11)                       # chimney 2 x 3
R1 = (-2, 16, -2, 16)                           # low roof rectangle (2-block eave)
R2 = (-2, 11, -2, 13)                           # upper roof rectangle (2-block eave)
TER_S = rect(0, 16, 15, 18)
TER_E = rect(15, 17, 4, 14)


def nb8(c):
    x, z = c
    return [(x + dx, z + dz) for dx in (-1, 0, 1) for dz in (-1, 0, 1) if dx or dz]


def perim(area):
    return {c for c in area if any(n not in area for n in nb8(c))}


E1P = perim(E1)
E1I = E1 - E1P
UP = perim(U)
UI = U - UP


def dist(r, x, z):
    x0, x1, z0, z1 = r
    return min(x - x0, x1 - x, z - z0, z1 - z)


def in_rect(r, x, z):
    return r[0] <= x <= r[1] and r[2] <= z <= r[3]


def edge_dir(r, x, z):
    """Direction a d=1 roof stair rises to (towards the middle of the roof)."""
    x0, x1, z0, z1 = r
    if z - z0 == 1:
        return "v"
    if z1 - z == 1:
        return "^"
    if x - x0 == 1:
        return ">"
    return "<"


def fascia(r, x, z):
    x0, x1, z0, z1 = r
    return "log_x" if z in (z0, z1) else "log_z"


def wall_mat(x, y, z):
    # deterministic ~15% mud bricks scattered through the brick walls
    return "mud" if (x * 11 + y * 7 + z * 3) % 7 == 2 else "brick"


# ---------------------------------------------------------------- 0 site
for x in LX:
    for z in LZ:
        put(x, -1, z, "grass", 0)

# ---------------------------------------------------------------- 1 foundation
for (x, z) in FOOT | TER_S | TER_E:
    put(x, -1, z, "andesite", 1)
for z in range(-3, 0):
    put(3, -1, z, "andesite", 1)                 # front path
TREES = [(18, 0), (-2, 18), (18, 18)]
for tx, tz in TREES:
    for (x, z) in rect(tx - 1, tx + 1, tz - 1, tz + 1):
        put(x, -1, z, "moss", 12)

# ---------------------------------------------------------------- 2 floors, terraces
for (x, z) in E1I:
    put(x, 0, z, "andesite" if x >= 10 else ("tuff" if z in (4, 11) else "smooth_stone"), 2)
for z in (9, 10, 11):
    put(1, 0, z, "calcite", 2)                   # hearth
for (x, z) in LOGGIA:
    put(x, 0, z, "tuff" if z == 12 else "andesite", 2)
for (x, z) in TER_S:
    put(x, 0, z, {15: "andesite", 16: "tuff", 17: "andesite", 18: "calcite"}[z], 2)
for (x, z) in TER_E:
    put(x, 0, z, {15: "andesite", 16: "tuff", 17: "calcite"}[x], 2)
for x in range(6, 11):
    put(x, 0, 19, "stslab", 2)                   # garden steps
put(3, 0, -1, "stslab", 2)                       # front step

# ---------------------------------------------------------------- 3 ground-floor walls
for (x, z) in E1P:
    put(x, 0, z, "sandstone", 3)
    for y in (1, 2, 3):
        put(x, y, z, wall_mat(x, y, z), 3)
GF_PYLONS = [(0, 0), (5, 0), (9, 0), (14, 0), (14, 5), (14, 9), (9, 9), (9, 14),
             (4, 14), (0, 14), (0, 7)]
for (x, z) in GF_PYLONS:
    for y in range(0, 4):
        put(x, y, z, "calcite", 3)
for y in range(0, 5):
    put(14, y, 14, "calcite", 3)                 # free loggia pier

GF_WIN = []   # (x, z, ys)
GF_WIN += [(2, 0, (1, 2, 3)), (4, 0, (1, 2, 3)), (3, 0, (3,))]
GF_WIN += [(x, 0, (2, 3)) for x in range(10, 14)]
GF_WIN += [(0, z, (2, 3)) for z in range(3, 6)]
GF_WIN += [(0, z, (1, 2, 3)) for z in (12, 13)]
GF_WIN += [(x, 14, (1, 2, 3)) for x in (1, 2, 3, 5, 6, 7, 8)]
GF_WIN += [(9, z, (1, 2, 3)) for z in (10, 12)] + [(9, 11, (3,))]
GF_WIN += [(x, 9, (1, 2, 3)) for x in (11, 12)]
GF_WIN += [(14, z, (2, 3)) for z in (2, 3, 4)] + [(14, z, (1, 2, 3)) for z in (6, 7, 8)]
DOORS = [(3, 1, 0), (9, 1, 11), (4, 5, 11), (5, 5, 2), (5, 5, 5), (6, 5, 7)]

for y in range(1, 4):                             # brick partitions
    for x in (1, 2, 3):
        put(x, y, 7, wall_mat(x, y, 7), 3)
    for z in range(1, 7):
        put(9, y, z, wall_mat(9, y, z), 3)

# ---------------------------------------------------------------- 4 slab Y=4 + low eaves
for (x, z) in E1P:
    put(x, 4, z, "sandstone", 4)
for (x, z) in E1I:
    put(x, 4, z, "smooth_stone" if (x, z) in BAL else "planks", 4)
for (x, z) in LOGGIA:
    put(x, 4, z, "planks", 4)
for (x, z) in [(11, 11), (13, 11), (11, 13), (13, 13)]:
    put(x, 4, z, "froglight", 4)
put(14, 4, 14, "calcite", 3)
for x in range(R1[0], R1[1] + 1):
    for z in range(R1[2], R1[3] + 1):
        if (x, z) in FOOT:
            continue
        d = dist(R1, x, z)
        if d == 0:
            put(x, 4, z, fascia(R1, x, z), 4)
        elif d == 1:
            put(x, 4, z, "froglight" if (x + z) % 4 == 0 else "planks", 4)
# stair 1st -> 2nd floor along x=8, rising north
for y, z in [(1, 6), (2, 5), (3, 4), (4, 3)]:
    put(8, y, z, "sst^", 4)
for (y, z) in [(1, 5), (1, 4), (2, 4), (1, 3), (2, 3), (3, 3)]:
    put(8, y, z, "planks", 4)                    # closed stringer under the flight
clear(8, 4, 4)
clear(8, 4, 5)                                   # stairwell opening

# ---------------------------------------------------------------- 5 upper walls, balcony
for (x, z) in UP:
    for y in (5, 6, 7):
        put(x, y, z, wall_mat(x, y, z), 5)
for (x, z) in [(0, 0), (9, 0), (9, 11)]:
    for y in (5, 6, 7):
        put(x, y, z, "calcite", 5)
UF_WIN = []
UF_WIN += [(x, 0, (6, 7)) for x in (1, 2, 3, 7, 8)]
UF_WIN += [(0, z, (6, 7)) for z in (2, 3, 8)] + [(0, z, (7,)) for z in (5, 6)]
UF_WIN += [(x, 11, (5, 6, 7)) for x in (2, 3, 5, 6, 7)] + [(4, 11, (7,))]
UF_WIN += [(9, z, (6, 7)) for z in (2, 3, 5, 8, 9, 10)]
for y in (5, 6, 7):
    for z in range(1, 7):
        put(5, y, z, "planks", 5)
    for x in range(1, 5):
        put(x, y, 4, "planks", 5)
    for x in range(1, 9):
        put(x, y, 7, "planks", 5)
for (x, z) in [(7, 4), (7, 5), (7, 6), (8, 6)]:
    put(x, 5, z, "fence", 5)                     # stairwell guard rail
for (x, z) in BAL & E1P:
    put(x, 5, z, "calcite", 5)                   # solid parapet
for x in (2, 3, 6, 7):
    put(x, 5, 14, "moss", 12)                    # flower boxes in the parapet

# ---------------------------------------------------------------- 6 ceiling Y=8 + upper eaves
for (x, z) in UP:
    put(x, 8, z, "sandstone", 6)
for (x, z) in UI:
    put(x, 8, z, "planks", 6)
for (x, z) in [(2, 2), (7, 2), (2, 5), (7, 5), (3, 9), (6, 9)]:
    put(x, 8, z, "froglight", 11)
for x in range(R2[0], R2[1] + 1):
    for z in range(R2[2], R2[3] + 1):
        d = dist(R2, x, z)
        if d == 0:
            put(x, 8, z, fascia(R2, x, z), 6)
        elif d == 1:
            put(x, 8, z, "froglight" if (x + z) % 4 == 0 else "planks", 6)

# ---------------------------------------------------------------- 7 windows, doors, frames
for (x, z, ys) in GF_WIN + UF_WIN:
    for y in ys:
        put(x, y, z, "glass", 7)
for (x, y, z) in DOORS:
    put(x, y, z, "door_l", 7)
    put(x, y + 1, z, "door_u", 7)


def outward(x, z, area):
    for dx, dz in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if (x + dx, z + dz) not in area:
            return (x + dx, z + dz)
    return None


for (x, z, ys) in GF_WIN:
    if 3 in ys:
        o = outward(x, z, E1)
        put(o[0], 3, o[1], "lintel", 7)
for (x, z, ys) in UF_WIN:
    if 7 in ys:
        o = outward(x, z, U)
        put(o[0], 7, o[1], "lintel", 7)

# ---------------------------------------------------------------- 8 low roof
for x in range(R1[0], R1[1] + 1):
    for z in range(R1[2], R1[3] + 1):
        if (x, z) in U or (x, z) in BAL:
            continue
        d = dist(R1, x, z)
        if d == 0:
            put(x, 5, z, "tslab", 8)
        elif d == 1:
            put(x, 5, z, "tst" + edge_dir(R1, x, z), 8)
        else:
            put(x, 5, z, "tiles", 8)
            put(x, 6, z, "tslab", 8)

# ---------------------------------------------------------------- 9 upper roof
for x in range(R2[0], R2[1] + 1):
    for z in range(R2[2], R2[3] + 1):
        d = dist(R2, x, z)
        if d == 0:
            put(x, 9, z, "tslab", 9)
        elif d == 1:
            put(x, 9, z, "tst" + edge_dir(R2, x, z), 9)
        else:
            put(x, 9, z, "tiles", 9)
            put(x, 10, z, "tslab", 9)

# ---------------------------------------------------------------- 10 chimney
for (x, z) in CHIM:
    for y in range(-1, 12):
        put(x, y, z, "calcite", 10)
    put(x, 12, z, "diorite", 10)
put(0, 1, 10, "campfire", 11)                    # fire box opens into the living room

# ---------------------------------------------------------------- 11 interior
FURN = [
    # ground floor: hall
    ((1, 1, 4), "sst<", "прихожая: скамья"), ((1, 1, 5), "sst<", "прихожая: скамья"),
    ((7, 1, 1), "barrel", "прихожая: шкаф"), ((8, 1, 1), "barrel", "прихожая: шкаф"),
    ((4, 3, 3), "lantern_h", "прихожая: свет"),
    # living
    ((4, 1, 9), "sst>", "гостиная: диван"), ((4, 1, 10), "sst>", "гостиная: диван"),
    ((4, 1, 11), "sst>", "гостиная: диван"), ((2, 1, 10), "sslab_b", "гостиная: журнальный столик"),
    ((1, 1, 8), "bookshelf", "гостиная: стеллаж"), ((1, 2, 8), "bookshelf", "гостиная: стеллаж"),
    ((5, 3, 10), "lantern_h", "гостиная: свет"), ((6, 3, 12), "lantern_h", "гостиная: свет"),
    # kitchen-dining
    ((10, 1, 1), "diorite", "кухня: столешница"), ((11, 1, 1), "smoker", "кухня: плита"),
    ((12, 1, 1), "cauldron", "кухня: мойка"), ((13, 1, 1), "barrel", "кухня: шкаф"),
    ((13, 1, 2), "diorite", "кухня: столешница"), ((13, 1, 3), "diorite", "кухня: столешница"),
    ((11, 3, 3), "lantern_h", "кухня: свет"),
    ((11, 1, 6), "sslab_t", "столовая: стол"), ((12, 1, 6), "sslab_t", "столовая: стол"),
    ((11, 1, 7), "sslab_t", "столовая: стол"), ((12, 1, 7), "sslab_t", "столовая: стол"),
    ((10, 1, 6), "sst<", "столовая: стул"), ((10, 1, 7), "sst<", "столовая: стул"),
    ((13, 1, 6), "sst>", "столовая: стул"), ((13, 1, 7), "sst>", "столовая: стул"),
    ((12, 3, 7), "lantern_h", "столовая: свет"),
    # loggia
    ((12, 1, 12), "sslab_t", "лоджия: столик"), ((11, 1, 12), "sst<", "лоджия: кресло"),
    ((13, 1, 12), "sst>", "лоджия: кресло"),
    # upper floor
    ((2, 5, 1), "sslab_t", "кабинет: письменный стол"), ((3, 5, 1), "sslab_t", "кабинет: письменный стол"),
    ((2, 5, 2), "sstv", "кабинет: стул"), ((4, 5, 3), "bookshelf", "кабинет: книги"),
    ((4, 6, 3), "bookshelf", "кабинет: книги"),
    ((1, 5, 5), "cauldron", "санузел: ванна"), ((2, 5, 5), "cauldron", "санузел: ванна"),
    ((4, 5, 6), "cauldron", "санузел: раковина"), ((1, 5, 6), "hopper", "санузел: унитаз"),
    ((1, 5, 9), "bed_h", "спальня: кровать, изголовье"), ((2, 5, 9), "bed_f", "спальня: кровать, изножье"),
    ((1, 5, 8), "barrel", "спальня: тумба"), ((1, 5, 10), "barrel", "спальня: тумба"),
    ((1, 6, 8), "lantern", "спальня: ночник"), ((8, 5, 8), "barrel", "спальня: комод"),
    ((7, 5, 10), "sstv", "спальня: кресло"),
    ((2, 5, 12), "sst^", "балкон: кресло"), ((7, 5, 12), "sst^", "балкон: кресло"),
]
for pos, key, _ in FURN:
    put(*pos, key, 11)

# ---------------------------------------------------------------- 12 landscape
PLANTERS = [(0, 4, 16, 18, 1), (12, 16, 16, 18, 1), (15, 17, 4, 8, 1), (5, 9, -3, -1, 0)]
for (x0, x1, z0, z1, y) in PLANTERS:
    for (x, z) in rect(x0, x1, z0, z1):
        inner = x0 < x < x1 and z0 < z < z1
        put(x, y, z, "moss" if inner else "diorite", 12)
        if inner:
            put(x, y + 1, z, "azf" if (x + z) % 3 == 0 else "az", 12)
for x in (2, 3, 6, 7):
    put(x, 6, 14, "azf" if x % 2 else "az", 12)
for tx, tz in TREES:
    for y in range(0, 5):
        put(tx, y, tz, "oak", 12)
        TREE.add((tx, y, tz))
    for y in range(3, 7):
        for (x, z) in rect(tx - 1, tx + 1, tz - 1, tz + 1):
            if (x, z) == (tx, tz) and y <= 4:
                continue
            if y == 6 and abs(x - tx) + abs(z - tz) > 1:
                continue
            put(x, y, z, "azf" if (x * 3 + y + z) % 3 == 0 else "az", 12)
            TREE.add((x, y, z))

# ================================================================= checks
errors = []
for (x, y, z) in M:
    if x not in LX or z not in LZ or y not in LY:
        errors.append("outside lot: %s" % ((x, y, z),))

# a) nothing floats: every block is 6-connected to the ground layer
seen = {c for c in M if c[1] == -1}
q = deque(seen)
while q:
    x, y, z = q.popleft()
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        n = (x + d[0], y + d[1], z + d[2])
        if n in M and n not in seen:
            seen.add(n)
            q.append(n)
floating = [c for c in M if c not in seen]
if floating:
    errors.append("floating blocks: %s" % floating[:10])

# b) stair: two blocks of air above every tread, and above the landing
for y, z in [(1, 6), (2, 5), (3, 4), (4, 3)]:
    for h in (1, 2):
        if (8, y + h, z) in M:
            errors.append("stair headroom blocked at %s" % ((8, y + h, z),))
for h in (5, 6):
    if (8, h, 2) in M:
        errors.append("landing blocked")

# c) envelope is closed: air inside cannot leak outside (doors count as shut)
seeds = [(x, y, z) for (x, z) in E1I for y in (1, 2, 3) if (x, y, z) not in M]
seeds += [(x, y, z) for (x, z) in UI for y in (5, 6, 7) if (x, y, z) not in M]
inside = set(seeds)
q = deque(seeds)
leak = None
while q and not leak:
    x, y, z = q.popleft()
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        n = (x + d[0], y + d[1], z + d[2])
        if n in M or n in inside:
            continue
        nx, ny, nz = n
        ok = ((nx, nz) in E1I and 1 <= ny <= 4) or ((nx, nz) in UI and 4 <= ny <= 7)
        if not ok:
            leak = n
            break
        inside.add(n)
        q.append(n)
if leak:
    errors.append("envelope leak at %s" % (leak,))

# d) roofs have no holes
for x in range(R1[0], R1[1] + 1):
    for z in range(R1[2], R1[3] + 1):
        if (x, z) not in U and (x, z) not in BAL and (x, 5, z) not in M:
            errors.append("hole in low roof %s" % ((x, 5, z),))
for x in range(R2[0], R2[1] + 1):
    for z in range(R2[2], R2[3] + 1):
        if (x, 9, z) not in M:
            errors.append("hole in upper roof %s" % ((x, 9, z),))

# e) mud brick share
nb = sum(1 for k in M.values() if k == "brick")
nm = sum(1 for k in M.values() if k == "mud")
mud_share = nm / (nb + nm)
if not 0.12 <= mud_share <= 0.18:
    errors.append("mud share %.3f" % mud_share)

# ================================================================= commands
def rel(v):
    return "~" if v == 0 else "~%d" % v


def boxes(cells):
    cells = set(cells)
    out = []
    for c in sorted(cells, key=lambda c: (c[1], c[2], c[0])):
        if c not in cells:
            continue
        x0, y0, z0 = c
        x1 = x0
        while (x1 + 1, y0, z0) in cells:
            x1 += 1
        z1 = z0
        while all((x, y0, z1 + 1) in cells for x in range(x0, x1 + 1)):
            z1 += 1
        y1 = y0
        while all((x, y1 + 1, z) in cells for x in range(x0, x1 + 1) for z in range(z0, z1 + 1)):
            y1 += 1
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    cells.discard((x, y, z))
        out.append((x0, y0, z0, x1, y1, z1))
    return out


def cmd(b, key):
    bid, st = P[key][0], P[key][1]
    tail = (" " + st) if st else ""
    x0, y0, z0, x1, y1, z1 = b
    if b[:3] == b[3:]:
        return "setblock %s %s %s %s%s" % (rel(x0), rel(y0), rel(z0), bid, tail)
    return "fill %s %s %s %s %s %s %s%s" % (rel(x0), rel(y0), rel(z0), rel(x1), rel(y1), rel(z1), bid, tail)


CMDS = []   # (phase, command)
CMDS.append((0, "fill ~-3 ~ ~-3 ~19 ~12 ~19 air"))
for ph in range(len(PHASES)):
    by_key = defaultdict(list)
    for c, k in M.items():
        if PH[c] == ph and k not in MANUAL:
            by_key[k].append(c)
    for k in sorted(by_key):
        for b in boxes(by_key[k]):
            CMDS.append((ph, cmd(b, k)))

# round trip: replay commands, compare with the model
sim = {}
for _, c in CMDS:
    parts = c.split(" ")
    if parts[0] == "fill":
        co = [int(p[1:] or 0) for p in parts[1:7]]
        bid = parts[7]
        st = parts[8] if len(parts) > 8 else ""
    else:
        co = [int(p[1:] or 0) for p in parts[1:4]] * 2
        bid = parts[4]
        st = parts[5] if len(parts) > 5 else ""
    vol = (co[3] - co[0] + 1) * (co[4] - co[1] + 1) * (co[5] - co[2] + 1)
    if vol > 32768:
        errors.append("fill too large: " + c)
    for x in range(co[0], co[3] + 1):
        for y in range(co[1], co[4] + 1):
            for z in range(co[2], co[5] + 1):
                if bid == "air":
                    sim.pop((x, y, z), None)
                else:
                    sim[(x, y, z)] = (bid, st)
want = {c: (P[k][0], P[k][1]) for c, k in M.items() if k not in MANUAL}
if sim != want:
    errors.append("commands do not reproduce the model (%d vs %d)" % (len(sim), len(want)))

if errors:
    raise SystemExit("CHECKS FAILED:\n" + "\n".join(errors))

# ================================================================= BOM
PURPOSE = {
    "grass_block": "газон участка (Y=-1)",
    "polished_andesite": "фундамент, дорожка, пол кухни, терраса",
    "smooth_stone": "пол 1-го этажа, пол балкона",
    "polished_tuff": "полосы в полу и на террасе",
    "calcite": "пилоны, труба, парапет, очаг, кромка террасы",
    "smooth_sandstone": "цоколь, поясные тяги Y=4 и Y=8",
    "polished_diorite": "кашпо, столешницы, оголовок трубы",
    "brick_block": "стены (~85%)",
    "mud_bricks": "фактурные вкрапления в стенах (~15%)",
    "gray_stained_glass_pane": "ленточные окна",
    "dark_oak_trapdoor": "рамы-перемычки над окнами",
    "dark_oak_door": "двери (3 наружные + 3 внутренние)",
    "spruce_planks": "перекрытие, потолки, софиты свесов, перегородки",
    "stripped_spruce_log": "деревянная полоса по торцу карнизов",
    "ochre_froglight": "скрытый свет в софитах и потолках",
    "lantern": "подвесные фонари, ночник",
    "deepslate_tiles": "тело кровли под верхним слэбом",
    "deepslate_tile_slab": "кровля: кромка и плоский верх",
    "deepslate_tile_stairs": "кровля: скат по периметру",
    "spruce_stairs": "лестница, стулья, диван, скамья",
    "spruce_slab": "столы",
    "smooth_stone_slab": "ступени у входа и в сад",
    "dark_oak_fence": "перила у лестничного проёма",
    "moss_block": "грунт кашпо и под деревьями",
    "azalea_leaves": "кусты в кашпо, кроны",
    "azalea_leaves_flowered": "цветущие кусты, кроны",
    "oak_log": "стволы деревьев",
    "campfire": "огонь в камине",
    "cauldron": "ванна, раковины, мойка",
    "smoker": "плита",
    "barrel": "шкафы, тумбы",
    "bookshelf": "стеллажи",
    "hopper": "унитаз",
    "bed": "кровать",
}
bom = defaultdict(int)
for c, k in M.items():
    if k in ("door_u", "bed_f"):
        continue
    bom[P[k][0]] += 1
order = list(PURPOSE)
assert set(bom) == set(order), set(bom) ^ set(order)
total = sum(bom.values())
total_cells = len(M)


def stacks(n):
    s, r = divmod(n, 64)
    return "%d ст. + %d" % (s, r) if s and r else ("%d ст." % s if s else "%d шт." % r)


# ================================================================= rendering
def code(c):
    k = M.get(c)
    return P[k][2] if k else "."


def grid(y):
    lines = ["     " + "".join("%3d" % x for x in LX)]
    for z in LZ:
        lines.append("%4d " % z + "".join("%3s" % code((x, y, z)) for x in LX))
    return "\n".join(lines)


def facade_south():
    lines = ["Y\\X  " + "".join("%3d" % x for x in LX)]
    for y in reversed(LY):
        row = []
        for x in LX:
            ch = "."
            for z in reversed(LZ):
                c = (x, y, z)
                if c in M and c not in TREE:
                    ch = P[M[c]][2]
                    break
            row.append("%3s" % ch)
        lines.append("%4d " % y + "".join(row))
    return "\n".join(lines)


def facade_east():
    zs = list(reversed(LZ))   # looking west: south on the left, north on the right
    lines = ["Y\\Z  " + "".join("%3d" % z for z in zs)]
    for y in reversed(LY):
        row = []
        for z in zs:
            ch = "."
            for x in reversed(LX):
                c = (x, y, z)
                if c in M and c not in TREE:
                    ch = P[M[c]][2]
                    break
            row.append("%3s" % ch)
        lines.append("%4d " % y + "".join(row))
    return "\n".join(lines)


used_codes = {}
for k in M.values():
    used_codes.setdefault(P[k][2], set()).add(k)


def legend():
    rows = ["| Код | Bedrock ID | Состояния | Что это |", "|---|---|---|---|"]
    for cd in sorted(used_codes):
        ks = sorted(used_codes[cd])
        k = ks[0]
        st = P[k][1]
        st = "ставится вручную" if st is None else (st or "—")
        desc = P[k][3] if len(ks) == 1 else P[k][3].split(" (")[0]
        rows.append("| `%s` | `%s` | `%s` | %s |" % (cd, P[k][0], st, desc))
    rows.append("| `.` | — | — | воздух |")
    return "\n".join(rows)


# bounding box of the building itself (house + roofs + chimney, no garden)
house = [c for c, k in M.items() if c[1] >= 0 and in_rect(R1, c[0], c[2]) and c not in TREE
         and (c[0], c[2]) not in TER_S | TER_E and k not in ("az", "azf", "moss", "diorite")
         or (c[0], c[2]) in CHIM]
hx = (min(c[0] for c in house), max(c[0] for c in house))
hz = (min(c[2] for c in house), max(c[2] for c in house))
hy = (min(c[1] for c in M), max(c[1] for c in M))

with open(os.path.join(HERE, "prairie_villa.mcfunction"), "w") as f:
    f.write("# Prairie villa - Minecraft Bedrock. Run from the NW foundation corner, feet at floor level.\n")
    f.write("# Generated by generate.py. Doors and the bed are placed by hand afterwards.\n")
    last = None
    for ph, c in CMDS:
        if ph != last:
            f.write("\n# %s\n" % PHASES[ph])
            last = ph
        f.write(c + "\n")

STATS = dict(
    total=total, cells=total_cells, cmds=len(CMDS), mud=mud_share, nb=nb, nm=nm,
    hx=hx, hz=hz, hy=hy, bom=bom, order=order,
)

if __name__ == "__main__":
    import blueprint_doc
    blueprint_doc.write(globals())
    print("ok: %d blocks, %d commands, mud %.1f%%, house X%s Z%s Y%s"
          % (total, len(CMDS), mud_share * 100, hx, hz, hy))
