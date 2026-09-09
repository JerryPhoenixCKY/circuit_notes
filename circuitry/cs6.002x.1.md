---
tags:
  - 电路学
  - 信号与系统
  - 电磁学
  - 知识树
date: 2026-08-15
aliases:
  - 电路原理
  - 电路与电子学
  - 电路基础
  - Circuits and Electronics
  - 6.002x
  - 电路原理知识树
---

# 电路原理 (Circuits and Electronics)

> [!NOTE] 本文件定位
> 「电路原理」的**知识树**，依据 MIT 6.002 官方教材 *Foundations of Analog and Digital Electronic Circuits* (Agarwal & Lang) 的 16 章结构组织。
> 作用：梳理知识点、标注重难点、导航跳转。**详细推导沉淀到各英文全称笔记**，随学习进度逐步扩充。
> ✅ 已建笔记　❗ 重难点　⚠️ 计划笔记（双链占位，待建）
>
> **命名约定**：未来笔记一律用英文全称命名（`英文全称`），中文名/缩写进 frontmatter `aliases`；电路图用 schemdraw 渲染成 `circuitry/assets/` 下的 SVG+PNG 嵌入。

## 知识树（按教材章节）

### Part 0 · 前置与数学工具
- **前置复习**
    - [[High School Electricity Review|高中电学复习]] ✅
- **数学工具**
    - [[Complex Numbers and Euler's Formula|复数与欧拉公式]] ✅
### Part 1 · 电路抽象与集总理论
- **电路抽象 (The Circuit Abstraction) — Ch.1**
    - [[The Circuit Abstraction|电路抽象]] ✅
        - 抽象的力量、集总电路抽象、LMD 三大约束、抽象适用局限
    - [[Lumped Matter Discipline|集总事物理论 (LMD)]] ✅
    - [[Practical Two-Terminal Elements|实际二端元件]] ✅（电池 / 线性电阻 / 关联变量约定 AVD）
    - [[Ideal Two-Terminal Elements|理想二端元件]] ✅（理想电压源 / 导线 / 电阻 / 电流源、元件定律）
    - [[Signal Representation|信号表示]] ✅（模拟信号 / 数字信号-取值离散化）
- **电磁学基础**
    - [[Maxwell's Equations|麦克斯韦方程组]] ✅
    - [[Two-Terminal Element Laws|二端元件定律]] ✅（电阻/电源/电容/电感的 v–i 关系总表）

### Part 2 · 电阻网络与线性电路分析
- **电阻网络 (Resistive Networks) — Ch.2**
    - [[Resistive Networks|电阻网络]] ✅
        - 拓扑术语：节点 (Node)/支路 (Branch)/回路 (Loop)/网孔 (Mesh)
    - [[Ohm's Law|欧姆定律]] ✅
    - [[Kirchhoff's Laws|基尔霍夫定律 (KCL / KVL)]] ✅ ❗
    - [[Basic Circuit Analysis Method|基本电路分析法]] ✅ ❗
        - 暴力法 (KVL-KCL)、元件组合规则 (Combination Rules)、节点法 (Node Analysis)
    - [[Circuit Analysis Methods in Practice|电路分析方法实战]] ✅ ❗（网孔法/节点法/支路法/叠加/戴维南对比、选型决策、完整例题）
    - [[Wheatstone Bridge and Wye-Delta Transformation|惠斯通电桥与星角变换]] ✅（ECE 2001 L1 扩展：电桥测阻/零示法/平衡条件 $R_x=R_2R_3/R_1$、Y-Δ/Δ-Y 等效变换、桥式网络化简例题）
- **网络定理 (Network Theorems) — Ch.3**
    - [[Superposition Theorem|叠加原理]] ✅ ❗
    - [[Thevenin's Theorem|戴维南定理]] ✅ ❗
    - [[Norton's Theorem|诺顿定理]] ✅ ❗
    - 最大功率传输 (Maximum Power Transfer) ✅（[[Maximum Power Transfer Theorem|最大功率传输定理]]）
- **非线性电路分析 (Nonlinear Circuits) — Ch.4**
    - [[Analysis of Nonlinear Circuits|非线性电路分析]] ✅ ❗
        - 分段线性化 (Piecewise Linearization) / 工作点 (Operating Point)
    - [[Small Signal Analysis|小信号分析]] ✅ ❗

### Part 3 · 数字抽象与器件
- **数字抽象 (The Digital Abstraction) — Ch.5**
    - [[The Digital Abstraction|数字抽象概述]] ✅ ❗
    - [[Static Discipline|静态纪律 (Static Discipline)]] ✅ ❗
    - [[Combinational Logic|组合逻辑 (Combinational Logic)]] ✅ ❗
    - [[Sequential Logic|时序逻辑 / 存储器 (Sequential Logic)]] ✅（双稳态 / SR 锁存器 / D 触发器 / 时钟同步 / 存储层次）
- **MOSFET 开关 (The MOSFET Switch) — Ch.6**
    - [[MOSFET|MOSFET 场效应管]] ✅（结构 / 符号 / 三种工作区）
    - [[The MOSFET Switch|MOSFET 开关]] ✅（S/SR 模型、开关电阻、门电路、导通/截止、静态约束）
- **MOSFET 放大器 (The MOSFET Amplifier) — Ch.7**
    - [[The MOSFET Amplifier|MOSFET 放大器]] ✅ （CS / CD / CG 三种组态、Q 点、增益、阻抗）
    - [[Large-Signal Model|大信号模型 (Large-Signal Model)]] ✅（Q 点 / 负载线 / 三区方程 / 沟道调制 / 偏置电路）
- **小信号模型 (The Small-Signal Model) — Ch.8**
    - [[Small Signal Analysis|小信号分析]] ✅ ❗（与 Ch.4 共用，BJT 参数 $g_m$、$r_\pi$、$r_o$）
    - [[Small Signal Circuit Representation|小信号电路表示 (Small Signal Circuit Representation)]] ✅（$g_m$/$r_o$、CS 增益 $A_v=-g_mR_D$、密勒效应）
- **能量存储元件 (Energy Storage Elements) — Ch.9**
    - [[Capacitor|电容 (Capacitor)]] ✅
    - [[Inductor|电感 (Inductor)]] ✅
    - [[Energy and Charge Conservation|能量 / 电荷 / 磁通守恒 (Energy and Charge Conservation)]] ✅（KCL ← 电荷守恒、KVL ← 能量守恒、LC 振荡）
    - [[Capacitive and Magnetic Devices|电容与磁器件 (Capacitive and Magnetic Devices)]] ✅（MOS 栅电容 $C_{ox}=\varepsilon/t_{ox}$、绕组电感 $L=N^2\mu A/\ell$、互感 $M=k\sqrt{L_1L_2}$、变压器）

### Part 4 · 动态电路（一阶/二阶与时域）
- **一阶暂态 (First-Order Transients) — Ch.10**
    - [[First-Order Transients|一阶暂态电路]] ✅ （RC / RL 阶跃、放电、方波、直觉分析、状态变量、传播延迟 $t_{pd}\sim R_{ON}C_L$）
    - 状态与状态变量 (State Variables) ✅（归入 First-Order Transients §二）
    - 传播延迟与数字抽象 (Propagation Delay) ✅（归入 First-Order Transients §七）
- **数字电路的能耗与功率 (Energy & Power) — Ch.11**
    - [[Energy and Power in Digital Circuits|数字电路的能量与功率]] ✅ （RC 充电 50% 损耗、$P_{dyn}=\alpha CV^2f$、NMOS 静态功耗、CMOS 零静态、DVFS）
- **二阶暂态 (Second-Order Circuits) — Ch.12**
    - [[Second-Order Transients|二阶暂态电路]] ✅ （LC 无阻尼振荡、串联/并联 RLC 欠/过/临界阻尼、$\zeta$/$\omega_0$、状态变量法、双电容/双电感）

### Part 5 · 正弦稳态与频域
- **正弦稳态：阻抗与频率响应 (Impedance) — Ch.13**
    - [[Sinusoidal Steady State|正弦稳态]] ✅（复指数激励、相量法、齐次+特解完整解、KCL/KVL 相量形式）
    - [[Impedance|阻抗 (Impedance)]] ✅（$Z_R=R,\ Z_C=1/j\omega C,\ Z_L=j\omega L$、分压/分流、功率因数、戴维南交流等效）
    - [[Frequency Response|频率响应]] ✅（$H(j\omega)$、Bode 图 $-20$/$-40$ dB/dec、$-3$ dB、极点/零点、带宽 $BW=\omega_0/Q$）
    - [[Filters|滤波器 (Filters)]] ✅（LP/HP/BP/Notch 传递函数、一阶 $-20$ dB/dec、二阶 $-40$ dB/dec、Butterworth/Chebyshev）
- **正弦稳态：谐振 (Resonance) — Ch.14**
    - [[Resonance|谐振 (Resonance)]] ✅（串联 $Z_{\min}=R$、并联 $Z_{\max}=R$、$\omega_0=1/\sqrt{LC}$、$Q=\omega_0L/R$、$BW=\omega_0/Q$、谐振峰）

### Part 6 · 有源器件与整流
- **运算放大器抽象 (Operational Amplifier) — Ch.15**
    - [[Operational Amplifier|运算放大器 (Op Amp)]] ✅（理想模型、虚短虚断、五参数、七种基本电路、积分器/微分器/Sallen-Key、饱和、正反馈、RC振荡器、二端口）



- **二极管 (Diodes) — Ch.16**
    - [[Diode|二极管 (Diode)]] ✅（I-V 特性、状态假设法、整流、削波钳位、Zener 稳压、LED/Schottky/Varactor）
- **进阶/扩展主题（跨章节）**
    - [[Amplifiers and Feedback|放大器与反馈]] ✅（反馈方程 $A/(1+A\beta)$、四大好处 G-B-I-O、正反馈/振荡、四拓扑）
    - [[Current Sources and Mirrors|电流源与电流镜]] ✅（偏置/有源负载、基本镜/Wilson/Cascode、$I_{\text{out}}=I_{\text{ref}}\cdot(W/L)_2/(W/L)_1$）
    - [[Power Supplies|电源]] ✅（线性稳压/LDO、开关 Buck/Boost/Buck-Boost、基准电压源）
    - [[DC-DC Converter|DC-DC 变换器]] ✅（Buck $V_o=D\cdot V_i$、Boost $V_o=V_i/(1-D)$、PWM/PFM、纹波/效率）


---

> [!TIP] 学习路线建议（非强制，按教材顺序推进）
> 前置/数学 → Ch.1–2 抽象与电阻网络 → Ch.3 网络定理 → Ch.4 非线性+小信号 → Ch.5 数字抽象 → Ch.6–9 器件(MOSFET/小信号/储能) → Ch.10–12 动态电路 → Ch.13–14 频域 → Ch.15–16 有源器件与二极管。
> 已建 ✅ 的笔记可立即复习；⚠️ 为待建框架占位，学到对应章再填充正文。
