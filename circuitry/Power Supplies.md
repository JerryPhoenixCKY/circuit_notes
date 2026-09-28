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

若可调稳压器把反馈脚稳定在 $V_{\text{ref}}$，且 $R_1$ 从输出接反馈脚、$R_2$ 从反馈脚接地，并忽略反馈脚电流，则
$$V_{\text{out}}\approx V_{\text{ref}}\left(1+\frac{R_1}{R_2}\right).$$

- **原理**：误差放大器（[[Operational Amplifier]]）比较输出分压与基准电压 $V_{\text{ref}}$，调整串联调整管 (pass transistor) 使 $V_{\text{out}}$ 恒定
- **效率**：$\eta=V_{\text{out}}I_{\text{load}}/[V_{\text{in}}(I_{\text{load}}+I_q)]$；仅在静态电流 $I_q$ 可忽略时近似为 $V_{\text{out}}/V_{\text{in}}$。
- **LDO (Low Dropout)**：低压差结构可用 PMOS、PNP 或其他调整管；最低压差取决于器件与负载电流，应查数据手册。

> [!WARNING] 线性稳压器的功耗
> $P_{\text{loss}}\approx(V_{\text{in}}-V_{\text{out}})I_{\text{load}}+V_{\text{in}}I_q$（简单串联稳压器近似）。
> 大压差 + 大电流 = 大功耗 → 需散热器

---

## 二、开关稳压电源 (Switching Regulator)

### 2.1 Buck Converter（降压）

以下三种拓扑的电压比均为**理想器件、稳态、连续导通模式**下的结果；损耗和断续导通会使实际结果偏离。

$$V_{\text{out}} = D \cdot V_{\text{in}}, \quad D = \frac{T_{\text{on}}}{T_{\text{on}}+T_{\text{off}}} \text{ (占空比)}$$

- **元件**：开关管（MOSFET）、续流二极管、[[Inductor]]（储能/滤波）、[[Capacitor]]（输出滤波）
- **效率**：通常在大压差时有机会高于线性稳压器；实际效率曲线须按输入、输出和负载查器件资料。

### 2.2 Boost Converter（升压）

$$V_{\text{out}} = \frac{V_{\text{in}}}{1-D}$$

### 2.3 Buck-Boost（反相）

$$V_{\text{out}} = -\frac{D}{1-D} V_{\text{in}}$$

> [!NOTE] 开关电源 vs 线性电源
> | 特性 | 线性稳压器 | 开关稳压器 |
> | :--- | :--- | :--- |
> | 效率 | 与电压比及静态电流有关 | 与拓扑、器件和负载有关 |
> | 噪声 | 极低（无开关） | 较高（开关纹波 + EMI）|
> | 面积 | 小（IC only）| 大（需电感）|
> | 成本 | 低 | 较高 |
> | 应用 | 模拟/射频 | 数字/大功率 |

---

## 三、基准电压源 (Voltage Reference)

| 类型 | 原理 | 设计时应核对 |
| :--- | :--- | :--- |
| **Zener 二极管** | 反向击穿附近钳位 | $V_Z$、工作电流、动态电阻、功耗和温度系数；温度系数的符号不固定 |
| **带隙基准 (Bandgap)** | 把负温度系数的 $V_{BE}$ 与正温度系数的 $\Delta V_{BE}$ 加权，常得到约 $1.2$ V | 初始精度、温漂、噪声与供电抑制 |
| **掩埋齐纳 (Buried Zener)** | 芯片内部击穿结作精密基准 | 修调后的精度、温漂、噪声、长期漂移与供电要求 |

精度和温漂没有适用于整类器件的固定数值，应从具体型号的数据手册按温度范围读取。

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
