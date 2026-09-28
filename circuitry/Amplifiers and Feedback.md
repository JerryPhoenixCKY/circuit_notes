---
tags:
  - 电路学
  - 放大器
  - 反馈
  - 课程笔记
date: 2026-09-08
aliases:
  - Amplifiers and Feedback
  - 放大器与反馈
  - 反馈理论
  - Negative Feedback
  - 负反馈
  - Positive Feedback
  - 正反馈
  - Barkhausen Criterion
  - 巴克豪森判据
  - Feedback Theory
---

# Amplifiers and Feedback（放大器与反馈）

> [!NOTE] 本笔记定位
> 反馈（feedback）把输出信号的一部分引回输入端，改变闭环行为。适当设计的**负反馈**可改善增益精度、线性度与带宽，但仍需保证稳定性；**正反馈**可用于迟滞或构成振荡条件。本笔记串联 [[Operational Amplifier]]、[[Small Signal Circuit Representation]] 与 [[The MOSFET Amplifier]] 中的反馈概念。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、反馈的基本概念

### 1.1 开环 vs 闭环

| 参数 | 开环 (Open-Loop) | 闭环 (Closed-Loop) |
| :--- | :--- | :--- |
| 增益 | $A$（可随频率和器件变化）| $A_{\text{cl}} = \dfrac{A}{1+A\beta}$（按下述模型）|
| 输入阻抗 | $R_{\text{in}}$ | 电压串联反馈的简化模型下约 $R_{\text{in}}(1+A\beta)$ |
| 输出阻抗 | $R_{\text{out}}$ | 电压取样的简化模型下约 $R_{\text{out}}/(1+A\beta)$ |
| 带宽 | 有限 | 单主极点且闭环稳定等条件下可随增益降低而扩展 |
| 线性度 | 差（依赖器件非线性）| 好（反馈压制非线性）|

### 1.2 反馈方程

$$\boxed{A_{\text{cl}} = \frac{A}{1 + A\beta}}$$

- 此式对应求和节点误差 $e=v_{in}-\beta v_o$、前向关系 $v_o=Ae$；$A$ 与 $\beta$ 可随频率变化。只有闭环稳定且 $|A\beta|\gg1$ 的频段才能进一步近似。
- $A$：开环增益（forward gain）
- $\beta$：反馈系数（feedback factor，输出→输入的比例）
- $A\beta$：环路增益（loop gain）
- 在稳定且 $|A\beta|\gg 1$ 的频段：$A_{\text{cl}} \approx 1/\beta$，增益主要由反馈网络决定。

---

## 二、负反馈的四大好处

> [!IMPORTANT] 负反馈的典型收益及条件
> 1. **Gain precision**（增益精度）：稳定且环路增益足够大时，$A_{\text{cl}}\approx1/\beta$，对开环增益变化不敏感。
> 2. **Bandwidth extension**（带宽扩展）：单主极点补偿的同相放大器可近似 $f_{\text{cl}}\approx\mathrm{GBW}/|A_{\text{cl}}|$；其他拓扑须看噪声增益和稳定性。
> 3. **Impedance change**（阻抗变化）：输入/输出阻抗的增减方向取决于串联或并联混合、输出取样方式，不能把同相电压放大器的结果套到所有电路。
> 4. **Linearity**（线性度）：在线性区且有足够环路增益的频段，反馈可压低前向通路失真；输出限幅时此近似失效。

---

## 三、正反馈与振荡

### 3.1 Barkhausen 振荡条件

$$\boxed{|A\beta| = 1, \quad \angle A + \angle \beta = 0^\circ \ (\text{或 } 360^\circ)}$$

该等式描述**某个频率上维持正弦振荡的必要环路条件**；能否起振还取决于启动时环路增益、极点位置与非线性限幅，不能仅凭它保证电路一定振荡。

> [!NOTE] RC 振荡器
> 反相增益级提供约 $180^\circ$，适当设计的 RC 网络在目标频率再提供约 $180^\circ$，总环路相位回到 $0^\circ$；各 RC 节点若互相加载，不能未经计算就把相移平均成“每级 $60^\circ$”。详见 [[Operational Amplifier]] §5.2。

### 3.2 迟滞比较器 (Schmitt Trigger)

正反馈引入**滞回 (hysteresis)**：两个阈值 $V_H > V_L$，避免比较器在噪声附近频繁翻转。以**反相施密特比较器**为例：输入 $v_i$ 接运放反相端，同相端经 $R_f$ 接输出、经 $R_g$ 接地；输出在 $\pm V_{sat}$ 间切换。定义 $\beta=R_g/(R_f+R_g)$，同相端电压为 $v_+=\beta v_o$，因此

$$V_H=+\beta V_{sat},\qquad V_L=-\beta V_{sat},\qquad \Delta V=V_H-V_L=2\beta V_{sat}.$$

输出为 HIGH 时，只有 $v_i$ **上升穿过 $V_H$** 才翻到 LOW；输出为 LOW 时，只有 $v_i$ **下降穿过 $V_L$** 才翻回 HIGH。$V_L<v_i<V_H$ 区间内，输出取决于之前状态。这是“有记忆的阈值”，而非两个独立的普通比较器。

若把反相端改接一个经 $R$ 从输出充放电的电容 $C$，电容电压在 $-\beta V_{sat}$ 与 $+\beta V_{sat}$ 之间往复，便形成松弛振荡器。假定理想对称饱和、无传播延迟，半周期和周期分别为

$$t_{1/2}=RC\ln\!\frac{1+\beta}{1-\beta},\qquad
T=2RC\ln\!\frac{1+\beta}{1-\beta}.$$

这是**RC 充放电加迟滞阈值**产生的时钟，与上节的正弦 RC 相移振荡器不同；RC 过程见 [[First-Order Transients]]。

**带偏置的施密特触发器。** 把待测 $v_i$ 接反相端；同相端的节点 $v_+$ 经 $R_1$ 接 $+V$、经 $R_2$ 接 $-V$、经 $R_f$ 接输出。输入电流忽略，输出先假定仅在 $+V$ 与 $-V$ 间切换。对 $v_+$ 列 KCL，得到两个**与当前输出状态相关**的阈值：

$$V_H=-V+2V\frac{R_2}{(R_1\parallel R_f)+R_2}\quad(v_o=+V;\ v_i\uparrow\text{ 时翻为低}),$$
$$V_L=-V+2V\frac{R_2\parallel R_f}{R_1+(R_2\parallel R_f)}\quad(v_o=-V;\ v_i\downarrow\text{ 时翻为高}).$$

其中 $R_a\parallel R_b=R_aR_b/(R_a+R_b)$；这两个式子**只适用于上述接线及输出电平假设**。例：$V=5\,\mathrm V$、$R_1=R_2=R_f=10\,\mathrm{k}\Omega$，则 $V_H\approx+1.67\,\mathrm V$、$V_L\approx-1.67\,\mathrm V$。检查极限 $R_f\to\infty$：两阈值都回到 $0\,\mathrm V$，即无迟滞的分压参考。真实器件若 $V_{OH}\ne+V$、$V_{OL}\ne-V$，应以实际输出电平重新对节点列 KCL，不能直接代入电源电压。

---

## 四、反馈拓扑

| 拓扑 | 输入采样 | 输出采样 | 效果 |
| :--- | :--- | :--- | :--- |
| 电压-串联 | 电压（并联）| 电压 | $R_{\text{in}}\uparrow,\ R_{\text{out}}\downarrow$（同相运放）|
| 电压-并联 | 电流（串联）| 电压 | $R_{\text{in}}\downarrow,\ R_{\text{out}}\downarrow$（反相运放）|
| 电流-串联 | 电压（并联）| 电流 | $R_{\text{in}}\uparrow,\ R_{\text{out}}\uparrow$（跨导放大器）|
| 电流-并联 | 电流（串联）| 电流 | $R_{\text{in}}\downarrow,\ R_{\text{out}}\uparrow$（电流放大器）|

---

## 相关笔记

- [[Operational Amplifier]] —— 运放是反馈的载体（七种基本电路都是反馈应用）
- [[Small Signal Circuit Representation]] —— 小信号增益 / 输入输出电阻的闭环分析
- [[The MOSFET Amplifier]] —— 晶体管放大器的偏置与反馈
- [[Large-Signal Model]] —— 饱和与非线性（反馈可线性化）
- [[Resonance]] —— LC 振荡腔与正反馈振荡器
- [[Diode]] —— 整流后稳压（Zener 也是简单的闭环反馈）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）

---

> [!NOTE] 后续深化
> 四种反馈拓扑的端口等效推导、频率相关环路增益与 Nyquist/Bode 稳定性、补偿方法仍需结合具体器件和电路单独展开。
