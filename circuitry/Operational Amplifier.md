---
tags:
  - 电路学
  - 有源器件
  - 运算放大器
  - 课程笔记
date: 2026-09-08
aliases:
  - Operational Amplifier
  - Op Amp
  - 运算放大器
  - 运放
  - Operational Amplifier Abstraction
  - Op-Amp Model
  - 虚短
  - 虚断
  - Virtual Short
  - Virtual Open
---

# Operational Amplifier（运算放大器）

> [!NOTE] 本笔记定位
> 运算放大器（Op-Amp）是模拟电子系统的**核心有源器件**：把一个差分电压信号放大 $10^5$–$10^6$ 倍。其强大之处不在于开环增益本身，而在于**负反馈**（negative feedback）——通过外接电阻网络把输出信号引回输入端，将增益压低到确定值，同时获得高输入阻抗、低输出阻抗、近似线性的传输特性。
> 承上：[[Small Signal Circuit Representation]]（输入/输出电阻、增益）/ [[Impedance]]（阻抗）；启下：[[Diode]]（整流后的信号要用运放滤波/缓冲）/ [[Filters]]（有源滤波器）/ [[Amplifiers and Feedback]]（反馈理论）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、运放符号与端口

![[opamp_symbol.svg]]

> ![[opamp_symbol.svg]]
> **运放电路符号**（5 端口）：同相输入 $v_+$（不反相）、反相输入 $v_-$（反相）、输出 $v_{\text{out}}$、正电源 $V_+$、负电源 $V_-$。

| 端口 | 符号 | 功能 |
| :--- | :--- | :--- |
| **同相输入 $v_+$** | `+` | 输入电压与输出同相（$v_{\text{out}}\propto +v_+$）|
| **反相输入 $v_-$** | `−` | 输入电压与输出反相（$v_{\text{out}}\propto -v_-$）|
| **输出 $v_{\text{out}}$** | — | 放大后的电压输出 |
| **正电源 $V_S+$** | — | 通常 $+15$ V（最高允许电压）|
| **负电源 $V_S-$** | — | 通常 $-15$ V（或接地/GND）|

---

## 二、理想运放模型（五参数）

> [!IMPORTANT] 理想运放的两条黄金规则
> 1. **虚短 (Virtual Short)**：$v_+ \approx v_-$（两个输入端电压几乎相等）
> 2. **虚断 (Virtual Open)**：$i_+ = i_- \approx 0$（两个输入端不汲取电流）
>
> 两者共同成立的前提：**运放工作在线性区（负反馈闭环）**。

### 2.1 理想参数表

| 参数 | 理想值 | 实际典型值 | 影响 |
| :--- | :--- | :--- | :--- |
| **开环电压增益 $A$** | $\infty$ | $10^5$–$10^6$ | 决定闭环精度 |
| **输入电阻 $R_{\text{in}}$** | $\infty$ | $10^6$–$10^{12}$ Ω | 高：前级不负载 |
| **输出电阻 $R_{\text{out}}$** | $0$ | $10$–$100$ Ω | 低：驱动能力强 |
| **带宽 $BW$** | $\infty$ | 有限（GBW = $A\cdot f_{-3dB}$）| 影响高频响应 |
| **输入偏置电流 $I_B$** | $0$ | nA–pA 级 | 失调电压源 |
| **输入失调电压 $V_{OS}$** | $0$ | μV–mV 级 | 零输入时的输出偏移 |

### 2.2 开环传输特性

$$v_{\text{out}} = A\,(v_+ - v_-)$$

- $A\to\infty$ 时，$v_+ - v_- = v_{\text{out}}/A \to 0$（虚短成立）
- **饱和**：$|v_{\text{out}}|$ 不能超过供电电压 $\pm V_{\text{SAT}}$（通常略低于 $\pm V_S$，典型 $\pm 13$–$\pm 14.5$ V）

> [!NOTE] 饱和的物理含义
> 运放内部晶体管进入非线性区（[[Large-Signal Model]]），输出被电源轨夹断。饱和时 $v_{\text{out}}\approx \pm V_{\text{SAT}}$，不再跟随 $v_+-v_-$，失真严重。设计时须保证 $v_{\text{out}}$ 在线性范围内。

---

## 三、七种基本运放电路

![[opamp_basic_circuits.svg]]

> ![[opamp_basic_circuits.svg]]
> **四种基本运放电路**：同相放大、反相放大、电压跟随器、差分放大器

### 3.1 同相放大器 (Non-Inverting Amplifier)

![[opamp_basic_circuits.svg]]
> 上排左图

$$\boxed{A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = 1 + \frac{R_f}{R_1}}$$

- **增益**：永远 $\ge 1$（最小值是 $1$，即电压跟随器）
- **输入阻抗**：$R_{\text{in}} \approx \infty$（虚断）
- **输出阻抗**：$R_{\text{out}} \approx 0$（负反馈降低输出阻抗）
- **相位**：同相（$v_{\text{out}}$ 与 $v_{\text{in}}$ 同方向）

> [!EXAMPLE] $R_f=9\text{k}\Omega,\ R_1=1\text{k}\Omega \Rightarrow A_v=10$
> $v_{\text{out}} = 10\times v_{\text{in}}$，输入 $0.5$ V $\to$ 输出 $5$ V（在线性范围内）

### 3.2 反相放大器 (Inverting Amplifier)

> 上排右图

$$\boxed{A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = -\frac{R_f}{R_1}}$$

- **增益**：可大可小，符号为负（输出与输入反相 $180^\circ$）
- **输入阻抗**：$R_{\text{in}} = R_1$（电流从 $v_{\text{in}}$ 经 $R_1$ 流入运放虚地）
- **"虚地 (Virtual Ground)"**：$v_-$ 被强制到接近 $0$ V（虚短 + $v_+=0$）

> [!NOTE] 虚地
> 反相放大器中 $v_+=0$（接地），虚短 $\Rightarrow v_-\approx 0$。因此 $v_-$ 是一个"虚假的接地"，称为**虚地 (Virtual Ground)**。输入电流 $i_{\text{in}} = v_{\text{in}}/R_1$，全部流入 $R_f$。

### 3.3 电压跟随器 (Voltage Follower / Buffer)

> 下排左图（同相放大器的特例：$R_f=0,\ R_1=\infty$）

$$\boxed{A_v = 1 \qquad v_{\text{out}} = v_{\text{in}}}$$

- **单位增益缓冲器**：输入阻抗极高、输出阻抗极低
- **作用**：隔离前后级（不让低阻抗后级拉低前级的信号）

> [!EXAMPLE] 传感器输出阻抗高，不能直接驱动 ADC
> 插入电压跟随器：传感器 $\to$ **跟随器** $\to$ ADC
> - 跟随器不汲取传感器电流（$R_{\text{in}}=\infty$）
> - 跟随器为 ADC 提供低阻抗驱动（$R_{\text{out}}\approx 0$）

### 3.4 差分放大器 (Differential Amplifier)

> 下排右图（减法器）

$$\boxed{v_{\text{out}} = \frac{R_f}{R_1}(v_2 - v_1) \quad \text{当 } R_1=R_2=R_f=R_g}$$

- **典型配置**：测量两个电势之差（如电桥输出、传感器差分信号）
- **CMRR（共模抑制比）**：$R_1/R_2$ 与 $R_f/R_g$ 的匹配精度决定共模抑制能力

### 3.5 加法器 (Summing Amplifier)

$$v_{\text{out}} = -\frac{R_f}{R_1}v_1 - \frac{R_f}{R_2}v_2 - \frac{R_f}{R_3}v_3$$

- **虚地原理**：所有输入端被强制到 $v_- \approx 0$（虚地），各路电流独立相加

> [!EXAMPLE] 音频混音器
> 三个音频信号 $v_1,v_2,v_3$ 按权重 $R_f/R_1$ 混合输出，实现混音效果。

### 3.6 积分器 (Integrator)

> 详见 §四·运放 RC 电路

$$v_{\text{out}}(t) = -\frac{1}{RC}\int_0^t v_{\text{in}}(\tau)\,d\tau + v_{\text{out}}(0)$$

### 3.7 微分器 (Differentiator)

$$v_{\text{out}}(t) = -RC\,\frac{dv_{\text{in}}}{dt}$$

---

## 四、运放 RC 电路（积分器 / 微分器 / Sallen-Key）

![[opamp_active_filter.svg]]

> ![[opamp_active_filter.svg]]
> **运放 RC 电路**：积分器（C 反馈）/ 微分器（C 输入）/ Sallen-Key LP / Sallen-Key HP

### 4.1 积分器（Op-Amp Integrator）

$$\boxed{H(s) = \frac{v_{\text{out}}}{v_{\text{in}}}(s) = -\frac{1}{sRC}}$$

> [!NOTE] 频率域含义
> $H(j\omega) = -1/(j\omega RC) = +j/( \omega RC)$，即：
> - $|H| \propto 1/\omega$（幅值随频率升高而衰减 $\Rightarrow$ **低通**）
> - 相位恒为 $+90^\circ$（输出超前输入 $90^\circ$）
> 这正是 [[Filters]] 中一阶低通滤波器的特性！

> [!WARNING] 积分器漂移问题
> 电容泄漏（有限电阻）会导致输出直流漂移积累（积分器是一个**不稳定系统**），实际电路须加**泄漏电阻** $R_{\text{leak}}$（与 $C$ 并联）抑制漂移，但会引入有限直流增益。

### 4.2 微分器（Op-Amp Differentiator）

$$\boxed{H(s) = \frac{v_{\text{out}}}{v_{\text{in}}}(s) = -sRC}$$

> [!NOTE] 频率域含义
> $|H| \propto \omega$（幅值随频率升高而增加 $\Rightarrow$ **高通**）
> 相位恒为 $-90^\circ$（输出滞后输入 $90^\circ$）
> 高频增益无穷大（实际被运放带宽限制）——容易放大高频噪声，**实际很少使用**。

### 4.3 Sallen-Key 有源滤波器

Sallen-Key 结构是**最常用的二阶有源滤波器**（[[Filters]] §4）：

$$\boxed{H_{\text{LP}}(s) = \frac{\omega_0^2}{s^2 + s(\omega_0/Q) + \omega_0^2}, \quad \omega_0 = \frac{1}{\sqrt{R_1R_2C_1C_2}},\ Q = \frac{\sqrt{R_1R_2C_1C_2}}{R_1+R_2}\sqrt{\frac{C_1}{C_2}}}$$

> [!NOTE] Sallen-Key 的优势
> - **有源滤波**（比无源 RLC 少电感）：易于集成、阻抗匹配好
> - **可调 $Q$**：通过调整电阻比 $R_1/R_2$ 或电容比 $C_1/C_2$ 控制谐振峰
> - **单位增益**（$K=1$）或**带增益**版本（[[Filters]] §4.1）

---

## 五、饱和、正反馈与振荡器

### 5.1 饱和

> [!IMPORTANT] 饱和 = 运放的"截止"与"饱和"（[[Large-Signal Model]]）
> - 当 $|v_{\text{out}}| \ge V_{\text{SAT}} \approx \pm 14$ V（$\pm 15$ V 供电）
> - 内部晶体管退出线性放大区，进入大信号模式
> - $v_{\text{out}}$ 被电源轨夹断，不再跟随 $v_+-v_-$
> - 失真：正弦波变成削顶波形（[[Diode]] §削波）

### 5.2 正反馈 (Positive Feedback)

负反馈（$v_-$ 反馈）使系统稳定；正反馈（$v_+$ 反馈）使系统不稳定：

$$v_{\text{out}} = A\,(v_+ - v_-) \quad\text{且}\quad v_+ = \beta\,v_{\text{out}}$$

$$\Rightarrow\quad v_{\text{out}} = \frac{A}{1-A\beta}\,v_{\text{in}}$$

- 当 $A\beta \to 1$（环路增益 $\to 1$）：$v_{\text{out}} \to \infty$（饱和或振荡）
- **Barkhausen 振荡条件**：
$$\boxed{|A\beta|=1, \quad \angle A + \angle \beta = 0^\circ}$$

> [!NOTE] RC 振荡器
> 由运放 + RC 相移网络（3 级 RC，每级 $60^\circ$，共 $180^\circ$）构成正反馈：
> - $\angle \beta = -180^\circ$（在特定频率）
> - $|A|=1$（运放设为单位增益）
> - $A\beta = -1 \Rightarrow |A\beta|=1$，满足振荡条件
> 详见 [[Amplifiers and Feedback]]。

### 5.3 滞回比较器（Hysteresis Comparator）

$$V_{\text{H}} = \frac{R_1}{R_1+R_2}V_{\text{SAT}}, \quad V_{\text{L}} = -\frac{R_1}{R_1+R_2}V_{\text{SAT}}$$

正反馈引入**滞回 (hysteresis)**：两个阈值 $V_H>V_L$，避免比较器在噪声附近的振荡（Schmitt Trigger）。

---

## 六、运放的二端口模型

### 6.1 闭环输入 / 输出电阻

| 电路 | $R_{\text{in,cl}}$ | $R_{\text{out,cl}}$ |
| :--- | :--- | :--- |
| **同相放大器** | $R_{\text{in}}(1+A\beta)$（极高）| $R_{\text{out}}/(1+A\beta)$（极低）|
| **反相放大器** | $R_1$ | $R_{\text{out}}(1+A)$（低）|
| **电压跟随器** | $\infty$ | $0$ |

> [!NOTE] 负反馈的普遍效果
> 负反馈（环路增益 $A\beta$）使输入阻抗**增加 $(1+A\beta)$ 倍**，输出阻抗**降低 $(1+A\beta)$ 倍**，同时将增益压低到 $1/\beta$（近似等于反馈网络的分压比）。

### 6.2 带宽扩展（Gain-Bandwidth Product, GBW）

开环增益 $A$ 与 $-3$ dB 带宽 $f_{-3dB}$ 的乘积是**常数**（运放的基本限制）：

$$\boxed{A\cdot f_{-3dB} = \text{GBW（常数）}}$$

- 同相放大器：闭环带宽 $f_{\text{cl}} = \dfrac{\text{GBW}}{A_{\text{cl}}}$
- 增益越高，带宽越窄（ tradeoff）

---

## 相关笔记

- [[Small Signal Circuit Representation]] —— 运放开环增益 / 输入输出阻抗的物理来源
- [[Impedance]] —— 运放的输入阻抗（虚断）与输出阻抗（负反馈降低）
- [[Frequency Response]] —— 运放 GBW / 带宽限制 / 相位补偿
- [[Filters]] —— Sallen-Key 有源滤波器（积分器是 LP 的特例）
- [[Diode]] —— 运放饱和时的削波（与二极管削波的联系）
- [[Large-Signal Model]] —— 运放的饱和模型（非线性特性）
- [[Amplifiers and Feedback]] —— 负反馈理论 / 振荡器（Barkhausen 条件）
- [[Complex Numbers and Euler's Formula]] —— 相量法在运放交流分析中的应用
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
