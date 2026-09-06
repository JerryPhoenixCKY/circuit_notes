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
| Resistor | 电阻 | 耗散电能的元件，满足 $V = IR$，见 [[Two-Terminal Element Laws|二端元件定律]] |
| Battery | 电池（实际电压源） | 实际电压源模型：理想 $V_s$ 串联内阻 $R_{int}$，带载时 $V_{out}=V_s\frac{R_L}{R_{int}+R_L}$，见 [[Practical Two-Terminal Elements|实际二端元件]] |
| Linear Resistor | 线性电阻 | 满足欧姆定律 $v=iR$ 的电阻，阻值恒定，见 [[Ohm's Law|欧姆定律]] |
| Ideal Voltage Source | 理想电压源 | 两端电压被强制为定值 $V_s$ 的二端元件，可提供任意电流，见 [[Ideal Two-Terminal Elements|理想二端元件]] |
| Capacitor | 电容 | 存储电场能的元件，满足 $i = C\frac{dv}{dt}$ |
| Inductor | 电感 | 存储磁场能的元件，满足 $v = L\frac{di}{dt}$ |
| Capacitance | 电容值 | 电容元件存储电荷能力的量度 $C$ |
| Inductance | 电感值 | 电感元件存储磁通能力的量度 $L$ |
| Voltage Source | 电压源 | 提供恒定电压的电源 |
| [[Superposition Theorem|Current Source]] | 电流源 | 提供恒定电流的电源，叠加时置零（开路）；独立源与受控源之分；并联叠加，禁止不同值串联 |
| Independent Source | 独立源 | 值由自身决定的电源 |
| Dependent Source | 受控源 | 值由电路中其他电压/电流控制的电源 |
| Constitutive Relation | 本构关系 | 描述元件物理量间固有约束的方程（如 $v=ir$、$q=Cv$、$\phi=Li$），见 [[Two-Terminal Element Laws|二端元件定律]] |
| Associated Variables Discipline | 关联变量约定 (AVD) | 端口电流 i 取**流入 + 端**的方向，$p=vi$ 为吸收功率；见 [[Practical Two-Terminal Elements|实际二端元件]] |
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
| Voltage Divider | 分压器 | 串联电阻按阻值瓜分总电压：$V_{out}=V_{in}\dfrac{R_2}{R_1+R_2}$，见 [[Ohm's Law|欧姆定律 §三]] |
| Current Divider | 分流器 | 并联电阻按电导瓜分总电流：$I_1=I\dfrac{R_2}{R_1+R_2}$，见 [[Ohm's Law|欧姆定律 §三]] |
| Equivalent Resistance | 等效电阻 | 把网络化简为端口单电阻 $R_{eq}$（串联相加 / 并联取倒数和），见 [[Resistive Networks|电阻网络 §四]] |
| Series Combination | 串联组合 | 电阻首尾相接、电流相同，等效 $R_{eq}=\sum R_k$ |
| Parallel Combination | 并联组合 | 电阻两端共节点、电压相同，等效 $1/R_{eq}=\sum 1/R_k$ |
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
| [[Basic Circuit Analysis Method\|Node Analysis]] | 节点法 / 节点分析法 / Nodal Analysis | 以节点电压为主未知数、对非参考节点写 KCL 的系统分析法，是 KVL/KCL 法的特例 |
| Node Voltage | 节点电压 | 某节点相对参考节点（地）的电势，节点法的主未知数 |
| Reference Node | 参考节点 / 地 (Ground) | 电压测量的基准点，电势定义为 0 |
| Conductance | 电导 (G) | 电阻的倒数 $G=1/R$，单位西门子 (S)，节点法中的核心变量 |
| Associated Variables Discipline | 关联变量约定 (AVD) | 电流定义为从元件正电压端流入；此时 $p=vi$ 为吸收功率 |
| Element Combination Rules | 元件组合规则 | 串并联等效化简（串联 $R$ 相加、并联 $G$ 相加、源串并联），配合叠加可解复杂电路 |
| Basic KVL/KCL Method | 基本 KVL/KCL 方法 / 暴力法 | 写全部元件关系 + 全部 KCL + 全部 KVL 后求解，通用但方程数爆炸 |

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
| [[Small Signal Analysis]] | 小信号分析 | 在工作点附近将非线性器件线性化的分析方法 |
| Small-Signal Conductance | 小信号电导 | 二极管工作点处的导数 $g_D = I_{DQ}/V_T$，单位西门子 (S) |
| Small-Signal Resistance | 小信号电阻 | 二极管工作点处的交流电阻 $r_d = V_T/I_{DQ}$ |
| Transconductance | 跨导 | 器件输出电流对输入电压的敏感度 $g_m = \partial i_{out}/\partial v_{in}$，单位西门子 |
| Input Resistance | 输入电阻 | 从放大器输入端看进去的小信号电阻 $R_{in}$ |
| Output Resistance | 输出电阻 | 从放大器输出端看进去的小信号电阻 $R_{out}$ |
| Voltage Gain | 电压增益 | 放大器输出电压与输入电压之比 $A_v = v_{out}/v_{in}$ |
| Current Gain | 电流增益 | 放大器输出电流与输入电流之比 $A_i = i_{out}/i_{in}$ |
| Bias Circuit | 偏置电路 | 为非线性器件建立稳定直流工作点的电路 |
| Thermal Voltage | 热电压 | $V_T = kT/q \approx 26\text{ mV}$（室温），小信号模型的核心参数 |

## 8. Signals & Response（信号与响应）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Analog Signal | 模拟信号 | 连续取值、连续变化的信号，见 [[Signal Representation|信号表示]] |
| Digital Signal | 数字信号 | 离散取值（0/1）的信号，抗噪源于阈值还原，见 [[Signal Representation|信号表示]] |
| Value Discretization | 取值离散化 | 把连续取值映射为有限离散电平的过程，数字抽象的核心，见 [[Signal Representation|信号表示]] |
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

## 10. Digital Abstraction（数字抽象）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[The Digital Abstraction\|Digital Abstraction]] | 数字抽象 | 把连续取值离散为 0/1 的抽象层，建立在集总电路抽象之上 |
| Value Discretization | 取值离散化 | 仅允许信号取两种值（HIGH/LOW ↔ 1/0 ↔ TRUE/FALSE） |
| [[The Digital Abstraction\|Digital System]] | 数字系统 | 发送端→带噪声导线→接收端，靠阈值判读还原 0/1 |
| Noise | 噪声 | 叠加在信号上的不期望电压波动，模拟系统的精度杀手 |
| [[Static Discipline\|Static Discipline]] | 静态纪律 | 输入合法 ⇒ 输出合法；用四阈值量化噪声容限 |
| [[Static Discipline\|Noise Margin]] | 噪声容限 | 信号变非法前能容忍的最大噪声：$NM_H=V_{OH}-V_{IH},\ NM_L=V_{IL}-V_{OL}$ |
| Voltage Threshold | 电压阈值 | 判读逻辑值的门槛电压 |
| [[Static Discipline\|Voltage Transfer Characteristic (VTC)]] | 电压传输特性 | $V_{out}$ 对 $V_{in}$ 的曲线，过渡区高增益实现信号再生 |
| Forbidden Region | 禁区 / 无主之地 | 发送/接收都不使用的电压间隙，即噪声容限的物理载体 |
| [[Combinational Logic\|Combinational Logic]] | 组合逻辑 | 输出仅为当前输入函数的数字逻辑（无记忆） |
| [[Combinational Logic\|Logic Gate]] | 逻辑门 | AND/OR/NOT/NAND 等实现布尔运算的电路单元 |
| Boolean Algebra | 布尔代数 | 以 0/1 为变量的代数体系，逻辑门的理论基础 |
| Truth Table | 真值表 | 枚举全部 $2^n$ 输入组合以定义组合函数 |
| Combinational Gate Abstraction | 组合门抽象 | 门作为黑箱：遵守静态纪律、输出仅依赖输入 |

## 11. Upcoming Topics（后续章节专题 · 框架占位）

> [!NOTE] 说明
> 以下词条对应教材 Ch.1–16 与附录的后续内容，双链为占位。其中 **Ch.1 五个专题笔记已建**（`[[The Circuit Abstraction]]`、`[[Practical Two-Terminal Elements]]`、`[[Ideal Two-Terminal Elements]]`、`[[Signal Representation]]`、`[[Two-Terminal Element Laws]]`，标记为 ✅），其余待建。学到对应章时再补正文并消除未解析链接。与 [[cs6.002x.1|知识树]] 同步维护。

| English                                    | 中文          | 解释                              |
| :----------------------------------------- | :---------- | :------------------------------ |
| [[The Circuit Abstraction]] ✅              | 电路抽象        | Ch.1：抽象的力量、集总电路抽象、LMD、抽象适用局限    |
| Lumped Circuit Abstraction                 | 集总电路抽象      | Ch.1：把空间分布系统抽象为集总元件网络           |
| [[Practical Two-Terminal Elements]] ✅      | 实际二端元件      | Ch.1：电池 / 线性电阻 / 关联变量约定 AVD     |
| [[Ideal Two-Terminal Elements]] ✅          | 理想二端元件      | Ch.1：理想电压源 / 导线 / 电阻 / 电流源、元件定律 |
| [[Signal Representation]] ✅                | 信号表示        | Ch.1：模拟信号 / 数字信号-取值离散化          |
| [[Resistive Networks]] ✅                   | 电阻网络        | Ch.2：拓扑术语、KCL/KVL、基本分析法、分压分流、串并联化简 |
| [[Ohm's Law]] ✅                             | 欧姆定律        | Ch.2：线性电阻 $V=IR$ 的电压-电流关系、功率、分压分流 |
| [[Maximum Power Transfer Theorem]] ✅        | 最大功率传输定理    | Ch.3：负载获最大功率的条件 $R_L=R_{Th}$    |
| [[Analysis of Nonlinear Circuits]] ✅        | 非线性电路分析     | Ch.4：分段线性化、工作点求解、负载线、图解法 |
| [[MOSFET]]                                 | MOSFET 场效应管 | Ch.6：结构 / 符号 / 截止-饱和-线性三区       |
| [[The MOSFET Switch]]                      | MOSFET 开关   | Ch.6：SRC 模型、开关电阻、导通/截止          |
| [[The MOSFET Amplifier]]                   | MOSFET 放大器  | Ch.7：大信号分析、负载线、偏置               |
| Large-Signal Model                         | 大信号模型       | Ch.7：含器件非线性的完整 v–i 模型           |
| Gain                                       | 增益          | Ch.8：电压/电流/功率增益 $A_v, A_i$      |
| [[Capacitor]]                              | 电容          | Ch.9：本构关系 $q=Cv$、串并联、储能         |
| [[Inductor]]                               | 电感          | Ch.9：本构关系 $\phi=Li$、串并联、储能      |
| Energy Charge Flux Conservation            | 能量/电荷/磁通守恒  | Ch.9：电容电感的能量与守恒关系               |
| [[First-Order Transients]]                 | 一阶暂态电路      | Ch.10：RC/RL 阶跃、放电、方波、直觉分析       |
| State Variables                            | 状态变量        | Ch.10：描述动态系统所需的最小变量集            |
| Propagation Delay                          | 传播延迟        | Ch.10：数字信号沿导线的延迟 $t_{pd}$       |
| [[Energy and Power in Digital Circuits]]   | 数字电路的能量与功率  | Ch.11：RC 平均功率、逻辑门功耗、NMOS/CMOS   |
| [[Second-Order Transients]]                | 二阶暂态电路      | Ch.12：LC/RLC 欠/过/临界阻尼、状态变量法     |
| [[Sinusoidal Steady State]]                | 正弦稳态        | Ch.13：复指数激励、齐次/特解、完整解           |
| [[Impedance]]                              | 阻抗          | Ch.13：电阻/电容/电感阻抗、分压频域分析         |
| [[Frequency Response]]                     | 频率响应        | Ch.13：幅频/相频、Bode 图、滤波器          |
| [[Filters]]                                | 滤波器         | Ch.13–14：低通/高通/带通/陷波、分频网络       |
| [[Resonance]]                              | 谐振          | Ch.14：并联/串联 RLC 频率响应、Bode、储能    |
| [[Operational Amplifier]]                  | 运算放大器       | Ch.15：理想模型、虚短虚断、输入/输出电阻         |
| Op Amp Circuits                            | 运放电路        | Ch.15：同相/反相/跟随器/加法器/减法器         |
| Op Amp RC Circuits                         | 运放 RC 电路    | Ch.15：积分器/微分器/Sallen-Key 有源滤波   |
| [[Diode]]                                  | 二极管         | Ch.16：特性、假设状态法、钳位/削波/整流桥/Zener  |


---

## 相关笔记

- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
- [[Maxwell's Equations]] / [[Lumped Matter Discipline]] / [[Superposition Theorem]] —— 已建专题笔记
