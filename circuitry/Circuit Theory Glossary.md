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
| [[Wheatstone Bridge and Wye-Delta Transformation\|Wheatstone Bridge]] | 惠斯通电桥 | 四臂桥式测阻电路：调节标准电阻使检流计零偏，平衡时 $R_x = R_2R_3/R_1$（零示法，精度只取决于电阻比） |
| [[Wheatstone Bridge and Wye-Delta Transformation\|Y-Δ Transformation]] | 星角变换 / Y-Δ 变换 | 三端 Δ(Π) 与 Y(T) 电阻网络的等效互换：$R_a = R_{ab}R_{ca}/\sum R_\Delta$，$R_{ab} = \sum R_aR_b/R_c$；化简非串并联（桥式）网络 |

## 4. Laws & Theorems（基本定律与定理）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| Ohm's Law | 欧姆定律 | $V = IR$，线性电阻的电压-电流关系 |
| [[Kirchhoff's Laws|KCL]] | 基尔霍夫电流定律 | 节点处电流代数和为 0（电荷守恒） |
| [[Kirchhoff's Laws|KVL]] | 基尔霍夫电压定律 | 回路中电压代数和为 0（能量守恒） |
| [[Superposition Theorem]] | 叠加原理 / 叠加定理 | 线性电路中响应 = 各独立源单独作用之和 |
| [[Thevenin's Theorem]] | 戴维南定理 / 戴维南等效 | 线性二端网络可等效为电压源串联电阻 |
| [[Norton's Theorem]] | 诺顿定理 / 诺顿等效 | 线性二端网络可等效为电流源并联电阻 |
| Linearity | 线性 | 系统满足齐次性与可加性的性质 |
| Homogeneity | 齐次性 | 输入放大 k 倍，输出也放大 k 倍 |
| Additivity | 可加性 | 多个输入之和的响应 = 各自响应之和 |
| Lenz's Law | 楞次定律 | 感应效应总是反抗引起它的磁通变化 |
| [[Basic Circuit Analysis Method|Node Analysis]] | 节点法 / 节点分析法 / Nodal Analysis | 以节点电压为主未知数、对非参考节点写 KCL 的系统分析法，是 KVL/KCL 法的特例 |
| Node Voltage | 节点电压 | 某节点相对参考节点（地）的电势，节点法的主未知数 |
| Reference Node | 参考节点 / 地 (Ground) | 电压测量的基准点，电势定义为 0 |
| Conductance | 电导 (G) | 电阻的倒数 $G=1/R$，单位西门子 (S)，节点法中的核心变量 |
| Associated Variables Discipline | 关联变量约定 (AVD) | 电流定义为从元件正电压端流入；此时 $p=vi$ 为吸收功率 |
| Element Combination Rules | 元件组合规则 | 串并联等效化简（串联 $R$ 相加、并联 $G$ 相加、源串并联），配合叠加可解复杂电路 |
| Basic KVL/KCL Method | 基本 KVL/KCL 方法 / 暴力法 | 写全部元件关系 + 全部 KCL + 全部 KVL 后求解，通用但方程数爆炸 |
| [[Circuit Analysis Methods in Practice\|Mesh Current Method]] | 网孔电流法 | 对每个网孔设假想回路电流、只写 KVL 的分析法，自动满足 KCL |
| [[Circuit Analysis Methods in Practice\|Branch Current Method]] | 支路电流法 | 每条支路设一个电流、KCL + KVL 联立求解的原始方法 |
| [[Circuit Analysis Methods in Practice\|Supernode]] | 超节点 | 跨在 floating voltage source 两端的两个节点视为一个整体写 KCL |
| Self-Resistance | 自阻 $R_{kk}$ | 网孔法电阻矩阵对角元素 = 网孔 $k$ 内所有电阻之和（恒正） |
| Mutual Resistance | 互阻 $R_{kj}$ | 网孔法电阻矩阵非对角元素 = 网孔 $k$ 与 $j$ 共享电阻之和的负值 |

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
| [[Lumped Matter Discipline|Lumped Matter Discipline (LMD)]] | 集总事物理论 | 使电路可用代数方程描述的约束假设 |
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
| [[First-Order Transients|Transient Response]] | 瞬态响应 | 电路从初始状态过渡到稳态期间的响应 |
| [[First-Order Transients|Time Constant]] | 时间常数 | 一阶电路响应变化的特征时间 $\tau = RC$ 或 $\tau = L/R$ |
| Impedance | 阻抗 | 交流下的广义电阻 $Z = R + jX$ |
| Filter | 滤波器 | 按频率选择性通过/衰减信号的电路 |

## 9. Mathematical Tools（数学工具）

| English                | 中文    | 解释                                       |
| :--------------------- | :---- | :--------------------------------------- |
| [[Complex Numbers and Euler's Formula|Euler's Formula]] | 欧拉公式  | $e^{j\theta} = \cos\theta + j\sin\theta$ |
| [[Complex Numbers and Euler's Formula|Euler's Identity]] | 欧拉恒等式 | $e^{j\pi} + 1 = 0$                       |
| [[Complex Numbers and Euler's Formula|Inverse Euler Formula]] | 反欧拉公式 | 用复指数表示三角函数 |
| [[Complex Numbers and Euler's Formula|Complex Number]] | 复数    | $z = x + jy$，含实部与虚部 |
| [[Complex Numbers and Euler's Formula|Complex Representation]] | 复数表示  | 代数/三角/极坐标三种等价形式 |
| [[Complex Numbers and Euler's Formula|Magnitude]] | 模     | 复数的长度 $r = \|z\|$ |
| [[Complex Numbers and Euler's Formula|Phase]] | 相角    | 复数的辐角 $\theta = \arg z$ |

## 10. Digital Abstraction（数字抽象）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[The Digital Abstraction|Digital Abstraction]] | 数字抽象 | 把连续取值离散为 0/1 的抽象层，建立在集总电路抽象之上 |
| Value Discretization | 取值离散化 | 仅允许信号取两种值（HIGH/LOW ↔ 1/0 ↔ TRUE/FALSE） |
| [[The Digital Abstraction|Digital System]] | 数字系统 | 发送端→带噪声导线→接收端，靠阈值判读还原 0/1 |
| Noise | 噪声 | 叠加在信号上的不期望电压波动，模拟系统的精度杀手 |
| [[Static Discipline|Static Discipline]] | 静态纪律 | 输入合法 ⇒ 输出合法；用四阈值量化噪声容限 |
| [[Static Discipline|Noise Margin]] | 噪声容限 | 信号变非法前能容忍的最大噪声：$NM_H=V_{OH}-V_{IH},\ NM_L=V_{IL}-V_{OL}$ |
| Voltage Threshold | 电压阈值 | 判读逻辑值的门槛电压 |
| [[Static Discipline|Voltage Transfer Characteristic (VTC)]] | 电压传输特性 | $V_{out}$ 对 $V_{in}$ 的曲线，过渡区高增益实现信号再生 |
| Forbidden Region | 禁区 / 无主之地 | 发送/接收都不使用的电压间隙，即噪声容限的物理载体 |
| [[Combinational Logic|Combinational Logic]] | 组合逻辑 | 输出仅为当前输入函数的数字逻辑（无记忆） |
| [[Sequential Logic]] ✅                   | 时序逻辑 / 存储器   | Ch.5：双稳态、SR 锁存器、D 触发器、时钟同步、存储层次 |
| Boolean Algebra | 布尔代数 | 以 0/1 为变量的代数体系，逻辑门的理论基础 |
| Truth Table | 真值表 | 枚举全部 $2^n$ 输入组合以定义组合函数 |
| Combinational Gate Abstraction | 组合门抽象 | 门作为黑箱：遵守静态纪律、输出仅依赖输入 |

## 12. Sinusoidal Steady State（正弦稳态）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[Sinusoidal Steady State]] ✅             | 正弦稳态       | 线性电路在正弦激励下的稳态响应，同频率正弦波 |
| [[Impedance]] ✅                           | 阻抗          | $Z=\tilde{V}/\tilde{I}$，$Z_R=R,\ Z_C=1/j\omega C,\ Z_L=j\omega L$ |
| Impedance (Complex) | 复阻抗        | $Z=R+jX$，实部电阻、虚部电抗 |
| Admittance | 导纳          | $Y=1/Z=G+jB$，单位西门子 (S) |
| [[Frequency Response]] ✅                 | 频率响应        | Ch.13：传递函数 $H(j\omega)$、Bode 图、极点/零点、$-3$ dB、带宽 |
| Transfer Function | 传递函数       | $H(j\omega)=\tilde{V}_{out}/\tilde{V}_{in}$ |
| Bode Plot | Bode 图       | 对数坐标下的幅频/相频图，斜率 $\pm 20/\pm 40$ dB/dec |
| Pole | 极点          | $H(s)$ 分母为零的点，稳定系统极点在左半平面 (LHP) |
| Zero | 零点          | $H(s)$ 分子为零的点 |
| Cutoff Frequency | 截止频率       | $|H|=1/\sqrt{2}$（$-3$ dB）处的频率 |
| Bandwidth (BW) | 带宽          | $|H|$ 下降至 $-3$ dB 的频率范围 |
| Quality Factor | 品质因数 $Q$   | $Q=\omega_0/BW$，谐振回路频率选择性的量度 |
| [[Filters]] ✅                             | 滤波器         | LP / HP / BP / Notch 四种频率选择网络 |
| [[Resonance]] ✅                          | 谐振          | Ch.14：串联 $Z_{\min}=R$、并联 $Z_{\max}=R$、$\omega_0=1/\sqrt{LC}$、$Q=\omega_0L/R$、$BW$ |
| Low-Pass Filter | 低通滤波器      | 通过 $\omega<\omega_c$，衰减 $\omega>\omega_c$ |
| High-Pass Filter | 高通滤波器      | 通过 $\omega>\omega_c$，衰减 $\omega<\omega_c$ |
| Band-Pass Filter | 带通滤波器      | 通过 $\omega_0\pm BW/2$，阻断其他频率 |
| Notch Filter | 陷波滤波器      | 阻断 $\omega\approx\omega_0$，通过其他频率 |
| [[Resonance]] ✅                          | 谐振          | $\omega=\omega_0=1/\sqrt{LC}$ 时阻抗极值、电流/电压极大 |
| Series Resonance | 串联谐振       | $\omega_0$ 处 $Z_{\min}=R$，电流最大 |
| Parallel Resonance | 并联谐振       | $\omega_0$ 处 $Z_{\max}=R$，电压最大 |
| Resonant Frequency | 谐振频率       | $\omega_0=1/\sqrt{LC}$，电感与电容能量交换的固有频率 |
| Phasor | 相量          | $\tilde{V}=V_m\angle\phi$，旋转矢量（长度=幅值，角度=相位）|
| Phasor Method | 相量法         | 用相量把微分方程变为复数代数方程的分析方法 |
| Complex Exponential | 复指数         | $e^{j\omega t}=\cos\omega t+j\sin\omega t$ |
| Euler's Formula | 欧拉公式        | $e^{j\theta}=\cos\theta+j\sin\theta$，相量法的数学基础 |
| Decibel (dB) | 分贝          | $20\log_{10}|H|$，对数幅度单位 |
| $-3$ dB Point | $-3$ dB 点     | 半功率点 $|H|=1/\sqrt{2}$，截止频率定义 |
| Decoupling Capacitor | 去耦电容       | 高频旁路电容，为交流提供低阻抗通路（见 [[Filters]]）|

## 13. Operational Amplifiers（运算放大器）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[Operational Amplifier]] ✅                 | 运算放大器       | 差分输入、单端输出、高增益有源器件，线性反馈核心 |
| Virtual Short | 虚短           | 负反馈运放：$v_+\approx v_-$（两输入端电压相等）|
| Virtual Open | 虚断           | 运放输入端不汲取电流：$i_+=i_-\approx 0$ |
| Non-Inverting Amplifier | 同相放大器     | $A_v=1+R_f/R_1$，$R_{\text{in}}\approx\infty$ |
| Inverting Amplifier | 反相放大器       | $A_v=-R_f/R_1$，$R_{\text{in}}=R_1$，虚地 $v_-\approx 0$ |
| Voltage Follower | 电压跟随器        | $A_v=1$，单位增益缓冲，$R_{\text{in}}=\infty,\ R_{\text{out}}\approx 0$ |
| Summing Amplifier | 加法器           | $v_{\text{out}}=-\sum R_f/R_n\cdot v_n$，虚地原理 |
| Differential Amplifier | 差分放大器       | $v_{\text{out}}=R_f/R_1(v_2-v_1)$（$R_1=R_2,\ R_f=R_g$）|
| Op-Amp Integrator | 积分器           | $H(s)=-1/(sRC)$，低通特性（见 [[Filters]]）|
| Op-Amp Differentiator | 微分器           | $H(s)=-sRC$，高通特性（高频噪声敏感）|
| Sallen-Key Filter | Sallen-Key 有源滤波 | 二阶有源滤波，$H_{\text{LP}}=\omega_0^2/(s^2+s\omega_0/Q+\omega_0^2)$ |
| Saturation | 饱和            | 输出被电源轨夹断，$|v_{\text{out}}|\ge V_{\text{SAT}}$，失真 |
| Positive Feedback | 正反馈           | $v_+=\beta v_{\text{out}}$，导致振荡或迟滞比较器 |
| Barkhausen Condition | 巴克豪森振荡条件   | $|A\beta|=1,\ \angle A+\beta=0^\circ$ |
| Slew Rate | 转换速率          | $SR=\max |dv_{\text{out}}/dt|$，大信号响应限制 |
| GBW (Gain-Bandwidth Product) | 增益带宽积   | $A\cdot f_{-3\text{dB}}=\text{GBW}$（常数），增益越高带宽越窄 |
| Input Offset Voltage | 输入失调电压      | $V_{OS}$，零输入时的输出直流偏移 |
| Common-Mode Rejection Ratio | 共模抑制比  | $CMRR=20\log_{10}|A_d/A_cm|$（dB），差分放大器质量指标 |
| Two-Port Model | 二端口模型        | $R_{\text{in,cl}}, R_{\text{out,cl}}, A_v$ 闭环参数 |
| [[Diode]] ✅                              | 二极管          | 单向导电的半导体 PN 结器件 |
| PN Junction | PN 结            | P 型与 N 型半导体接触面，形成耗尽层 |
| Forward Bias | 正向偏置          | $V_D>0.6$–$0.7$ V 时导通，电流指数增长 |
| Reverse Bias | 反向偏置          | $V_D<0$ 时截止，漏电流 $I\approx I_S$ |
| Shockley Diode Equation | 肖克利二极管方程 | $i_D=I_S(e^{v_D/nV_T}-1)$，$V_T=kT/q\approx 26$ mV |
| Assumed-State Method | 状态假设法        | 先假设导通/截止，验证自洽，逐步求解二极管电路 |
| Knee Voltage | 导通阈值          | $V_{\text{knee}}\approx 0.6$–$0.7$ V（Si）|
| Reverse Recovery Time | 反向恢复时间      | 二极管从导通切换到截止所需时间（Schottky 更快）|
| Half-Wave Rectifier | 半波整流         | 只通过正半周期，纹波频率 $=f_{\text{in}}$ |
| Full-Wave Rectifier | 全波整流         | 通过正负半周期，纹波频率 $=2f_{\text{in}}$ |
| Bridge Rectifier | 桥式整流         | 4 只二极管，无需中心抽头，$v_{\text{out}}=|v_{\text{in}}|-2V_D$ |
| Smoothing Capacitor | 滤波电容         | 整流后并联电容，$\Delta v\approx I_{\text{load}}/(f\cdot C)$ |
| Ripple Voltage | 纹波电压          | 电容放电造成的输出电压波动（见 [[Capacitor]]）|
| Clipper / Limiter | 削波/限幅器       | 截断波形顶部或底部，保护电路 |
| Clamper | 钳位器            | 整体上移/下移波形直流电平，不改变波形形状 |
| Zener Diode | 齐纳二极管         | 反向击穿区 $V_Z$ 恒定，用于稳压 |
| Zener Regulator | 齐纳稳压器        | $V_{\text{out}}\approx V_Z$，$R_s=(V_{\text{in}}-V_Z)/(I_{\text{load}}+I_Z)$ |
| LED (Light-Emitting Diode) | 发光二极管   | $V_F\approx 1.8$–$3.5$ V（波长决定），光功率 $\propto I_F$ |
| Schottky Diode | 肖特基二极管        | 金属-半导体结，$V_F\approx 0.2$–$0.4$ V，高速 |
| Varactor (Varicap) | 变容二极管        | 反向偏置时电容 $\propto 1/V_R$，调谐电路 |
| TVS Diode | 瞬态电压抑制二极管    | 瞬态过压钳位（防雷、ESD）|

| [[Amplifiers and Feedback]] ✅              | 放大器与反馈       | 反馈方程 $A/(1+A\beta)$、负反馈四大好处、Barkhausen 振荡条件、四拓扑 |
| [[Current Sources and Mirrors]] ✅          | 电流源与电流镜     | 偏置/有源负载、基本镜/Wilson/Cascode、$I_{\text{out}}=I_{\text{ref}}\cdot(W/L)_2/(W/L)_1$ |
| [[Power Supplies]] ✅                      | 电源            | 线性稳压/LDO、开关 Buck/Boost/Buck-Boost、基准电压源、效率 |
| [[DC-DC Converter]] ✅                     | DC-DC 变换器     | Buck $V_o=DV_i$、Boost $V_o=V_i/(1-D)$、PWM/PFM、纹波/效率 |

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
| [[MOSFET]] ✅                                 | MOSFET 场效应管 | Ch.6：结构 / 符号 / 截止-饱和-线性三区       |
| [[The MOSFET Switch]] ✅                      | MOSFET 开关   | Ch.6：SRC 模型、开关电阻、导通/截止          |
| [[The MOSFET Amplifier]] ✅             | MOSFET 放大器  | Ch.7：CS / CD / CG 三种组态、Q 点、增益、阻抗 |
| [[Large-Signal Model]] ✅                | 大信号模型       | Ch.7：Q 点 / 负载线 / 三区方程 / 沟道调制 / 偏置电路 |
| [[Small Signal Circuit Representation]] ✅ | 小信号电路表示    | Ch.8：$g_m$/$r_o$、CS 增益 $A_v=-g_mR_D$、密勒效应 |
| [[Capacitor]] ✅                         | 电容          | Ch.9：本构关系 $q=Cv$、$i=C\dv/dt$、串并联、储能 |
| [[Inductor]] ✅                           | 电感          | Ch.9：本构关系 $\phi=Li$、$v=L\di/dt$、串并联、耦合电感 |
| [[Capacitive and Magnetic Devices]] ✅    | 电容与磁器件     | Ch.9：MOS 栅电容 $C_{ox}=\varepsilon/t_{ox}$、绕组电感 $L=N^2\mu A/\ell$、互感 $M=k\sqrt{L_1L_2}$、变压器 |
| [[Energy and Charge Conservation]] ✅     | 能量 / 电荷 / 磁通守恒 | Ch.9：KCL ← 电荷守恒、KVL ← 能量守恒、LC 振荡 |
| [[First-Order Transients]] ✅               | 一阶暂态电路      | Ch.10：RC/RL 阶跃、放电、方波、直觉分析、状态变量、传播延迟 $t_{pd}\sim R_{ON}C_L$ |
| State Variables ✅                          | 状态变量        | Ch.10：$v_C$ / $i_L$，编码储能元件的全部历史（归入 [[First-Order Transients]] §二） |
| Propagation Delay ✅                        | 传播延迟        | Ch.10：$t_{pd}\approx 0.69\,R_{ON}C_L$，数字门翻转延迟（归入 [[First-Order Transients]] §七） |
| [[Energy and Power in Digital Circuits]] ✅  | 数字电路的能量与功率  | Ch.11：RC 充电 50% 损耗、$P_{dyn}=\alpha CV^2f$、NMOS 静态功耗、CMOS 零静态、DVFS |
| [[Second-Order Transients]] ✅               | 二阶暂态电路      | Ch.12：LC 无阻尼振荡、串联/并联 RLC 欠/过/临界阻尼、$\zeta$/$\omega_0$、状态变量法 |
| [[Sinusoidal Steady State]] ✅                | 正弦稳态        | Ch.13：复指数激励、齐次/特解、完整解           |
| [[Impedance]] ✅                              | 阻抗          | Ch.13：$Z_R=R,\ Z_C=1/j\omega C,\ Z_L=j\omega L$、分压/分流、功率因数 |
| [[Frequency Response]] ✅                    | 频率响应        | Ch.13：传递函数 $H(j\omega)$、Bode 图、$-3$ dB、极点/零点、带宽 $BW$ |
| [[Filters]] ✅                               | 滤波器         | Ch.13–14：LP/HP/BP/Notch 传递函数、一阶 $-20$ dB/dec、二阶 $-40$ dB/dec |
| [[Operational Amplifier]] ✅                  | 运算放大器       | Ch.15：理想模型、虚短虚断、七种基本电路、积分器/微分器/Sallen-Key、饱和、正反馈、振荡器         |
| [[Diode]] ✅                                  | 二极管         | Ch.16：I-V 特性、状态假设法、整流、削波钳位、Zener 稳压、LED/Schottky/Varactor  |


---

## 12. Dynamic Circuits（动态电路与暂态分析）

| English | 中文 | 解释 |
| :--- | :--- | :--- |
| [[First-Order Transients|Transient Response]] | 暂态响应 | 电路从初始状态过渡到稳态期间的响应，由储能元件的"记忆"引起 |
| [[First-Order Transients|Steady State]] | 稳态 | $t\to\infty$ 后电路达到的稳定状态（直流稳态下电容开路、电感短路） |
| [[First-Order Transients|Switching Theorem]] | 换路定则 | 换路瞬间状态变量不变：$v_C(0^+)=v_C(0^-)$、$i_L(0^+)=i_L(0^-)$ |
| [[First-Order Transients|Time Constant]] | 时间常数 $\tau$ | 一阶电路响应的特征时间：$\tau=RC$（RC）或 $\tau=L/R$（RL）；$t=\tau$ 时到达终值 63.2% |
| [[First-Order Transients|Zero-Input Response]] | 零输入响应 | 无外加激励、仅由初始储能引起的响应（自然衰减） |
| [[First-Order Transients|Zero-State Response]] | 零状态响应 | 初始储能为零、仅由外加激励引起的响应 |
| [[First-Order Transients|Step Response]] | 阶跃响应 | 电路对单位阶跃输入的响应 |
| [[First-Order Transients|Intuitive Analysis]] | 直觉分析 | 三步法求一阶全响应：$x(t)=x(\infty)+[x(0)-x(\infty)]e^{-t/\tau}$ |
| [[First-Order Transients|Propagation Delay]] | 传播延迟 $t_{pd}$ | 数字门输出越过判定阈值的时间，$\sim 0.69\,R_{ON}C_L$ |
| [[Energy and Power in Digital Circuits|Dynamic Power]] | 动态功耗 $P_{dyn}$ | 充放电负载电容引起的功耗：$P_{dyn}=\alpha C V_{DD}^2 f$ |
| [[Energy and Power in Digital Circuits|Static Power]] | 静态功耗 $P_{static}$ | 不翻转时的功耗：NMOS 为 $V^2/(R_L+R_{ON})$，CMOS 为泄漏电流 $V_{DD}I_{leak}$ |
| [[Energy and Power in Digital Circuits|Activity Factor]] | 活动因子 $\alpha$ | 每时钟周期内实际发生翻转的节点比例（典型 0.1–0.5） |
| [[Energy and Power in Digital Circuits|Power-Delay Product]] | 功耗延迟积 PDP | $P\times t_{pd}$，衡量开关一次的能效 |
| [[Energy and Power in Digital Circuits|DVFS]] | 动态电压频率调节 | 降低 $V_{DD}$ 和 $f$ 以减少功耗（$P\propto V^2$） |
| [[Second-Order Transients|Natural Frequency]] | 自然频率 $\omega_0$ | 二阶电路的固有振荡频率：$\omega_0=1/\sqrt{LC}$ |
| [[Second-Order Transients|Damping Ratio]] | 阻尼比 $\zeta$ | 表征阻尼强弱的无量纲量：$\zeta>1$ 过阻尼、$=1$ 临界、$<1$ 欠阻尼 |
| [[Second-Order Transients|Damped Natural Frequency]] | 阻尼自然频率 $\omega_d$ | 欠阻尼下的实际振荡频率：$\omega_d=\omega_0\sqrt{1-\zeta^2}$ |
| [[Second-Order Transients|Overdamped]] | 过阻尼 | $\zeta>1$，两个负实根，单调衰减无振荡 |
| [[Second-Order Transients|Critically Damped]] | 临界阻尼 | $\zeta=1$，重根，最快无振荡衰减 |
| [[Second-Order Transients|Underdamped]] | 欠阻尼 | $\zeta<1$，共轭复根，衰减振荡 |
| [[Second-Order Transients|Characteristic Impedance]] | 特征阻抗 $Z_0$ | LC 回路的阻抗参数：$Z_0=\sqrt{L/C}$，决定振荡电流幅度 |
| [[Second-Order Transients|State Variable Method]] | 状态变量法 | 用 $n$ 个状态变量的一阶 ODE 组替代 $n$ 阶 ODE 的系统化方法 |
| [[Second-Order Transients|Envelope]] | 包络线 | 衰减振荡的幅值上界 $e^{-\zeta\omega_0 t}$ |

---

## 相关笔记

- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
- [[Maxwell's Equations]] / [[Lumped Matter Discipline]] / [[Superposition Theorem]] —— 已建专题笔记
