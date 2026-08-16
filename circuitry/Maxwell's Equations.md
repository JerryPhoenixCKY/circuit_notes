---
tags:
  - 电磁学
  - 电路学
  - 课程笔记
date: 2026-08-15
aliases:
  - 麦克斯韦方程组
  - 麦克斯韦方程
  - 麦克斯韦四大方程
  - 麦克斯韦四个方程
  - Maxwell Equations
  - Maxwell's Equations
---

# 麦克斯韦方程组 (Maxwell's Equations)

> [!IMPORTANT] 核心地位
> 麦克斯韦方程组是**经典电磁学的统一理论**，将电场与磁场、电荷与电流统一到四个方程之中。
> 电路理论（KCL、KVL、欧姆定律）是它在 [[Lumped Matter Discipline|集总事物理论 (LMD)]] 条件下的**简化近似**——先把电磁学搞清楚，才能理解电路为什么"能用几条代数方程"描述。

---

## 一、四大方程总览

| # | 定律 | 微分形式 | 积分形式 | 物理意义 |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **高斯定律** (Gauss's Law) | $\nabla \cdot \mathbf{E} = \dfrac{\rho}{\epsilon_0}$ | $\displaystyle\oint \mathbf{E} \cdot d\mathbf{S} = \dfrac{q_{enc}}{\epsilon_0}$ | 电荷是电场的"源" |
| 2 | **磁场高斯定律** (Gauss's Law for Magnetism) | $\nabla \cdot \mathbf{B} = 0$ | $\displaystyle\oint \mathbf{B} \cdot d\mathbf{S} = 0$ | 不存在磁单极子，磁感线闭合 |
| 3 | **法拉第电磁感应定律** (Faraday's Law) | $\nabla \times \mathbf{E} = -\dfrac{\partial \mathbf{B}}{\partial t}$ | $\displaystyle\oint \mathbf{E} \cdot d\mathbf{l} = -\dfrac{\partial \Phi_B}{\partial t}$ | 变化的磁场产生电场 |
| 4 | **安培-麦克斯韦定律** (Ampère–Maxwell Law) | $\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\epsilon_0\dfrac{\partial \mathbf{E}}{\partial t}$ | $\displaystyle\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{enc} + \mu_0\epsilon_0\dfrac{\partial \Phi_E}{\partial t}$ | 电流与变化的电场产生磁场 |

> [!NOTE] 符号约定
> - $\mathbf{E}$：电场强度；$\mathbf{B}$：磁感应强度；$\mathbf{J}$：电流密度；$\rho$：电荷密度。
> - $\epsilon_0$：真空介电常数；$\mu_0$：真空磁导率。
> - $q_{enc}$ / $I_{enc}$：闭合曲面内净电荷 / 闭合回路包围的净电流。

---

## 二、各方程详解

### 1. 高斯定律（电场）—— 电荷是电场的源

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \quad\Longleftrightarrow\quad \oint \mathbf{E} \cdot d\mathbf{S} = \frac{q_{enc}}{\epsilon_0}$$

- **含义**：穿过任意闭合曲面的电通量，正比于曲面内包围的净电荷。
- **要点**：电场线**始于正电荷、终于负电荷**（有源有汇）。

### 2. 磁场高斯定律 —— 无磁单极子

$$\nabla \cdot \mathbf{B} = 0 \quad\Longleftrightarrow\quad \oint \mathbf{B} \cdot d\mathbf{S} = 0$$

- **含义**：穿过任意闭合曲面的磁通量**恒为零**。
- **要点**：磁感线永远是**闭合曲线**，不存在孤立的"N 极"或"S 极"。把磁铁掰断，得到的是两块各带 N/S 的新磁铁，而不是单独的磁极。

### 3. 法拉第电磁感应定律 —— 变化的磁场产生电场

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \quad\Longleftrightarrow\quad \oint \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial \Phi_B}{\partial t}$$

- **含义**：随时间变化的磁场，会**环绕**产生电场（感应电场是"涡旋场"，不是由电荷激发的）。
- **负号**：即**楞次定律 (Lenz's Law)**——感应电场的方向总是**反抗**磁通量的变化。
- **电路中的体现**：这正是**电感 (Inductor)** 工作的物理根源，也是 [[Lumped Matter Discipline|LMD]] 中要"约束掉"的那一项。

### 4. 安培-麦克斯韦定律 —— 电流 + 变化的电场产生磁场

$$\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t} \quad\Longleftrightarrow\quad \oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{enc} + \mu_0\epsilon_0\frac{\partial \Phi_E}{\partial t}$$

- **含义**：磁场由**传导电流**和**变化的电场（位移电流）**共同产生。
- **位移电流 (Displacement Current)**：麦克斯韦的原创贡献 $\mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t}$。没有它，电容极板之间"看似没有电流流过"的地方就无法产生磁场，方程会自相矛盾。

---

## 三、电荷连续性方程 (Charge Conservation)

> [!NOTE] 连续性方程
> $$\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t} \quad\Longleftrightarrow\quad \oint \mathbf{J} \cdot d\mathbf{S} = -\frac{\partial q}{\partial t}$$

- **含义**：流出某区域的电流 = 该区域内电荷的减少速率。这是**电荷守恒**的微分表述。
- **地位**：它不是独立的第五条方程，而是**高斯定律 + 安培-麦克斯韦定律**的必然推论（对安培定律两边取散度即可导出）。
- **电路中的体现**：它是 [[Lumped Matter Discipline|LMD]] 推导 **KCL** 的直接物理基础。

---

## 四、与电路理论的关系（关键过渡）

麦克斯韦方程组是**偏微分方程**，描述的是空间中每一点、每一时刻的场。直接用它解电路，复杂度不可接受。

[[Lumped Matter Discipline|集总事物理论 (LMD)]] 通过三条假设，把"场的问题"降维成"电路元件之间连线的问题"：

| 麦克斯韦方程 | LMD 假设 | 降维结果 |
| :--- | :--- | :--- |
| 法拉第定律 $\dfrac{\partial \Phi_B}{\partial t}$ | 元件外部磁通变化率为 0 | **KVL（基尔霍夫电压定律）** |
| 连续性方程 $\dfrac{\partial q}{\partial t}$ | 节点处电荷积累率为 0 | **KCL（基尔霍夫电流定律）** |

> [!TIP] 一句话总结
> **电路理论不是"新的物理"，而是麦克斯韦方程在特定约束下的工程近似。** 理解了这一点，KCL/KVL 就不再是死记硬背的规则，而是"场论在集总条件下的必然结果"。

---

## 相关笔记

- [[Lumped Matter Discipline]] —— LMD 三条假设与 KCL/KVL 的推导
- [[cs6.002x.1开头]] —— 电路基础概念与基本定律（主笔记）
