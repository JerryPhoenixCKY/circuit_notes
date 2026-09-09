---
tags:
  - 电路学
  - 电阻网络
  - 电路分析方法
  - 课程笔记
date: 2026-09-09
aliases:
  - 惠斯通电桥
  - Wheatstone Bridge
  - 星角变换
  - 星形三角变换
  - Y-Δ Transformation
  - Wye-Delta Transformation
  - Delta-Wye Transformation
  - Δ-Y Transformation
  - T-Π Transformation
  - 桥式电路
  - Bridge Circuit
  - 惠斯通电桥与星角变换
---

# Wheatstone Bridge and Wye-Delta Transformation（惠斯通电桥与星角变换）

> [!NOTE] 本笔记定位
> 来自 ECE 2001 *Basic Circuit Theory* Lecture 1（Basic Concepts, Basic Laws, and Simple Resistive Circuits）Part II 的扩展内容。串并联等效（[[Resistive Networks]]）与分压/分流（[[Ohm's Law]] §三）解决不了**桥式网络 (bridge network)**——其中的电阻**既非串联也非并联**。本笔记给出两件武器：
> - **惠斯通电桥 (Wheatstone Bridge)**：经典的精密测阻电路，用零示法 (null method) 把"测电阻"变成"调平衡"；
> - **Y-Δ 变换 (Wye-Delta Transformation)**：三端 Δ(Π) 网络与 Y(T) 网络的等效互换，让桥式网络退化为普通串并联。
>
> 前置：[[Ohm's Law]]、[[Resistive Networks]]、[[Kirchhoff's Laws]]；方法选型对照见 [[Circuit Analysis Methods in Practice]]。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、动机：串并联失效的地方

桥式网络：两条串联支路并联后，中间再跨接一条"桥臂"（如检流计、中间电阻 $R_m$）。此时 $R_1$、$R_2$、$R_m$ 构成**三角形 (Δ) 连接**，$R_1$、$R_m$、$R_3$ 构成**星形 (Y) 连接**——任何一个电阻都找不出严格的串/并联搭档，[[Resistive Networks|串并联化简]]直接失效。

> [!IMPORTANT] 三条出路
> 1. **通用方法**：节点法 / 网孔法硬解（[[Basic Circuit Analysis Method]]、[[Circuit Analysis Methods in Practice]]）——通用但方程多；
> 2. **端口等效**：[[Thevenin's Theorem|戴维南等效]]——关注单一支路时高效；
> 3. **拓扑变换**：Y-Δ 变换（本笔记）——直接改写电路结构，一步退化为串并联。

---

## 二、惠斯通电桥 (Wheatstone Bridge)

### 2.1 先说测量的困境：理想电表与朴素方法

| 仪表 | 等效电阻 | 接法 | 理想极限 |
| :--- | :--- | :--- | :--- |
| 理想电流表 (ideal ammeter) | $0\,\Omega$ | **串联**接入 | 短路（不影响电路） |
| 理想电压表 (ideal voltmeter) | $\infty\,\Omega$ | **并联**接入 | 开路（不分流） |

朴素测阻法：安培计测 $I$ + 伏特计测 $V$，再 $R = V/I$。问题：
- 待测电阻**很小**时，电流表的有限内阻不可忽略；
- 待测电阻**很大**时，电压表的有限内阻分流不可忽略；
- 两种情况下误差都随阻值极端化而爆炸。

### 2.2 电桥结构与平衡条件

![[wheatstone_bridge.svg]]

四臂电桥：$R_1$、$R_2$ 为**比例臂 (ratio arms)**，$R_3$ 为可调**标准电阻 (standard resistor)**，$R_x$ 为**待测电阻 (unknown)**，节点 $a$、$b$ 之间跨接检流计/电流表。

**操作**：调节 $R_3$ 直到电流表读**零**（电桥平衡，balanced）。

> [!IMPORTANT] 平衡条件推导
> 平衡时 $i_G = 0$，意味着 $a$、$b$ **等电位**（$v_{ab} = 0$）。左支路电流 $i_1$ 过 $R_1 \to R_3$，右支路 $i_2$ 过 $R_2 \to R_x$，沿两条路径从顶母线压降到同一电位：
> $$i_1 R_1 = i_2 R_2 \qquad i_1 R_3 = i_2 R_x$$
> 两式相除消去电流：
> $$\boxed{R_x = \frac{R_2}{R_1}\,R_3}$$
> 待测电阻 = 比例臂之比 × 标准电阻读数。

> [!WARNING] 零电流 ≠ 开路 (open circuit)
> 平衡时 $a$、$b$ 之间**没有电流**，但**不是断开**——只是两点等电位、没有电位差驱动电流。检流计支路依然物理连通，一旦失去平衡立刻有电流流过。

### 2.3 为什么电桥更好：零示法 (Null Method)

- 电表**只用于判断"有没有电流"**（零/非零），不需要精确读数 → 电表精度误差不进入结果；
- 结果只取决于**电阻比** $R_2/R_1$ 与标准电阻 $R_3$，可做成高精度；
- 量程 (range) 灵活：改变比例臂之比即可跨越多个数量级。

> [!TIP] 工程延伸：传感器电桥
> 把任一桥臂换成传感器电阻（应变片 strain gauge、热电阻 RTD、光敏电阻），电桥失衡输出 $\propto$ 阻值变化——这正是压力传感器、电子秤、温度测量的经典前端电路。差分结构还能抑制共模干扰（对照 [[Operational Amplifier|运放]] 差分放大）。

---

## 三、Y-Δ 变换 (Wye-Delta Transformation)

### 3.1 三端网络与等效条件

![[wye_delta_transform.svg]]

Δ 与 Y 都只对外暴露**三个端子** $a$、$b$、$c$。等效 (equivalent) 的定义：

> [!IMPORTANT] 等效条件
> 任意一对端子之间的等效电阻相等（第三端**开路**）：
> $$R_{ab}:\; R_{ab}^{\Delta} = R_{ab}^{Y}, \qquad R_{bc}:\; R_{bc}^{\Delta} = R_{bc}^{Y}, \qquad R_{ca}:\; R_{ca}^{\Delta} = R_{ca}^{Y}$$
> 三个方程恰好定出三个未知电阻——变换唯一。

### 3.2 Δ→Y 公式（相邻乘积 / 三臂之和）

$$R_a = \frac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}, \qquad R_b = \frac{R_{ab}R_{bc}}{\sum R_\Delta}, \qquad R_c = \frac{R_{bc}R_{ca}}{\sum R_\Delta}$$

> [!TIP] 记忆法
> **Y 的每个电阻 = 该端相邻的两个 Δ 臂之积 ÷ 三个 Δ 臂之和**（"挨着我的两个，乘起来除以总和"）。

### 3.3 Y→Δ 公式（两两乘积和 / 对面电阻）

$$R_{ab} = \frac{R_aR_b + R_bR_c + R_cR_a}{R_c}, \qquad R_{bc} = \frac{\sum R_aR_b}{R_a}, \qquad R_{ca} = \frac{\sum R_aR_b}{R_b}$$

> [!TIP] 记忆法
> **Δ 的每个电阻 = Y 电阻两两乘积之和 ÷ 对面那个 Y 电阻**（$R_{ab}$ 对面是 $R_c$）。
> 隐藏恒等式：记 $R_s = R_a+R_b+R_c$，则 $R_aR_b + R_bR_c + R_cR_a = \dfrac{R_aR_bR_c}{R_s}$——可用于快速验算。

> [!NOTE] 对称性自检
> 若 Δ 三臂相等（$R_{ab}=R_{bc}=R_{ca}=R_\Delta$），则 Y 三臂也相等：$R_Y = R_\Delta^2/3R_\Delta = R_\Delta/3$；反向 $R_\Delta = 3R_Y$。**对称结构变换后仍对称**，可作公式速查。

### 3.4 推导思路

以 $R_{ab}$ 为例：Δ 侧 $c$ 开路时 $R_{ab}^{\Delta} = R_{ab} \parallel (R_{bc}+R_{ca})$，Y 侧 $R_{ab}^{Y} = R_a + R_b$。对三对端子各写一个这样的方程，联立解出 $R_a, R_b, R_c$（或反向解 $R_{ab}, R_{bc}, R_{ca}$）。本质仍是 [[Thevenin's Theorem|端口等效]] + [[Kirchhoff's Laws|KCL/KVL]]。

---

## 四、例题（Worked Examples）

### 例 1 · Δ→Y 化简桥式网络（Lecture 例题）

桥式网络中某 Δ 三臂为 $R_{ab}=30\,\Omega$、$R_{bc}=50\,\Omega$、$R_{ca}=20\,\Omega$（$\sum R_\Delta = 100\,\Omega$），端口经 13 Ω 电阻接 240 V 源。

**Δ→Y**：
$$R_a = \frac{30\times 20}{100} = 6\,\Omega, \qquad R_b = \frac{30\times 50}{100} = 15\,\Omega, \qquad R_c = \frac{50\times 20}{100} = 10\,\Omega$$

变换后桥式退化为串并联，与外电路 24 Ω、10 Ω 组合：
$$R_{AB} = 13 + (24+6)\parallel(10+10) + 15 = 13 + 30\parallel 20 + 15 = 13 + 12 + 15 = 40\,\Omega$$
$$i = \frac{240\,\text{V}}{40\,\Omega} = 6\,\text{A}$$

### 例 2 · Δ→Y 求电源功率（Lecture Practice）

40 V 源供电，桥内 Δ 三臂为 $R_{ab}=100\,\Omega$、$R_{bc}=125\,\Omega$、$R_{ca}=25\,\Omega$（$\sum = 250\,\Omega$）：

$$R_a = \frac{100\times 25}{250} = 10\,\Omega, \qquad R_b = \frac{100\times 125}{250} = 50\,\Omega, \qquad R_c = \frac{125\times 25}{250} = 12.5\,\Omega$$

$$R_{eq} = 5 + 50 + (10+40)\parallel(12.5+37.5) = 55 + 50\parallel 50 = 55 + 25 = 80\,\Omega$$
$$i = \frac{40}{80} = 0.5\,\text{A}, \qquad p = vi = 40\times 0.5 = 20\,\text{W}$$

### 例 3 · Y→Δ 反向变换（Lecture Practice）

Y 三臂 $R_a = 20\,\Omega$、$R_b = 10\,\Omega$、$R_c = 5\,\Omega$，两两乘积和 $= 200+50+100 = 350$：

$$R_{ab} = \frac{350}{R_c} = 70\,\Omega, \qquad R_{bc} = \frac{350}{R_a} = 17.5\,\Omega, \qquad R_{ca} = \frac{350}{R_b} = 35\,\Omega$$

与外电路 28 Ω、70 Ω、105 Ω 组合后，2 A 电流源两端：
$$R_{eq} = 35 \parallel (28\parallel 70 + 17.5\parallel 105) = 35\parallel(20+15) = 35\parallel 35 = 17.5\,\Omega$$
$$v = 2\,\text{A}\times 17.5\,\Omega = 35\,\text{V}$$

> [!TIP] 考试提示（来自讲义）
> Lecture 明确：这两个变换公式若考试需要**会直接给出**——重点不是背公式，而是**识别 Δ/Y 结构**并正确套用。

---

## 五、方法选型：Y-Δ 在工具箱里的位置

| 方法 | 适用场景 | 代价 | 笔记 |
| :--- | :--- | :--- | :--- |
| 串并联化简 | 规则梯形/并联网络 | 几乎零 | [[Resistive Networks]] |
| 分压 / 分流 | 已知总电压/总电流求分量 | 几乎零 | [[Ohm's Law]] §三 |
| **Y-Δ 变换** | **桥式 / 三端网络** | 代入公式 | 本笔记 |
| 节点法 (Node Analysis) | 任意网络，通用 | 解方程组 | [[Basic Circuit Analysis Method]] |
| 网孔法 (Mesh Analysis) | 平面网络 | 解方程组 | [[Circuit Analysis Methods in Practice]] |
| 戴维南 / 诺顿等效 | 只关心某一支路 | 需求 $V_{oc}$/$R_{eq}$ | [[Thevenin's Theorem]] / [[Norton's Theorem]] |
| 叠加定理 | 多独立源线性网络 | 逐源求解 | [[Superposition Theorem]] |

> [!NOTE] KCL/KVL 是万能的，变换是提速的
> 讲义原话：*"KCL & KVL are general methods, but sometimes it is faster to use these transformation techniques."*——先用 Y-Δ 把电路"扳直"，再走串并联/分压分流，常比列方程快得多。

---

## 相关笔记

- [[Ohm's Law]] —— 分压/分流公式（例题化简的每一步都在用）
- [[Resistive Networks]] —— 串并联等效（Y-Δ 是它在非串并联网络上的延伸）
- [[Kirchhoff's Laws]] —— 平衡条件与等效条件的推导根基
- [[Thevenin's Theorem]] / [[Norton's Theorem]] —— 端口等效思想的同门兄弟
- [[Basic Circuit Analysis Method]] / [[Circuit Analysis Methods in Practice]] —— 通用解法与方法选型
- [[Ideal Two-Terminal Elements]] —— 理想源、短路/开路的极限模型（理想电表即其应用）
- [[Circuit Theory Glossary]] —— 术语表
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
