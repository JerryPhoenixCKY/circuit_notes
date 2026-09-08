---
tags:
  - 电路学
  - 正弦稳态
  - 谐振
  - RLC
  - 课程笔记
date: 2026-09-08
aliases:
  - Resonance
  - 谐振
  - 谐振电路
  - 共振
  - LC Resonance
  - 串联谐振
  - 并联谐振
  - Series Resonance
  - Parallel Resonance
  - 谐振频率
  - Resonant Frequency
  - 品质因数
  - Quality Factor
  - Q因子
  - Bandwidth
  - 带宽
---

# Resonance（谐振）

> [!NOTE] 本笔记定位
> 谐振是 LC 电路在正弦稳态下的核心现象：**当激励频率等于固有振荡频率 $\omega_0=1/\sqrt{LC}$ 时，电路呈现纯电阻特性（阻抗最小或最大）**，产生电流/电压的极大值。这是 [[Filters]] 中带通/陷波滤波器的物理基础，也是电力系统、无线通信、振荡器的核心机制。
> 承上：[[Impedance]]（LC 阻抗特性）/ [[Frequency Response]]（频率响应/Bode 图）；启下：[[Filters]]（谐振滤波器）/ [[Second-Order Transients]]（LC 固有振荡的时域分析）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、谐振的物理本质

### 1.1 什么是谐振？

> [!NOTE] 谐振的定义
> **谐振 (Resonance)**：外部激励频率等于系统**固有频率**时，系统响应达到极值的现象。
> - 机械系统：音叉被同频声波激发（声音共鸣）
> - 电路系统：LC 电路在 $\omega_0 = 1/\sqrt{LC}$ 处阻抗最小/最大

### 1.2 LC 电路的固有振荡频率

无阻尼 LC 电路（电容初始充电后释放）的自由振荡频率：

$$\omega_0 = \frac{1}{\sqrt{LC}}, \qquad f_0 = \frac{1}{2\pi\sqrt{LC}}$$

推导（来自 [[Second-Order Transients]]）：
$$L\frac{di}{dt} + \frac{1}{C}\int i\,dt = 0 \Longrightarrow \frac{d^2v}{dt^2} + \frac{1}{LC}v = 0$$
特征方程：$s^2 + \omega_0^2 = 0 \Rightarrow s = \pm j\omega_0$（纯虚根 $\Rightarrow$ 持续振荡）

> [!IMPORTANT] 谐振频率的物理意义
> $\omega_0$ 是电容"试图"充电和电感"试图"放电之间的**交换速率**：
> - 电容电压最大时 → 电感电流为零（能量全在电场）
> - 电感电流最大时 → 电容电压为零（能量全在磁场）
> - 能量在电场与磁场之间来回交换，频率为 $\omega_0$

### 1.3 两种谐振结构

| 类型 | 电路 | 谐振时阻抗 | 谐振时电流/电压 |
| :--- | :--- | :--- | :--- |
| **串联谐振** | R + L + C 串联 | $|Z|_{\min}=R$ | $I_{\max}=V_s/R$ |
| **并联谐振** | R ‖ L ‖ C | $|Z|_{\max}=R$ | $I_s$ 在 L/C 支路间交换 |

---

## 二、串联 RLC 谐振（Series Resonance）

### 2.1 阻抗特性

$$Z_{\text{series}} = R + j\!\left(\omega L - \frac{1}{\omega C}\right)$$

- **电抗 $X_s = \omega L - 1/(\omega C)$**
- **谐振条件**：$X_s = 0 \Rightarrow \omega_0 L = \dfrac{1}{\omega_0 C} \Rightarrow \boxed{\omega_0 = \dfrac{1}{\sqrt{LC}}}$

> [!NOTE] 谐振时的物理状态
> - 电感电压 $V_L = j\omega_0 L\,I$ 与电容电压 $V_C = -j/(\omega_0 C)\,I$ **大小相等、方向相反**（$180^\circ$ 相位差）
> - 两者在内部完全抵消，电路对外表现为纯电阻 $R$
> - 总电压 $V_s = R\,I$，电流 $I$ 达到最大值

### 2.2 谐振曲线

![[series_resonance.svg]]

> ![[series_resonance.svg]]
> **串联 RLC**：$|Z|$ 在 $\omega_0$ 处最小（$=R$），$|I|$ 在 $\omega_0$ 处最大（$=V_s/R$）

| 频率 | $\omega<\omega_0$（电容主导）| $\omega>\omega_0$（电感主导）|
| :--- | :--- | :--- |
| 电抗 $X_s$ | $-1/(\omega C)$（容性，负）| $+\omega L$（感性，正）|
| 阻抗幅值 | $>R$ | $>R$ |
| 电流 | $< V_s/R$ | $< V_s/R$ |
| 相位 $\angle Z$ | $-90^\circ<\theta<0$（电压滞后）| $0<\theta<+90^\circ$（电压超前）|

> [!NOTE] 电流超前/滞后与电抗符号
> - 容性（$X<0$）：电流超前电压（$I$ 试图给电容充电）
> - 感性（$X>0$）：电压超前电流（电感对抗电流变化）

---

## 三、并联 RLC 谐振（Parallel Resonance）

### 3.1 导纳与阻抗

$$Y_{\text{parallel}} = \frac{1}{R} + \frac{1}{j\omega L} + j\omega C = \frac{1}{R} + j\!\left(\omega C - \frac{1}{\omega L}\right)$$

$$Z_{\text{parallel}} = \frac{1}{Y_{\text{parallel}}} = \frac{1}{\dfrac{1}{R} + j\!\left(\omega C - \dfrac{1}{\omega L}\right)}$$

- **谐振条件**：$\omega_0 C = \dfrac{1}{\omega_0 L} \Rightarrow \boxed{\omega_0 = \dfrac{1}{\sqrt{LC}}}$（与串联相同！）

> [!NOTE] 并联谐振时
> - $Y$ 的虚部为零，$Y_{\min}=1/R$
> - $Z_{\max}=R$（阻抗最大，等于并联电阻）
> - 总电流 $I_s = V_s/R$，但流过 L 和 C 的电流可能远大于 $I_s$（谐振环流）

### 3.2 谐振环流（Tank Circuit 现象）

并联谐振时，电感支路电流 $I_L = V_s/(j\omega_0 L)$ 与电容支路电流 $I_C = j\omega_0 C\,V_s$ 大小相等、方向相反（$180^\circ$ 差），在 LC 支路之间来回交换：

$$|I_L| = |I_C| = Q\,|I_s| \quad \text{其中 } Q = \frac{R}{Z_0} = R\sqrt{\frac{C}{L}}$$

> [!IMPORTANT] $Q$ 的并联含义
> 并联谐振的 $Q$ 表示**储能相对耗能的比例**：
> $Q = 2\pi \times \dfrac{\text{最大储能}}{\text{每周期耗能}} = R\sqrt{\dfrac{C}{L}} = \dfrac{R}{\omega_0 L} = \omega_0 RC$
> - $Q$ 大：LC 环流远大于外部电流（储能大、耗能少）
> - 这就是 **LC 槽路 (Tank Circuit)** 的名称来源——能量在 LC 之间来回"振荡"（tank），很少消耗在电阻上

### 3.3 谐振曲线

![[parallel_resonance.svg]]

> ![[parallel_resonance.svg]]
> **并联 RLC**：$|Z|$ 在 $\omega_0$ 处最大（$=R$），阻抗随频率偏离而下降

---

## 四、品质因数 $Q$（Quality Factor）

### 4.1 两种定义的统一

| 视角 | 串联 RLC | 并联 RLC |
| :--- | :--- | :--- |
| **基本定义** | $Q = \dfrac{\omega_0 L}{R} = \dfrac{1}{R}\sqrt{\dfrac{L}{C}}$ | $Q = R\sqrt{\dfrac{C}{L}} = \dfrac{R}{\omega_0 L} = \omega_0 RC$ |
| **物理含义** | $Q = 2\pi \dfrac{\text{最大磁能}}{\text{每周期耗能}}$ | $Q = 2\pi \dfrac{\text{最大电能}}{\text{每周期耗能}}$ |
| **谐振峰表达** | $I_{\max}/I(\omega\neq\omega_0)$ | $V_{\max}/V(\omega\neq\omega_0)$ |
| **带宽关系** | $BW = \dfrac{\omega_0}{Q} = \dfrac{R}{L}$ | $BW = \dfrac{\omega_0}{Q} = \dfrac{1}{RC}$ |

> [!IMPORTANT] $Q$ 的统一表达式
> $$\boxed{Q = \frac{\omega_0 \times \text{最大储能}}{\text{平均耗散功率}}}$$
> 两种定义在数学上等价（因为串联和并联的 $Q$ 定义互为倒数）。

### 4.2 $Q$ 对频率选择性的影响

$$\boxed{BW = \frac{\omega_0}{Q}}$$

| $Q$ | $BW$ | 选择性 | 典型应用 |
| :--- | :--- | :--- | :--- |
| $Q=1$ | $BW=\omega_0$ | 一般 | 宽频带放大器 |
| $Q=10$ | $BW=\omega_0/10$ | 良好 | 音频选频 |
| $Q=100$ | $BW=\omega_0/100$ | 优秀 | 收音机中频 (IF) |
| $Q=1000$ | $BW=\omega_0/1000$ | 极优秀 | 晶体滤波器 |

> [!TIP] $Q$ 越大，带宽越窄，频率选择性越好
> 这与 [[Frequency Response]] 中 $Q$ 控制谐振峰高度的结论一致。

---

## 五、谐振电路的 Bode 图

### 5.1 串联 RLC 的幅频与相频

$$H(j\omega) = \frac{\tilde{V}_R}{\tilde{V}_s} = \frac{R}{R + j(\omega L - 1/\omega C)}$$

| 频率区间 | $|H|$ 特性 | $\angle H$ 特性 |
| :--- | :--- | :--- |
| $\omega\ll\omega_0$ | $\approx 1/(\omega RC)$（$-20$ dB/dec）| $\approx +90^\circ$（电容主导）|
| $\omega\approx\omega_0$ | 峰值（$Q>1$ 时）| 快速穿越 $0^\circ$ |
| $\omega\gg\omega_0$ | $\approx R/(\omega L)$（$-20$ dB/dec）| $\approx -90^\circ$（电感主导）|

### 5.2 $Q$ 对谐振峰的影响

$$|H(\omega_0)| = \frac{1}{R}\sqrt{\frac{L}{C}} = Q$$

> [!IMPORTANT] 谐振峰增益 = $Q$
> - $Q=1$：峰值 $|H|=1$（无过冲）
> - $Q=2$：峰值 $|H|=2$（2 倍增益）
> - $Q=10$：峰值 $|H|=10$（10 倍增益！）
> - $Q\to\infty$：理论上增益无穷大（无阻尼理想 LC 振荡）

> [!WARNING] 实际 $Q$ 受限因素
> 电感绕组电阻 $R_L$、电容 ESR（等效串联电阻）、趋肤效应损耗限制了实际 $Q$：
> - 实际电感 $Q_L = \omega L/(R_{\text{DC}}+R_{\text{AC}})$ 通常在 $10$–$200$ 范围
> - 空心线圈 $Q$ 可达 $300$–$500$；铁芯电感 $Q$ 通常 $5$–$50$

---

## 六、谐振滤波器的实际应用

### 6.1 收音机调谐电路（带通滤波）

$$\omega_0 = \frac{1}{\sqrt{LC}}, \quad BW = \frac{\omega_0}{Q}$$

- 调节电容 $C$（可变电容）改变 $\omega_0$，选择不同电台频率
- $Q\approx 50$–$100$（AM 广播频段 530 kHz–1.7 MHz）
- 带宽 $BW \approx 10$–$30$ kHz（刚好容纳语音带宽）

### 6.2 陷波滤波器（并联 RLC 并联分流）

在信号通路中并联一个 LC 串联电路（零阻抗在 $\omega_0$），实现陷波：

$$Z_{\text{LC}} = R_s + j(\omega L - 1/\omega C)$$

- 在 $\omega_0$ 处 $Z_{\text{LC}}\approx R_s$（最小阻抗）
- $\omega_0$ 频率被短路到地，阻断通过
- 详见 [[Filters]] §5。

### 6.3 振荡器（谐振反馈）

$$|H(j\omega_0)\,β(j\omega_0)| = 1, \quad \angle H + \angle β = 0^\circ$$

> [!NOTE] 振荡器条件（[[Amplifiers and Feedback]]）
> 放大器 + 谐振选频网络构成正反馈环路，在 $\omega_0$ 处增益为 1、相位为 $0^\circ$ 时产生自激振荡（无输入也能维持正弦输出）。
> 常见振荡器：Hartley ($\omega_0\approx 1/\sqrt{LC}$)、Colpitts ($\omega_0\approx 1/\sqrt{LC_{\text{eff}}}$)

---

## 七、谐振与暂态的对比

| 维度 | 谐振（正弦稳态）| 固有振荡（暂态）|
| :--- | :--- | :--- |
| 驱动 | **外部正弦激励**（强制响应）| **初始条件**（固有响应）|
| 频率 | 驱动频率 $\omega$ | 固有频率 $\omega_0=1/\sqrt{LC}$ |
| 结果 | $\omega=\omega_0$ 时响应极值 | 自由振荡频率 $\omega_0$（无阻尼）|
| 分析工具 | 相量法 / 阻抗 | 微分方程 / 特征根 |

> [!NOTE] 谐振 = 强制振荡与固有振荡的频率匹配
> 当外部激励频率等于固有频率时，强制振荡与固有振荡**同频同相**，两者叠加导致振幅急剧增加（共振）。

---

## 相关笔记

- [[Impedance]] —— LC 元件的阻抗（$Z_C=1/j\omega C$、$Z_L=j\omega L$）
- [[Frequency Response]] —— Bode 图 / 极点/零点（谐振是频率响应的一种特殊情况）
- [[Filters]] —— 带通 / 陷波滤波器的电路实现（谐振的直接应用）
- [[Second-Order Transients]] —— LC 固有振荡的时域分析（$v(t)=V_0\cos\omega_0 t$）
- [[Complex Numbers and Euler's Formula]] —— 复阻抗的极坐标形式（$Z=|Z|\angle\theta$）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
