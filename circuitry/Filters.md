---
tags:
  - 电路学
  - 正弦稳态
  - 滤波器
  - 电路设计
  - 课程笔记
date: 2026-09-08
aliases:
  - Filters
  - 滤波器
  - 电子滤波器
  - 滤波电路
  - 低通滤波器
  - 高通滤波器
  - 带通滤波器
  - 陷波滤波器
  - Filter Design
  - Low-Pass
  - High-Pass
  - Band-Pass
  - Notch Filter
  - Band-Stop
---

# Filters（滤波器）

> [!NOTE] 本笔记定位
> 频率响应在**信号处理**中的直接应用：滤波器根据频率选择性地通过或阻断信号，是所有电子系统（通信、音频、电源）的核心模块。四种基本类型（LP/HP/BP/Notch）对应不同的频域特性，由一阶/二阶 RC/RL/RLC 电路实现。
> 承上：[[Frequency Response]]（频率响应/Bode 图基础）/ [[Impedance]]（阻抗）；启下：[[Resonance]]（谐振滤波器的 Q 与带宽）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、滤波器的本质：频率选择

### 1.1 四种基本滤波器

| 类型 | 简称 | 通过频段 | 阻断频段 | 典型应用 |
| :--- | :---: | :--- | :--- | :--- |
| **低通 (Low-Pass)** | LP | $0\sim\omega_c$ | $\omega>\omega_c$ | 抗混叠、积分器、电源平滑 |
| **高通 (High-Pass)** | HP | $\omega>\omega_c$ | $0\sim\omega_c$ | 耦合电容（隔直通交）、微分器 |
| **带通 (Band-Pass)** | BP | $\omega_0\pm BW/2$ | 其他 | 收音机选台、锁相环 (PLL) |
| **陷波 / 带阻 (Notch / Band-Stop)** | BS | 除 $\omega_0$ 外 | $\omega\approx\omega_0$ | 去除工频干扰（50/60 Hz）|

> [!NOTE] 滤波器的频率选择性由极点/零点决定
> 极点决定**增益峰值**出现的位置（[[Frequency Response]] §4），零点决定**衰减最深**的位置。

### 1.2 幅频特性图

![[filter_magnitude.svg]]
> ![[filter_magnitude.svg]]
> 四种基本滤波器的典型幅频响应（dB vs $\omega$，对数坐标）

---

## 二、一阶滤波器（单 RC/RL 网络）

### 2.1 一阶低通 (LP) 滤波器

> [!EXAMPLE] RC 低通
> 输入 $v_{\text{in}}$ 加在 RC 串联上，输出 $v_{\text{out}}$ 取电容两端：
> $$H(j\omega) = \frac{\tilde{V}_{\text{out}}}{\tilde{V}_{\text{in}}} = \frac{1/j\omega C}{R+1/j\omega C} = \frac{1}{1+j\omega RC}$$
> - **截止频率** $\omega_c = 1/(RC)$，$|H(\omega_c)|=1/\sqrt{2}$（$-3$ dB）
> - **斜率**：高频衰减 $-20$ dB/dec（一阶系统，斜率 $-20$ dB/dec）
> - **相位**：$\angle H = -\arctan(\omega RC)$，从 $0^\circ$（低频）到 $-90^\circ$（高频）

| 频率 | $|H|$ | $\angle H$ | 物理解释 |
| :--- | :--- | :--- | :--- |
| $\omega\ll\omega_c$ | $\approx 1$ | $\approx 0^\circ$ | 电容阻抗大，$v_{\text{out}}\approx v_{\text{in}}$ |
| $\omega=\omega_c$ | $1/\sqrt{2}$ | $-45^\circ$ | 转折点 |
| $\omega\gg\omega_c$ | $\approx 1/(\omega RC)$ | $\approx -90^\circ$ | 电容阻抗小，$v_{\text{out}}\approx i/j\omega C$（积分效应）|

> [!NOTE] 积分器 ↔ 低通的联系
> $\omega\gg\omega_c$ 时，$v_{\text{out}}\approx \dfrac{1}{RC}\int v_{\text{in}}\,dt$（对输入积分）—— 这是一阶低通在高频区的行为，也是[[Sinusoidal Steady State]]中 RC 对高频正弦信号"跟不上"的本质。

### 2.2 一阶高通 (HP) 滤波器

> [!EXAMPLE] RC 高通
> 输出 $v_{\text{out}}$ 取电阻两端：
> $$H(j\omega) = \frac{\tilde{V}_{\text{out}}}{\tilde{V}_{\text{in}}} = \frac{R}{R+1/j\omega C} = \frac{j\omega RC}{1+j\omega RC}$$
> - **截止频率**：同样是 $\omega_c = 1/(RC)$
> - **斜率**：低频上升 $+20$ dB/dec
> - **相位**：$\angle H = +\arctan(\omega RC)$，从 $+90^\circ$（低频）到 $0^\circ$（高频）

> [!NOTE] 耦合电容的滤波作用
> 输入级之间的耦合电容（隔直电容）本质上就是高通滤波器——阻断直流偏置，只让交流信号通过。例如音频放大器的输入耦合电容阻止前级的直流电压偏移影响本级偏置。

---

## 三、二阶滤波器（RLC 网络）

### 3.1 二阶低通 (LP) 滤波器

> [!EXAMPLE] RLC 串联二阶 LP
> $$H(j\omega) = \frac{1/(LC)}{s^2 + s(R/L) + 1/(LC)}\bigg|_{s=j\omega}, \quad \omega_0 = \frac{1}{\sqrt{LC}},\ Q = \frac{1}{R}\sqrt{\frac{L}{C}}$$
> - **高频衰减**：$-40$ dB/dec（两阶 pole，斜率加倍）
> - **谐振峰**：当 $Q>1/\sqrt{2}$ 时，在 $\omega_0$ 附近出现增益过冲
> - **$Q$ 控制阻尼**：
>   - $Q>0.707$：过冲（peaking）
>   - $Q=0.707$：**Butterworth（最大平坦）**（无过冲）
>   - $Q<0.707$：单调下降

### 3.2 二阶带通 (BP) 滤波器

> [!EXAMPLE] 串联 RLC 带通（[[Resonance]] 的直接应用）
> 输出取自电阻 $R$ 两端（$v_R = R\,i$）：
> $$H(j\omega) = \frac{\tilde{V}_R}{\tilde{V}_s} = \frac{R}{R + j(\omega L - 1/\omega C)} = \frac{j\omega/(Q\omega_0)}{1+j\omega/(Q\omega_0) + (j\omega/\omega_0)^2}$$
> - **中心频率**：$\omega_0 = 1/\sqrt{LC}$
> - **带宽**：$BW = \omega_0/Q$
> - **选择性**：$Q$ 越大，带宽越窄，选择性越好

| $Q$ | $BW$ | 选择性 | 典型应用 |
| :--- | :--- | :--- | :--- |
| $Q=1$ | $BW=\omega_0$ | 一般 | 音频分频 |
| $Q=50$ | $BW=\omega_0/50$ | 良好 | AM 收音机选台 |
| $Q=500$ | $BW=\omega_0/500$ | 优秀 | 晶体振荡器 |

---

## 四、有源滤波器（Active Filters）

> [!NOTE] 无源 vs 有源
> **无源滤波器**（本笔记）：仅由 R、C、L 构成，结构简单，但：
> - **插入损耗**：电感损耗、串联电阻导致通带增益 $<1$
> - **负载效应**：难以驱动低阻抗负载
>
> **有源滤波器**：加入运算放大器（运放），利用运放的高输入阻抗/低输出阻抗特性克服上述缺点。

### 4.1 一阶有源低通

$$H(j\omega) = \left(1+\frac{R_f}{R_1}\right)\frac{1}{1+j\omega RC}$$

- **通带增益**：由运放同相放大器设定 $(1+R_f/R_1)$
- **截止频率**：$\omega_c = 1/(RC)$（与无源相同）
- **优势**：通带增益可 $>1$，可驱动低阻抗负载

### 4.2 常见滤波器阶数与过渡带宽

| 阶数 | 每十倍频程衰减 | 过渡带宽度（相对 $\omega_c$）| 特性 |
| :--- | :--- | :--- | :--- |
| 一阶 | $-20$ dB/dec | 宽 | 最简单，但选择性差 |
| 二阶 | $-40$ dB/dec | 中 | $Q$ 控制谐振峰，常用 |
| 三阶 | $-60$ dB/dec | 较窄 | 级联两个二阶（$\times$ 一阶）|
| $n$ 阶 | $-20n$ dB/dec | 越窄越陡 | 滤波器阶数越高，选择性越好 |

> [!NOTE] 滤波器设计的工程权衡
> - **阶数越高**：过渡带越陡（频率选择性好），但结构越复杂（更多元件）
> - **$Q$ 越大**：谐振峰越高（选择性更好），但过冲可能引起振铃（ringing）

---

## 五、陷波滤波器（Notch Filter）

### 5.1 理想陷波特性

$$H(j\omega) = \begin{cases} 0 & \omega = \omega_0 \\ 1 & \text{otherwise} \end{cases}$$

- **完全阻断** $\omega_0$ 频率
- **对其他频率完全透明**
- 过渡带宽：$\Delta\omega\to 0$（理想不可能）

### 5.2 实际陷波滤波器

> [!EXAMPLE] 并联 RLC 陷波（阻抗并联分流）
> 在信号通路中并联一个 **LC 并联谐振电路**（[[Resonance]]）：
> - 在 $\omega_0=1/\sqrt{LC}$ 处，LC 并联阻抗 $\to\infty$（开路）
> - $\omega_0$ 频率被阻断，其他频率正常通过
> - 品质因数 $Q$ 决定陷波深度与宽度

| 参数 | 对陷波特性的影响 |
| :--- | :--- |
| $Q\uparrow$ | 陷波越窄（频率选择性好），但实现难度增加 |
| $L\uparrow$ 或 $C\uparrow$ | $\omega_0\downarrow$（谐振频率降低） |
| $R_{\text{series}}\uparrow$ | 陷波深度减小（$Q$ 降低） |

> [!TIP] 工频噪声陷波
> 去除 50/60 Hz 交流电网干扰：设计陷波滤波器 $\omega_0 = 2\pi\times 50\text{ or }60$ rad/s，可使用双 T 型陷波网络（Twin-T Notch），$Q\approx 0.25$。

---

## 六、滤波器设计概要

### 6.1 设计步骤

1. **确定规格**：
   - 通带边界 $\omega_p$（允许的最大衰减 $A_p$ dB）
   - 阻带边界 $\omega_s$（要求的最小衰减 $A_s$ dB）
   - 通带增益（通常 $0$ dB）
2. **选择阶数**：根据过渡带宽度，查表得最小阶数 $n$
3. **选择响应类型**：Butterworth（最大平坦）/ Chebyshev（更陡过渡带）/ Bessel（线性相位）
4. **综合电路**：由传递函数综合出具体 R、L、C 值
5. **仿真验证**：用 SPICE 或计算验证 $-3$ dB 频率、阻带衰减

### 6.2 响应类型对比

| 类型 | 特点 | 权衡 |
| :--- | :--- | :--- |
| **Butterworth** | 通带最大平坦 $|H|=1$（$\omega<\omega_c$）| 过渡带中等 |
| **Chebyshev** | 通带/阻带有纹波，过渡带更陡 | 相位非线性，可能振铃 |
| **Bessel** | 相位响应线性（群延迟恒定）| 过渡带最缓 |

---

## 相关笔记

- [[Frequency Response]] —— 频率响应 / Bode 图 / 极点/零点（滤波器的理论基础）
- [[Impedance]] —— 阻抗（RC/RL/RLC 的阻抗计算）
- [[Resonance]] —— 串联/并联 RLC 谐振（BP 滤波器和陷波滤波器的核心）
- [[Sinusoidal Steady State]] —— 相量法（滤波器传递函数的推导工具）
- [[Small Signal Circuit Representation]] —— 有源滤波器中的运放（参考有源滤波部分）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
