---
tags:
  - 电路学
  - 器件
  - 半导体
date: 2026-09-07
aliases:
  - MOSFET
  - 金属-氧化物半导体场效应管
  - 场效应管
  - MOS 场效应晶体管
  - Metal–Oxide–Semiconductor Field-Effect Transistor
---

# MOSFET（金属-氧化物半导体场效应管）

> [!NOTE] 定位
> MOSFET 是数字电路（开关）与模拟电路（放大器）共同的**核心有源器件**。本笔记对应教材 Ch.6（The MOSFET Switch）与 Ch.7（The MOSFET Amplifier）的器件基础：物理结构 → 符号与分类 → 三工作区 → SRC 大信号模型 → 作为开关的电阻特性 → 作为放大器的偏置与负载线。
> 前置：[[Ohm's Law]]、[[Kirchhoff's Laws]]；下游：[[The MOSFET Switch]]、[[The MOSFET Amplifier]]、[[Small Signal Analysis]]。

## 一、物理结构

MOSFET（以 NMOS 增强型为例）自顶向下四层：

- **Gate（栅）**：多晶硅，与沟道间由极薄 **SiO₂ 氧化层** 绝缘 → 栅极几乎不取电流（输入阻抗极高）。
- **Oxide（氧化层）**：厚度 $t_{ox}$ 决定工艺参数 $C_{ox}$（单位面积栅电容）。
- **Channel（沟道）**：源–漏之间的半导体表面反型层；栅压 $v_{GS}$ 超过阈值 $V_T$ 后才"感应"出导电沟道。
- **Source / Drain（源 / 漏）**：同型重掺杂区，对称（可互换，取决于谁电位更低）。

> [!TIP] 为什么叫"场效应"？
> 栅压在氧化层下产生**垂直电场**，静电"感应"出表面沟道；沟道电导再由 $v_{GS}$ 控制，从而以**电压控制电流**——这正是 FET（Field-Effect Transistor）的本义，与双极型（电流控制）相对。

## 二、符号与分类

| 类型 | 沟道 | 阈值 | 导通条件 | 符号要点 |
|---|---|---|---|---|
| NMOS 增强型 | n | $V_T>0$ | $v_{GS}\ge V_T$ | 箭头**向内**（指向衬底） |
| PMOS 增强型 | p | $V_T<0$ | $v_{SG}\ge |V_T|$ | 箭头**向外** |
| 耗尽型 | n/p | 零偏即有沟道 | 常通 | 虚线沟道 |

> [!IMPORTANT] NMOS 与 PMOS 的对称性
> 一切 NMOS 公式把电压取负、电流反向即得到 PMOS（衬底接最高电位）。下文本笔记以 **NMOS 增强型** 为基准推导。

## 三、三个工作区（大信号 SRC 模型）

NMOS 增强型，令 $v_{DS}\ge 0$，定义 **过驱电压 (overdrive)** $v_{OV}=v_{GS}-V_T$，**饱和电压 (saturation voltage)** $v_{DS,sat}=v_{OV}=v_{GS}-V_T$。

$$
i_{DS}=
\begin{cases}
0, & v_{GS}<V_T \quad\textbf{(Cutoff 截止)}\\[6pt]
K\big[(v_{GS}-V_T)v_{DS}-\tfrac{1}{2}v_{DS}^{2}\big], & V_T\le v_{GS},\; 0\le v_{DS}< v_{GS}-V_T \quad\textbf{(Triode 线性/三极管)}\\[6pt]
\dfrac{K}{2}(v_{GS}-V_T)^{2}, & V_T\le v_{GS},\; v_{DS}\ge v_{GS}-V_T \quad\textbf{(Saturation 饱和)}
\end{cases}
$$

其中 $K=\dfrac{1}{2}\mu_n C_{ox}\dfrac{W}{L}$（跨导参数，单位 mA/V² 量级），与工艺、宽长比 $W/L$ 相关。

> [!NOTE] 三区物理含义
> - **截止 Cutoff**：$v_{GS}<V_T$，无反型沟道，$i_{DS}=0$（开关断开）。
> - **线性/三极管 Triode**：$v_{DS}$ 很小，沟道全程导通，器件近似为**受 $v_{GS}$ 控制的电阻** $R_{on}\approx 1/[K(v_{GS}-V_T)]$（开关闭合、模拟传输门）。
> - **饱和 Saturation**：$v_{DS}$ 足够大，沟道在漏端"夹断"，电流**饱和**为仅由 $v_{GS}$ 决定的常量——放大器工作区。

![[mosfet_id_vds.svg|420]]

## 四、饱和区平方律（放大器基础）

饱和区 $i_{DS}$ 只与 $v_{GS}$ 有关，呈**平方律**：

$$i_{DS}=\frac{K}{2}(v_{GS}-V_T)^2,\qquad v_{GS}\ge V_T$$

![[mosfet_id_vgs.svg|420]]

> [!IMPORTANT] 平方律是"一阶"模型
> 真实工艺有迁移率退化、沟道长度调制 ($\lambda$)、体效应 ($V_{SB}$) 等二阶效应；本笔记用平方律建立直觉，小信号与高阶效应见 [[Small Signal Analysis]]。

## 五、作为开关（数字抽象）

- **关 (OFF)**：$v_{GS}<V_T$ → $i_{DS}=0$，等效开路。
- **开 (ON)**：$v_{GS}\gg V_T$ → 进入深三极管，等效小电阻 $R_{on}\approx 1/[K(v_{GS}-V_T)]$。
- 数字抽象里把 $R_{on}$ 当作"低"，开路当作"高"，构成 NAND/NOR 等门电路（见 [[Combinational Logic]]、[[The Digital Abstraction]]）。

## 六、作为放大器（模拟基础）

共源 (Common-Source) 放大器：栅极接输入 $v_{IN}=v_{GS}$，漏极经负载电阻 $R_D$ 接 $V_{DD}$，输出 $v_{OUT}=v_{DS}$。

**负载线**：由 KVL 在输出回路得
$$i_{DS}=\frac{V_{DD}-v_{DS}}{R_D}$$

它与器件 i–v 曲线（§三）的交点即**工作点 Q (Operating Point / Quiescent Point)**。偏置 Q 必须落在**饱和区**（$v_{DS,Q}\ge v_{GS,Q}-V_T$），放大器才有线性增益。

![[amplifier_loadline.svg|420]]

**转移特性** $v_{OUT}$–$v_{IN}$：

- $v_{IN}<V_T$ → 截止，$v_{OUT}=V_{DD}$；
- $V_T\le v_{IN}$ 且 Q 在饱和区 → $v_{OUT}$ 近似线性下降（**增益区**），小信号增益 $A_v\approx -g_m R_D$；
- $v_{IN}$ 很大 → 进入三极管区，$v_{OUT}$ 被拉低到一个非零下限（电阻负载无法到 0）。

![[amplifier_transfer.svg|420]]

> [!TIP] 开关 vs 放大器：同一器件，两种用法
> 关键在**工作区与偏置**：截止/深三极管 → 数字开关；饱和区 + 合适 Q 点 → 线性放大器。小信号分析即在 Q 点对平方律做一阶泰勒展开，见 [[Small Signal Analysis]]。

## 七、相关笔记

- 前置：[[Ohm's Law]]、[[Kirchhoff's Laws]]、[[Two-Terminal Element Laws]]
- 器件物理/符号：[[MOSFET]]（本笔记）
- 开关应用：[[The MOSFET Switch]]、[[The Digital Abstraction]]、[[Combinational Logic]]、[[Sequential Logic]]
- 放大器：[[The MOSFET Amplifier]]、[[Small Signal Analysis]]
- 大信号模型：[[Large-Signal Model]]
- 知识树：[[cs6.002x.1]]
