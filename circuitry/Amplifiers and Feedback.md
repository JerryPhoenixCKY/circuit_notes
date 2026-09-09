---
tags:
  - 电路学
  - 放大器
  - 反馈
  - 占位笔记
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
> 反馈（Feedback）是模拟电路设计的**核心思想**：把输出信号引回输入端，改变系统的闭环行为。**负反馈**使系统稳定、线性化、带宽扩展；**正反馈**导致振荡或迟滞。本笔记串联 [[Operational Amplifier]]（运放是反馈的载体）、[[Small Signal Circuit Representation]]（小信号增益/输入输出电阻）、[[The MOSFET Amplifier]]（晶体管放大器偏置）等已有笔记中的反馈概念，形成统一框架。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、反馈的基本概念

### 1.1 开环 vs 闭环

| 参数 | 开环 (Open-Loop) | 闭环 (Closed-Loop) |
| :--- | :--- | :--- |
| 增益 | $A$（大但不精确）| $A_{\text{cl}} = \dfrac{A}{1+A\beta}$（精确）|
| 输入阻抗 | $R_{\text{in}}$ | $R_{\text{in}}(1+A\beta)$（负反馈增大）|
| 输出阻抗 | $R_{\text{out}}$ | $R_{\text{out}}/(1+A\beta)$（负反馈减小）|
| 带宽 | $f_{-3\text{dB}}$ | $f_{-3\text{dB}}(1+A\beta)$（扩展）|
| 线性度 | 差（依赖器件非线性）| 好（反馈压制非线性）|

### 1.2 反馈方程

$$\boxed{A_{\text{cl}} = \frac{A}{1 + A\beta}}$$

- $A$：开环增益（forward gain）
- $\beta$：反馈系数（feedback factor，输出→输入的比例）
- $A\beta$：环路增益（loop gain）
- 当 $A\beta \gg 1$：$A_{\text{cl}} \approx 1/\beta$（增益仅由反馈网络决定）

---

## 二、负反馈的四大好处

> [!IMPORTANT] 负反馈的四大优势（记缩写 **G-B-I-O**）
> 1. **Gain precision**（增益精确）：$A_{\text{cl}}\approx 1/\beta$，不依赖 $A$
> 2. **Bandwidth extension**（带宽扩展）：$f_{\text{cl}} = \text{GBW}/A_{\text{cl}}$
> 3. **Input/Output impedance improvement**（阻抗改善）：$R_{\text{in}}\uparrow,\ R_{\text{out}}\downarrow$
> 4. **Linearity / Distortion reduction**（线性化）：非线性被环路增益压制

---

## 三、正反馈与振荡

### 3.1 Barkhausen 振荡条件

$$\boxed{|A\beta| = 1, \quad \angle A + \angle \beta = 0^\circ \ (\text{或 } 360^\circ)}$$

当环路增益幅值为 1 且总相移为 $0^\circ$ 时，系统自激振荡。

> [!NOTE] RC 振荡器
> 运放 + 3 级 RC 相移网络（每级 $60^\circ$，共 $180^\circ$）+ 反相运放（$180^\circ$）= $360^\circ$，满足 Barkhausen 条件。详见 [[Operational Amplifier]] §5.2。

### 3.2 迟滞比较器 (Schmitt Trigger)

正反馈引入**滞回 (hysteresis)**：两个阈值 $V_H > V_L$，避免比较器在噪声附近频繁翻转。

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

> [!WARNING] 本笔记为占位骨架
> 当前为框架占位，待深入学习 MIT 6.002x 对应章节后填充正文（反馈方程推导、四种拓扑详细分析、稳定性判据 Nyquist/Bode、补偿技术等）。
