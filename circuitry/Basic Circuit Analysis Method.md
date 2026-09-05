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
