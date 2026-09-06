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
> **命名约定**：未来笔记一律用英文全称命名（`[[英文全称]]`），中文名/缩写进 frontmatter `aliases`；电路图用 schemdraw 渲染成 `circuitry/assets/` 下的 SVG+PNG 嵌入。

## 知识树（按教材章节）

### Part 0 · 前置与数学工具
- **前置复习**
    - [[High School Electricity Review|高中电学复习]] 
- **数学工具**
    - [[Complex Numbers and Euler's Formula|复数与欧拉公式]] 
### Part 1 · 电路抽象与集总理论
- **电路抽象 (The Circuit Abstraction) — Ch.1**
    - [[The Circuit Abstraction|电路抽象]]
        - 抽象的力量、集总电路抽象、LMD 三大约束、抽象适用局限
    - [[Lumped Matter Discipline|集总事物理论 (LMD)]] 
    - [[Practical Two-Terminal Elements|实际二端元件]] （电池 / 线性电阻 / 关联变量约定 AVD）
    - [[Ideal Two-Terminal Elements|理想二端元件]] （理想电压源 / 导线 / 电阻 / 电流源、元件定律）
    - [[Signal Representation|信号表示]]  （模拟信号 / 数字信号-取值离散化）
- **电磁学基础**
    - [[Maxwell's Equations|麦克斯韦方程组]]  
    - [[Two-Terminal Element Laws|二端元件定律]]  （电阻/电源/电容/电感的 v–i 关系总表）

### Part 2 · 电阻网络与线性电路分析
- **电阻网络 (Resistive Networks) — Ch.2**
    - [[Resistive Networks|电阻网络]] ✅
        - 拓扑术语：节点 (Node)/支路 (Branch)/回路 (Loop)/网孔 (Mesh)
    - [[Ohm's Law|欧姆定律]] ✅
    - [[Kirchhoff's Laws|基尔霍夫定律 (KCL / KVL)]] ✅ ❗
    - [[Basic Circuit Analysis Method|基本电路分析法]] ✅ ❗
        - 暴力法 (KVL-KCL)、元件组合规则 (Combination Rules)、节点法 (Node Analysis)
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
    - 时序逻辑 / 存储器 (Sequential Logic / Memory) ⚠️
- **MOSFET 开关 (The MOSFET Switch) — Ch.6**
    - [[MOSFET|MOSFET 场效应管]] ⚠️（结构 / 符号 / 三种工作区）
    - [[The MOSFET Switch|MOSFET 开关]] ⚠️（SRC 模型、开关电阻、导通/截止）
- **MOSFET 放大器 (The MOSFET Amplifier) — Ch.7**
    - [[The MOSFET Amplifier|MOSFET 放大器]] ⚠️（大信号分析、负载线、偏置）
    - 大信号模型 (Large-Signal Model) ⚠️
- **小信号模型 (The Small-Signal Model) — Ch.8**
    - [[Small Signal Analysis|小信号分析]] ✅ ❗（与 Ch.4 共用）
    - 小信号电路表示、输入/输出电阻、增益 (Gain) ⚠️
- **能量存储元件 (Energy Storage Elements) — Ch.9**
    - [[Capacitor|电容 (Capacitor)]] ⚠️（ constituent law $q=Cv$、串并联）
    - [[Inductor|电感 (Inductor)]] ⚠️（ constituent law $\phi=Li$、串并联）
    - 能量/电荷/磁通守恒 ⚠️
    - MOS 栅电容 / 绕组电感 / 变压器 ⚠️

### Part 4 · 动态电路（一阶/二阶与时域）
- **一阶暂态 (First-Order Transients) — Ch.10**
    - [[First-Order Transients|一阶暂态电路]] ⚠️（RC / RL 阶跃、放电、方波、直觉分析）
    - 状态与状态变量 (State Variables) ⚠️
    - 传播延迟与数字抽象 (Propagation Delay) ⚠️
- **数字电路的能耗与功率 (Energy & Power) — Ch.11**
    - [[Energy and Power in Digital Circuits|数字电路的能量与功率]] ⚠️（RC 平均功率、逻辑门功耗、NMOS/CMOS）
- **二阶暂态 (Second-Order Circuits) — Ch.12**
    - [[Second-Order Transients|二阶暂态电路]] ⚠️（LC / RLC 欠/过/临界阻尼、串联/并联、状态变量法）
    - 直觉分析、双电容/双电感电路 ⚠️

### Part 5 · 正弦稳态与频域
- **正弦稳态：阻抗与频率响应 (Impedance) — Ch.13**
    - [[Sinusoidal Steady State|正弦稳态]] ⚠️（复指数激励、齐次/特解、完整解）
    - [[Impedance|阻抗 (Impedance)]] ⚠️（电阻/电容/电感阻抗、分压频域分析）
    - [[Frequency Response|频率响应]] ⚠️（幅频/相频、Bode 图、滤波器）
    - [[Filters|滤波器 (Filters)]] ⚠️（低通/高通/带通/陷波、分频网络）
- **正弦稳态：谐振 (Resonance) — Ch.14**
    - [[Resonance|谐振 (Resonance)]] ⚠️（并联/串联 RLC 频率响应、Bode、滤波器实例、储能）

### Part 6 · 有源器件与整流
- **运算放大器抽象 (Operational Amplifier) — Ch.15**
    - [[Operational Amplifier|运算放大器 (Op Amp)]] ⚠️（理想模型、虚短虚断、输入/输出电阻）
    - 基本运放电路 ⚠️（同相/反相/电压跟随器/加法器/减法器）
    - 运放 RC 电路 ⚠️（积分器/微分器/Sallen-Key 有源滤波）
    - 饱和 / 正反馈 / RC 振荡器 / 二端口 ⚠️
- **二极管 (Diodes) — Ch.16**
    - [[Diode|二极管 (Diode)]] ⚠️（特性、假设状态法、钳位/削波/限幅/整流桥/Zener 稳压）

### 附录（Appendices）
- **附录 A** Maxwell's Equations & LMD（已并入 [[Maxwell's Equations]] / [[Lumped Matter Discipline]]）
- **附录 B** [[Trigonometric Functions and Identities|三角恒等式]] ⚠️
- **附录 C** [[Complex Numbers and Euler's Formula|复数]] ✅（已建独立笔记）
- **附录 D** [[Solving Simultaneous Linear Equations|线性方程组求解]] ⚠️

---

> [!TIP] 学习路线建议（非强制，按教材顺序推进）
> 前置/数学 → Ch.1–2 抽象与电阻网络 → Ch.3 网络定理 → Ch.4 非线性+小信号 → Ch.5 数字抽象 → Ch.6–9 器件(MOSFET/小信号/储能) → Ch.10–12 动态电路 → Ch.13–14 频域 → Ch.15–16 有源器件与二极管。
> 已建 ✅ 的笔记可立即复习；⚠️ 为待建框架占位，学到对应章再填充正文。
