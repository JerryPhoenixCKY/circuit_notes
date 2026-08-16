---
tags:
  - 电路学
  - 信号与系统
  - 电磁学
  - 课程笔记
date: 2026-08-07
aliases:
  - 电路原理
  - 电路与电子学
  - 电路基础
  - Circuits and Electronics
  - 6.002x
---

---

## 一、 电路基础概念与基本定律

### 1. 基础物理量与元件
- **分析类型**：DC analysis（直流分析）、AC analysis（交流分析）
- **基本物理量**：Voltage（电压）、Current（电流）。
- **基本元件**：
  - Resistor（电阻）
  - Capacitor（电容），其数值为 Capacitance（电容值）
  - Inductor（电感），其数值为 Inductance（电感值）
  - Lumped elements（集总元件）

### 2. 电路拓扑结构
- **Node**（节点）
- **Branch**（支路）
- **Loop**（回路）
- **Mesh**（网孔）
- **连接方式**：Series（串联）、Parallel（并联）

### 3. 核心定理与公式

> [!NOTE] 欧姆定律 (Ohm's Law)
> $$I = \frac{V}{R}$$

> [!NOTE] 基尔霍夫定律 (Kirchhoff's Laws)
> - **KCL (基尔霍夫电流定律)**：节点处电流代数和为 0（The sum of the currents in a node is 0）。
> - **KVL (基尔霍夫电压定律)**：闭合回路中电压代数和为 0（The sum of the voltages in a loop is 0）。

- **[[Superposition Theorem]] ([[Superposition Theorem|叠加原理]])**：适用于 Linear circuit（线性电路）。

---

## 二、 电路分析方法与信号处理

### 1. 放大器与非线性电路分析
- **核心器件**：Diode（二极管）、Transistor（晶体管）、Amplifier（放大器）。
- **状态与静态工作点**：
  - Saturation（饱和状态）
  - Bias point / Operating point / Quiescent point（偏置点 / 工作点 / 静态工作点）
  - Load line（负载线）
- **分析方法**：Small signal Analysis（小信号分析）。

### 2. 时域与频域响应
- **信号分类**：Analog / Digital signal（模拟 / 数字信号）。
- **分析维度**：Time Domain（时域）/ Frequency Domain（频域）。
- **响应特性**：
  - Transient Response（瞬态响应）
  - Time constant（时间常数）
  - Impedance（阻抗）
  - Filter（滤波器）

---

## 三、 数学工具：欧拉公式与复数

在交流电路与频域分析中，复数与指数形式是极为重要的工具。

> [!MATH] 欧拉公式 (Euler's Formula)
> $$e^{j\theta} = \cos\theta + j\sin\theta$$

- **运算性质**：
  - 指数相乘：$e^{j(\alpha+\beta)} = e^{j\alpha} \cdot e^{j\beta}$
  - 微分性质：$\frac{d}{d\theta} e^{j\theta} = j e^{j\theta}$
- **特例（欧拉恒等式）**：
  $$e^{j\pi} + 1 = 0$$

### 1. 复数形式转换 (Complex Representation)
复数 $z$ 可表示为代数形式、三角形式与极坐标（指数）形式：
$$z = x + jy = r(\cos\theta + j\sin\theta) = r e^{j\theta}$$

### 2. 反欧拉公式 (Inverse Euler Formula)
$$\sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}$$

---

## 四、 电磁学基础与集总事物理论 (LMD)

电路理论是麦克斯韦方程组在满足特定条件下的简化近似。

### 1. [[Maxwell's Equations|麦克斯韦方程组]] (Maxwell's Equations)

| 物理定律 | 微分形式 (Differential Form) | 积分形式 (Integral Form) |
| :--- | :--- | :--- |
| **法拉第电磁感应定律** | $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | $\oint \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial \Phi_B}{\partial t}$ |
| **电荷连续性方程** | $\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t}$ | $\oint \mathbf{J} \cdot d\mathbf{S} = -\frac{\partial q}{\partial t}$ |
| **高斯定律** | $\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$ | $\oint \mathbf{E} \cdot d\mathbf{S} = \frac{q}{\epsilon_0}$ |

### 2. [[Lumped Matter Discipline|集总事物理论]](Lumped Matter Discipline, LMD)

> [!IMPORTANT] LMD 成立前提条件
> 为了能够将复杂的电磁场问题简化为集总电路模型，在**元件外部（Outside elements）** 必须严格满足以下假设：
> 1. **磁场限制**：磁通量随时间的变化率为 0：
>    $$\frac{\partial \Phi_B}{\partial t} = 0$$
> 2. **电荷限制**：电荷量随时间的变化率为 0：
>    $$\frac{\partial q}{\partial t} = 0$$