---
tags:
  - 电路学
  - 电路基础
  - 基本定律
date: 2026-09-06
aliases:
  - 欧姆定律
  - 欧姆定律定理
  - Ohm Law
  - Ohm's Law
  - 电阻的电压-电流关系
  - 线性电阻定律
---

# Ohm's Law（欧姆定律）

> [!NOTE] 一句话
> **欧姆定律 (Ohm's Law)** 描述**线性电阻 (Linear Resistor)** 两端电压与流过电流的正比关系：$v = iR$。它是把单个元件的"本构关系 (Constitutive Relation)"写出来的最基础定律，是整个电阻网络分析的"元件层"基石。

$$\boxed{v = iR \qquad\Longleftrightarrow\qquad i = Gv,\;\; G=\frac{1}{R}}$$

- $R$ 为**电阻 (Resistance)**，单位 $\Omega$（欧姆）；
- $G$ 为**电导 (Conductance)**，单位 S（西门子，Siemens），$G = 1/R$。

> [!IMPORTANT] 欧姆定律只管"一个元件"，不管"元件之间怎么连"
> 欧姆定律只约束**单个电阻**的端口关系；而**元件之间如何相互约束**由 [[Kirchhoff's Laws|基尔霍夫定律 (KCL/KVL)]] 负责。二者配合，才能解出整个 [[Resistive Networks|电阻网络]]。这是电路分析中"元件定律 + 拓扑约束"这一对核心思想的第一次登场。

---

## 一、与关联变量约定 (AVD) 的配合

在 [[Practical Two-Terminal Elements|关联变量约定 (AVD)]] 下，端口电流 $i$ 取**流入 + 端**的方向，则该元件**吸收**的功率为

$$p = vi = (iR)\,i = i^{2}R = \frac{v^{2}}{R}$$

> [!TIP] 功率的三种写法
> - $p = vi$（定义式，任何元件都成立）
> - $p = i^{2}R$（已知电流时方便）
> - $p = v^{2}/R$（已知电压时方便）
>
> 对线性电阻，功率是电压/电流的**二次函数**，因此**功率不可线性叠加**——这正是 [[Superposition Theorem|叠加原理]] 只能叠加电压、电流而不能叠加功率的微观原因。

电阻是**无源、耗能**元件：无论电流方向如何，$p = i^{2}R \ge 0$ 恒成立（永远吸收功率，永不发出）。

---

## 二、v–i 特性是一条过原点的直线

对线性电阻，$v = iR$ 在 $v$–$i$ 平面上是一条**过原点、斜率 = $R$** 的直线：

![[ohms_law_iv.svg]]

> [!NOTE] 斜率的物理意义
> - 斜率越大（$R$ 越大）→ 同样电流下压降越大 → 电阻"越阻碍"电流；
> - 短路 ($R=0$)：直线水平为 0，任意电流下 $v=0$；
> - 开路 ($R\to\infty$)：直线竖直，任意电压下 $i=0$。

对比 [[Two-Terminal Element Laws|二端元件定律]]：电压源是**竖直线**（电压被钉死）、电流源是**水平线**（电流被钉死）、电容/电感是**微分**关系（有记忆），而电阻是**代数、无记忆**的最简情形。

---

## 三、分压 (Voltage Divider) 与分流 (Current Divider)

### 3.1 分压 — 串联电阻按阻值瓜分总电压

两个电阻 $R_1, R_2$ 串联，总电压 $V_{in}$ 在二者间按阻值分配（由 KVL + 欧姆定律即得）：

$$V_{out} = V_{in}\,\frac{R_2}{R_1 + R_2}$$

> [!TIP] 记忆口诀
> "**抽头电压 = 总压 ×（抽头下方电阻 ÷ 总电阻）**"。这是 [[Resistive Networks|电阻网络]] 里最常用的直觉公式之一，也是 [[Practical Two-Terminal Elements|实际电池带载]] 时 $V_{out}=V_s\frac{R_L}{R_{int}+R_L}$ 的同一个式子。

### 3.2 分流 — 并联电阻按电导瓜分总电流

两个电阻 $R_1, R_2$ 并联，流过 $R_1$ 的电流为

$$I_1 = I\,\frac{R_2}{R_1 + R_2} = I\,\frac{G_1}{G_1 + G_2}$$

> [!NOTE] 并联用"电导"更自然
> 并联时各支路电压相同，电流按**电导**分配（电导越大、分到的电流越多）。用 $G=1/R$ 视角，分流公式与分压公式**完全对称**。

---

## 四、为什么二极管、晶体管不满足欧姆定律？

欧姆定律成立的前提是**电阻值为常数 $R$**（与 $v, i$ 无关）。而

- **二极管 (Diode)**：电流随电压呈指数关系 $i = I_s(e^{v/V_T}-1)$，阻值随工作点剧烈变化；
- **晶体管 (Transistor / [[MOSFET|MOSFET]])**：漏极电流是栅源电压的二次函数（饱和区），$i$ 与 $v$ 根本不是直线。

> [!WARNING] 非线性元件 ≠ 没有"定律"
> 非线性元件只是**不服从欧姆定律**，它们有自己的本构关系（见 [[Two-Terminal Element Laws|二端元件定律]] 与 [[Analysis of Nonlinear Circuits|非线性电路分析]]）。处理它们需要分段线性化、负载线、工作点等更高级的工具——这正是 [[Small Signal Analysis|小信号分析]] 在直流工作点附近把非线性"局部线性化"成欧姆式关系的动机。

---

## 五、典型例题

> [!EXAMPLE] 分压求未知
> 电路：$V_{in}=10\text{ V}$，串联 $R_1=2\,\text{k}\Omega$、$R_2=3\,\text{k}\Omega$，求 $R_2$ 两端电压。
> $$V_{out}=10\cdot\frac{3}{2+3}=10\cdot\frac{3}{5}=6\text{ V}$$
> 吸收功率：$P_{R_2}=\dfrac{V_{out}^{2}}{R_2}=\dfrac{36}{3000}=12\text{ mW}$。

> [!EXAMPLE] 分流求未知
> 电路：总电流 $I=5\text{ A}$，$R_1=4\,\Omega$ 与 $R_2=6\,\Omega$ 并联，求 $R_1$ 支路电流。
> $$I_1 = 5\cdot\frac{6}{4+6}=5\cdot\frac{6}{10}=3\text{ A},\qquad I_2=5-3=2\text{ A}$$

---

## 相关笔记

- [[Kirchhoff's Laws]] —— KCL/KVL：元件之间的拓扑约束（与欧姆定律"元件层"互补）
- [[Resistive Networks]] —— 电阻网络：分压/分流、串并联化简、等效电阻
- [[Two-Terminal Element Laws]] —— 所有二端元件的 v–i 关系总表（电阻只是其中一行）
- [[Practical Two-Terminal Elements]] —— 实际电阻与理想电阻、AVD 约定
- [[Analysis of Nonlinear Circuits]] —— 非线性元件为何不服从欧姆定律
- [[Superposition Theorem]] —— 功率 $p\propto i^2/v^2$ 不能叠加
- [[Wheatstone Bridge and Wye-Delta Transformation]] —— 分压/分流思想的进阶舞台：惠斯通电桥与 Y-Δ 变换
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
