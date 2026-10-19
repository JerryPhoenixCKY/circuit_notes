---
tags:
  - 电路学
  - 动态电路
  - 暂态分析
  - 课程笔记
date: 2026-09-08
updated: 2026-10-19
aliases:
  - 二阶暂态
  - 二阶暂态电路
  - Second-Order Transients
  - Second-Order Circuit
  - Second-Order Circuits
  - RLC Circuit
  - LC Oscillation
  - Damping Ratio
  - 阻尼比
  - Damping Factor
  - 衰减系数
  - Overdamped
  - 过阻尼
  - Underdamped
  - 欠阻尼
  - Critically Damped
  - 临界阻尼
  - Natural Frequency
  - 自然频率
  - 状态变量法
  - State Variable Method
---

# Second-Order Transients（二阶暂态电路）

> [!NOTE] 本笔记定位
> 对应教材 Ch.12 *Second-Order Circuits*，并结合 ECE 2001 [[ECE2001/L6 Second-order Circuits 20261018.pdf|Lecture 6]]。二阶电路 (second-order circuit) 有两个独立储能状态，其动态可由二阶常微分方程 (ordinary differential equation, ODE) 描述。核心步骤：**求初值与初始导数 → 判断特征根 → 写暂态与特解 → 用两个初始条件求系数**。
> 前置：[[Capacitor]]、[[Inductor]]、[[Kirchhoff's Laws]]、[[First-Order Transients]]；后续：[[Resonance]]、[[Frequency Response]]、[[Filters]]。
> 讲义 Example 1–7、运放例子及勘误见 [[Second-Order Circuit Worked Examples|二阶电路例题]]。页码均指 PDF 实际页码，与幻灯片页脚编号不同。

## 一、从一阶到二阶：两个状态变量

**状态变量 (state variables)** 是电容电压与电感电流。阶数取决于独立状态数，不能只数储能元件：两个并联电容可合并，只有一个独立电压；无法合并的两个 C 或两个 L 也可以形成二阶电路。

| 维度 | 一阶 (First-Order) | 二阶 (Second-Order) |
| :--- | :--- | :--- |
| 独立状态 | 1 个 | 2 个 |
| 恒定激励下的稳定暂态 | 单个衰减指数 | 两个实指数、重根形式或衰减振荡 |
| 需要的初始条件 | $x(0^+)$ | $x(0^+)$ 与 $\dot x(0^+)$，或两个独立状态 |
| 特征参数 | 时间常数 $\tau$ | 无阻尼自然角频率 $\omega_0$、衰减系数 $\alpha$、阻尼比 $\zeta$ |

以下假设元件理想、参数恒定，$L,C>0$，无源电阻为正；时间 $t$ 以 s 计，电压以 V、电流以 A 计。使用[[Two-Terminal Element Laws|关联参考方向 (passive sign convention)]]：电流流入元件电压的正端。标准 RLC 的 $\omega_0=1/\sqrt{LC}$；一般二阶电路须从 ODE 识别参数。

### 1.1 初值、初始导数与终值 (Initial and Final Conditions)

讲义依据：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=4|PDF pp.4–12]]。

1. **$t=0^-$**：若换路前已达直流稳态，用电容开路、电感短路求 $V_0=v_C(0^-)$、$I_0=i_L(0^-)$。
2. **$t=0^+$**：保留换路后的拓扑与电源。若电容电流无冲激、电感电压无冲激，则 $v_C(0^+)=V_0$、$i_L(0^+)=I_0$。瞬时计算时，可将电容表示为指定电压 $V_0$ 的电压源，将电感表示为指定电流 $I_0$ 的电流源。
3. **初始斜率 (initial slope)**：在 $0^+$ 电路上，用 KCL/KVL 求 $i_C(0^+)$、$v_L(0^+)$，再用
   $$\boxed{\dot v_C(0^+)=\frac{i_C(0^+)}C,\qquad \dot i_L(0^+)=\frac{v_L(0^+)}L.}$$
4. **$t\to\infty$**：仅在换路后存在可达的稳定直流终态时，用电容开路、电感短路求终值。理想无阻尼 LC 一般不收敛，不能强行指定终值。

> [!WARNING] 连续的是状态，导数通常不连续
> 电容电流、电感电压、电阻电压/电流均可能跳变；不能沿用 $0^-$ 的导数。也不能在 $0^+$ 一律把电容开路、电感短路。
> 理想冲激、强制不相容初态的理想开关连接，需另行分析，不属于普通连续换路公式的适用条件。

给定 $V_0,I_0$ 后，导数由电路方程决定，不能再独立指定第三个任意初值。若输出是电阻电压等非状态量，先将它写成状态量的组合，再求初值与导数，见例题 2。

## 二、LC 无阻尼振荡 (Undamped Oscillation)

### 2.1 电路与方程

在串联回路中取 $i_L$ 流入电容正端；理想 $R=0$，$v_C(0)=V_0$、$i_L(0)=0$。由 KVL 与元件定律：

$$L\frac{di_L}{dt}+v_C=0,\qquad i_L=C\frac{dv_C}{dt}
\quad\Longrightarrow\quad
\boxed{\ddot v_C+\omega_0^2v_C=0,\quad\omega_0=\frac1{\sqrt{LC}}.}$$

### 2.2 解与能量交换

$$v_C(t)=V_0\cos\omega_0t,\qquad
 i_L(t)=-\frac{V_0}{Z_0}\sin\omega_0t,\qquad Z_0=\sqrt{\frac LC}.$$

$Z_0$ 是 LC **特征阻抗 (characteristic impedance)**，单位 $\Omega$。负电流表示实际放电方向与所选参考方向相反。$\omega_0$ 单位为 rad/s，$f_0=\omega_0/(2\pi)$ 单位为 Hz，周期 $T_0=2\pi/\omega_0$。

![[lc_undamped.svg|500]]

*理想模型计算图。横轴为归一化时间 $\omega_0t$；状态分别归一化为 $v_C/V_0$、$i_LZ_0/V_0$，能量归一化为 $E/E_0$，其中 $E_0=CV_0^2/2$。*

总储能为

$$E=\frac12Cv_C^2+\frac12Li_L^2=\frac12CV_0^2.$$

$t=0$ 时全在电场；$t=T_0/4$ 时全在磁场。$L$ 或 $C$ 越大，能量交换越慢。详见 [[Energy and Charge Conservation]]。

## 三、串联 RLC 暂态 (Series RLC)

### 3.1 方程、参考方向与初始条件

![[l6-series-rlc.png|400]]

*无源串联拓扑，摘自 [[ECE2001/L6 Second-order Circuits 20261018.pdf#page=14|L6，PDF p.14]]。加电压源时，取其沿回路提供电压升 $V_S$；回路电流 $i$ 流入电容电压 $v_C$ 的正端。*

对于 $t>0$ 的恒定电压源 $V_S$：

$$L\dot i+Ri+v_C=V_S,\qquad i=C\dot v_C,$$

$$\boxed{\ddot v_C+\frac RL\dot v_C+\frac1{LC}v_C=\frac{V_S}{LC}.}$$

对原 KVL 求导，在 $t>0$ 且 $V_S$ 恒定的区间内，还得到

$$\ddot i+\frac RL\dot i+\frac1{LC}i=0.$$

**电流方程齐次不表示没有电源**：恒定电压求导后消失，其作用保留在初始斜率与电容终值中。阶跃时刻不能忽略输入的冲激导数；实际求解直接使用 $0^+$ 的原始 KVL：

$$\boxed{\dot v_C(0^+)=\frac{I_0}C,\qquad
\dot i(0^+)=\frac{V_S-RI_0-V_0}L.}$$

若响应稳定收敛，则 $v_C(\infty)=V_S$、$i(\infty)=0$。无源时令 $V_S=0$。依据：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=15|PDF pp.15–18、36–38]]。

### 3.2 衰减系数、自然频率与阻尼比

讲义使用**衰减系数 (damping factor)** $\alpha$，也称奈培频率 (neper frequency)，单位 $\mathrm{s}^{-1}$。**无阻尼自然角频率 (undamped natural frequency)** $\omega_0$ 的单位为 rad/s；**阻尼比 (damping ratio)** $\zeta$ 无量纲：

$$\boxed{\alpha=\frac{R}{2L},\qquad \omega_0=\frac1{\sqrt{LC}},\qquad
\zeta=\frac{\alpha}{\omega_0}=\frac R2\sqrt{\frac CL}.}$$

**特征方程 (characteristic equation)** 及其根为

$$s^2+2\alpha s+\omega_0^2=0,\qquad
s_{1,2}=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}.$$

特征根 $s$ 的单位为 $\mathrm{s}^{-1}$；其虚部表示振荡角频率，实部表示衰减率，不能把实部当作 Hz。

### 3.3 阻尼分类 (Damping Regimes)

| 分类 | 条件（正阻尼） | 特征根 | 自然响应 |
| :--- | :--- | :--- | :--- |
| 过阻尼 (Overdamped) | $\alpha>\omega_0$，$\zeta>1$ | 两个不同负实根 | $A_1e^{s_1t}+A_2e^{s_2t}$ |
| 临界阻尼 (Critically Damped) | $\alpha=\omega_0$，$\zeta=1$ | 重根 $s=-\alpha$ | $(A_1+A_2t)e^{-\alpha t}$ |
| 欠阻尼 (Underdamped) | $0<\alpha<\omega_0$，$0<\zeta<1$ | $-\alpha\pm j\omega_d$ | $e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$ |
| 无阻尼 (Undamped) | $\alpha=0$ | $\pm j\omega_0$ | $B_1\cos\omega_0t+B_2\sin\omega_0t$ |

$$\omega_d=\sqrt{\omega_0^2-\alpha^2}=\omega_0\sqrt{1-\zeta^2}$$

是**阻尼自然角频率 (damped natural frequency)**，$f_d=\omega_d/(2\pi)$。串联临界电阻为

$$\boxed{R_{\mathrm{crit,series}}=2\sqrt{L/C}.}$$

![[rlc_damping.svg|500]]

*理想模型计算图。固定相同的 $L,C$ 与初态 $v_C(0)=V_0$、$i_L(0)=0$，比较 $\zeta=2,1,0.3$；横轴为 $\omega_0t$，纵轴为 $v_C/V_0$。三条曲线的初始斜率均为零。*

> [!IMPORTANT] 不能用“是否单调”定义阻尼区
> 过阻尼没有正弦自然模态，但两个指数的系数组合可能产生转折或一次越过终值。临界阻尼也可能受非零初态影响而越过终值。“临界最快无过冲”应限定为相同 $\omega_0$、零初态、标准低通阶跃的单调趋近比较。
> 串联 $R$ 很大时，慢根 $s_{\rm slow}\approx-1/(RC)$；大电阻并不意味着所有暂态衰减得更快。

### 3.4 包络与测量 (Envelope and Measurement)

欠阻尼的 $x(t)-x_\infty$ 可写成 $A e^{-\alpha t}\cos(\omega_dt+\phi)$；$A$ 与 $\phi$ 由初态决定，$x_\infty$ 为稳定终值。幅度**包络 (envelope)** 为 $|A|e^{-\alpha t}$，包络时间常数为

$$\tau_{\mathrm{env}}=\frac1\alpha.$$

对同号的相邻峰值，先扣除终值，记 $a_n=|x(t_n)-x_\infty|$。**对数衰减率 (logarithmic decrement)** 为

$$\delta=\ln\frac{a_n}{a_{n+1}}=\frac{2\pi\alpha}{\omega_d}
=\frac{2\pi\zeta}{\sqrt{1-\zeta^2}},\qquad
\zeta=\frac{\delta}{\sqrt{4\pi^2+\delta^2}}.$$

测量振铃时可用同号峰间隔 $T_d$ 求 $\omega_d=2\pi/T_d$，用 $\alpha=\delta/T_d$ 求衰减率，再求 $\omega_0=\sqrt{\omega_d^2+\alpha^2}$。探头负载及电感/电容寄生损耗会改变实际阻尼，计算模型须包含这些影响。

### 3.5 为什么重根要乘 $t$？(Repeated Root)

重根时两个 $e^{-\alpha t}$ 线性相关，只能留下一个独立常数，无法满足一般的两个初始条件。令自然响应为 $y$，则

$$\left(\frac d{dt}+\alpha\right)^2y=0.$$

令 $z=\dot y+\alpha y$，先解 $\dot z+\alpha z=0$，再以积分因子 $e^{\alpha t}$ 解 $\dot y+\alpha y=K e^{-\alpha t}$，得到

$$\boxed{y=(A_1+A_2t)e^{-\alpha t}.}$$

因此 $A_1$ 与 $A_2$ 的单位不同：若 $y$ 为 V，$A_1$ 为 V、$A_2$ 为 V/s。推导对应 [[ECE2001/L6 Second-order Circuits 20261018.pdf#page=23|PDF pp.23–24]]。

## 四、并联 RLC 暂态 (Parallel RLC)

### 4.1 参考方向与初始条件

![[l6-parallel-rlc.png|450]]

*摘自 [[ECE2001/L6 Second-order Circuits 20261018.pdf#page=39|L6，PDF p.39]]。公共电压 $v$ 上正下负，R/L/C 支路电流向下。加电流源时，取 $I_S$ 从参考节点向上注入。*

KCL 与电感定律给出

$$\frac vR+C\dot v+i_L=I_S,\qquad v=L\dot i_L.$$

因此

$$\boxed{\dot v(0^+)=\frac{I_S-V_0/R-I_0}C,\qquad
\dot i_L(0^+)=\frac{V_0}L.}$$

无源响应令 $I_S=0$。对 $t>0$ 的恒定 $I_S$，电压满足

$$\boxed{\ddot v+\frac1{RC}\dot v+\frac1{LC}v=0,}$$

电感电流满足

$$\boxed{\ddot i_L+\frac1{RC}\dot i_L+\frac1{LC}i_L=\frac{I_S}{LC}.}$$

稳定直流终态为 $v(\infty)=0$、$i_L(\infty)=I_S$。因此**恒定电流激励的并联 RLC，电压暂态没有非零直流常数项，电感电流有**。依据：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=40|PDF pp.40–47]]。

### 4.2 串并联对照

| 参数 | 串联 RLC，电压源驱动 | 并联 RLC，电流源驱动 |
| :--- | :--- | :--- |
| $\omega_0$ | $1/\sqrt{LC}$ | $1/\sqrt{LC}$ |
| $\alpha$ | $R/(2L)$ | $1/(2RC)$ |
| $\zeta$ | $(R/2)\sqrt{C/L}$ | $(1/2R)\sqrt{L/C}$ |
| 临界电阻 | $2\sqrt{L/C}$ | $\tfrac12\sqrt{L/C}$ |
| 过阻尼条件 | $R>2\sqrt{L/C}$ | $R<\tfrac12\sqrt{L/C}$ |
| 增大 $R$ 的结果 | 阻尼增大 | 阻尼减小 |
| 直流终值 | $v_C=V_S,\ i=0$ | $v=0,\ i_L=I_S$ |

无源时，串联总储能满足 $\dot E=-Ri^2$；并联满足 $\dot E=-v^2/R$。这解释了电阻对阻尼的相反作用；不能据此假设不同 $R$ 的实际轨迹具有相同电流或电压。

## 五、全响应与系数速算 (Complete Response)

### 5.1 两种分解不能混淆

对线性常系数电路：**全响应 (complete response)** = **齐次/自然响应 (homogeneous/natural response)** + **特解 (particular solution)**。恒定激励且系统渐近稳定时，常数特解等于稳定终值 $x_\infty$，所以

$$x(t)=x_\infty+x_t(t).$$

**零输入响应 (zero-input response)** + **零状态响应 (zero-state response)** 是另一种分解：前者只保留初始储能，后者只保留外部激励并置初态为零。零状态响应本身也通常含暂态，不能等同于稳态项。

### 5.2 通用系数表

令 $X_0=x(0^+)$、$D_0=\dot x(0^+)$、$\Delta=X_0-x_\infty$。以下要求激励在所求区间恒定，并且 $x_\infty$ 是该电路的常数特解：

| 根的类型 | 全响应 | 系数 |
| :--- | :--- | :--- |
| 不同实根 | $x_\infty+A_1e^{s_1t}+A_2e^{s_2t}$ | $A_1=(D_0-s_2\Delta)/(s_1-s_2)$；$A_2=(s_1\Delta-D_0)/(s_1-s_2)$ |
| 重根 $-\alpha$ | $x_\infty+(A_1+A_2t)e^{-\alpha t}$ | $A_1=\Delta$；$A_2=D_0+\alpha\Delta$ |
| 复根 $-\alpha\pm j\omega_d$ | $x_\infty+e^{-\alpha t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$ | $B_1=\Delta$；$B_2=(D_0+\alpha\Delta)/\omega_d$ |

单位检查：$A_1,A_2$（不同实根）及 $B_1,B_2$ 与 $x$ 同单位；重根行的 $A_2$ 与 $x$/s 同单位。表中系数由 $x(0^+),\dot x(0^+)$ 直接联立推导。

### 5.3 零初态串联电容阶跃响应

取 $V_0=I_0=0$、$V_S$ 为恒定阶跃幅值。欠阻尼时：

$$\boxed{v_C(t)=V_S\left[1-e^{-\alpha t}\left(\cos\omega_dt+
\frac\alpha{\omega_d}\sin\omega_dt\right)\right],\quad t\ge0.}$$

临界阻尼时：

$$v_C(t)=V_S\left[1-(1+\omega_0t)e^{-\omega_0t}\right].$$

验证：初值为零、初始斜率为零、稳定终值为 $V_S$。非零初态不能直接套这两条零状态公式，应使用系数表。

### 5.4 一般二阶电路的解题流程

从 KCL/KVL 消元得到

$$a_2\ddot x+a_1\dot x+a_0x=b,\qquad a_2\ne0.$$

当 $a_0\ne0$ 时，常数特解为 $b/a_0$。归一化后识别 $2\alpha=a_1/a_2$、$\omega_0^2=a_0/a_2$；只有这些比值满足相应正值条件时，才能沿用上述稳定阻尼分类。

1. 按 §1.1 求 $X_0,D_0$ 和可达的稳定终值。
2. 求自然模态时关闭**独立源**：理想电压源短路、理想电流源开路；受控源与运放关系保留。也可直接从完整 ODE 取齐次部分。
3. 列 KCL/KVL 并消元，求特征方程与暂态形式。
4. 加上特解，用系数表求常数。
5. 检查 $0^+$ 的值与斜率、终值、原始 KCL/KVL 和单位。只检查两个初值不足以发现错误频率。

对于非恒定输入，特解通常不是常数；有零根、无阻尼或不稳定模态时，也不能无条件写成“终值 + 衰减项”。讲义通用方法见 [[ECE2001/L6 Second-order Circuits 20261018.pdf#page=57|PDF p.57、pp.64–65]]。

## 六、状态变量法 (State Variable Method)

选状态向量 $\mathbf x=[v_C,i_L]^{\mathsf T}$，串联 RLC 可写为

$$\begin{bmatrix}\dot v_C\\\dot i_L\end{bmatrix}
=\begin{bmatrix}0&1/C\\-1/L&-R/L\end{bmatrix}
\begin{bmatrix}v_C\\i_L\end{bmatrix}
+\begin{bmatrix}0\\V_S/L\end{bmatrix}.$$

这是**状态空间 (state space)** 表示。状态矩阵的特征值就是 $s_{1,2}$。状态法保留物理方向与两个独立初态，可直接用于数值积分；非线性、时变系统也可以写状态方程，但不一定仍有上述常系数指数通解。

## 七、双电容/双电感电路与机械类比

### 7.1 不止 L+C

通过无源正电阻网络连接的两个独立电容，可形成二阶 RC 电路；两个独立电感也可形成二阶 RL 电路。在这里的理想无源模型下，它们的自然模态不呈正弦振荡。L 与 C 的两种储能交换可产生振荡；加入有源器件或受控源后，纯 RC 网络也可能振荡，不能把无源结论推广过去。

讲义双电感例子通过消元得到 $\ddot i_1+13\dot i_1+30i_1=70$，自然根为 $-3,-10\ \mathrm{s}^{-1}$。完整推导见 [[Second-Order Circuit Worked Examples#例 7：双电感一般二阶电路 (Two-Inductor Circuit)|例 7]]。

运放加两个独立电容也可构成二阶有源滤波电路。讲义运放电路的标号与现有 Sallen-Key 图中的电容标号互换，推导见 [[Operational Amplifier#4.4 二阶运放电路的时域方程 (Second-Order Op-Amp Dynamics)|运放笔记 §4.4]]，不能跨图直接套标号。

### 7.2 电-力类比 (Mechanical Analogy)

令电荷 $q=Cv_C$，则串联 KVL 为 $L\ddot q+R\dot q+q/C=V_S$，对应机械模型 $m\ddot x+b\dot x+kx=F$：

| 电路量 | 机械量 |
| :--- | :--- |
| $L$ | 质量 $m$ |
| $R$ | 阻尼系数 $b$ |
| $1/C$ | 弹簧常数 $k$ |
| 电荷 $q$ | 位移 $x$ |
| 电流 $i=\dot q$ | 速度 $\dot x$ |
| 电容电压 $v_C=q/C$ | 弹簧力 $kx$ |
| 电源电压 $V_S$ | 外力 $F$ |

这是力-电压类比，避免直接把 $v_C$ 与位移对应却又沿用 $L\leftrightarrow m$ 的不一致。

## 八、典型例题

### 8.1 串联 RLC 零输入：过阻尼

$R=20\,\Omega$、$L=5\,\mathrm{mH}$、$C=80\,\mu\mathrm F$、$V_0=10\,\mathrm V$、$I_0=0$，按 §3 参考方向：

$$\omega_0=1581.14\ \mathrm{rad/s},\quad\alpha=2000\ \mathrm{s}^{-1},\quad\zeta=1.265>1.$$

$$s_{1,2}=-2000\pm\sqrt{1.5\times10^6}
\approx-775.255,-3224.745\ \mathrm{s}^{-1}.$$

由 $v_C(0)=10$、$\dot v_C(0)=I_0/C=0$，得

$$v_C(t)\approx(13.1650e^{-775.255t}-3.1650e^{-3224.745t})\ \mathrm V.$$

检查：根之和 $-4000=-R/L$，根之积 $2.5\times10^6=1/(LC)$，初值为 10 V，终值为零。指数中的 $t$ 以 s 计。

### 8.2 欠阻尼频率与包络

$R=2\,\Omega$、$L=1\,\mathrm{mH}$、$C=1\,\mu\mathrm F$、$V_0=5\,\mathrm V$、$I_0=0$：

$$\omega_0=31622.8\ \mathrm{rad/s},\quad\alpha=1000\ \mathrm{s}^{-1},\quad
\zeta=0.03162,\quad\omega_d=31607.0\ \mathrm{rad/s}.$$

故 $f_d\approx5.03\,\mathrm{kHz}$、$\tau_{\mathrm{env}}=1\,\mathrm{ms}$；完整响应为

$$v_C(t)=5e^{-1000t}\left(\cos\omega_dt+\frac{1000}{\omega_d}\sin\omega_dt\right)\ \mathrm V.$$

初始斜率为零，正弦项不能省略；包络在 1 ms 后降为初始包络的 $1/e$。

### 8.3 临界阻尼设计

$L=1\,\mathrm{mH}$、$C=10\,\mu\mathrm F$ 时：

$$R_{\mathrm{crit,series}}=2\sqrt{10^{-3}/10^{-5}}=20\,\Omega,$$

同一 L、C 若改成并联，临界电阻是 $\tfrac12\sqrt{L/C}=5\,\Omega$。两者相差四倍，不能混用。

更多含换路前储能的完整练习见 [[Second-Order Circuit Worked Examples]]。

## 九、常见误区 (Pitfalls)

- **忘记两个条件**：$x(0^+)$ 与 $\dot x(0^+)$ 都需要；其来源是两个独立状态。
- **漏掉直流特解**：标准串联电容阶跃需加 $V_S$；标准并联电感电流阶跃需加 $I_S$。
- **混用串/并联阻尼参数**：先检查 ODE 的一阶导系数，再取一半得到 $\alpha$。
- **把 $\alpha$ 当作 $\zeta$，或把 rad/s 当 Hz**：前者有量纲，后者无量纲；角频率须除以 $2\pi$ 才是 Hz。
- **临界只写一个指数**：必须保留 $te^{-\alpha t}$ 才有两个独立常数。
- **认为暂态系数等于零输入系数**：完整响应中的系数由“初态减去特解”的偏差确定。
- **用三种不同初态的曲线直接证明谁最快**：讲义例 5 的初态随 $R$ 改变；比较速度时须说明输入、初态及性能指标。
- **把有源电路中的受控源关掉**：只关闭独立源，受控关系必须保留。

## 十、与频域的衔接 (Time and Frequency Domains)

对标准二阶分母，**品质因数 (quality factor)** 为 $Q=1/(2\zeta)$。标准串联 RLC 电流带通或并联 RLC 阻抗的半功率角带宽为

$$\Delta\omega=\frac{\omega_0}{Q}=2\alpha,\qquad
\Delta f=\frac{\Delta\omega}{2\pi}.$$

该带宽公式需指定拓扑与输出量，不能无条件用于任意二阶低通的 $-3$ dB 带宽。自由振铃的 $\omega_d$、无阻尼 $\omega_0$ 与某个传递函数的谐振峰频率也不能一概相等。详见 [[Resonance]]、[[Frequency Response]] 与 [[Filters]]。

## 相关笔记

- [[First-Order Transients]] —— 一阶三要素法与换路基础
- [[Second-Order Circuit Worked Examples]] —— 初始导数、串/并联、双电感与运放例题
- [[Capacitor]] / [[Inductor]] —— 本构关系与储能
- [[Energy and Charge Conservation]] —— 能量交换与耗散
- [[Basic Circuit Analysis Method]] / [[Kirchhoff's Laws]] —— 列写方程与消元
- [[Operational Amplifier]] —— 有源二阶 RC 电路
- [[Impedance]] / [[Resonance]] / [[Frequency Response]] / [[Filters]] —— 频域衔接
- [[Circuit Theory Glossary]] / [[cs6.002x.1]] —— 术语表与知识树

## 来源与推导说明

- CUHK-Shenzhen，ECE 2001 *Basic Circuit Theory*，Lecture 6，[[ECE2001/L6 Second-order Circuits 20261018.pdf|L6 Second-order Circuits 20261018]]：PDF pp.3–12（阶数与初始条件），pp.14–35（串联自然响应与阻尼），pp.36–38（串联阶跃），pp.39–47（并联），pp.48–63（例题与一般二阶电路），pp.64–65（学习目标与总结）。文件日期：2026-10-18。
- 系数速算、状态空间、能量导数、机械类比、零初态阶跃式及频域联系，是基于文中理想模型的数学推导与扩展；讲义中的数值勘误集中列于配套例题笔记。
