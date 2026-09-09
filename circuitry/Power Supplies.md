---
tags:
  - 电路学
  - 电源
  - 整流
  - 稳压
  - 占位笔记
date: 2026-09-08
aliases:
  - Power Supplies
  - 电源
  - 稳压电源
  - Linear Regulator
  - 线性稳压器
  - Switching Regulator
  - 开关稳压器
  - Voltage Regulator
  - 电压稳压器
  - LDO
  - 低压差线性稳压器
---

# Power Supplies（电源）

> [!NOTE] 本笔记定位
> 电源系统把交流市电（AC 220V）转换为电子器件所需的直流低压（DC 1.8V/3.3V/5V 等）。经典流程：**变压 → 整流 → 滤波 → 稳压**。本笔记串联 [[Diode]]（整流器/Zener 稳压器）、[[Capacitor]]（滤波电容）、[[Operational Amplifier]]（误差放大器）、[[Inductor]]（开关电源储能元件）等已有笔记，形成完整的电源设计链路。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、线性稳压电源架构

```
AC 220V → 变压器 → 整流桥 → 滤波电容 → 稳压器 → DC 输出
          (Step     (Diode    (Capacitor   (Regulator  (V_out
          down)     Bridge)   Smoothing)   LDO/LM317)  regulated)
```

### 1.1 各级功能与对应笔记

| 级 | 功能 | 对应笔记 |
| :--- | :--- | :--- |
| **变压器** | 降压 AC 220V → AC 低压 | [[Capacitive and Magnetic Devices]]（变压器原理）|
| **整流桥** | AC → 脉动 DC | [[Diode]] §3（半波/全波/桥式整流）|
| **滤波电容** | 脉动 DC → 较平滑 DC | [[Capacitor]]（纹波 $\Delta v = I/(fC)$）|
| **稳压器** | 平滑 DC → 精确 DC | [[Diode]] §5（Zener）/ 本笔记 |

### 1.2 线性稳压器 (Linear Regulator / LDO)

$$V_{\text{out}} = V_{\text{ref}} \cdot \left(1 + \frac{R_1}{R_2}\right)$$

- **原理**：误差放大器（[[Operational Amplifier]]）比较输出分压与基准电压 $V_{\text{ref}}$，调整串联调整管 (pass transistor) 使 $V_{\text{out}}$ 恒定
- **效率**：$\eta = V_{\text{out}} / V_{\text{in}}$（压差越大效率越低）
- **LDO (Low Dropout)**：调整管用 PMOS 或 PNP，压差可低至 50–200 mV

> [!WARNING] 线性稳压器的功耗
> $P_{\text{loss}} = (V_{\text{in}} - V_{\text{out}}) \times I_{\text{load}}$
> 大压差 + 大电流 = 大功耗 → 需散热器

---

## 二、开关稳压电源 (Switching Regulator)

### 2.1 Buck Converter（降压）

$$V_{\text{out}} = D \cdot V_{\text{in}}, \quad D = \frac{T_{\text{on}}}{T_{\text{on}}+T_{\text{off}}} \text{ (占空比)}$$

- **元件**：开关管（MOSFET）、续流二极管、[[Inductor]]（储能/滤波）、[[Capacitor]]（输出滤波）
- **效率**：$\eta \approx 90\%$–$95\%$（远高于线性稳压器）

### 2.2 Boost Converter（升压）

$$V_{\text{out}} = \frac{V_{\text{in}}}{1-D}$$

### 2.3 Buck-Boost（反相）

$$V_{\text{out}} = -\frac{D}{1-D} V_{\text{in}}$$

> [!NOTE] 开关电源 vs 线性电源
> | 特性 | 线性稳压器 | 开关稳压器 |
> | :--- | :--- | :--- |
> | 效率 | 30–60% | 85–95% |
> | 噪声 | 极低（无开关） | 较高（开关纹波 + EMI）|
> | 面积 | 小（IC only）| 大（需电感）|
> | 成本 | 低 | 较高 |
> | 应用 | 模拟/射频 | 数字/大功率 |

---

## 三、基准电压源 (Voltage Reference)

| 类型 | 原理 | 精度 | 温度系数 |
| :--- | :--- | :--- | :--- |
| **Zener 二极管** | 反向击穿 $V_Z$ | ±5% | $-2$ mV/°C |
| **带隙基准 (Bandgap)** | $V_{\text{ref}} = V_{BE} + K\cdot \Delta V_{BE}$ → $1.2$ V | ±1% | $10$–$50$ ppm/°C |
| **掩埋齐纳 (Buried Zener)** | IC 内部 Zener | ±0.05% | $1$–$5$ ppm/°C |

---

## 相关笔记

- [[Diode]] —— 整流桥 / Zener 稳压（电源入口级）
- [[Capacitor]] —— 滤波电容 / 纹波电压
- [[Inductor]] —— 开关电源储能电感
- [[Operational Amplifier]] —— 误差放大器
- [[Capacitive and Magnetic Devices]] —— 变压器（降压/隔离）
- [[DC-DC Converter]] —— 开关 DC-DC 变换器（进阶）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）

---

> [!WARNING] 本笔记为占位骨架
> 当前为框架占位，待深入学习后填充正文（LM317/LM78xx 应用电路、Buck/Boost 详细推导、PWM 控制、环路补偿等）。
