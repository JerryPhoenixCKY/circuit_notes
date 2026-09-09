---
tags:
  - 电路学
  - 器件
  - 数字电路
  - 开关
date: 2026-09-07
aliases:
  - The MOSFET Switch
  - MOSFET 开关
  - MOSFET Switch
  - Switch Model
  - S Model
  - SR Model
  - Switch-Resistor Model
---

# The MOSFET Switch（MOSFET 开关 / 开关模型）

> [!NOTE]
> 本笔记对应教材 *Foundations of Analog and Digital Electronic Circuits* (Agarwal & Lang) **Ch.6** 与 MIT 6.002 **Lecture 5 *Inside the Digital Gate***。
> 它把 [[MOSFET|MOSFET 场效应管]] 这个三端器件当作**受电压控制的开关 (voltage-controlled switch)** 来使用，由此用开关网络（switch network）搭出全部数字门（digital gates）。器件物理与三工作区见主笔记 [[MOSFET]]；本笔记聚焦 **Ch.6 的开关抽象、门电路实现、开关电阻与静态约束 (static discipline)**。

---

## 1. The Controlled-Switch Abstraction（受控开关抽象）

把 MOSFET 抽象为一个**三端受控开关 (controlled switch)**：

- 两个**数据端** `in` / `out`（即 D、S）；
- 一个**控制端** `C`（即 G）；
- 行为由控制端电平决定：

| 控制端 `C` | `in`–`out` 之间 |
|---|---|
| `C = 0` | **断开 (open circuit)** —— 截止 (OFF) |
| `C = 1` | **短路 (short circuit)** —— 导通 (ON) |

> [!NOTE]
> 这里的 "0 / 1" 指逻辑值（低/高电平），不是具体电压。具体电压由 [[Static Discipline|static discipline]] 的四个阈值 ($V_{OL},V_{IL},V_{IH},V_{OH}$) 决定。

这就是 **S model（Switch model，理想开关模型）**：导通时一根理想导线，截止时彻底断开。

---

## 2. nMOS / pMOS as Switches（nMOS 与 pMOS 作为开关）

MOSFET 分两类，作为开关时极性相反：

- **nMOS（NMOS）**：栅极高电平 → 导通 (ON, short)；栅极低电平 → 截止 (OFF, open)。
  - 用途：**下拉网络 (pull-down network, PDN)** —— 把输出拉向 GND。
- **pMOS（PMOS）**：栅极低电平 → 导通；栅极高电平 → 截止。
  - 用途：**上拉网络 (pull-up network, PUN)** —— 把输出拉向 $V_{DD}$。

> [!IMPORTANT]
> 在绝大多数数字应用里 D、S 行为对称，可互换；只有栅极 G 是控制端，且栅极电流 $i_G \approx 0$（栅氧化层绝缘）。这与 [[MOSFET]] 主笔记的三工作区大信号模型一致：$v_{GS} < V_T$ 截止，$v_{GS} \ge V_T$ 导通。

---

## 3. Building Gates from Switch Networks（用开关网络搭门）

把"逻辑"直接映射成开关的**串 / 并联**连接方式：

| 开关拓扑 | 逻辑功能 | 说明 |
|---|---|---|
| 上拉电阻 + 单个 nMOS 下拉 | **反相器 (NOT / inverter)** | nMOS 导通 → 输出被拉到 GND（"0"）；nMOS 截止 → 输出被上拉到 $V_{DD}$（"1"） |
| 两 nMOS **串联** 下拉 + 上拉 | **NAND** | 任一输入为 "0"（该管截止，下拉断开）→ 输出 "1"；两输入皆为 "1"（两管皆导通，下拉通）→ 输出 "0" |
| 两 nMOS **并联** 下拉 + 上拉 | **NOR** | 任一输入为 "1"（该管导通，下拉接通）→ 输出 "0"；两输入皆为 "0"（皆截止）→ 输出 "1" |
| 串/并组合 | **复合门 (compound gate)** | 例如 $(A\cdot B)+C$ 作下拉网络 → 输出 $\overline{(A\cdot B)+C}$：A、B 串联后再与 C 并联 |

> [!TIP]
> **串联 = AND 语义，并联 = OR 语义**；取反输出即得到 NAND / NOR。任意组合逻辑都能用同一套"开关 + 上拉"范式实现。

### 3.1 The Inverter（反相器，NOT gate）

最基础的门：上拉电阻 $R_L$ 接 $V_S$，下方串一个受控 nMOS 开关到 GND，输入 $A$ 控制栅极。

| $A$ (C) | nMOS | $V_{OUT}$ |
|---|---|---|
| 0 | OFF（开路） | $V_S$ = "1" |
| 1 | ON（短路） | GND = "0" |

真值表即 $B = \overline{A}$。这就是用"受控开关 + 上拉电阻"实现的 **inverter / NOT gate**。

> [!NOTE]
> **抽象的力量 (power of abstraction)**：反相器的符号隐藏了内部 $V_S, R_L,$ GND 等一切细节；所有门共享同一电源与地。后级门只看它的逻辑接口（static discipline），不关心里面是 MOSFET 还是水龙头。

### 3.2 CMOS Inverter（互补 MOS 反相器）

真实芯片用 **CMOS（Complementary MOS）**：上方 **pMOS 上拉** + 下方 **nMOS 下拉**，两管栅极共接输入、漏极共接输出。

![[cmos_inverter.svg]]

> [!IMPORTANT]
> **为什么用 pMOS 上拉而不是电阻上拉？** 电阻上拉的反相器在输出为 "0"（nMOS 导通）时，$R_L$ 上始终有静态电流 $V_S/(R_L+R_{on})$ 流过 → **持续功耗**。CMOS 中 pMOS 在输出 "0" 时截止、nMOS 导通，没有直流通路 → **静态功耗几乎为零**（只在翻转瞬间充放电时耗电）。这正是现代数字集成电路的基石。

---

## 4. The MOSFET as the Switch Device（MOSFET 作为开关器件）

从 [[MOSFET]] 主笔记回顾三端模型：

- **G = gate**（控制端），$i_G \approx 0$；
- **D = drain**、$S = source$（数据端，应用中对称）；
- 可视为 **two-port element**：G–S 为输入（控制）端口，D–S 为输出（受控）端口；
- **阈值电压 $V_T \approx 1\,\text{V}$**（典型值）；
- **S model（开关模型）**：
  - $v_{GS} < V_T$ → D–S **断开 (OFF)**；
  - $v_{GS} \ge V_T$ → D–S **闭合 (ON)**，导通电流。

---

## 5. S Model vs SR Model（理想开关 vs 开关-电阻模型）

理想开关模型 (S model) 把导通当成短路。更精确一点：

> [!NOTE]
> **SR model（Switch-Resistor model）**：导通时 D–S 之间不是理想短路，而是阻值为 **$R_{ON}$** 的有限电阻。
> - $v_{GS} < V_T$ → 断开 (open)；
> - $v_{GS} \ge V_T$ → 等效为电阻 $R_{ON}$（ON）。

从 [[MOSFET]] 平方律可导出导通电阻近似：

$$R_{ON} \;\approx\; \frac{1}{K\,(v_{GS}-V_T)} \qquad (v_{GS} \ge V_T)$$

其中 $K$ 为工艺参数（与 $W/L$ 成正比）。**$v_{GS}-V_T$ 越大 → $R_{ON}$ 越小**，开关越"硬"、越接近理想。

在 i–v 平面上：
- **S model**：导通时 $i_{DS}$–$v_{DS}$ 曲线为**竖直线**（理想短路）；
- **SR model**：导通时为**过原点的直线**，斜率 $1/R_{ON}$，即 $i_{DS}=v_{DS}/R_{ON}$（欧姆定律）。

> [!WARNING]
> $R_{ON}$ 是有限值，这直接破坏了"理想 0/1 电平"：输出高不是完美的 $V_{DD}$，输出低也不是完美的 0（见 §6）。

---

## 6. Inverter Output Set by Resistive Divider（分压决定输出电平）

电阻上拉反相器：nMOS 下拉（ON 时 $R_{ON}$），上方 $R_L$ 上拉到 $V_S$。当 nMOS 导通时，输出由分压决定：

$$V_{OUT} \;=\; V_S\,\frac{R_{ON}}{R_{ON}+R_L} \;\le\; V_{OL}$$

设计准则：**让 $R_{ON} \ll R_L$** 才能使 $V_{OUT} \approx 0$（低电平达标）；而 nMOS 截止时 $V_{OUT}=V_S$（高电平达标，需 $R_{ON,off} \gg R_L$）。即

$$R_{ON}(\text{on}) \;\ll\; R_L \;\ll\; R_{ON}(\text{off})$$

![[inverter_vtc.svg]]

> [!NOTE]
> 上图即电阻上拉反相器的 **VTC（电压传输特性）**：输入低于 $V_T$ 时输出被上拉到高，高于 $V_T$ 后跌到由分压给出的低电平。绿色虚线标出 $V_{OH},V_{IH},V_{IL},V_{OL}$ 与 forbidden region —— 这正是 [[Static Discipline]] 要守住的四个阈值。

---

## 7. Static Discipline Check（用静态约束校验反相器）

反相器必须满足 [[Static Discipline|static discipline]]：只要输入守住合法阈值，输出必守住合法阈值。以 $V_S=5\,\text{V},\; V_T=1\,\text{V}$ 为例：

| 参数 | 值 | 约束 |
|---|---|---|
| $V_{OL}$ | 0.5 V | $V_{OL} < V_{IL}$ |
| $V_{IL}$ | 0.9 V | |
| $V_{OH}$ | 4.5 V | $V_{OH} > V_{IH}$ |
| $V_{IH}$ | 4.1 V | |

满足 $[0,0.5]\subset[0,V_{IL}]$ 且 $[4.5,5]\subset[V_{IH},5]$ → **our inverter satisfies this**。不满足的例子：$V_{OL}=1.5\,\text{V} > V_{IL}=0.9\,\text{V}$（输出低电平落入禁区，"0" 可能被下级错读成 "1"）→ 破坏静态约束。

> [!IMPORTANT]
> 同时成立 **$V_{OL}<V_{IL}$ 且 $V_{OH}>V_{IH}$** 是门能被级联（cascade）的前提 —— 一级的输出直接喂给下一级的输入而不丢失逻辑值。

---

## 8. Noise Margin & $R_{ON}$（噪声容限与导通电阻）

噪声容限（见 [[Static Discipline]]）：

$$NM_H = V_{OH}-V_{IH},\qquad NM_L = V_{IL}-V_{OL}$$

- $R_{ON}$ 越小、负载越轻 → $V_{OL}$ 更低、$V_{OH}$ 更高 → **$NM_H, NM_L$ 都增大**，抗噪更好；
- 反之 $R_{ON}$ 过大 → $V_{OL}$ 被抬高、$V_{OH}$ 被压低 → 噪声容限缩小，易受干扰。

> [!TIP]
> 设计原则 $R_{ON}(\text{on}) \ll R_L \ll R_{ON}(\text{off})$，且驱动大负载时插入 **buffer（缓冲器 = 两级反相器级联）** 来恢复接近理想的 0/1 电平与噪声容限。

---

## 9. Buffer（缓冲器）

两个反相器级联：IN → inverter → inverter → OUT，得到 **buffer（$V_{OUT}=IN$，同相）**。

作用：**增强驱动能力**、隔离前后级，使输出电阻几乎不受负载影响，从而恢复接近理想的 0/1 电平与噪声容限。

---

## 10. Bridge to Dynamics（通向动态：传播延迟）

SR model 中导通管有有限 $R_{ON}$，而实际负载（下级输入、寄生）含电容 $C_L$。输出高低电平的翻转时间由 **$R_{ON}$ 与 $C_L$ 的 RC 乘积** 决定：

$$t_{PD} \;\sim\; R_{ON}\,C_L$$

这就是 **propagation delay（传播延迟）** 的来源 —— 属于 Part 4（动态电路 / Ch.10–11）的内容，此处仅作衔接。减小 $R_{ON}$（更"强"的晶体管）或减小负载电容可加快门速度。

---

## 11. 与知识树其他笔记的关系

- 器件物理、三工作区、平方律 → [[MOSFET]]
- 阈值、噪声容限、VTC、静态约束 → [[Static Discipline]]
- 门的符号、布尔代数、组合逻辑 → [[Combinational Logic]]
- 数字抽象动机（抗噪、取值离散化）→ [[The Digital Abstraction]]
- 放大器应用（负载线、偏置、$R_{on}$ 近似）→ [[The MOSFET Amplifier]]

> [!TIP]
> 学习路线：先建立"MOSFET = 受控开关"的直觉（本笔记），再用 [[Small Signal Analysis|小信号模型]] 分析模拟放大器，最后在 Part 4 用 $R_{ON}C_L$ 分析数字门的动态行为。
