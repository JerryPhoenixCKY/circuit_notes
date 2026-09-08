---
tags:
  - 电路学
  - 正弦稳态
  - 频率响应
  - Bode图
  - 课程笔记
date: 2026-09-08
aliases:
  - Frequency Response
  - 频率响应
  - 幅频响应
  - 相频响应
  - Frequency Response Analysis
  - Bode Plot
  - Bode图
  - 传递函数
  - Transfer Function
  - 系统函数
  - System Function
---

# Frequency Response（频率响应）

> [!NOTE] 本笔记定位
> 正弦稳态分析的**核心目标**：研究线性系统的传递函数 $H(j\omega)$ 随频率 $\omega$ 的变化规律。幅频响应 $|H(j\omega)|$ 告诉我们系统对不同频率信号的**放大/衰减程度**，相频响应 $\angle H(j\omega)$ 告诉我们**相位偏移**。Bode 图是工程上描述频率响应的标准工具，也是 [[Filters]]（滤波器）的理论基础。
> 承上：[[Impedance]]（阻抗/相量法）；启下：[[Filters]]（四类滤波器）/ [[Resonance]]（谐振峰的频率响应分析）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、传递函数 $H(j\omega)$ 的定义

### 1.1 输入-输出关系（频域）

对于线性时不变 (LTI) 系统：

$$\boxed{H(j\omega) = \frac{\tilde{V}_{\text{out}}}{\tilde{V}_{\text{in}}}(\omega) = |H(j\omega)|\,e^{j\angle H(\omega)}}$$

- $H(j\omega)$ 是复数，随 $\omega$ 变化
- 幅值 $|H(j\omega)|$：信号被放大/衰减的倍数
- 相角 $\angle H(\omega)$：输出相对于输入的相位偏移

> [!NOTE] 频率响应是相量法在"系统"层面的应用
> 把电路视为**两端口网络**（输入端口 + 输出端口），$H(j\omega)$ 描述这个网络的频率特性。

### 1.2 $H(j\omega)$ 的物理来源

由电路的阻抗网络直接计算：

$$H(j\omega) = \frac{Z_{\text{feedback}}}{Z_{\text{input}}+Z_{\text{feedback}}},\quad H(j\omega) = \frac{1/j\omega C}{R+1/j\omega C},\ \text{等}$$

---

## 二、频率响应的两个维度

### 2.1 幅频响应（Magnitude Response）

$$|H(j\omega)| \quad \text{单位：无量纲（放大倍数）}$$

通常用分贝 (dB) 表示：

$$|H(j\omega)|_{\text{dB}} = 20\log_{10}|H(j\omega)|$$

| dB 值 | 放大倍数 | 物理直觉 |
| :---: | :--- | :--- |
| $+6$ dB | $2\times$ | 幅值翻倍 |
| $0$ dB | $1\times$ | 不变（单位增益） |
| $-3$ dB | $0.707\times$ | **半功率点** |
| $-6$ dB | $0.5\times$ | 幅值减半 |
| $-20$ dB/dec | $0.1\times$ per decade | 每 10 倍频率衰减 10 倍 |

> [!IMPORTANT] $-3$ dB = 半功率点
> $|H(j\omega)| = 1/\sqrt{2}$ 时，输出功率为最大值的 $1/2$，称为**截止频率 (cutoff frequency)** 或 **$-3$ dB 频率**。

### 2.2 相频响应（Phase Response）

$$\angle H(\omega) = \arg(H(j\omega))$$

- 正相角（$+90^\circ$）：输出**超前**输入（电流超前电压）
- 负相角（$-90^\circ$）：输出**滞后**输入（电压滞后电流）

> [!NOTE] 相位的重要性
> 音频系统中相位失真会影响声音的空间感；数字通信中相位误差会导致符号间干扰 (ISI)。

---

## 三、Bode 图（Bode Plot）

### 3.1 什么是 Bode 图？

Bode 图是频率响应的**对数坐标图**，包括：

1. **幅频图**：$\omega$（对数坐标）vs $|H|_{\text{dB}}$（线性坐标）
2. **相频图**：$\omega$（对数坐标）vs $\angle H$（线性坐标，度）

> [!NOTE] Bode 图的对数优势
> - **压缩频率范围**：从 Hz 到 GHz 可在同一坐标轴上显示
> - **乘法变加法**：$H=H_1\cdot H_2 \Rightarrow |H|_{\text{dB}}=|H_1|_{\text{dB}}+|H_2|_{\text{dB}}$，各因子幅值 dB 直接相加
> - **渐近线近似**：一阶因子 $\omega/(\omega_c+j\omega)$ 的幅频曲线由两条直线段（折线）近似，斜率 $\pm 20$ dB/dec

### 3.2 一阶系统的 Bode 图

![[bode_first_order.svg]]

> ![[bode_first_order.svg]]
> **左图：一阶低通 (LP)** $H(j\omega)=\frac{1}{1+j\omega/\omega_c}$
> **右图：一阶高通 (HP)** $H(j\omega)=\frac{j\omega/\omega_c}{1+j\omega/\omega_c}$

| 特征 | 低通 (LP) | 高通 (HP) |
| :--- | :--- | :--- |
| 低频增益 | $0$ dB | $20\log_{10}\omega/\omega_c$（上升，斜率 $+20$ dB/dec） |
| 高频增益 | $-20\log_{10}\omega/\omega_c$（下降，斜率 $-20$ dB/dec） | $0$ dB |
| 截止频率 $\omega_c$ | $\omega_c = 1/RC$（LP）| $\omega_c = R/L$（HP） |
| $-3$ dB 频率 | $\omega_c$ | $\omega_c$ |

### 3.3 二阶系统的 Bode 图（谐振峰）

![[bode_second_order.svg]]

> ![[bode_second_order.svg]]
> **串联 RLC 带通响应**：$H(j\omega) = \dfrac{j\omega/(Q\omega_0)}{1+j\omega/(Q\omega_0)+(j\omega/\omega_0)^2}$
> - $Q\uparrow$（阻尼小）$\Rightarrow$ 谐振峰更高
> - $Q$ 的定义与 [[Resonance]] 一致：$Q=\omega_0 L/R = 1/(R)\sqrt{L/C}$

> [!IMPORTANT] 品质因数 $Q$ 与谐振峰
> - $Q>1/\sqrt{2}\approx 0.707$：幅频曲线出现**谐振峰 (resonance peak)**
> - $Q$ 越大（电阻越小），峰越尖锐
> - $Q\to\infty$（无阻尼）：峰无穷大（理论上无限增益）
> - $Q=0.707$：最大平坦（Butterworth 响应），无过冲

---

## 四、极点与零点（Poles & Zeros）

### 4.1 定义

把 $H(j\omega)$ 的分子分母写成因式分解形式：

$$H(s) = K\cdot\frac{(s-z_1)(s-z_2)\cdots(s-z_m)}{(s-p_1)(s-p_2)\cdots(s-p_n)}, \quad s=j\omega$$

| 术语 | 定义 | 频率响应影响 |
| :--- | :--- | :--- |
| **零点 (Zero)** $z_k$ | 分子为零时 $s=z_k$ | $|H|$ 在 $z_k$ 处衰减，$\angle H$ 产生 $-90^\circ$ 跳变 |
| **极点 (Pole)** $p_k$ | 分母为零时 $s=p_k$ | $|H|$ 在 $p_k$ 处增益无穷大（无阻尼），$\angle H$ 产生 $+90^\circ$ 跳变 |
| **左半平面 (LHP)** | $\Re\{p_k\}<0$ | 系统稳定 |
| **右半平面 (RHP)** | $\Re\{p_k\}>0$ | 系统不稳定 |

> [!NOTE] 稳定系统的极点
> 对于**稳定**的 LTI 系统，所有极点必须在左半平面 (LHP)，即 $\Re\{p_k\}<0$。这保证了 $t\to\infty$ 时齐次响应（暂态）衰减到零。

### 4.2 一阶系统的极点/零点

| 系统 | 传递函数 | 极点 | 零点 | 截止频率 |
| :--- | :--- | :--- | :--- | :--- |
| LP $RC$ | $H=1/(1+j\omega/\omega_c)$ | $p=-\omega_c$ | 无 | $\omega_c=1/RC$ |
| HP $RC$ | $H=j\omega/\omega_c/(1+j\omega/\omega_c)$ | $p=-\omega_c$ | $z=0$ | $\omega_c=1/RC$ |

---

## 五、Bode 图的渐近线近似（工程实用法）

### 5.1 幅频渐近线规则

| 因子 | 低频（$\omega\ll\omega_c$）| 高频（$\omega\gg\omega_c$）|
| :--- | :--- | :--- |
| **常数 $K$** | $K$（dB）| $K$（dB）|
| **一阶极点 $(1+j\omega/\omega_c)^{-1}$** | $0$ dB | $-20$ dB/dec 斜率 |
| **一阶零点 $(1+j\omega/\omega_c)$** | $0$ dB | $+20$ dB/dec 斜率 |
| **二阶极点 $(1+j\omega/\omega_0+(j\omega/\omega_0)^2)^{-1}$** | $0$ dB | $-40$ dB/dec 斜率 |

> [!NOTE] 每十倍频程 (decade) 的 dB 变化
> $|H|_{\text{dB}} = 20\log_{10}|H|$
> - 一阶因子：$\pm 20$ dB/dec = $\pm 6$ dB/oct（每倍频程）
> - 二阶因子：$\pm 40$ dB/dec = $\pm 12$ dB/oct

### 5.2 相频渐近线规则

| 因子 | $\omega\ll\omega_c$ | $\omega\approx\omega_c$ | $\omega\gg\omega_c$ |
| :--- | :--- | :--- | :--- |
| **一阶极点 $(1+j\omega/\omega_c)^{-1}$** | $0^\circ$ | $-45^\circ$ | $-90^\circ$ |
| **一阶零点 $(1+j\omega/\omega_c)$** | $0^\circ$ | $+45^\circ$ | $+90^\circ$ |
| **二阶（$Q$ 依赖）** | $0^\circ$ | $\approx -90^\circ$ | $-180^\circ$ |

> [!TIP] 相位曲线的折线近似
> 以 $\omega_c$ 为中心，$\pm$ 一 decade 范围内线性过渡：$0^\circ\to-90^\circ$（极点）或 $0^\circ\to+90^\circ$（零点）。

---

## 六、带宽与频率选择性

### 6.1 带宽 (Bandwidth) 的定义

$$BW = \omega_2 - \omega_1$$

其中 $\omega_1$、$\omega_2$ 是 $|H(j\omega)|$ 下降到最大值的 $1/\sqrt{2}$（$-3$ dB）处的频率。

> [!IMPORTANT] 带宽 ↔ 时间常数的对偶
> - 时域：$\tau = RC \Rightarrow f_c = 1/(2\pi RC)$（一阶 $-3$ dB 频率）
> - 频域：$BW = \omega_c = 1/\tau$（对于一阶低通）
> **时间常数越小（响应越快） $\Leftrightarrow$ 带宽越宽**

### 6.2 频率选择性与 $Q$

$$Q = \frac{\omega_0}{BW}$$

- **$Q$ 大** $\Rightarrow$ 带宽窄 $\Rightarrow$ 频率选择性好（谐振峰尖锐）
- **$Q$ 小** $\Rightarrow$ 带宽宽 $\Rightarrow$ 频率选择性差（平坦响应）

---

## 七、实际频率响应举例

> [!EXAMPLE] RC 低通滤波器的频率响应
> $H(j\omega) = \dfrac{1}{1+j\omega RC}$
> - $\omega\ll 1/RC$：$|H|\approx 1$（0 dB），$\angle H\approx 0^\circ$
> - $\omega=1/RC$：$|H|=1/\sqrt{2}$（$-3$ dB），$\angle H=-45^\circ$
> - $\omega\gg 1/RC$：$|H|\approx 1/(\omega RC)$（$-20$ dB/dec 衰减），$\angle H\approx -90^\circ$

> [!EXAMPLE] 共源 MOSFET 放大器的高频响应
> 密勒效应：$C_{gd}$ 在输入端被放大为 $C_M = C_{gd}(1+|A_v|)$
> 高频截止：$\omega_H = 1/(R_{\text{in}}\,C_M)$
> 详见 [[Small Signal Circuit Representation]] 与 [[The MOSFET Amplifier]]。

---

## 相关笔记

- [[Impedance]] —— 阻抗的定义（$Z_R=R,\ Z_C=1/j\omega C,\ Z_L=j\omega L$）
- [[Sinusoidal Steady State]] —— 相量法基础（$H(j\omega)$ 的推导来源）
- [[Filters]] —— 低通 / 高通 / 带通 / 陷波的传递函数与设计
- [[Resonance]] —— LC 谐振的频率响应（$Q$ 与带宽的关系）
- [[Small Signal Circuit Representation]] —— 放大器的高频响应与密勒效应
- [[Complex Numbers and Euler's Formula]] —— Bode 图的数学基础（对数/相量）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
