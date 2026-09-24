---
tags:
  - 电路学
  - 电路分析方法
date: 2026-09-05
aliases:
  - 基本电路分析法
  - 电路分析法
  - 电路分析方法
  - 基本电路分析方法
  - KVL KCL Method
  - KVL/KCL 方法
  - 节点法
  - 节点分析法
  - 节点电压法
  - Nodal Analysis
  - 节点分析法 (Nodal Analysis)
  - Basic Circuit Analysis Method
  - 超节点
  - Supernode
  - 克莱姆法则
  - Cramer's Rule
---

# Basic Circuit Analysis *Method*

> [!NOTE] 定位 (Positioning)
> MIT 6.002x **Lecture 2** 的核心内容：当电路给定后，如何**系统地求出每一个元件的电压 $v$ 与电流 $i$**。
> 本课给出三条递进的路径（path）：
> 1. **Method 1 — Basic KVL/KCL method**：最朴素的暴力法 (brute force)。
> 2. **Method 2 — Element combination rules**：利用串并联等效化简 (reduction)。
> 3. **Method 3 — Node analysis**：节点法（本课真正的"肌肉"，也是 SPICE 等仿真器的内核）。
>
> 三者并非并列竞争，而是**层层抽象**：Method 3 是 Method 1 的一个特例（把 KVL 预先吸收进节点电压的定义里），组合规则则是 Method 3 在树状/梯形拓扑下的快捷方式。

---

## 1. Review: From LMD to KVL/KCL

电路分析之所以能用**代数方程**而非麦克斯韦偏微分方程，根源在于 **Lumped Matter Discipline (LMD，集总事物理论)** 施加的两条约束：

$$
\frac{\partial \phi_B}{\partial t}=0 \quad \text{(outside elements, 元件外部)}
\qquad\qquad
\frac{\partial q}{\partial t}=0 \quad \text{(inside elements, 元件内部)}
$$

- 第一条保证**信号传播视为瞬时**（尺寸 $\ll$ 波长）；第二条保证**节点不会累积净电荷**。
- 由此 Maxwell's equations 在集总假设下坍缩 (collapse) 为两条代数定律：
  - **KVL (Kirchhoff's Voltage Law)**：任一回路电压代数和为 0 —— $\displaystyle\sum_{j} v_j = 0$，本质是**能量守恒**。
  - **KCL (Kirchhoff's Current Law)**：任一节点电流代数和为 0 —— $\displaystyle\sum_{j} i_j = 0$，本质是**电荷守恒**。
- 集总元件 (lumped element) 的功率 (power)：

$$
p = v\,i
$$

> [!TIP] 一句串起来
> LMD 让 Maxwell → KVL + KCL；KVL/KCL 让"求所有 $v,i$"变成"列方程、解未知量"的代数游戏。后面所有方法都是这个游戏的**不同玩法**。

---

## 2. Associated Variables Discipline (AVD, 关联变量约定)

在动笔列方程前，必须先统一**符号约定 (sign convention)**，否则正负号会乱套。

> [!IMPORTANT] 关联变量约定
> **电流 $i$ 定义为从元件的"正电压端 (+)"流入 (current positive INTO the + terminal)。**
> 此时元件**消耗的功率** (power consumed) $p = vi$ 恒为非负：$p>0$ 表示吸收功率，$p<0$ 表示释放功率（如电源）。

![[avd_element.svg]]

- 本笔记所有 $v,i$ 默认采用 AVD（除非显式说明）。
- 这是 6.002 一以贯之的约定，连到 [[Small Signal Analysis|小信号分析]] 时同样适用。

---

## 3. Method 1 — Basic KVL/KCL Method (暴力法)

**Goal (目标)**：求出电路中**所有**元件的 $v$ 与 $i$。

**Procedure (步骤)**：
1. **Write element $v$–$i$ relationships**（写出每个元件的本构关系，来自集总抽象）。
2. **Write KCL for all nodes**（对每个节点写 KCL）。
3. **Write KVL for all loops**（对每个回路写 KVL）。
4. **Solve**（解大量方程 → 大量未知数 → 大量"乐趣")。

> [!WARNING] 为什么叫暴力法
> 未知数 = 每个元件的 $v$ 和 $i$；方程数 = 元件数 + 节点数 + 回路数。对中等规模电路会**迅速爆炸 (explode)**。课本用一张"12 方程解 12 未知数 + 抓狂表情"的图调侃它。理解它很重要，但**真干活别老用它**。

### 3.1 Demo Circuit (演示电路)

![[demo_bridge.svg]]

- 电压源 $V_0$ 在左支路（a 上、c 下）；电阻 $R_1$(a–b)、$R_2$(b–c)、$R_3$(b–d)、$R_4$(a–d)、$R_5$(d–c)。
- 4 个节点：a（上）、b（中左）、c（下）、d（右）。
- 元件电流：$i_0$（源）、$i_1$(R₁)、$i_2$(R₂)、$i_3$(R₃)、$i_4$(R₄)、$i_5$(R₅)，均按 AVD 方向（源/电阻上正下负 → 电流向下）。

**12 unknowns (未知数)**：$v_0\ldots v_5,\; i_0\ldots i_5$

**(1) Element relationships (6 equations)**
$$
v_0 = V_0,\quad v_1=i_1R_1,\quad v_2=i_2R_2,\quad v_3=i_3R_3,\quad v_4=i_4R_4,\quad v_5=i_5R_5
$$

**(2) KCL at nodes (4 个方程，3 个独立)**
$$
\begin{aligned}
\text{node a:}&\quad i_0+i_1+i_4 = 0 \\
\text{node b:}&\quad i_2+i_3-i_1 = 0 \\
\text{node d:}&\quad i_5-i_3-i_4 = 0 \\
\text{node c (冗余):}&\quad -i_0-i_2-i_5 = 0
\end{aligned}
$$

**(3) KVL for loops (4 个方程，3 个独立)** —— 取 L1(左网孔)、L2(上右)、L3(下右)、L4(外圈)：

$$
\begin{aligned}
\text{L1:}&\quad -v_0 + v_1 + v_2 = 0 \\
\text{L2:}&\quad v_1 + v_3 - v_4 = 0 \\
\text{L3:}&\quad v_3 + v_5 - v_2 = 0 \\
\text{L4 (冗余):}&\quad -v_0 + v_4 + v_5 = 0
\end{aligned}
$$

> [!NOTE] 计数
> 独立方程 = $6$（元件）+ $3$（KCL）+ $3$（KVL）= $12$ = 未知数个数。闭合可解。第 4 个 KCL / 第 4 个 KVL 分别可由其他方程推出（依赖关系 by charge/energy conservation），故称"冗余 (redundant)"。

---

## 4. Method 2 — Element Combination Rules (等效化简)

当电路是**树状/梯形 (ladder)** 拓扑、能用串并联逐步化简时，组合规则比暴力法快得多：

| Rule | Combination | Formula |
| :--- | :--- | :--- |
| 串联电阻 Series $R$ | $R_1\!-\!R_2\!-\!\cdots\!-\!R_N$ | $R_{\text{eq}} = R_1+R_2+\cdots+R_N$ |
| 并联电导 Parallel $G$ | $G_1\!\parallel\!G_2\!\parallel\!\cdots$ | $G_{\text{eq}} = G_1+G_2+\cdots+G_N,\;\; G_i=\dfrac{1}{R_i}$ |
| 串联电压源 Series $V$ | 同向 aiding | $V_{\text{eq}} = V_1+V_2$ |
| 并联电流源 Parallel $I$ | 同向 | $I_{\text{eq}} = I_1+I_2$ |

> [!TIP] 为什么并联用"电导 $G$"而不是"电阻 $R$"？
> 因为并联时**总电导 = 各电导之和**（与串联电阻同构），而总电阻是倒数和：$\displaystyle \frac{1}{R_{\text{eq}}}=\sum\frac{1}{R_i}$。节点法 (Node analysis) 正是大量利用这一点的。

**Example (例题)**：

![[method2_example.svg]]

- Step 1：$R_2 \parallel R_3 = \dfrac{R_2R_3}{R_2+R_3}$
- Step 2：再与 $R_1$ 串联 $\Rightarrow R = R_1 + \dfrac{R_2R_3}{R_2+R_3}$
- Step 3：$I = \dfrac{V}{R}$

> [!NOTE] 课本原话
> "Surprisingly, these rules (along with [[Superposition Theorem|superposition]], which you will learn later) can solve the circuit on page 8." —— 即连 Demo Circuit 这种桥式结构，配合**叠加原理**也能解（把电源逐个处理、每次化简为串并联）。组合规则 + 叠加 = 一张"免暴力"的牌。

---

## 5. Method 3 — Node Analysis (节点法) ★ 本课核心

> [!IMPORTANT] 本质
> **Node analysis = KVL/KCL method 的一个特例 (particular application)**。它预先用"节点电压 (node voltage)"把 KVL 吸收掉，于是**只剩下对每个非参考节点写 KCL**，未知数骤减。

### 5.1 Procedure (五步法)

1. **Select reference node (⊥ ground)**：选一个参考节点（地），所有电压都相对它测量。
2. **Label node voltages**：给其余每个节点标电压 $e_1,e_2,\ldots$（**primary unknowns，主未知数**）。
3. **Write KCL** at every non-ground node, **substituting device laws and KVL**（用欧姆定律把支路电流写成 $(e_{\text{node}}-e_{\text{neighbor}})\cdot G$）。
4. **Solve** for node voltages.
5. **Back solve** for branch voltages and currents（**secondary unknowns，次未知数**）。

### 5.2 Example: "Old Faithful plus current source"

![[old_faithful.svg]]

- 元件：$V_0$（顶到地）、$R_1$(V₀–e₁)、$R_2$(e₁–地)、$R_3$(e₁–e₂)、$R_4$(V₀–e₂)、$R_5$(e₂–地)、$I_1$（地→e₂，箭头向上）。
- **Unknown node voltages (主未知数)**：只有 $e_1, e_2$（$V_0$ 是已知电压源，不是未知数）。

**Step 3 — KCL in conductance form (电导形式)**，记 $G_i = 1/R_i$。每项是"本节点电压 − 邻节点电压"× 电导（流出的电流）：

$$
\begin{aligned}
\text{KCL@}e_1:&\quad (e_1-V_0)G_1 + (e_1-e_2)G_3 + (e_1)G_2 = 0 \\
\text{KCL@}e_2:&\quad (e_2-e_1)G_3 + (e_2-V_0)G_4 + (e_2)G_5 - I_1 = 0
\end{aligned}
$$

> [!NOTE] 电流源怎么处理
> $I_1$ 箭头**指向** $e_2$（注入节点），所以在"流出电流之和 = 0"的式子中表现为 **$-I_1$**（它不流出，是流入的源项）。更一般地：电流源项永远作为**源项移到等式右侧**。

**Step 4 — Rearrange (移项整理)**：把未知节点电压归到左边，已知源项归到右边：

$$
\begin{aligned}
e_1(G_1+G_2+G_3) + e_2(-G_3) &= V_0 G_1 \\
e_1(-G_3) + e_2(G_3+G_4+G_5) &= V_0 G_4 + I_1
\end{aligned}
$$

→ **2 equations, 2 unknowns**，直接可解。

**Matrix form (矩阵形式)**：

$$
\underbrace{
\begin{bmatrix}
G_1+G_2+G_3 & -G_3 \\
-G_3 & G_3+G_4+G_5
\end{bmatrix}}_{\text{conductivity matrix 电导矩阵}}
\begin{bmatrix} e_1 \\ e_2 \end{bmatrix}
=
\underbrace{
\begin{bmatrix} G_1 V_0 \\ G_4 V_0 + I_1 \end{bmatrix}}_{\text{sources 源向量}}
$$

**Solve via inverse (求逆解)**：

$$
\begin{bmatrix} e_1 \\ e_2 \end{bmatrix}
=
\frac{1}{\Delta}
\begin{bmatrix}
G_3+G_4+G_5 & G_3 \\
G_3 & G_1+G_2+G_3
\end{bmatrix}
\begin{bmatrix} G_1 V_0 \\ G_4 V_0 + I_1 \end{bmatrix},
\quad
\Delta = (G_1+G_2+G_3)(G_3+G_4+G_5) - G_3^2
$$

显式解（分母即电导矩阵行列式，恒正）：

$$
e_1 = \frac{(G_3+G_4+G_5)(G_1V_0) + G_3(G_4V_0+I_1)}{\Delta},
\qquad
e_2 = \frac{G_3(G_1V_0) + (G_1+G_2+G_3)(G_4V_0+I_1)}{\Delta}
$$

> [!NOTE] 物理直觉 (key observation)
> 解对 $V_0, I_1$ **线性 (linear)**，分母（行列式）**无负号、恒为正**——这是电路**线性 + 无源**的自然结果，也是检验答案是否合理的快速判据。

**Numerical check (数值校验)** —— 取 $G_1=G_5=1/8.2\text{K},\; G_2=G_4=1/3.9\text{K},\; G_3=1/1.5\text{K},\; I_1=0$：

$$
G_1+G_2+G_3 = \frac{1}{8.2}+\frac{1}{3.9}+\frac{1}{1.5} = 1,
\qquad
G_3+G_4+G_5 = \frac{1}{1.5}+\frac{1}{3.9}+\frac{1}{8.2} = 1
$$

$$
e_2 = \frac{\dfrac{1}{8.2}\cdot\dfrac{1}{1.5} + 1\cdot\dfrac{1}{3.9}}{1 - \left(\dfrac{1}{1.5}\right)^2}\,V_0
\;\;\Rightarrow\;\;
\boxed{e_2 = 0.6\,V_0}
$$

若 $V_0 = 3\text{ V}$，则 $e_2 = 1.8\text{ V}$。

### 5.3 含电压源的节点法：超节点 (Supernode)

> [!IMPORTANT] 为什么电压源会给节点法带来麻烦？
> 节点法的核心是写 KCL，而 KCL 需要知道每条支路的电流。**电压源的电流无法由电压直接求出**（欧姆定律不适用）——它的电流由外电路决定。需要特殊处理。

#### 情形一：电压源一端接地（参考节点）

最简单的情况：**另一端的节点电压直接被电压源锁定**。

- 若电压源 + 端接节点 $k$、− 端接地，则 $e_k = V_S$
- 该节点不需要写 KCL（电压已知，不列方程）
- 未知数直接减少一个

#### 情形二：电压源跨在两个非参考节点之间 → 超节点

当电压源两端都不接地（floating voltage source），两个节点电压都不直接已知，此时用**超节点 (Supernode)**：

> [!DEFINITION] 超节点 (Supernode)
> 将被电压源连接的两个节点（以及与电压源并联的任何元件）**合并**视为一个"超节点"，对超节点的外边界写 KCL（流入 = 流出），再用 KVL 补充两节点电压的约束：$e_i - e_j = V_S$。

**超节点的三个性质**：
1. 电压源提供了一个约束方程：$e_i - e_j = V_S$（取决于极性）
2. 超节点本身没有"自己的电压"——它是两个节点电压的联合
3. 超节点需要**同时使用 KCL 和 KVL**（与超网孔对偶）

> [!EXAMPLE] 超节点例题
> 电路：节点 1 接 $10\,\text{V}$ 电压源到地（$e_1=10\,\text{V}$，已知）；节点 2 与节点 3 之间跨一个 $5\,\text{V}$ 电压源（+ 在 2、− 在 3）；节点 1 经 $2\,\Omega$ 到节点 2、经 $4\,\Omega$ 到节点 3；节点 2 经 $8\,\Omega$ 到地；节点 3 经 $6\,\Omega$ 到地。
>
> **Step 1 — 识别超节点**：节点 2 和节点 3 被 $5\,\text{V}$ 电压源连接 → 合并为超节点。
>
> **Step 2 — 对超节点写 KCL**（流入超节点的电流 = 流出的电流）：
> $$\frac{e_1 - e_2}{2} + \frac{e_1 - e_3}{4} = \frac{e_2}{8} + \frac{e_3}{6}$$
>
> **Step 3 — 补 KVL 约束**（电压源两端电压差）：
> $$e_2 - e_3 = 5$$
>
> **Step 4 — 代入已知量并联立求解**：
> 已知 $e_1 = 10\,\text{V}$，且 $e_2 = e_3 + 5$，代入 KCL 方程：
> $$\frac{10 - (e_3+5)}{2} + \frac{10 - e_3}{4} = \frac{e_3+5}{8} + \frac{e_3}{6}$$
> 解得：$\boxed{e_3 \approx 2.86\,\text{V}}$，$\boxed{e_2 \approx 7.86\,\text{V}}$。

> [!TIP] 直接法（引入电流变量）
> 也可以设电压源的电流为 $i_5$，分别对节点 2 和节点 3 写 KCL，再补 $e_2 - e_3 = 5$ 的约束。变量多一个但更直观，最终方程与超节点法完全等价。超节点法只是"预先把两式相加消去 $i_5$"的快捷方式。

### 5.4 解方程的工具：克莱姆法则 (Cramer's Rule)

节点法/网孔法最终都归结为解线性方程组 $A\mathbf{x} = \mathbf{b}$。**克莱姆法则**是手算小规模方程组的标准方法：

> [!IMPORTANT] 克莱姆法则
> 若系数矩阵 $A$ 的行列式 $\det(A) \neq 0$，则方程组 $A\mathbf{x} = \mathbf{b}$ 有唯一解，第 $i$ 个未知数为：
> $$x_i = \frac{\det(A_i)}{\det(A)}$$
> 其中 $A_i$ 是将 $A$ 的第 $i$ 列替换为右端向量 $\mathbf{b}$ 得到的矩阵。

以 2×2 节点电压方程为例：
$$\begin{cases} G_{11}e_1 + G_{12}e_2 = s_1 \\ G_{21}e_1 + G_{22}e_2 = s_2 \end{cases}$$

$$\Delta = \det\begin{bmatrix}G_{11}&G_{12}\\G_{21}&G_{22}\end{bmatrix} = G_{11}G_{22} - G_{12}G_{21}$$

$$e_1 = \frac{1}{\Delta}\det\begin{bmatrix}s_1&G_{12}\\s_2&G_{22}\end{bmatrix} = \frac{s_1G_{22} - s_2G_{12}}{\Delta}, \qquad e_2 = \frac{1}{\Delta}\det\begin{bmatrix}G_{11}&s_1\\G_{21}&s_2\end{bmatrix} = \frac{G_{11}s_2 - G_{21}s_1}{\Delta}$$

> [!NOTE] 行列式恒正的物理意义
> 对无源电阻网络，电导矩阵/电阻矩阵的行列式**恒为正**——这是电路**无源、稳定**的数学体现。如果算出行列式为负或零，先检查方程列错了没有。

> [!TIP] 替代方法
> - **消元法**（加减消元、代入消元）：2–3 个未知数时更快
> - **矩阵求逆**：$\mathbf{x} = A^{-1}\mathbf{b}$，概念清晰但手算麻烦
> - **数值方法**：大规模电路用 SPICE 等仿真器（高斯消元 / LU 分解）

> [!TIP] 对比 Method 1
> 同一个含桥式结构的电路，暴力法要 **12 方程**；节点法只用了 **2 方程**（$e_1,e_2$ 两个未知数）。拓扑越复杂，差距越悬殊。这就是节点法成为"主力 (workhorse)"的原因。

---

## 6. Which Method When? (方法选型)

```mermaid
flowchart TD
    A[给定电路, 求所有 v,i] --> B{能否化简为<br>纯串并联?}
    B -- 能 --> C[Method 2: 组合规则<br>+ 叠加原理]
    B -- 不能 --> D[Method 3: 节点法<br>Nodal Analysis]
    A --> E[Method 1: 暴力法<br>仅用于理解/小电路]
    D --> F[写出电导矩阵 [G][e]=[s]<br>求逆/高斯消元]
```

| Method | 适用场景 | 未知数规模 | 评价 |
| :--- | :--- | :--- | :--- |
| 1. Basic KVL/KCL | 任意电路、教学演示 | 大（2×元件数） | 通用但**繁琐** |
| 2. Combination rules | 树状/梯形、可串并联化简 | 小 | **最快**，但受拓扑限制 |
| 3. Node analysis | **任意拓扑**、含电流源 | 小（节点数−1） | **主力方法**，可程序化（SPICE 用改进节点法 MNA） |

---

## 7. 与其他笔记的关联 (Connections)

- [[Kirchhoff's Laws|基尔霍夫定律 (KCL/KVL)]] —— 本课的两条"地基"定律
- [[Lumped Matter Discipline|集总事物理论 (LMD)]] —— KVL/KCL 得以成立的前提
- [[Superposition Theorem|叠加原理]] —— 与组合规则配合可解桥式等复杂电路
- [[Thevenin's Theorem|戴维南定理]] / [[Norton's Theorem|诺顿定理]] —— 节点法求出的端口量可进一步做等效化简
- [[Small Signal Analysis|小信号分析]] —— 非线性器件在工作点附近的线性化，同样建立在节点法框架上
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）

---

## 相关笔记

- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
- [[Kirchhoff's Laws]] / [[Lumped Matter Discipline]] —— 定律与理论前提
- [[Superposition Theorem]] / [[Thevenin's Theorem]] / [[Norton's Theorem]] —— 进阶分析方法
