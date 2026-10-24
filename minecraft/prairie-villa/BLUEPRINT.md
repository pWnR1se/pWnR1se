# Вилла в стиле Prairie — строительный чертёж для Minecraft Bedrock 26.x

Документ собран скриптом `generate.py` из одной 3D-модели. Планы, фасады, ведомость и команды печатаются из одних и тех же данных, поэтому расходиться им не в чем. Перед записью скрипт сам проверяет модель (раздел «Проверки»). Готовая функция для игры лежит в `prairie_villa.mcfunction`.

Композиция: двухэтажный кирпичный объём 10×12 на западе, одноэтажное крыло-кухня 5×10 на востоке, крытая лоджия 5×5 в юго-восточном углу. Над всем первым этажом идёт низкая вальмовая крыша (Y=4–6) с выносом 2 блока, над вторым этажом — верхняя (Y=8–10), тоже с выносом 2. Обе по торцу оторочены полосой из обтёсанной ели, снизу — еловый софит со скрытыми жаболампами. С запада стоит кальцитовая труба 2×3, она поднимается до Y=12.

## 1. Система координат

- **(0,0,0)** — северо-западный угол фундамента на уровне пола первого этажа.
- **X** растёт на восток, **Z** на юг, **Y** вверх. На всех планах север сверху, запад слева.
- **Y=-1**: фундамент заподлицо с газоном (газон участка тоже на Y=-1). **Y=0**: чистый пол и цоколь, он на 1 блок выше земли.
- Этажи: 1-й — пол Y=0, воздух Y=1–3, перекрытие Y=4. 2-й — воздух Y=5–7, потолок Y=8. Кровля: нижняя Y=5–6, верхняя Y=9–10, труба до Y=12.
- Участок: X −3…19, Z −3…19 (23×23). Дом без свесов: X 0…14, Z 0…14 (15×15). С крышей: X −2…16, Z −2…16.
- **Главный вход — с севера**, дверь в точке (3, 1, 0). К ней ведёт дорожка X=3, Z −3…−1 со ступенью-слэбом. Выходы в сад: из гостиной на лоджию (9, 1, 11), из спальни на балкон (4, 5, 11). Терраса и сад смотрят на юг и восток.

## 2. Ведомость материалов

Числа посчитаны по модели: каждая клетка плана — один блок. Дверь и кровать занимают по 2 клетки, но считаются за 1 предмет.

| Блок (Bedrock ID) | Назначение | Кол-во | Стаки по 64 |
|---|---|---:|---|
| `grass_block` | газон участка (Y=-1) | 170 | 2 ст. + 42 |
| `polished_andesite` | фундамент, дорожка, пол кухни, терраса | 422 | 6 ст. + 38 |
| `smooth_stone` | пол 1-го этажа, пол балкона | 109 | 1 ст. + 45 |
| `polished_tuff` | полосы в полу и на террасе | 49 | 49 шт. |
| `calcite` | пилоны, труба, парапет, очаг, кромка террасы | 176 | 2 ст. + 48 |
| `smooth_sandstone` | цоколь, поясные тяги Y=4 и Y=8 | 132 | 2 ст. + 4 |
| `polished_diorite` | кашпо, столешницы, оголовок трубы | 57 | 57 шт. |
| `brick_block` | стены (~85%) | 107 | 1 ст. + 43 |
| `mud_bricks` | фактурные вкрапления в стенах (~15%) | 20 | 20 шт. |
| `gray_stained_glass_pane` | ленточные окна | 122 | 1 ст. + 58 |
| `dark_oak_trapdoor` | рамы-перемычки над окнами | 52 | 52 шт. |
| `dark_oak_door` | двери (3 наружные + 3 внутренние) | 6 | 6 шт. |
| `spruce_planks` | перекрытие, потолки, софиты свесов, перегородки | 353 | 5 ст. + 33 |
| `stripped_spruce_log` | деревянная полоса по торцу карнизов | 128 | 2 ст. |
| `ochre_froglight` | скрытый свет в софитах и потолках | 36 | 36 шт. |
| `lantern` | подвесные фонари, ночник | 6 | 6 шт. |
| `deepslate_tiles` | тело кровли под верхним слэбом | 192 | 3 ст. |
| `deepslate_tile_slab` | кровля: кромка и плоский верх | 320 | 5 ст. |
| `deepslate_tile_stairs` | кровля: скат по периметру | 106 | 1 ст. + 42 |
| `spruce_stairs` | лестница, стулья, диван, скамья | 19 | 19 шт. |
| `spruce_slab` | столы | 8 | 8 шт. |
| `smooth_stone_slab` | ступени у входа и в сад | 6 | 6 шт. |
| `dark_oak_fence` | перила у лестничного проёма | 4 | 4 шт. |
| `moss_block` | грунт кашпо и под деревьями | 43 | 43 шт. |
| `azalea_leaves` | кусты в кашпо, кроны | 67 | 1 ст. + 3 |
| `azalea_leaves_flowered` | цветущие кусты, кроны | 39 | 39 шт. |
| `oak_log` | стволы деревьев | 15 | 15 шт. |
| `campfire` | огонь в камине | 1 | 1 шт. |
| `cauldron` | ванна, раковины, мойка | 4 | 4 шт. |
| `smoker` | плита | 1 | 1 шт. |
| `barrel` | шкафы, тумбы | 6 | 6 шт. |
| `bookshelf` | стеллажи | 4 | 4 шт. |
| `hopper` | унитаз | 1 | 1 шт. |
| `bed` | кровать | 1 | 1 шт. |
| **Итого** | | **2782** | **43 ст. + 30** |

Без газона (`grass_block`, если участок уже травяной) — **2612** блоков. Кирпич из грязи — 20 из 127 кирпичных клеток, то есть **15.7%**.

**Отличия ID в Bedrock** от привычных Java-имён: `bricks` здесь называется `brick_block`, `flowering_azalea_leaves` — `azalea_leaves_flowered`. Остальные блоки из задания называются одинаково, в том числе `smooth_sandstone`, `polished_diorite`, `polished_andesite`, `smooth_stone_slab`, `spruce_slab` и `gray_stained_glass_pane`. В версиях 1.20–1.21 их сделали отдельными ID. Кровать в Bedrock — предмет `bed` с цветом, через команду её не ставим.

## 3. Послойные планы

Одна сетка на каждый слой Y, от −1 до 12. Столбцы — X, строки — Z. Одна клетка — один блок. Ступени помечены стрелкой: она показывает, куда идёт подъём, там же у ступени высокая сторона или спинка стула.

### Легенда

| Код | Bedrock ID | Состояния | Что это |
|---|---|---|---|
| `Af` | `azalea_leaves_flowered` | `["persistent_bit"=true]` | цветущая листва азалии |
| `An` | `polished_andesite` | `—` | полированный андезит |
| `Az` | `azalea_leaves` | `["persistent_bit"=true]` | листва азалии |
| `Ba` | `barrel` | `—` | бочка (шкаф, тумба) |
| `Bd` | `bed` | `ставится вручную` | кровать |
| `Bk` | `bookshelf` | `—` | книжная полка |
| `Br` | `brick_block` | `—` | кирпич |
| `C<` | `spruce_stairs` | `["weirdo_direction"=1,"upside_down_bit"=false]` | еловая ступень, спинка/подъём на запад |
| `C>` | `spruce_stairs` | `["weirdo_direction"=0,"upside_down_bit"=false]` | еловая ступень, спинка/подъём на восток |
| `C^` | `spruce_stairs` | `["weirdo_direction"=3,"upside_down_bit"=false]` | еловая ступень, спинка/подъём на север |
| `Ca` | `calcite` | `—` | кальцит (пилоны, труба) |
| `Cf` | `campfire` | `—` | костёр (огонь камина) |
| `Cv` | `spruce_stairs` | `["weirdo_direction"=2,"upside_down_bit"=false]` | еловая ступень, спинка/подъём на юг |
| `Di` | `polished_diorite` | `—` | полированный диорит (кашпо) |
| `Dr` | `dark_oak_door` | `ставится вручную` | дверь тёмного дуба |
| `Ds` | `deepslate_tile_slab` | `["minecraft:vertical_half"="bottom"]` | плиточный слэб, нижний |
| `Dt` | `deepslate_tiles` | `—` | глубинносланцевая плитка (полный блок) |
| `Fe` | `dark_oak_fence` | `—` | забор тёмного дуба (перила) |
| `Fr` | `ochre_froglight` | `—` | охровая жаболампа |
| `Gl` | `gray_stained_glass_pane` | `—` | серая стеклянная панель |
| `Gr` | `grass_block` | `—` | трава (участок) |
| `Ho` | `hopper` | `—` | воронка (унитаз) |
| `Ku` | `cauldron` | `—` | котёл (ванна, раковина) |
| `L-` | `stripped_spruce_log` | `["pillar_axis"="x"]` | обтёсанное еловое бревно, ось X |
| `Ln` | `lantern` | `["hanging"=true]` | фонарь подвесной |
| `Lo` | `oak_log` | `["pillar_axis"="y"]` | дубовое бревно (ствол) |
| `L|` | `stripped_spruce_log` | `["pillar_axis"="z"]` | обтёсанное еловое бревно, ось Z |
| `Mo` | `moss_block` | `—` | блок мха |
| `Mu` | `mud_bricks` | `—` | кирпич из грязи |
| `R<` | `deepslate_tile_stairs` | `["weirdo_direction"=1,"upside_down_bit"=false]` | плиточная ступень, подъём на запад |
| `R>` | `deepslate_tile_stairs` | `["weirdo_direction"=0,"upside_down_bit"=false]` | плиточная ступень, подъём на восток |
| `R^` | `deepslate_tile_stairs` | `["weirdo_direction"=3,"upside_down_bit"=false]` | плиточная ступень, подъём на север |
| `Rv` | `deepslate_tile_stairs` | `["weirdo_direction"=2,"upside_down_bit"=false]` | плиточная ступень, подъём на юг |
| `Sa` | `smooth_sandstone` | `—` | гладкий песчаник (цоколь, пояс) |
| `Sb` | `smooth_stone_slab` | `["minecraft:vertical_half"="bottom"]` | слэб гладкого камня (ступень) |
| `Sm` | `smoker` | `—` | коптильня (плита) |
| `Sp` | `spruce_planks` | `—` | еловые доски |
| `Ss` | `smooth_stone` | `—` | гладкий камень |
| `Td` | `dark_oak_trapdoor` | `["upside_down_bit"=true,"open_bit"=false]` | люк тёмного дуба, верхний, закрыт (рама-перемычка) |
| `Tu` | `polished_tuff` | `—` | полированный туф (полосы) |
| `ln` | `lantern` | `["hanging"=false]` | фонарь стоячий |
| `wb` | `spruce_slab` | `["minecraft:vertical_half"="bottom"]` | еловый слэб, нижний |
| `wt` | `spruce_slab` | `["minecraft:vertical_half"="top"]` | еловый слэб, верхний |
| `.` | — | — | воздух |

### Y = -1 — фундамент, дорожка, мох под деревьями, основание трубы

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3  Gr Gr Gr Gr Gr Gr An Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr
  -2  Gr Gr Gr Gr Gr Gr An Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr
  -1  Gr Gr Gr Gr Gr Gr An Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Mo Mo Mo
   0  Gr Gr Gr An An An An An An An An An An An An An An An Gr Gr Mo Mo Mo
   1  Gr Gr Gr An An An An An An An An An An An An An An An Gr Gr Mo Mo Mo
   2  Gr Gr Gr An An An An An An An An An An An An An An An Gr Gr Gr Gr Gr
   3  Gr Gr Gr An An An An An An An An An An An An An An An Gr Gr Gr Gr Gr
   4  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
   5  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
   6  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
   7  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
   8  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
   9  Gr Gr Ca Ca An An An An An An An An An An An An An An An An An Gr Gr
  10  Gr Gr Ca Ca An An An An An An An An An An An An An An An An An Gr Gr
  11  Gr Gr Ca Ca An An An An An An An An An An An An An An An An An Gr Gr
  12  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
  13  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
  14  Gr Gr Gr An An An An An An An An An An An An An An An An An An Gr Gr
  15  Gr Gr Gr An An An An An An An An An An An An An An An An An Gr Gr Gr
  16  Gr Gr Gr An An An An An An An An An An An An An An An An An Gr Gr Gr
  17  Mo Mo Mo An An An An An An An An An An An An An An An An An Mo Mo Mo
  18  Mo Mo Mo An An An An An An An An An An An An An An An An An Mo Mo Mo
  19  Mo Mo Mo Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Mo Mo Mo
```

### Y = 0 — чистый пол, цоколь из песчаника, кальцитовые пилоны, терраса, ступени

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  . Di Di Di Di Di  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  . Di Mo Mo Mo Di  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  . Sb  . Di Di Di Di Di  .  .  .  .  .  .  .  .  .  .
   0   .  .  . Ca Sa Sa Sa Sa Ca Sa Sa Sa Ca Sa Sa Sa Sa Ca  .  .  . Lo  .
   1   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Sa  .  .  .  .  .
   2   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Sa  .  .  .  .  .
   3   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Sa  .  .  .  .  .
   4   .  .  . Sa Tu Tu Tu Tu Tu Tu Tu Tu Tu An An An An Sa An Tu Ca  .  .
   5   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Ca An Tu Ca  .  .
   6   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Sa An Tu Ca  .  .
   7   .  .  . Ca Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Sa An Tu Ca  .  .
   8   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Ss An An An An Sa An Tu Ca  .  .
   9   .  . Ca Ca Ca Ss Ss Ss Ss Ss Ss Ss Ca Sa Sa Sa Sa Ca An Tu Ca  .  .
  10   .  . Ca Ca Ca Ss Ss Ss Ss Ss Ss Ss Sa An An An An An An Tu Ca  .  .
  11   .  . Ca Ca Ca Tu Tu Tu Tu Tu Tu Tu Sa An An An An An An Tu Ca  .  .
  12   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Sa Tu Tu Tu Tu Tu An Tu Ca  .  .
  13   .  .  . Sa Ss Ss Ss Ss Ss Ss Ss Ss Sa An An An An An An Tu Ca  .  .
  14   .  .  . Ca Sa Sa Sa Ca Sa Sa Sa Sa Ca An An An An Ca An Tu Ca  .  .
  15   .  .  . An An An An An An An An An An An An An An An An An  .  .  .
  16   .  .  . Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu Tu  .  .  .
  17   .  .  . An An An An An An An An An An An An An An An An An  .  .  .
  18   . Lo  . Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca  . Lo  .
  19   .  .  .  .  .  .  .  .  . Sb Sb Sb Sb Sb  .  .  .  .  .  .  .  .  .
```

### Y = 1 — 1-й этаж: двери, окна в пол, мебель, кашпо на террасе

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  . Az Az Af  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   0   .  .  . Ca Br Gl Dr Gl Ca Br Br Br Ca Br Mu Br Br Ca  .  .  . Lo  .
   1   .  .  . Br  .  .  .  .  .  . Ba Ba Br Di Sm Ku Ba Br  .  .  .  .  .
   2   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  . Di Br  .  .  .  .  .
   3   .  .  . Mu  .  .  .  .  .  .  . Sp Br  .  .  . Di Mu  .  .  .  .  .
   4   .  .  . Br C<  .  .  .  .  .  . Sp Br  .  .  .  . Br Di Di Di  .  .
   5   .  .  . Br C<  .  .  .  .  .  . Sp Mu  .  .  .  . Ca Di Mo Di  .  .
   6   .  .  . Br  .  .  .  .  .  .  . C^ Br C< wt wt C> Gl Di Mo Di  .  .
   7   .  .  . Ca Br Br Br  .  .  .  .  .  . C< wt wt C> Gl Di Mo Di  .  .
   8   .  .  . Br Bk  .  .  .  .  .  .  .  .  .  .  .  . Gl Di Di Di  .  .
   9   .  . Ca Ca  .  .  . C>  .  .  .  . Ca Br Gl Gl Mu Ca  .  .  .  .  .
  10   .  . Ca Cf  . wb  . C>  .  .  .  . Gl  .  .  .  .  .  .  .  .  .  .
  11   .  . Ca Ca  .  .  . C>  .  .  .  . Dr  .  .  .  .  .  .  .  .  .  .
  12   .  .  . Gl  .  .  .  .  .  .  .  . Gl  . C< wt C>  .  .  .  .  .  .
  13   .  .  . Gl  .  .  .  .  .  .  .  . Br  .  .  .  .  .  .  .  .  .  .
  14   .  .  . Ca Gl Gl Gl Ca Gl Gl Gl Gl Ca  .  .  .  . Ca  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  . Di Di Di Di Di  .  .  .  .  .  .  . Di Di Di Di Di  .  .  .
  17   .  .  . Di Mo Mo Mo Di  .  .  .  .  .  .  . Di Mo Mo Mo Di  .  .  .
  18   . Lo  . Di Di Di Di Di  .  .  .  .  .  .  . Di Di Di Di Di  . Lo  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 2 — 1-й этаж: средний ряд окон, верх дверей

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   0   .  .  . Ca Br Gl Dr Gl Ca Br Br Br Ca Gl Gl Gl Gl Ca  .  .  . Lo  .
   1   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  .  . Br  .  .  .  .  .
   2   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  .  . Gl  .  .  .  .  .
   3   .  .  . Gl  .  .  .  .  .  .  . Sp Br  .  .  .  . Gl  .  .  .  .  .
   4   .  .  . Gl  .  .  .  .  .  .  . Sp Br  .  .  .  . Gl  .  .  .  .  .
   5   .  .  . Gl  .  .  .  .  .  .  . C^ Mu  .  .  .  . Ca  . Af  .  .  .
   6   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  .  . Gl  . Az  .  .  .
   7   .  .  . Ca Br Br Br  .  .  .  .  .  .  .  .  .  . Gl  . Az  .  .  .
   8   .  .  . Br Bk  .  .  .  .  .  .  .  .  .  .  .  . Gl  .  .  .  .  .
   9   .  . Ca Ca  .  .  .  .  .  .  .  . Ca Br Gl Gl Mu Ca  .  .  .  .  .
  10   .  . Ca Ca  .  .  .  .  .  .  .  . Gl  .  .  .  .  .  .  .  .  .  .
  11   .  . Ca Ca  .  .  .  .  .  .  .  . Dr  .  .  .  .  .  .  .  .  .  .
  12   .  .  . Gl  .  .  .  .  .  .  .  . Gl  .  .  .  .  .  .  .  .  .  .
  13   .  .  . Gl  .  .  .  .  .  .  .  . Br  .  .  .  .  .  .  .  .  .  .
  14   .  .  . Ca Gl Gl Gl Ca Gl Gl Gl Gl Ca  .  .  .  . Ca  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  . Af Az Az  .  .  .  .  .  .  .  .  . Af Az Az  .  .  .  .
  18   . Lo  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Lo  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 3 — 1-й этаж: верх окон, подвесные фонари, рамы-перемычки из люков

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  . Td Td Td  .  .  .  .  . Td Td Td Td  .  .  . Az Az Az
   0   .  .  . Ca Br Gl Gl Gl Ca Br Br Br Ca Gl Gl Gl Gl Ca  .  . Af Lo Af
   1   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  .  . Br  .  . Az Az Az
   2   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  .  . Gl Td  .  .  .  .
   3   .  . Td Gl  .  .  . Ln  .  .  . Sp Br  . Ln  .  . Gl Td  .  .  .  .
   4   .  . Td Gl  .  .  .  .  .  .  . C^ Br  .  .  .  . Gl Td  .  .  .  .
   5   .  . Td Gl  .  .  .  .  .  .  .  . Mu  .  .  .  . Ca  .  .  .  .  .
   6   .  .  . Br  .  .  .  .  .  .  .  . Br  .  .  .  . Gl Td  .  .  .  .
   7   .  .  . Ca Br Br Br  .  .  .  .  .  .  .  . Ln  . Gl Td  .  .  .  .
   8   .  .  . Br  .  .  .  .  .  .  .  .  .  .  .  .  . Gl Td  .  .  .  .
   9   .  . Ca Ca  .  .  .  .  .  .  .  . Ca Br Gl Gl Mu Ca  .  .  .  .  .
  10   .  . Ca Ca  .  .  .  . Ln  .  .  . Gl Td Td Td  .  .  .  .  .  .  .
  11   .  . Ca Ca  .  .  .  .  .  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
  12   .  . Td Gl  .  .  .  .  . Ln  .  . Gl Td  .  .  .  .  .  .  .  .  .
  13   .  . Td Gl  .  .  .  .  .  .  .  . Br  .  .  .  .  .  .  .  .  .  .
  14   .  .  . Ca Gl Gl Gl Ca Gl Gl Gl Gl Ca  .  .  .  . Ca  .  .  .  .  .
  15   .  .  .  . Td Td Td  . Td Td Td Td  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17  Az Az Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az Az Az
  18  Af Lo Af  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Af Lo Af
  19  Az Az Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az Az Az
```

### Y = 4 — перекрытие, поясная тяга, нижние свесы: торец из бревна, софит, свет

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   . L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L-  .  .  .
  -1   . L| Sp Sp Fr Sp Sp Sp Fr Sp Sp Sp Fr Sp Sp Sp Fr Sp Sp L| Af Af Af
   0   . L| Sp Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sp L| Az Lo Az
   1   . L| Fr Sa Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sa Fr L| Az Az Az
   2   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .
   3   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp C^ Sp Sp Sp Sp Sp Sa Sp L|  .  .  .
   4   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp  . Sp Sp Sp Sp Sp Sa Sp L|  .  .  .
   5   . L| Fr Sa Sp Sp Sp Sp Sp Sp Sp  . Sp Sp Sp Sp Sp Sa Fr L|  .  .  .
   6   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .
   7   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .
   8   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .
   9   . L| Ca Ca Sp Sp Sp Sp Sp Sp Sp Sp Sa Sa Sa Sa Sa Sa Fr L|  .  .  .
  10   . L| Ca Ca Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp Sp Sp Sp Sp Sp L|  .  .  .
  11   . L| Ca Ca Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp Fr Sp Fr Sp Sp L|  .  .  .
  12   . L| Sp Sa Ss Ss Ss Ss Ss Ss Ss Ss Sa Sp Sp Sp Sp Sp Sp L|  .  .  .
  13   . L| Fr Sa Ss Ss Ss Ss Ss Ss Ss Ss Sa Sp Fr Sp Fr Sp Fr L|  .  .  .
  14   . L| Sp Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sp Sp Sp Sp Ca Sp L|  .  .  .
  15   . L| Sp Sp Fr Sp Sp Sp Fr Sp Sp Sp Fr Sp Sp Sp Fr Sp Sp L|  .  .  .
  16   . L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L-  .  .  .
  17  Af Af Af  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Af Af Af
  18  Az Lo Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az Lo Az
  19  Az Az Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az Az Az
```

### Y = 5 — 2-й этаж, балкон с парапетом; кровля нижней крыши (кромка, скат, тело)

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .
  -1   . Ds Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Ds Az Az Az
   0   . Ds R> Ca Br Br Br Mu Br Br Br Br Ca Dt Dt Dt Dt Dt R< Ds Az Az Az
   1   . Ds R> Br  . wt wt  . Sp  .  .  . Br Dt Dt Dt Dt Dt R< Ds Af Af Af
   2   . Ds R> Br  . Cv  .  . Dr  .  .  . Br Dt Dt Dt Dt Dt R< Ds  .  .  .
   3   . Ds R> Mu  .  .  . Bk Sp  .  .  . Br Dt Dt Dt Dt Dt R< Ds  .  .  .
   4   . Ds R> Br Sp Sp Sp Sp Sp  . Fe  . Br Dt Dt Dt Dt Dt R< Ds  .  .  .
   5   . Ds R> Br Ku Ku  .  . Dr  . Fe  . Mu Dt Dt Dt Dt Dt R< Ds  .  .  .
   6   . Ds R> Br Ho  .  . Ku Sp  . Fe Fe Br Dt Dt Dt Dt Dt R< Ds  .  .  .
   7   . Ds R> Br Sp Sp Sp Sp Sp Dr Sp Sp Br Dt Dt Dt Dt Dt R< Ds  .  .  .
   8   . Ds R> Br Ba  .  .  .  .  .  . Ba Br Dt Dt Dt Dt Dt R< Ds  .  .  .
   9   . Ds Ca Ca Bd Bd  .  .  .  .  .  . Br Dt Dt Dt Dt Dt R< Ds  .  .  .
  10   . Ds Ca Ca Ba  .  .  .  .  . Cv  . Br Dt Dt Dt Dt Dt R< Ds  .  .  .
  11   . Ds Ca Ca Mu Gl Gl Dr Gl Gl Gl Mu Ca Dt Dt Dt Dt Dt R< Ds  .  .  .
  12   . Ds R> Ca  . C^  .  .  .  . C^  . Ca Dt Dt Dt Dt Dt R< Ds  .  .  .
  13   . Ds R> Ca  .  .  .  .  .  .  .  . Ca Dt Dt Dt Dt Dt R< Ds  .  .  .
  14   . Ds R> Ca Ca Mo Mo Ca Ca Mo Mo Ca Ca Dt Dt Dt Dt Dt R< Ds  .  .  .
  15   . Ds R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ Ds  .  .  .
  16   . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .
  17  Az Az Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az Az Az
  18  Az Az Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az Az Az
  19  Af Af Af  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Af Af Af
```

### Y = 6 — 2-й этаж; плоский верх нижней крыши

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az  .
   0   .  .  . Ca Gl Gl Gl Mu Br Br Gl Gl Ca Ds Ds Ds Ds Ds  .  . Af Af Af
   1   .  .  . Br  .  .  .  . Sp  .  .  . Br Ds Ds Ds Ds Ds  .  .  . Az  .
   2   .  .  . Gl  .  .  .  . Dr  .  .  . Gl Ds Ds Ds Ds Ds  .  .  .  .  .
   3   .  .  . Gl  .  .  . Bk Sp  .  .  . Gl Ds Ds Ds Ds Ds  .  .  .  .  .
   4   .  .  . Br Sp Sp Sp Sp Sp  .  .  . Br Ds Ds Ds Ds Ds  .  .  .  .  .
   5   .  .  . Br  .  .  .  . Dr  .  .  . Gl Ds Ds Ds Ds Ds  .  .  .  .  .
   6   .  .  . Br  .  .  .  . Sp  .  .  . Br Ds Ds Ds Ds Ds  .  .  .  .  .
   7   .  .  . Br Sp Sp Sp Sp Sp Dr Sp Sp Br Ds Ds Ds Ds Ds  .  .  .  .  .
   8   .  .  . Gl ln  .  .  .  .  .  .  . Gl Ds Ds Ds Ds Ds  .  .  .  .  .
   9   .  . Ca Ca  .  .  .  .  .  .  .  . Gl Ds Ds Ds Ds Ds  .  .  .  .  .
  10   .  . Ca Ca  .  .  .  .  .  .  .  . Gl Ds Ds Ds Ds Ds  .  .  .  .  .
  11   .  . Ca Ca Mu Gl Gl Dr Gl Gl Gl Mu Ca Ds Ds Ds Ds Ds  .  .  .  .  .
  12   .  .  .  .  .  .  .  .  .  .  .  .  . Ds Ds Ds Ds Ds  .  .  .  .  .
  13   .  .  .  .  .  .  .  .  .  .  .  .  . Ds Ds Ds Ds Ds  .  .  .  .  .
  14   .  .  .  .  . Az Af  .  . Az Af  .  . Ds Ds Ds Ds Ds  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   . Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az  .
  18  Af Af Af  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Af Af Af
  19   . Az  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . Az  .
```

### Y = 7 — 2-й этаж: верх окон, рамы-перемычки

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  . Td Td Td  .  .  . Td Td  .  .  .  .  .  .  .  .  .  .  .
   0   .  .  . Ca Gl Gl Gl Mu Br Br Gl Gl Ca  .  .  .  .  .  .  .  .  .  .
   1   .  .  . Br  .  .  .  . Sp  .  .  . Br  .  .  .  .  .  .  .  .  .  .
   2   .  . Td Gl  .  .  .  . Sp  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
   3   .  . Td Gl  .  .  .  . Sp  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
   4   .  .  . Br Sp Sp Sp Sp Sp  .  .  . Br  .  .  .  .  .  .  .  .  .  .
   5   .  . Td Gl  .  .  .  . Sp  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
   6   .  . Td Gl  .  .  .  . Sp  .  .  . Br  .  .  .  .  .  .  .  .  .  .
   7   .  .  . Br Sp Sp Sp Sp Sp Sp Sp Sp Br  .  .  .  .  .  .  .  .  .  .
   8   .  . Td Gl  .  .  .  .  .  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
   9   .  . Ca Ca  .  .  .  .  .  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
  10   .  . Ca Ca  .  .  .  .  .  .  .  . Gl Td  .  .  .  .  .  .  .  .  .
  11   .  . Ca Ca Mu Gl Gl Gl Gl Gl Gl Mu Ca  .  .  .  .  .  .  .  .  .  .
  12   .  .  .  .  . Td Td Td Td Td Td  .  .  .  .  .  .  .  .  .  .  .  .
  13   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  14   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  18   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 8 — потолок 2-го этажа, верхние свесы: торец, софит, жаболампы

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   . L- L- L- L- L- L- L- L- L- L- L- L- L- L-  .  .  .  .  .  .  .  .
  -1   . L| Sp Sp Fr Sp Sp Sp Fr Sp Sp Sp Fr Sp L|  .  .  .  .  .  .  .  .
   0   . L| Sp Sa Sa Sa Sa Sa Sa Sa Sa Sa Sa Sp L|  .  .  .  .  .  .  .  .
   1   . L| Fr Sa Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .  .  .  .  .  .
   2   . L| Sp Sa Sp Fr Sp Sp Sp Sp Fr Sp Sa Fr L|  .  .  .  .  .  .  .  .
   3   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .  .  .  .  .  .
   4   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .  .  .  .  .  .
   5   . L| Fr Sa Sp Fr Sp Sp Sp Sp Fr Sp Sa Sp L|  .  .  .  .  .  .  .  .
   6   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sa Fr L|  .  .  .  .  .  .  .  .
   7   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .  .  .  .  .  .
   8   . L| Sp Sa Sp Sp Sp Sp Sp Sp Sp Sp Sa Sp L|  .  .  .  .  .  .  .  .
   9   . L| Ca Ca Sp Sp Fr Sp Sp Fr Sp Sp Sa Sp L|  .  .  .  .  .  .  .  .
  10   . L| Ca Ca Sp Sp Sp Sp Sp Sp Sp Sp Sa Fr L|  .  .  .  .  .  .  .  .
  11   . L| Ca Ca Sa Sa Sa Sa Sa Sa Sa Sa Sa Sp L|  .  .  .  .  .  .  .  .
  12   . L| Sp Fr Sp Sp Sp Fr Sp Sp Sp Fr Sp Sp L|  .  .  .  .  .  .  .  .
  13   . L- L- L- L- L- L- L- L- L- L- L- L- L- L-  .  .  .  .  .  .  .  .
  14   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  18   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 9 — верхняя крыша: кромка, скат, тело

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .
  -1   . Ds Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Rv Ds  .  .  .  .  .  .  .  .
   0   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   1   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   2   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   3   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   4   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   5   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   6   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   7   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   8   . Ds R> Dt Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
   9   . Ds Ca Ca Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
  10   . Ds Ca Ca Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
  11   . Ds Ca Ca Dt Dt Dt Dt Dt Dt Dt Dt Dt R< Ds  .  .  .  .  .  .  .  .
  12   . Ds R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ R^ Ds  .  .  .  .  .  .  .  .
  13   . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .
  14   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  18   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 10 — плоский верх верхней крыши, труба

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   0   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   1   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   2   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   3   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   4   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   5   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   6   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   7   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   8   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   9   .  . Ca Ca Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
  10   .  . Ca Ca Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
  11   .  . Ca Ca Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
  12   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  13   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  14   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  18   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 11 — труба над крышей

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   0   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   4   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   5   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   6   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   7   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   8   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   9   .  . Ca Ca  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  10   .  . Ca Ca  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  11   .  . Ca Ca  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  12   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  13   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  14   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  18   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

### Y = 12 — оголовок трубы

```
      -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  -3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  -1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   0   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   1   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   2   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   3   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   4   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   5   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   6   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   7   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   8   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
   9   .  . Di Di  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  10   .  . Di Di  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  11   .  . Di Di  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  12   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  13   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  14   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  15   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  16   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  17   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  18   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  19   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
```

## 4. Фасады

Для каждой клетки фасада показан первый блок, который видно с этой стороны. Деревья убраны, чтобы не закрывали дом. Кашпо и террасы оставлены.

Хорошо видна ярусность: торец нижнего карниза из бревна (`L-`/`L|`) на Y=4, кровля Y=5–6, ряд перемычек `Td` на Y=7, затем верхний карниз на Y=8 и кровля Y=9–10. Труба выходит над всеми ярусами.

### Южный фасад (смотрим на север, запад слева)

```
Y\X   -3 -2 -1  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
  12   .  . Di Di  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  11   .  . Ca Ca  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
  10   .  . Ca Ca Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .  .  .
   9   . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .  .  .  .  .  .
   8   . L- L- L- L- L- L- L- L- L- L- L- L- L- L-  .  .  .  .  .  .  .  .
   7   .  . Ca Ca Mu Td Td Td Td Td Td Mu Ca Td  .  .  .  .  .  .  .  .  .
   6   .  . Ca Ca Mu Az Af Dr Gl Az Af Mu Ca Ds Ds Ds Ds Ds  .  .  .  .  .
   5   . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .
   4   . L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L- L-  .  .  .
   3   .  . Td Ca Td Td Td Ca Td Td Td Td Ca Td Td Td Mu Ca Td  .  .  .  .
   2   .  . Ca Ca Af Az Az Ca Gl Gl Gl Gl Ca Br Gl Gl Af Az Az Az  .  .  .
   1   .  . Ca Di Di Di Di Di Gl Gl Gl Gl Ca Br C< Di Di Di Di Di Di  .  .
   0   .  . Ca Ca Ca Ca Ca Ca Ca Sb Sb Sb Sb Sb Ca Ca Ca Ca Ca Ca Ca  .  .
  -1  Mo Mo Mo Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Mo Mo Mo
```

### Восточный фасад (смотрим на запад, юг слева)

```
Y\Z   19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0 -1 -2 -3
  12   .  .  .  .  .  .  .  . Di Di Di  .  .  .  .  .  .  .  .  .  .  .  .
  11   .  .  .  .  .  .  .  . Ca Ca Ca  .  .  .  .  .  .  .  .  .  .  .  .
  10   .  .  .  .  .  .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .
   9   .  .  .  .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .
   8   .  .  .  .  .  . L- L| L| L| L| L| L| L| L| L| L| L| L| L| L| L-  .
   7   .  .  .  .  .  .  . Td Ca Td Td Td Br Br Td Br Td Td Br Ca Td  .  .
   6   .  .  .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .  .  .
   5   .  .  . Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds Ds  .
   4   .  .  . L- L| L| L| L| L| L| L| L| L| L| L| L| L| L| L| L| L| L-  .
   3   .  .  .  . Td Ca Br Td Td Td Ca Td Td Td Ca Td Td Td Br Ca Td  .  .
   2   .  . Az  .  . Ca Br Gl Dr Gl Ca Gl Az Az Af Gl Gl Gl Br Ca  .  .  .
   1   . Di Di Di  . Ca Br C> Dr Gl Ca Di Di Di Di Di Mu Br Br Ca  . Af  .
   0  Sb Ca An Tu An Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Ca Sa Sa Sa Ca Di Di Di
  -1  Mo Mo Mo Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Gr Mo Mo Mo Gr Gr
```

На восточном фасаде видны три яруса подряд: одноэтажное крыло (Y=0–6), над ним отступающий второй этаж (Y=5–7) и широкий верхний свес (Y=8–10).

## 5. Планировка

Размеры даны в блоках по чистому полу, без стен. Высота потолка на обоих этажах — 3 блока.

| Этаж | Помещение | Координаты | Размер | Площадь |
|---|---|---|---|---:|
| 1 | Прихожая (вход с севера, дверь в точке 3,1,0) | X1–7 × Z1–6 | 7 × 6 | 42 |
| 1 | Лестница на 2-й этаж (марш вдоль X=8, подъём на север) | X8 × Z3–6 | 1 × 4 | 4 |
| 1 | Кладовая под площадкой | X8 × Z1–2 | 1 × 2 | 2 |
| 1 | Гостиная с камином (топка в западной стене, 0,1,10) | X1–8 × Z8–13 | 8 × 6 | 48 |
| 1 | Кухня (рабочая зона у северной стены) | X10–13 × Z1–4 | 4 × 4 | 16 |
| 1 | Столовая (окна в пол на восток и на лоджию) | X10–13 × Z5–8 | 4 × 4 | 16 |
| 1 | Проход кухня–гостиная | X9 × Z7–8 | 1 × 2 | 2 |
| 1 | Крытая терраса-лоджия под нижней крышей | X10–14 × Z10–14 | 5 × 5 | 25 |
| 2 | Холл с лестничным проёмом | X6–8 × Z1–6 | 3 × 6 | 18 |
| 2 | Кабинет | X1–4 × Z1–3 | 4 × 3 | 12 |
| 2 | Санузел | X1–4 × Z5–6 | 4 × 2 | 8 |
| 2 | Спальня (камин-труба в западной стене) | X1–8 × Z8–10 | 8 × 3 | 24 |
| 2 | Балкон над гостиной (за парапетом) | X1–8 × Z12–13 | 8 × 2 | 16 |

- Перегородки 1-го этажа из кирпича: Z=7 при X1–3 (прихожая/гостиная) и X=9 при Z1–6 (лестница/кухня). Гостиная открыта в прихожую проёмом шириной 5 (X4–8) и в кухню-столовую проёмом шириной 2 (Z7–8).
- Перегородки 2-го этажа из еловых досок: X=5 (Z1–6), Z=4 (X1–4), Z=7 (X1–8). Внутренние двери: кабинет (5,5,2), санузел (5,5,5), спальня (6,5,7).
- Лестница: 4 еловые ступени в (8,1,6), (8,2,5), (8,3,4), (8,4,3), подъём на север. Проём в перекрытии над (8,4,4) и (8,4,5). Ограждение — забор в (7,5,4), (7,5,5), (7,5,6), (8,5,6). Снизу марш закрыт досками.

## 6. Интерьер

| Помещение: предмет | Блок | Координаты (x, y, z) |
|---|---|---|
| прихожая: скамья | `spruce_stairs` `["weirdo_direction"=1,"upside_down_bit"=false]` | 1, 1, 4 |
| прихожая: скамья | `spruce_stairs` `["weirdo_direction"=1,"upside_down_bit"=false]` | 1, 1, 5 |
| прихожая: шкаф | `barrel` | 7, 1, 1 |
| прихожая: шкаф | `barrel` | 8, 1, 1 |
| прихожая: свет | `lantern` `["hanging"=true]` | 4, 3, 3 |
| гостиная: диван | `spruce_stairs` `["weirdo_direction"=0,"upside_down_bit"=false]` | 4, 1, 9 |
| гостиная: диван | `spruce_stairs` `["weirdo_direction"=0,"upside_down_bit"=false]` | 4, 1, 10 |
| гостиная: диван | `spruce_stairs` `["weirdo_direction"=0,"upside_down_bit"=false]` | 4, 1, 11 |
| гостиная: журнальный столик | `spruce_slab` `["minecraft:vertical_half"="bottom"]` | 2, 1, 10 |
| гостиная: стеллаж | `bookshelf` | 1, 1, 8 |
| гостиная: стеллаж | `bookshelf` | 1, 2, 8 |
| гостиная: свет | `lantern` `["hanging"=true]` | 5, 3, 10 |
| гостиная: свет | `lantern` `["hanging"=true]` | 6, 3, 12 |
| кухня: столешница | `polished_diorite` | 10, 1, 1 |
| кухня: плита | `smoker` | 11, 1, 1 |
| кухня: мойка | `cauldron` | 12, 1, 1 |
| кухня: шкаф | `barrel` | 13, 1, 1 |
| кухня: столешница | `polished_diorite` | 13, 1, 2 |
| кухня: столешница | `polished_diorite` | 13, 1, 3 |
| кухня: свет | `lantern` `["hanging"=true]` | 11, 3, 3 |
| столовая: стол | `spruce_slab` `["minecraft:vertical_half"="top"]` | 11, 1, 6 |
| столовая: стол | `spruce_slab` `["minecraft:vertical_half"="top"]` | 12, 1, 6 |
| столовая: стол | `spruce_slab` `["minecraft:vertical_half"="top"]` | 11, 1, 7 |
| столовая: стол | `spruce_slab` `["minecraft:vertical_half"="top"]` | 12, 1, 7 |
| столовая: стул | `spruce_stairs` `["weirdo_direction"=1,"upside_down_bit"=false]` | 10, 1, 6 |
| столовая: стул | `spruce_stairs` `["weirdo_direction"=1,"upside_down_bit"=false]` | 10, 1, 7 |
| столовая: стул | `spruce_stairs` `["weirdo_direction"=0,"upside_down_bit"=false]` | 13, 1, 6 |
| столовая: стул | `spruce_stairs` `["weirdo_direction"=0,"upside_down_bit"=false]` | 13, 1, 7 |
| столовая: свет | `lantern` `["hanging"=true]` | 12, 3, 7 |
| лоджия: столик | `spruce_slab` `["minecraft:vertical_half"="top"]` | 12, 1, 12 |
| лоджия: кресло | `spruce_stairs` `["weirdo_direction"=1,"upside_down_bit"=false]` | 11, 1, 12 |
| лоджия: кресло | `spruce_stairs` `["weirdo_direction"=0,"upside_down_bit"=false]` | 13, 1, 12 |
| кабинет: письменный стол | `spruce_slab` `["minecraft:vertical_half"="top"]` | 2, 5, 1 |
| кабинет: письменный стол | `spruce_slab` `["minecraft:vertical_half"="top"]` | 3, 5, 1 |
| кабинет: стул | `spruce_stairs` `["weirdo_direction"=2,"upside_down_bit"=false]` | 2, 5, 2 |
| кабинет: книги | `bookshelf` | 4, 5, 3 |
| кабинет: книги | `bookshelf` | 4, 6, 3 |
| санузел: ванна | `cauldron` | 1, 5, 5 |
| санузел: ванна | `cauldron` | 2, 5, 5 |
| санузел: раковина | `cauldron` | 4, 5, 6 |
| санузел: унитаз | `hopper` | 1, 5, 6 |
| спальня: кровать, изголовье | `bed` (ставится вручную) | 1, 5, 9 |
| спальня: кровать, изножье | `bed` (ставится вручную) | 2, 5, 9 |
| спальня: тумба | `barrel` | 1, 5, 8 |
| спальня: тумба | `barrel` | 1, 5, 10 |
| спальня: ночник | `lantern` `["hanging"=false]` | 1, 6, 8 |
| спальня: комод | `barrel` | 8, 5, 8 |
| спальня: кресло | `spruce_stairs` `["weirdo_direction"=2,"upside_down_bit"=false]` | 7, 5, 10 |
| балкон: кресло | `spruce_stairs` `["weirdo_direction"=3,"upside_down_bit"=false]` | 2, 5, 12 |
| балкон: кресло | `spruce_stairs` `["weirdo_direction"=3,"upside_down_bit"=false]` | 7, 5, 12 |
| камин: огонь | `campfire` | 0, 1, 10 |
| камин: очаг | `calcite` | 1, 0, 9–11 |

**Свет.** Видимых факелов нет. Источники такие:

- Жаболампы `ochre_froglight` заподлицо в софитах свесов, через каждые 4 блока (клетки, где x+z делится на 4): нижний свес Y=4, верхний Y=8. Ещё 4 штуки в потолке лоджии (11,4,11), (13,4,11), (11,4,13), (13,4,13). Сверху их закрывает кровля, свет идёт только вниз.
- Жаболампы в потолке 2-го этажа (Y=8): кабинет (2,8,2), холл (7,8,2) и (7,8,5), санузел (2,8,5), спальня (3,8,9) и (6,8,9).
- Подвесные фонари на 1-м этаже висят под перекрытием на Y=3. Ночник — стоячий фонарь на тумбе.

## 7. Порядок строительства

Этапы совпадают с разделами в `prairie_villa.mcfunction`. В скобках — сколько блоков ставит этап.

1. **Подготовка участка** (170) — Расчистить участок 23×23 от Y=0 до Y=12 и выложить газон на Y=-1.
2. **Фундамент (Y=-1)** (326) — Залить фундамент 15×15 и основания террас полированным андезитом, проложить дорожку X=3 к входу.
3. **Полы и террасы (Y=0)** (275) — Пол 1-го этажа: гладкий камень с полосами туфа на Z=4 и Z=11, андезит в кухне, кальцитовый очаг. Лоджия, южная (X0–16, Z15–18) и восточная (X15–17, Z4–14) террасы с полосой туфа и кальцитовой кромкой. Ступени в сад.
4. **Стены 1-го этажа** (164) — Цоколь из песчаника на Y=0, кирпичные стены Y=1–3 с вкраплениями грязевого кирпича, кальцитовые пилоны на углах и в простенках, столб лоджии (14,0–4,14), кирпичные перегородки.
5. **Перекрытие и нижние свесы (Y=4)** (361) — Перекрытие Y=4: поясная тяга из песчаника по периметру, доски внутри, пол балкона из гладкого камня. Нижний свес: торец из бревна, софит из досок с жаболампами. Лестница и закрытый марш.
6. **Стены 2-го этажа и балкон** (125) — Стены 2-го этажа (Y=5–7), пилоны, перегородки из досок, перила у проёма, кальцитовый парапет балкона.
7. **Потолок 2-го этажа и верхние свесы (Y=8)** (212) — Потолок 2-го этажа Y=8: тяга из песчаника по стенам, доски внутри. Верхний свес на 2 блока: торец из бревна, софит, жаболампы.
8. **Окна и рамы** (180) — Стеклянные панели во все проёмы, рамы-перемычки из люков тёмного дуба (верхние, закрытые) снаружи над каждым окном. После этого вручную поставить 6 дверей (см. ниже).
9. **Нижняя крыша (Y=5..6)** (283) — Нижняя крыша: слэб по кромке на Y=5, ступени ската на втором ряду, полные плитки над крылом и лоджией, сверху плоский слой слэбов на Y=6.
10. **Верхняя крыша (Y=9..10)** (335) — Верхняя крыша по той же схеме: Y=9 — кромка, скат, тело; Y=10 — плоский верх из слэбов.
11. **Каминная труба** (83) — Каминная труба 2×3 из кальцита от Y=-1 до Y=11, оголовок из диорита на Y=12. Она проходит сквозь стены и оба свеса.
12. **Интерьер и свет** (56) — Мебель, костёр в камине, фонари, жаболампы в потолке 2-го этажа. Кровать ставится вручную.
13. **Ландшафт** (212) — Кашпо из диорита с мхом и кустами азалии (на террасах, у входа, в парапете балкона), три цветущих азалиевых дерева на мху.

**Двери и кровать ставятся вручную**: состояния направления дверей в Bedrock менялись между версиями, а рукой их ставить надёжнее.

- Наружные: (3,1,0) — ставить, стоя снаружи с севера; (9,1,11) — стоя на лоджии с востока; (4,5,11) — стоя на балконе с юга.
- Внутренние: (5,5,2) и (5,5,5) — стоя в холле с востока; (6,5,7) — стоя в холле с севера.
- Кровать: изголовье в (1,5,9), изножье в (2,5,9). Ставить, стоя в (3,5,9) лицом на запад.

## 8. Команды Bedrock

**Как запускать.** Встаньте на газон так, чтобы ноги были в блоке будущего северо-западного угла фундамента: это и есть (0,0,0), то есть `~ ~ ~`. Смотрите на юг. Самый надёжный способ — положить `prairie_villa.mcfunction` в `functions/` behavior pack и выполнить `/function prairie_villa`. Можно и командными блоками, по одной строке. Каждая команда `fill` укладывается в лимит 32 768 блоков, самая большая — расчистка, 7 406 блоков. Перед запуском убедитесь, что вся область 23×23 прогружена.

**Синтаксис Bedrock 26.x, проверенный для этого чертежа:**

- `/fill x1 y1 z1 x2 y2 z2 <id> [состояния]` и `/setblock x y z <id> [состояния]`. Состояния пишутся в квадратных скобках как `"имя"=значение`: строки в кавычках, числа и `true`/`false` без кавычек.
- **Слэбы:** `["minecraft:vertical_half"="top"]` или `"bottom"`. Состояние `top_slot_bit` из задания устарело: начиная с 1.20.30 слэбы перевели на `minecraft:vertical_half`, и в 26.x команда с `top_slot_bit` выдаст ошибку.
- **Ступени:** `["weirdo_direction"=N,"upside_down_bit"=false]`, где 0 — восток, 1 — запад, 2 — юг, 3 — север. N указывает, куда поднимается ступень, там же её высокая сторона. Угловые формы на углах вальмы Bedrock строит сам.
- **Брёвна:** `["pillar_axis"="x"|"y"|"z"]`. Торцевая полоса карниза уложена вдоль кромки.
- **Листва:** `["persistent_bit"=true]`. Без этого кусты в кашпо опадут, потому что рядом с ними нет ствола.
- **Фонарь:** `["hanging"=true]` — подвесной. **Люк-перемычка:** `["upside_down_bit"=true,"open_bit"=false]` — закрытая пластина в верхней половине блока.

Ниже полный список, 431 команд, в порядке выполнения. Он совпадает с `.mcfunction`, только там строки без начального `/`.

### 0. Подготовка участка

```
/fill ~-3 ~ ~-3 ~19 ~12 ~19 air
/fill ~-3 ~-1 ~-3 ~2 ~-1 ~-1 grass_block
/fill ~4 ~-1 ~-3 ~19 ~-1 ~-2 grass_block
/fill ~4 ~-1 ~-1 ~16 ~-1 ~-1 grass_block
/fill ~-3 ~-1 ~ ~-1 ~-1 ~8 grass_block
/fill ~15 ~-1 ~ ~16 ~-1 ~3 grass_block
/fill ~17 ~-1 ~2 ~19 ~-1 ~3 grass_block
/fill ~18 ~-1 ~4 ~19 ~-1 ~16 grass_block
/fill ~-3 ~-1 ~9 ~-2 ~-1 ~16 grass_block
/fill ~-1 ~-1 ~12 ~-1 ~-1 ~16 grass_block
/fill ~17 ~-1 ~15 ~17 ~-1 ~16 grass_block
/fill ~ ~-1 ~19 ~16 ~-1 ~19 grass_block
```

### 1. Фундамент (Y=-1)

```
/fill ~3 ~-1 ~-3 ~3 ~-1 ~18 polished_andesite
/fill ~ ~-1 ~ ~2 ~-1 ~8 polished_andesite
/fill ~4 ~-1 ~ ~14 ~-1 ~18 polished_andesite
/fill ~15 ~-1 ~4 ~17 ~-1 ~14 polished_andesite
/fill ~1 ~-1 ~9 ~2 ~-1 ~18 polished_andesite
/fill ~ ~-1 ~12 ~ ~-1 ~18 polished_andesite
/fill ~15 ~-1 ~15 ~16 ~-1 ~18 polished_andesite
```

### 2. Полы и террасы (Y=0)

```
/fill ~10 ~ ~1 ~13 ~ ~8 polished_andesite
/fill ~15 ~ ~4 ~15 ~ ~15 polished_andesite
/fill ~10 ~ ~10 ~14 ~ ~11 polished_andesite
/fill ~10 ~ ~13 ~14 ~ ~13 polished_andesite
/fill ~10 ~ ~14 ~13 ~ ~15 polished_andesite
/fill ~ ~ ~15 ~9 ~ ~15 polished_andesite
/setblock ~14 ~ ~15 polished_andesite
/setblock ~16 ~ ~15 polished_andesite
/fill ~ ~ ~17 ~16 ~ ~17 polished_andesite
/fill ~17 ~ ~4 ~17 ~ ~14 calcite
/fill ~1 ~ ~9 ~1 ~ ~11 calcite
/fill ~ ~ ~18 ~16 ~ ~18 calcite
/fill ~1 ~ ~1 ~9 ~ ~3 smooth_stone
/fill ~1 ~ ~5 ~9 ~ ~8 smooth_stone
/fill ~2 ~ ~9 ~8 ~ ~10 smooth_stone
/fill ~1 ~ ~12 ~8 ~ ~13 smooth_stone
/setblock ~3 ~ ~-1 smooth_stone_slab ["minecraft:vertical_half"="bottom"]
/fill ~6 ~ ~19 ~10 ~ ~19 smooth_stone_slab ["minecraft:vertical_half"="bottom"]
/fill ~1 ~ ~4 ~9 ~ ~4 polished_tuff
/fill ~16 ~ ~4 ~16 ~ ~14 polished_tuff
/fill ~2 ~ ~11 ~8 ~ ~11 polished_tuff
/fill ~10 ~ ~12 ~14 ~ ~12 polished_tuff
/fill ~ ~ ~16 ~16 ~ ~16 polished_tuff
```

### 3. Стены 1-го этажа

```
/fill ~1 ~1 ~ ~1 ~3 ~ brick_block
/fill ~6 ~1 ~ ~8 ~3 ~ brick_block
/setblock ~10 ~1 ~ brick_block
/fill ~12 ~1 ~ ~13 ~1 ~ brick_block
/fill ~ ~1 ~1 ~ ~3 ~2 brick_block
/fill ~9 ~1 ~1 ~9 ~3 ~4 brick_block
/fill ~14 ~1 ~1 ~14 ~1 ~2 brick_block
/fill ~ ~1 ~4 ~ ~1 ~6 brick_block
/setblock ~14 ~1 ~4 brick_block
/fill ~9 ~1 ~6 ~9 ~3 ~6 brick_block
/fill ~1 ~1 ~7 ~3 ~3 ~7 brick_block
/fill ~ ~1 ~8 ~ ~3 ~8 brick_block
/fill ~10 ~1 ~9 ~10 ~3 ~9 brick_block
/fill ~9 ~1 ~13 ~9 ~3 ~13 brick_block
/fill ~14 ~2 ~1 ~14 ~3 ~1 brick_block
/fill ~ ~2 ~6 ~ ~3 ~6 brick_block
/fill ~ ~ ~ ~ ~3 ~ calcite
/fill ~5 ~ ~ ~5 ~3 ~ calcite
/fill ~9 ~ ~ ~9 ~3 ~ calcite
/fill ~14 ~ ~ ~14 ~3 ~ calcite
/fill ~14 ~ ~5 ~14 ~3 ~5 calcite
/fill ~ ~ ~7 ~ ~3 ~7 calcite
/fill ~9 ~ ~9 ~9 ~3 ~9 calcite
/fill ~14 ~ ~9 ~14 ~3 ~9 calcite
/fill ~ ~ ~14 ~ ~3 ~14 calcite
/fill ~4 ~ ~14 ~4 ~3 ~14 calcite
/fill ~9 ~ ~14 ~9 ~3 ~14 calcite
/fill ~14 ~ ~14 ~14 ~4 ~14 calcite
/setblock ~11 ~1 ~ mud_bricks
/setblock ~ ~1 ~3 mud_bricks
/setblock ~14 ~1 ~3 mud_bricks
/fill ~9 ~1 ~5 ~9 ~3 ~5 mud_bricks
/fill ~13 ~1 ~9 ~13 ~3 ~9 mud_bricks
/fill ~1 ~ ~ ~4 ~ ~ smooth_sandstone
/fill ~6 ~ ~ ~8 ~ ~ smooth_sandstone
/fill ~10 ~ ~ ~13 ~ ~ smooth_sandstone
/fill ~ ~ ~1 ~ ~ ~6 smooth_sandstone
/fill ~14 ~ ~1 ~14 ~ ~4 smooth_sandstone
/fill ~14 ~ ~6 ~14 ~ ~8 smooth_sandstone
/setblock ~ ~ ~8 smooth_sandstone
/fill ~10 ~ ~9 ~13 ~ ~9 smooth_sandstone
/fill ~9 ~ ~10 ~9 ~ ~13 smooth_sandstone
/fill ~ ~ ~12 ~ ~ ~13 smooth_sandstone
/fill ~1 ~ ~14 ~3 ~ ~14 smooth_sandstone
/fill ~5 ~ ~14 ~8 ~ ~14 smooth_sandstone
```

### 4. Перекрытие и нижние свесы (Y=4)

```
/setblock ~1 ~4 ~-1 ochre_froglight
/setblock ~5 ~4 ~-1 ochre_froglight
/setblock ~9 ~4 ~-1 ochre_froglight
/setblock ~13 ~4 ~-1 ochre_froglight
/setblock ~-1 ~4 ~1 ochre_froglight
/setblock ~15 ~4 ~1 ochre_froglight
/setblock ~-1 ~4 ~5 ochre_froglight
/setblock ~15 ~4 ~5 ochre_froglight
/setblock ~15 ~4 ~9 ochre_froglight
/setblock ~11 ~4 ~11 ochre_froglight
/setblock ~13 ~4 ~11 ochre_froglight
/setblock ~-1 ~4 ~13 ochre_froglight
/setblock ~11 ~4 ~13 ochre_froglight
/setblock ~13 ~4 ~13 ochre_froglight
/setblock ~15 ~4 ~13 ochre_froglight
/setblock ~1 ~4 ~15 ochre_froglight
/setblock ~5 ~4 ~15 ochre_froglight
/setblock ~9 ~4 ~15 ochre_froglight
/setblock ~13 ~4 ~15 ochre_froglight
/fill ~-2 ~4 ~-2 ~16 ~4 ~-2 stripped_spruce_log ["pillar_axis"="x"]
/fill ~-2 ~4 ~16 ~16 ~4 ~16 stripped_spruce_log ["pillar_axis"="x"]
/fill ~-2 ~4 ~-1 ~-2 ~4 ~15 stripped_spruce_log ["pillar_axis"="z"]
/fill ~16 ~4 ~-1 ~16 ~4 ~15 stripped_spruce_log ["pillar_axis"="z"]
/fill ~8 ~1 ~3 ~8 ~1 ~5 spruce_planks
/fill ~8 ~2 ~3 ~8 ~2 ~4 spruce_planks
/setblock ~8 ~3 ~3 spruce_planks
/fill ~-1 ~4 ~-1 ~ ~4 ~-1 spruce_planks
/fill ~2 ~4 ~-1 ~4 ~4 ~-1 spruce_planks
/fill ~6 ~4 ~-1 ~8 ~4 ~-1 spruce_planks
/fill ~10 ~4 ~-1 ~12 ~4 ~-1 spruce_planks
/fill ~14 ~4 ~-1 ~15 ~4 ~-1 spruce_planks
/setblock ~-1 ~4 ~ spruce_planks
/setblock ~15 ~4 ~ spruce_planks
/fill ~1 ~4 ~1 ~13 ~4 ~2 spruce_planks
/fill ~-1 ~4 ~2 ~-1 ~4 ~4 spruce_planks
/fill ~15 ~4 ~2 ~15 ~4 ~4 spruce_planks
/fill ~1 ~4 ~3 ~7 ~4 ~11 spruce_planks
/fill ~9 ~4 ~3 ~13 ~4 ~8 spruce_planks
/fill ~-1 ~4 ~6 ~-1 ~4 ~8 spruce_planks
/fill ~8 ~4 ~6 ~8 ~4 ~11 spruce_planks
/fill ~15 ~4 ~6 ~15 ~4 ~8 spruce_planks
/fill ~10 ~4 ~10 ~15 ~4 ~10 spruce_planks
/fill ~10 ~4 ~11 ~10 ~4 ~15 spruce_planks
/fill ~12 ~4 ~11 ~12 ~4 ~15 spruce_planks
/fill ~14 ~4 ~11 ~15 ~4 ~12 spruce_planks
/setblock ~-1 ~4 ~12 spruce_planks
/setblock ~11 ~4 ~12 spruce_planks
/setblock ~13 ~4 ~12 spruce_planks
/setblock ~14 ~4 ~13 spruce_planks
/fill ~-1 ~4 ~14 ~-1 ~4 ~15 spruce_planks
/fill ~11 ~4 ~14 ~11 ~4 ~15 spruce_planks
/setblock ~13 ~4 ~14 spruce_planks
/fill ~15 ~4 ~14 ~15 ~4 ~15 spruce_planks
/setblock ~ ~4 ~15 spruce_planks
/fill ~2 ~4 ~15 ~4 ~4 ~15 spruce_planks
/fill ~6 ~4 ~15 ~8 ~4 ~15 spruce_planks
/setblock ~14 ~4 ~15 spruce_planks
/fill ~ ~4 ~ ~14 ~4 ~ smooth_sandstone
/fill ~ ~4 ~1 ~ ~4 ~8 smooth_sandstone
/fill ~14 ~4 ~1 ~14 ~4 ~9 smooth_sandstone
/fill ~9 ~4 ~9 ~13 ~4 ~9 smooth_sandstone
/fill ~9 ~4 ~10 ~9 ~4 ~14 smooth_sandstone
/fill ~ ~4 ~12 ~ ~4 ~14 smooth_sandstone
/fill ~1 ~4 ~14 ~8 ~4 ~14 smooth_sandstone
/fill ~1 ~4 ~12 ~8 ~4 ~13 smooth_stone
/setblock ~8 ~1 ~6 spruce_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/setblock ~8 ~2 ~5 spruce_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/setblock ~8 ~3 ~4 spruce_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/setblock ~8 ~4 ~3 spruce_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
```

### 5. Стены 2-го этажа и балкон

```
/fill ~1 ~5 ~ ~3 ~5 ~ brick_block
/fill ~5 ~5 ~ ~8 ~5 ~ brick_block
/fill ~ ~5 ~1 ~ ~5 ~2 brick_block
/fill ~9 ~5 ~1 ~9 ~5 ~4 brick_block
/fill ~ ~5 ~4 ~ ~5 ~8 brick_block
/fill ~9 ~5 ~6 ~9 ~5 ~10 brick_block
/fill ~5 ~6 ~ ~6 ~7 ~ brick_block
/fill ~ ~6 ~1 ~ ~7 ~1 brick_block
/fill ~9 ~6 ~1 ~9 ~7 ~1 brick_block
/fill ~ ~6 ~4 ~ ~6 ~7 brick_block
/fill ~9 ~6 ~4 ~9 ~7 ~4 brick_block
/fill ~9 ~6 ~6 ~9 ~7 ~7 brick_block
/setblock ~ ~7 ~4 brick_block
/setblock ~ ~7 ~7 brick_block
/fill ~ ~5 ~ ~ ~7 ~ calcite
/fill ~9 ~5 ~ ~9 ~7 ~ calcite
/fill ~9 ~5 ~11 ~9 ~5 ~14 calcite
/fill ~ ~5 ~12 ~ ~5 ~14 calcite
/setblock ~1 ~5 ~14 calcite
/fill ~4 ~5 ~14 ~5 ~5 ~14 calcite
/setblock ~8 ~5 ~14 calcite
/fill ~9 ~6 ~11 ~9 ~7 ~11 calcite
/fill ~7 ~5 ~4 ~7 ~5 ~6 dark_oak_fence
/setblock ~8 ~5 ~6 dark_oak_fence
/fill ~4 ~5 ~ ~4 ~7 ~ mud_bricks
/setblock ~ ~5 ~3 mud_bricks
/setblock ~9 ~5 ~5 mud_bricks
/fill ~1 ~5 ~11 ~1 ~7 ~11 mud_bricks
/fill ~8 ~5 ~11 ~8 ~7 ~11 mud_bricks
/fill ~5 ~5 ~1 ~5 ~7 ~1 spruce_planks
/fill ~5 ~5 ~3 ~5 ~7 ~4 spruce_planks
/fill ~1 ~5 ~4 ~4 ~7 ~4 spruce_planks
/fill ~5 ~5 ~6 ~5 ~7 ~7 spruce_planks
/fill ~1 ~5 ~7 ~4 ~7 ~7 spruce_planks
/fill ~7 ~5 ~7 ~8 ~7 ~7 spruce_planks
/setblock ~5 ~7 ~2 spruce_planks
/setblock ~5 ~7 ~5 spruce_planks
/setblock ~6 ~7 ~7 spruce_planks
```

### 6. Потолок 2-го этажа и верхние свесы (Y=8)

```
/setblock ~1 ~8 ~-1 ochre_froglight
/setblock ~5 ~8 ~-1 ochre_froglight
/setblock ~9 ~8 ~-1 ochre_froglight
/setblock ~-1 ~8 ~1 ochre_froglight
/setblock ~10 ~8 ~2 ochre_froglight
/setblock ~-1 ~8 ~5 ochre_froglight
/setblock ~10 ~8 ~6 ochre_froglight
/setblock ~10 ~8 ~10 ochre_froglight
/setblock ~ ~8 ~12 ochre_froglight
/setblock ~4 ~8 ~12 ochre_froglight
/setblock ~8 ~8 ~12 ochre_froglight
/fill ~-2 ~8 ~-2 ~11 ~8 ~-2 stripped_spruce_log ["pillar_axis"="x"]
/fill ~-2 ~8 ~13 ~11 ~8 ~13 stripped_spruce_log ["pillar_axis"="x"]
/fill ~-2 ~8 ~-1 ~-2 ~8 ~12 stripped_spruce_log ["pillar_axis"="z"]
/fill ~11 ~8 ~-1 ~11 ~8 ~12 stripped_spruce_log ["pillar_axis"="z"]
/fill ~-1 ~8 ~-1 ~ ~8 ~-1 spruce_planks
/fill ~2 ~8 ~-1 ~4 ~8 ~-1 spruce_planks
/fill ~6 ~8 ~-1 ~8 ~8 ~-1 spruce_planks
/fill ~10 ~8 ~-1 ~10 ~8 ~1 spruce_planks
/setblock ~-1 ~8 ~ spruce_planks
/fill ~1 ~8 ~1 ~8 ~8 ~1 spruce_planks
/fill ~-1 ~8 ~2 ~-1 ~8 ~4 spruce_planks
/fill ~1 ~8 ~2 ~1 ~8 ~10 spruce_planks
/fill ~3 ~8 ~2 ~6 ~8 ~8 spruce_planks
/fill ~8 ~8 ~2 ~8 ~8 ~10 spruce_planks
/fill ~2 ~8 ~3 ~2 ~8 ~4 spruce_planks
/fill ~7 ~8 ~3 ~7 ~8 ~4 spruce_planks
/fill ~10 ~8 ~3 ~10 ~8 ~5 spruce_planks
/fill ~-1 ~8 ~6 ~-1 ~8 ~8 spruce_planks
/fill ~2 ~8 ~6 ~2 ~8 ~10 spruce_planks
/fill ~7 ~8 ~6 ~7 ~8 ~10 spruce_planks
/fill ~10 ~8 ~7 ~10 ~8 ~9 spruce_planks
/fill ~4 ~8 ~9 ~5 ~8 ~10 spruce_planks
/setblock ~3 ~8 ~10 spruce_planks
/setblock ~6 ~8 ~10 spruce_planks
/fill ~10 ~8 ~11 ~10 ~8 ~12 spruce_planks
/setblock ~-1 ~8 ~12 spruce_planks
/fill ~1 ~8 ~12 ~3 ~8 ~12 spruce_planks
/fill ~5 ~8 ~12 ~7 ~8 ~12 spruce_planks
/setblock ~9 ~8 ~12 spruce_planks
/fill ~ ~8 ~ ~9 ~8 ~ smooth_sandstone
/fill ~ ~8 ~1 ~ ~8 ~8 smooth_sandstone
/fill ~9 ~8 ~1 ~9 ~8 ~11 smooth_sandstone
/fill ~1 ~8 ~11 ~8 ~8 ~11 smooth_sandstone
```

### 7. Окна и рамы

```
/fill ~2 ~1 ~ ~2 ~3 ~ gray_stained_glass_pane
/fill ~4 ~1 ~ ~4 ~3 ~ gray_stained_glass_pane
/fill ~14 ~1 ~6 ~14 ~3 ~8 gray_stained_glass_pane
/fill ~11 ~1 ~9 ~12 ~3 ~9 gray_stained_glass_pane
/fill ~9 ~1 ~10 ~9 ~3 ~10 gray_stained_glass_pane
/fill ~ ~1 ~12 ~ ~3 ~13 gray_stained_glass_pane
/fill ~9 ~1 ~12 ~9 ~3 ~12 gray_stained_glass_pane
/fill ~1 ~1 ~14 ~3 ~3 ~14 gray_stained_glass_pane
/fill ~5 ~1 ~14 ~8 ~3 ~14 gray_stained_glass_pane
/fill ~10 ~2 ~ ~13 ~3 ~ gray_stained_glass_pane
/fill ~14 ~2 ~2 ~14 ~3 ~4 gray_stained_glass_pane
/fill ~ ~2 ~3 ~ ~3 ~5 gray_stained_glass_pane
/setblock ~3 ~3 ~ gray_stained_glass_pane
/setblock ~9 ~3 ~11 gray_stained_glass_pane
/fill ~2 ~5 ~11 ~3 ~7 ~11 gray_stained_glass_pane
/fill ~5 ~5 ~11 ~7 ~7 ~11 gray_stained_glass_pane
/fill ~1 ~6 ~ ~3 ~7 ~ gray_stained_glass_pane
/fill ~7 ~6 ~ ~8 ~7 ~ gray_stained_glass_pane
/fill ~ ~6 ~2 ~ ~7 ~3 gray_stained_glass_pane
/fill ~9 ~6 ~2 ~9 ~7 ~3 gray_stained_glass_pane
/fill ~9 ~6 ~5 ~9 ~7 ~5 gray_stained_glass_pane
/fill ~ ~6 ~8 ~ ~7 ~8 gray_stained_glass_pane
/fill ~9 ~6 ~8 ~9 ~7 ~10 gray_stained_glass_pane
/fill ~ ~7 ~5 ~ ~7 ~6 gray_stained_glass_pane
/setblock ~4 ~7 ~11 gray_stained_glass_pane
/fill ~2 ~3 ~-1 ~4 ~3 ~-1 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~10 ~3 ~-1 ~13 ~3 ~-1 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~15 ~3 ~2 ~15 ~3 ~4 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~-1 ~3 ~3 ~-1 ~3 ~5 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~15 ~3 ~6 ~15 ~3 ~8 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~10 ~3 ~10 ~12 ~3 ~10 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~10 ~3 ~11 ~10 ~3 ~12 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~-1 ~3 ~12 ~-1 ~3 ~13 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~1 ~3 ~15 ~3 ~3 ~15 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~5 ~3 ~15 ~8 ~3 ~15 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~1 ~7 ~-1 ~3 ~7 ~-1 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~7 ~7 ~-1 ~8 ~7 ~-1 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~-1 ~7 ~2 ~-1 ~7 ~3 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~10 ~7 ~2 ~10 ~7 ~3 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~-1 ~7 ~5 ~-1 ~7 ~6 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/setblock ~10 ~7 ~5 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/setblock ~-1 ~7 ~8 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~10 ~7 ~8 ~10 ~7 ~10 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
/fill ~2 ~7 ~12 ~7 ~7 ~12 dark_oak_trapdoor ["upside_down_bit"=true,"open_bit"=false]
```

### 8. Нижняя крыша (Y=5..6)

```
/fill ~10 ~5 ~ ~14 ~5 ~14 deepslate_tiles
/fill ~-2 ~5 ~-2 ~16 ~5 ~-2 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~-2 ~5 ~-1 ~-2 ~5 ~16 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~16 ~5 ~-1 ~16 ~5 ~16 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~-1 ~5 ~16 ~15 ~5 ~16 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~10 ~6 ~ ~14 ~6 ~14 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~15 ~5 ~ ~15 ~5 ~14 deepslate_tile_stairs ["weirdo_direction"=1,"upside_down_bit"=false]
/fill ~-1 ~5 ~ ~-1 ~5 ~8 deepslate_tile_stairs ["weirdo_direction"=0,"upside_down_bit"=false]
/fill ~-1 ~5 ~12 ~-1 ~5 ~14 deepslate_tile_stairs ["weirdo_direction"=0,"upside_down_bit"=false]
/fill ~-1 ~5 ~15 ~15 ~5 ~15 deepslate_tile_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/fill ~-1 ~5 ~-1 ~15 ~5 ~-1 deepslate_tile_stairs ["weirdo_direction"=2,"upside_down_bit"=false]
```

### 9. Верхняя крыша (Y=9..10)

```
/fill ~ ~9 ~ ~9 ~9 ~8 deepslate_tiles
/fill ~1 ~9 ~9 ~9 ~9 ~11 deepslate_tiles
/fill ~-2 ~9 ~-2 ~11 ~9 ~-2 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~-2 ~9 ~-1 ~-2 ~9 ~13 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~11 ~9 ~-1 ~11 ~9 ~13 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~-1 ~9 ~13 ~10 ~9 ~13 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~ ~10 ~ ~9 ~10 ~8 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~1 ~10 ~9 ~9 ~10 ~11 deepslate_tile_slab ["minecraft:vertical_half"="bottom"]
/fill ~10 ~9 ~ ~10 ~9 ~11 deepslate_tile_stairs ["weirdo_direction"=1,"upside_down_bit"=false]
/fill ~-1 ~9 ~ ~-1 ~9 ~8 deepslate_tile_stairs ["weirdo_direction"=0,"upside_down_bit"=false]
/fill ~-1 ~9 ~12 ~10 ~9 ~12 deepslate_tile_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/fill ~-1 ~9 ~-1 ~10 ~9 ~-1 deepslate_tile_stairs ["weirdo_direction"=2,"upside_down_bit"=false]
```

### 10. Каминная труба

```
/fill ~-1 ~-1 ~9 ~ ~ ~11 calcite
/fill ~-1 ~1 ~9 ~ ~11 ~9 calcite
/fill ~-1 ~1 ~10 ~-1 ~11 ~11 calcite
/fill ~ ~1 ~11 ~ ~11 ~11 calcite
/fill ~ ~2 ~10 ~ ~11 ~10 calcite
/fill ~-1 ~12 ~9 ~ ~12 ~11 polished_diorite
```

### 11. Интерьер и свет

```
/fill ~7 ~1 ~1 ~8 ~1 ~1 barrel
/setblock ~13 ~1 ~1 barrel
/setblock ~1 ~5 ~8 barrel
/setblock ~8 ~5 ~8 barrel
/setblock ~1 ~5 ~10 barrel
/fill ~1 ~1 ~8 ~1 ~2 ~8 bookshelf
/fill ~4 ~5 ~3 ~4 ~6 ~3 bookshelf
/setblock ~ ~1 ~10 campfire
/setblock ~12 ~1 ~1 cauldron
/fill ~1 ~5 ~5 ~2 ~5 ~5 cauldron
/setblock ~4 ~5 ~6 cauldron
/setblock ~10 ~1 ~1 polished_diorite
/fill ~13 ~1 ~2 ~13 ~1 ~3 polished_diorite
/setblock ~2 ~8 ~2 ochre_froglight
/setblock ~7 ~8 ~2 ochre_froglight
/setblock ~2 ~8 ~5 ochre_froglight
/setblock ~7 ~8 ~5 ochre_froglight
/setblock ~3 ~8 ~9 ochre_froglight
/setblock ~6 ~8 ~9 ochre_froglight
/setblock ~1 ~5 ~6 hopper
/setblock ~1 ~6 ~8 lantern ["hanging"=false]
/setblock ~4 ~3 ~3 lantern ["hanging"=true]
/setblock ~11 ~3 ~3 lantern ["hanging"=true]
/setblock ~12 ~3 ~7 lantern ["hanging"=true]
/setblock ~5 ~3 ~10 lantern ["hanging"=true]
/setblock ~6 ~3 ~12 lantern ["hanging"=true]
/setblock ~11 ~1 ~1 smoker
/setblock ~2 ~1 ~10 spruce_slab ["minecraft:vertical_half"="bottom"]
/fill ~11 ~1 ~6 ~12 ~1 ~7 spruce_slab ["minecraft:vertical_half"="top"]
/setblock ~12 ~1 ~12 spruce_slab ["minecraft:vertical_half"="top"]
/fill ~2 ~5 ~1 ~3 ~5 ~1 spruce_slab ["minecraft:vertical_half"="top"]
/fill ~1 ~1 ~4 ~1 ~1 ~5 spruce_stairs ["weirdo_direction"=1,"upside_down_bit"=false]
/fill ~10 ~1 ~6 ~10 ~1 ~7 spruce_stairs ["weirdo_direction"=1,"upside_down_bit"=false]
/setblock ~11 ~1 ~12 spruce_stairs ["weirdo_direction"=1,"upside_down_bit"=false]
/fill ~13 ~1 ~6 ~13 ~1 ~7 spruce_stairs ["weirdo_direction"=0,"upside_down_bit"=false]
/fill ~4 ~1 ~9 ~4 ~1 ~11 spruce_stairs ["weirdo_direction"=0,"upside_down_bit"=false]
/setblock ~13 ~1 ~12 spruce_stairs ["weirdo_direction"=0,"upside_down_bit"=false]
/setblock ~2 ~5 ~12 spruce_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/setblock ~7 ~5 ~12 spruce_stairs ["weirdo_direction"=3,"upside_down_bit"=false]
/setblock ~2 ~5 ~2 spruce_stairs ["weirdo_direction"=2,"upside_down_bit"=false]
/setblock ~7 ~5 ~10 spruce_stairs ["weirdo_direction"=2,"upside_down_bit"=false]
```

### 12. Ландшафт

```
/fill ~6 ~1 ~-2 ~7 ~1 ~-2 azalea_leaves ["persistent_bit"=true]
/fill ~16 ~2 ~6 ~16 ~2 ~7 azalea_leaves ["persistent_bit"=true]
/fill ~2 ~2 ~17 ~3 ~2 ~17 azalea_leaves ["persistent_bit"=true]
/fill ~14 ~2 ~17 ~15 ~2 ~17 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~3 ~-1 ~19 ~3 ~-1 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~3 ~1 ~19 ~4 ~1 azalea_leaves ["persistent_bit"=true]
/fill ~-3 ~3 ~17 ~-1 ~3 ~17 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~3 ~17 ~19 ~3 ~17 azalea_leaves ["persistent_bit"=true]
/fill ~-3 ~3 ~19 ~-1 ~4 ~19 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~3 ~19 ~19 ~4 ~19 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~4 ~ ~17 ~5 ~ azalea_leaves ["persistent_bit"=true]
/fill ~19 ~4 ~ ~19 ~5 ~ azalea_leaves ["persistent_bit"=true]
/fill ~-3 ~4 ~18 ~-3 ~5 ~18 azalea_leaves ["persistent_bit"=true]
/fill ~-1 ~4 ~18 ~-1 ~5 ~18 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~4 ~18 ~17 ~5 ~18 azalea_leaves ["persistent_bit"=true]
/fill ~19 ~4 ~18 ~19 ~5 ~18 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~5 ~-1 ~19 ~5 ~-1 azalea_leaves ["persistent_bit"=true]
/setblock ~18 ~5 ~ azalea_leaves ["persistent_bit"=true]
/fill ~-3 ~5 ~17 ~-1 ~5 ~17 azalea_leaves ["persistent_bit"=true]
/fill ~17 ~5 ~17 ~19 ~5 ~17 azalea_leaves ["persistent_bit"=true]
/setblock ~-2 ~5 ~18 azalea_leaves ["persistent_bit"=true]
/setblock ~18 ~5 ~18 azalea_leaves ["persistent_bit"=true]
/setblock ~18 ~6 ~-1 azalea_leaves ["persistent_bit"=true]
/setblock ~18 ~6 ~1 azalea_leaves ["persistent_bit"=true]
/setblock ~2 ~6 ~14 azalea_leaves ["persistent_bit"=true]
/setblock ~6 ~6 ~14 azalea_leaves ["persistent_bit"=true]
/setblock ~-2 ~6 ~17 azalea_leaves ["persistent_bit"=true]
/setblock ~18 ~6 ~17 azalea_leaves ["persistent_bit"=true]
/setblock ~-2 ~6 ~19 azalea_leaves ["persistent_bit"=true]
/setblock ~18 ~6 ~19 azalea_leaves ["persistent_bit"=true]
/setblock ~8 ~1 ~-2 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~16 ~2 ~5 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~1 ~2 ~17 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~13 ~2 ~17 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~17 ~3 ~ azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~19 ~3 ~ azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~-3 ~3 ~18 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~-1 ~3 ~18 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~17 ~3 ~18 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~19 ~3 ~18 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~17 ~4 ~-1 ~19 ~4 ~-1 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~-3 ~4 ~17 ~-1 ~4 ~17 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~17 ~4 ~17 ~19 ~4 ~17 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~17 ~5 ~1 ~19 ~5 ~1 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~-3 ~5 ~19 ~-1 ~5 ~19 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~17 ~5 ~19 ~19 ~5 ~19 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~17 ~6 ~ ~19 ~6 ~ azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~3 ~6 ~14 azalea_leaves_flowered ["persistent_bit"=true]
/setblock ~7 ~6 ~14 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~-3 ~6 ~18 ~-1 ~6 ~18 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~17 ~6 ~18 ~19 ~6 ~18 azalea_leaves_flowered ["persistent_bit"=true]
/fill ~5 ~ ~-3 ~9 ~ ~-3 polished_diorite
/fill ~5 ~ ~-2 ~5 ~ ~-1 polished_diorite
/fill ~9 ~ ~-2 ~9 ~ ~-1 polished_diorite
/fill ~6 ~ ~-1 ~8 ~ ~-1 polished_diorite
/fill ~15 ~1 ~4 ~17 ~1 ~4 polished_diorite
/fill ~15 ~1 ~5 ~15 ~1 ~8 polished_diorite
/fill ~17 ~1 ~5 ~17 ~1 ~8 polished_diorite
/setblock ~16 ~1 ~8 polished_diorite
/fill ~ ~1 ~16 ~4 ~1 ~16 polished_diorite
/fill ~12 ~1 ~16 ~16 ~1 ~16 polished_diorite
/fill ~ ~1 ~17 ~ ~1 ~18 polished_diorite
/fill ~4 ~1 ~17 ~4 ~1 ~18 polished_diorite
/fill ~12 ~1 ~17 ~12 ~1 ~18 polished_diorite
/fill ~16 ~1 ~17 ~16 ~1 ~18 polished_diorite
/fill ~1 ~1 ~18 ~3 ~1 ~18 polished_diorite
/fill ~13 ~1 ~18 ~15 ~1 ~18 polished_diorite
/fill ~17 ~-1 ~-1 ~19 ~-1 ~1 moss_block
/fill ~-3 ~-1 ~17 ~-1 ~-1 ~19 moss_block
/fill ~17 ~-1 ~17 ~19 ~-1 ~19 moss_block
/fill ~6 ~ ~-2 ~8 ~ ~-2 moss_block
/fill ~16 ~1 ~5 ~16 ~1 ~7 moss_block
/fill ~1 ~1 ~17 ~3 ~1 ~17 moss_block
/fill ~13 ~1 ~17 ~15 ~1 ~17 moss_block
/fill ~2 ~5 ~14 ~3 ~5 ~14 moss_block
/fill ~6 ~5 ~14 ~7 ~5 ~14 moss_block
/fill ~18 ~ ~ ~18 ~4 ~ oak_log ["pillar_axis"="y"]
/fill ~-2 ~ ~18 ~-2 ~4 ~18 oak_log ["pillar_axis"="y"]
/fill ~18 ~ ~18 ~18 ~4 ~18 oak_log ["pillar_axis"="y"]
```

## Проверки

`generate.py` прерывается с ошибкой, если хоть одна проверка не прошла. Этот документ записан, значит прошли все:

1. **Согласованность.** Список команд проигрывается на пустом поле, и результат сравнивается с моделью блок в блок (вместе с состояниями). Совпадают все клетки, кроме 6 дверей и кровати, которые ставятся вручную. Ведомость, планы и фасады считаются из той же модели.
2. **Нет висящих блоков.** Каждый блок связан по граням с фундаментом или газоном Y=-1: свесы держатся за стены, фонари за потолок, кусты за мох.
3. **Оболочка замкнута.** Воздух из любой комнаты обоих этажей при закрытых дверях не выходит наружу. Значит, в стенах, окнах, перекрытии и потолке нет дыр. Лоджия и балкон открыты намеренно.
4. **Крыши без дыр.** Слой Y=5 нижней крыши (кроме части над вторым этажом и балконом) и слой Y=9 верхней крыши заполнены полностью.
5. **Лестница проходима.** Над каждой из 4 ступеней и над площадкой (8,4,2) — 2 блока воздуха.
6. **Всё в пределах участка** X −3…19, Z −3…19, Y −1…12. Доля грязевого кирпича — от 12 до 18%, сейчас 15.7%.

## Сводка

- **Габариты дома с крышей:** 19 × 19 × 14 (X × Z × Y). Это X -2…16, Z -2…16, Y -1…12, считая фундамент и трубу. Над землёй — 13 блоков (Y 0…12), конёк верхней крыши на Y=10, труба до Y=12.
- **Основание:** 15 × 15. **2-й этаж:** 10 × 12. **Участок:** 23 × 23.
- **Всего блоков: 2782** (43 ст. + 30), из них 170 — газон участка. Команд: 431.
