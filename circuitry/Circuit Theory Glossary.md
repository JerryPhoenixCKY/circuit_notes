---
tags:
  - 电路学
  - 术语表
  - 课程笔记
date: 2026-08-15
aliases:
  - 电路理论术语表
  - 电路术语表
  - 术语表
  - 中英对照词汇表
  - Circuit Theory Glossary
  - Glossary
  - Terminology
---

# Circuit Theory Glossary

> [!NOTE] 说明
> 「电路原理」核心理论词汇的**中英对照与简要解释**，覆盖目前所学内容（基础量、元件、拓扑、定律、电磁学、LMD、信号与数学工具）。随学习进度持续扩充。

---

## 1. Basic Quantities（基本物理量）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Voltage | 电压 | 两点间的电势差，驱动电流的"压力"，单位伏特 (V) |
| Current | 电流 | 电荷的定向流动速率，单位安培 (A) |
| Electric Field | 电场 | 电荷激发的场 $\mathbf{E}$，对电荷施加力 |
| Magnetic Field | 磁场 | 电流/磁体激发的场 $\mathbf{B}$ |
| Current Density | 电流密度 | 单位面积流过的电流 $\mathbf{J}$ |
| Charge Density | 电荷密度 | 单位体积/面积/长度内的电荷量 $\rho$ |
| Permittivity | 介电常数 | 表征材料对电场的响应能力，真空值 $\epsilon_0$ |
| Permeability | 磁导率 | 表征材料对磁场的响应能力，真空值 $\mu_0$ |

## 2. Circuit Elements（电路元件）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Resistor | 电阻 | 耗散电能的元件，满足 $V = IR$ |
| Capacitor | 电容 | 存储电场能的元件，满足 $i = C\frac{dv}{dt}$ |
| Inductor | 电感 | 存储磁场能的元件，满足 $v = L\frac{di}{dt}$ |
| Capacitance | 电容值 | 电容元件存储电荷能力的量度 $C$ |
| Inductance | 电感值 | 电感元件存储磁通能力的量度 $L$ |
| Voltage Source | 电压源 | 提供恒定电压的电源 |
| Current Source | 电流源 | 提供恒定电流的电源 |
| Independent Source | 独立源 | 值由自身决定的电源 |
| Dependent Source | 受控源 | 值由电路中其他电压/电流控制的电源 |
| Lumped Elements | 集总元件 | 尺寸远小于波长、可视为"点"的元件 |
| Ideal Wire | 理想导线 | 无电阻、无寄生效应、两端等电位的导线 |
| Diode | 二极管 | 单向导电的非线性器件 |
| Transistor | 晶体管 | 三端放大/开关器件，放大器核心 |
| Amplifier | 放大器 | 将小信号放大为大幅值的电路 |

## 3. Circuit Topology（电路拓扑）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Node | 节点 | 两个及以上支路的连接点 |
| Branch | 支路 | 两个节点之间的一段电路 |
| Loop | 回路 | 从某节点出发沿支路回到原点的闭合路径 |
| Mesh | 网孔 | 内部不含其他回路的回路（平面电路） |
| Series | 串联 | 元件首尾相接，电流相同 |
| Parallel | 并联 | 元件两端共接节点，电压相同 |
| Short Circuit | 短路 | 两端直接相连，电压为 0，等效导线 |
| Open Circuit | 开路 | 电路断开，电流为 0 |

## 4. Laws & Theorems（基本定律与定理）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Ohm's Law | 欧姆定律 | $V = IR$，线性电阻的电压-电流关系 |
| [[Kirchhoff's Current Law (KCL)|Kirchhoff's Current Law (KCL)]] | 基尔霍夫电流定律 | 节点处电流代数和为 0（电荷守恒） |
| [[Kirchhoff's Voltage Law (KVL)|Kirchhoff's Voltage Law (KVL)]] | 基尔霍夫电压定律 | 回路中电压代数和为 0（能量守恒） |
| [[Superposition Theorem]] | 叠加原理 / 叠加定理 | 线性电路中响应 = 各独立源单独作用之和 |
| [[Thevenin's Theorem]] | 戴维南定理 / 戴维南等效 | 线性二端网络可等效为电压源串联电阻 |
| [[Norton's Theorem]] | 诺顿定理 / 诺顿等效 | 线性二端网络可等效为电流源并联电阻 |
| Linearity | 线性 | 系统满足齐次性与可加性的性质 |
| Homogeneity | 齐次性 | 输入放大 k 倍，输出也放大 k 倍 |
| Additivity | 可加性 | 多个输入之和的响应 = 各自响应之和 |
| Lenz's Law | 楞次定律 | 感应效应总是反抗引起它的磁通变化 |

## 5. Maxwell's Equations & Field Theory（麦克斯韦方程组与场论）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[Maxwell's Equations]] | 麦克斯韦方程组 | 统一电磁学的四个基本方程 |
| Gauss's Law | 高斯定律（电场） | 电通量正比于闭合面内净电荷 |
| Gauss's Law for Magnetism | 磁场高斯定律 | 磁通量恒为 0，不存在磁单极子 |
| Faraday's Law | 法拉第电磁感应定律 | 变化的磁场产生感应电场 |
| Ampère–Maxwell Law | 安培-麦克斯韦定律 | 电流与变化的电场共同产生磁场 |
| Charge Continuity Equation | 电荷连续性方程 | 流出电流 = 区域内电荷减少速率 |
| Charge Conservation | 电荷守恒 | 电荷既不能创造也不能消灭 |
| Displacement Current | 位移电流 | 变化的电场等效的"电流"项 |
| Differential Form | 微分形式 | 用散度/旋度描述场在每点的性质 |
| Integral Form | 积分形式 | 用通量/环量描述场的整体性质 |
| Divergence | 散度 | 场在某点的"源"强度 $\nabla \cdot$ |
| Curl | 旋度 | 场在某点的"旋转"强度 $\nabla \times$ |
| Flux | 通量 | 场穿过某曲面的总量 |

## 6. Lumped Matter Discipline（集总事物理论）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[Lumped Matter Discipline\|Lumped Matter Discipline (LMD)]] | 集总事物理论 | 使电路可用代数方程描述的约束假设 |
| Constitutive Relation | 本构关系 | 元件自身的电压-电流关系（如 $V=IR$） |
| Quasi-static Assumption | 准静态假设 | 电路尺寸远小于波长，传播视为瞬时 |
| Wavelength | 波长 | 电磁波一个周期的空间长度 $\lambda$ |
| Propagation Delay | 传播延迟 | 信号沿导线传播所需时间 |
| Parasitic Capacitance | 寄生电容 | 元件外部不希望存在的电容效应 |
| Parasitic Inductance | 寄生电感 | 元件外部不希望存在的电感效应 |
| Transmission Line | 传输线 | 波长与尺寸可比时需用分布参数建模的导线 |
| Distributed Circuit | 分布参数电路 | 参数沿导线分布、不能用集总模型描述的电路 |

## 7. Devices & Nonlinear Analysis（器件与非线性分析）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| DC Analysis | 直流分析 | 恒定电压/电流下的电路分析 |
| AC Analysis | 交流分析 | 正弦稳态下的电路分析 |
| Saturation | 饱和状态 | 器件输出达到极限、不再随输入线性变化的状态 |
| Bias Point | 偏置点 | 为器件设定的直流工作点 |
| Operating Point | 工作点 | 同 Bias Point |
| Quiescent Point | 静态工作点 | 无信号输入时器件的直流状态点 |
| Load Line | 负载线 | 负载约束下器件的工作点轨迹 |
| Small Signal Analysis | 小信号分析 | 在工作点附近将非线性器件线性化的分析方法 |

## 8. Signals & Response（信号与响应）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Analog Signal | 模拟信号 | 连续取值、连续变化的信号 |
| Digital Signal | 数字信号 | 离散取值（0/1）的信号 |
| Time Domain | 时域 | 以时间为自变量的分析视角 |
| Frequency Domain | 频域 | 以频率为自变量的分析视角 |
| Transient Response | 瞬态响应 | 电路从初始状态过渡到稳态期间的响应 |
| Time Constant | 时间常数 | 一阶电路响应变化的特征时间 $\tau = RC$ 或 $\tau = L/R$ |
| Impedance | 阻抗 | 交流下的广义电阻 $Z = R + jX$ |
| Filter | 滤波器 | 按频率选择性通过/衰减信号的电路 |

## 9. Mathematical Tools（数学工具）

| English                | 中文    | 解释                                       |
| :--------------------- | :---- | :--------------------------------------- |
| [[Complex Numbers and Euler's Formula\|Euler's Formula]] | 欧拉公式  | $e^{j\theta} = \cos\theta + j\sin\theta$ |
| [[Complex Numbers and Euler's Formula\|Euler's Identity]] | 欧拉恒等式 | $e^{j\pi} + 1 = 0$                       |
| [[Complex Numbers and Euler's Formula\|Inverse Euler Formula]] | 反欧拉公式 | 用复指数表示三角函数 |
| [[Complex Numbers and Euler's Formula\|Complex Number]] | 复数    | $z = x + jy$，含实部与虚部 |
| [[Complex Numbers and Euler's Formula\|Complex Representation]] | 复数表示  | 代数/三角/极坐标三种等价形式 |
| [[Complex Numbers and Euler's Formula\|Magnitude]] | 模     | 复数的长度 $r = \|z\|$ |
| [[Complex Numbers and Euler's Formula\|Phase]] | 相角    | 复数的辐角 $\theta = \arg z$ |

---

## 相关笔记

- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
- [[Maxwell's Equations]] / [[Lumped Matter Discipline]] / [[Superposition Theorem]] —— 已建专题笔记
