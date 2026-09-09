---
tags:
  - 电路学
  - 电源
  - DC-DC
  - 开关电源
  - 占位笔记
date: 2026-09-08
aliases:
  - DC-DC Converter
  - DC-DC 变换器
  - 直流-直流变换器
  - Buck Converter
  - 降压变换器
  - Boost Converter
  - 升压变换器
  - Buck-Boost Converter
  - 升降压变换器
  - Flyback Converter
  - 反激变换器
  - PWM
  - 脉宽调制
---

# DC-DC Converter（DC-DC 变换器）

> [!NOTE] 本笔记定位
> DC-DC 变换器把一个直流电压转换为另一个直流电压（升压/降压/反转），核心原理是**高频开关 + 电感储能 + 电容滤波**。相比线性稳压器（[[Power Supplies]]），效率可达 90%+，是大电流/大压差场景的首选。本笔记承上：[[Inductor]]（储能元件）/ [[Capacitor]]（滤波）/ [[MOSFET]]（开关管）；启下：PWM 控制、环路补偿、EMI 设计。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、三种基本拓扑

### 1.1 Buck（降压）

$$\boxed{V_{\text{out}} = D \cdot V_{\text{in}}, \quad 0 < D < 1}$$

| 状态 | 开关管 Q | 二极管 D | 电感 L |
| :--- | :--- | :--- | :--- |
| **$T_{\text{on}}$**（Q 导通）| ON | 截止 | $L$ 储能，$i_L$ 上升 |
| **$T_{\text{off}}$**（Q 截止）| OFF | 导通（续流）| $L$ 放能，$i_L$ 下降 |

> [!NOTE] 连续导通模式 (CCM)
> 电感电流在整个周期内不为零：$\Delta i_L = \frac{V_{\text{in}}-V_{\text{out}}}{L}\cdot D\cdot T = \frac{V_{\text{out}}}{L}\cdot(1-D)\cdot T$

### 1.2 Boost（升压）

$$\boxed{V_{\text{out}} = \frac{V_{\text{in}}}{1-D}, \quad 0 < D < 1}$$

- Q 导通时 $L$ 储能（$V_L = V_{\text{in}}$），Q 截止时 $L$ 放能叠加到 $V_{\text{out}}$（$V_L = V_{\text{in}} - V_{\text{out}} < 0$）

### 1.3 Buck-Boost（反相升降压）

$$\boxed{V_{\text{out}} = -\frac{D}{1-D} V_{\text{in}}}$$

- 输出极性反转（负电压），幅度可升可降

---

## 二、关键参数

| 参数 | 公式 / 说明 |
| :--- | :--- |
| **占空比 $D$** | $D = T_{\text{on}} / T_{\text{sw}}$（开关周期 $T_{\text{sw}} = 1/f_{\text{sw}}$）|
| **电感纹波电流 $\Delta i_L$** | $\Delta i_L = V_L \cdot D \cdot T_{\text{sw}} / L$ |
| **输出纹波电压 $\Delta v_{\text{out}}$** | $\Delta v_{\text{out}} \approx \Delta i_L / (8 f_{\text{sw}} C_{\text{out}})$ |
| **效率 $\eta$** | $\eta = P_{\text{out}} / P_{\text{in}} \approx 85$–$95\%$ |
| **开关频率 $f_{\text{sw}}$** | 典型 $100$ kHz – $2$ MHz（越高→电感越小但开关损耗越大）|

---

## 三、控制方式

### 3.1 PWM（脉宽调制）

- 固定开关频率 $f_{\text{sw}}$，调整占空比 $D$ 控制 $V_{\text{out}}$
- 误差放大器比较 $V_{\text{out}}$ 分压与 $V_{\text{ref}}$，生成误差信号 → PWM 比较器 → 栅极驱动

### 3.2 PFM（脉频调制）

- 固定占空比，调整开关频率（轻载时降频提高效率）

---

## 相关笔记

- [[Inductor]] —— 电感储能/释放（DC-DC 核心元件）
- [[Capacitor]] —— 输入/输出滤波电容（纹波）
- [[MOSFET]] —— 开关管（$R_{\text{on}}$ 影响导通损耗）
- [[Diode]] —— 续流二极管 / 同步整流
- [[Power Supplies]] —— 电源系统架构（DC-DC 是稳压级的一种选择）
- [[Energy and Charge Conservation]] —— 电感/电容能量交换
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）

---

> [!WARNING] 本笔记为占位骨架
> 当前为框架占位，待深入学习后填充正文（CCM/DCM 边界、小信号建模、环路补偿 Type I/II/III、EMI 滤波器设计等）。
