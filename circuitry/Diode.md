---
tags:
  - 电路学
  - 有源器件
  - 二极管
  - 整流
  - 课程笔记
date: 2026-09-08
aliases:
  - Diode
  - 二极管
  - 半导体二极管
  - Diode Characteristics
  - 二极管特性
  - PN Junction
  - PN结
  - Forward Bias
  - 正向偏置
  - Reverse Bias
  - 反向偏置
  - Rectifier
  - 整流器
  - Zener Diode
  - 齐纳二极管
  - 稳压二极管
  - Zener Regulator
  - 齐纳稳压
  - Clipping
  - 削波
  - Clamping
  - 钳位
  - Limiting
  - 限幅
---

# Diode（二极管）

> [!NOTE] 本笔记定位
> 二极管是**单向导电器件**：电流只能从阳极流向阴极，是模拟电子系统的"电子阀门"。它的两个核心应用——**整流**（把交流变直流）和**稳压**（Zener 二极管）——几乎存在于所有电源系统中。分析二极管电路的经典方法是**状态假设法 (Assumed-State Method)**：先假设二极管导通或截止，验证假设自洽，逐步求解。
> 承上：[[Large-Signal Model]]（PN 结的大信号行为）/ [[Capacitor]]（整流后滤波）；启下：[[Operational Amplifier]]（整流后信号的处理）/ [[Power Supplies]]（电源设计）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、二极管 I-V 特性

![[diode_iv.svg]]

> ![[diode_iv.svg]]
> **左：线性坐标**：正向导通（$V\approx 0.6$–$0.7$ V）、反向截至（$I\approx -I_S$）。**右：半对数坐标**：正向指数增长（斜率 $=1/(nV_T)$）、反向饱和电流 $I_S\approx 10^{-14}$ A。

### 1.1 肖克利二极管方程 (Shockley Diode Equation)

$$i_D = I_S\!\left(e^{\frac{v_D}{nV_T}} - 1\right)$$

| 符号 | 含义 | 典型值 |
| :--- | :--- | :--- |
| $I_S$ | 反向饱和电流 (reverse saturation current) | $10^{-12}$–$10^{-15}$ A（Si）|
| $n$ | 理想因子 (ideality factor) | $1$–$2$（理想二极管 $n=1$）|
| $V_T$ | 热电压 (thermal voltage) | $V_T = kT/q \approx 26$ mV @ 300 K |
| $k$ | 玻尔兹曼常数 | $1.38\times 10^{-23}$ J/K |
| $T$ | 绝对温度 (K) | ~300 K（室温）|
| $q$ | 电子电荷 | $1.6\times 10^{-19}$ C |

### 1.2 两个关键电压

| 状态 | 电压 | 物理含义 |
| :--- | :--- | :--- |
| **导通阈值 (Knee Voltage)** | $V_{\text{knee}} \approx 0.6$–$0.7$ V（Si）| 正向电压降超过此值，电流急剧上升 |
| **反向击穿电压** | $V_{\text{BR}} \approx -50$ V 及以下（取决于型号）| 反向电压超过此值，二极管击穿（Zener：稳压区） |

> [!NOTE] 温度对 $V_D$ 的影响
> $V_T = kT/q$ 随温度升高而增大，但 $I_S$ 随温度升高而**指数增长**（每升高 $10^\circ$C，$I_S$ 翻倍）。综合效果：正向压降 $V_D$ 随温度升高而**降低**（约 $-2$ mV/°C）—— 这正是二极管温度传感器的原理。

---

## 二、状态假设法 (Assumed-State Method)

> [!IMPORTANT] 状态假设法——分析含二极管电路的标准流程
> 1. **假设状态**：假设每个二极管是导通（ON）还是截止（OFF）
> 2. **列方程**：导通时 $V_D\approx 0.7$ V，截止时 $I_D\approx 0$
> 3. **验证假设**：检查假设与电路 KCL/KVL 是否自洽
> 4. **迭代**：若不自洽，切换假设状态，重新分析
> 5. **解电路**：代入正确的二极管模型，求各支路电流电压

### 2.1 二极管两种状态模型

| 状态 | 等效电路 | 条件 | 模型 |
| :--- | :--- | :--- | :--- |
| **导通 (ON)** | 短路 + 串联 $0.7$ V 电池 | $V_D > V_{\text{knee}}$（约 $0.6$–$0.7$ V）| $V_D \approx 0.7$ V，$I_D > 0$ |
| **截止 (OFF)** | 开路 | $V_D < 0$（或 $<0.7$ V 若不确定）| $I_D \approx 0$，$V_D$ 由外电路决定 |

### 2.2 单二极管电路实例

> [!EXAMPLE] 二极管 + 电阻 + 电压源
> - 电路：$V_S=5$ V → 串联 $R=1\text{k}\Omega$ → 二极管 D → 地
> - **假设 D 导通**：$V_D\approx 0.7$ V，$I_D = (5-0.7)/1\text{k}\Omega = 4.3$ mA $> 0$ ✓ 自洽
> - 结论：D 导通，$I_D=4.3$ mA，$V_D\approx 0.7$ V

> [!EXAMPLE] 二极管反向电压分析
> - 电路：$V_S=5$ V → 串联 $R=1\text{k}\Omega$ → 二极管 D（反向）→ 地
> - **假设 D 截止**：$I_D\approx 0$，电阻两端无压降，$V_D = -5$ V（全部电压加在 D 两端）$< 0$ ✓ 自洽
> - 结论：D 截止，$V_D = -5$ V

### 2.3 多二极管电路

> [!EXAMPLE] 两个二极管并联（OR 门逻辑）
> - 两个二极管 D1、D2 并联，各自有阳极电压 $V_1=3.3$ V、$V_2=5$ V，阴极共用输出
> - D2 先导通（$5 > 3.3$ V）：$V_{\text{out}} = 5 - 0.7 = 4.3$ V
> - D1 承受反向电压 $V_{D1} = 3.3 - 4.3 = -1.0$ V $\Rightarrow$ 截止 ✓

---

## 三、整流电路 (Rectifier)

整流是把**交流 (AC) 变成直流 (DC)** 的核心电路，是所有电源的入口级。

![[rectifier.svg]]

> ![[rectifier.svg]]
> **上排**：半波整流（只通过正半周期）/ 加滤波电容后
> **下排**：全波整流（双二极管桥式）/ 加滤波电容后

### 3.1 半波整流 (Half-Wave Rectifier)

$$v_{\text{out}} = \begin{cases} v_{\text{in}} - V_D & v_{\text{in}} > V_D \\ 0 & v_{\text{in}} \le V_D \end{cases}$$

- **利用率低**：只利用了输入信号的 $50\%$（半个周期）
- **纹波频率**：等于输入频率 $f$

### 3.2 全波整流 (Full-Wave Rectifier)

> [!EXAMPLE] 中心抽头 (Center-Tap) 全波整流
> 变压器次级中间抽头接地，两侧二极管交替导通：
> - 正半周期：D1 导通，电流从上抽头流出
> - 负半周期：D2 导通，电流从下抽头流出（方向相同）
> - 输出频率：输入频率的 **2 倍**（每半周期一个脉冲）

### 3.3 桥式整流 (Bridge Rectifier)

$$v_{\text{out}} = |v_{\text{in}}| - 2V_D \quad (\text{两只二极管串联})$$

- **无需中心抽头**：4 只二极管构成电桥
- **输出电压**：比半波/中心抽头低 $2V_D$（两只二极管压降）

### 3.4 滤波电容 (Smoothing Capacitor)

$$v_{\text{out}}(t) \approx V_{\text{peak}} - \frac{I_{\text{load}}}{C}\,t \quad (\text{放电期间})$$

> [!NOTE] 纹波电压 (Ripple Voltage)
> $$\Delta v_{\text{ripple}} \approx \frac{I_{\text{load}}}{f_{\text{ripple}}\cdot C}$$
> - 纹波与负载电流成正比、与电容容量和频率成反比
> - 电容越大，纹波越小（详见 [[Capacitor]] 与 [[Operational Amplifier]] 积分器）

---

## 四、削波与钳位电路

### 4.1 削波电路 (Clipper / Limiter)

削波把波形的**顶部或底部**截断，常用于保护电路（限制过压）：

![[diode_clipping.svg]]

> ![[diode_clipping.svg]]
> **左上：串联削波**（正向超 $0.7$ V 时导通）；**右上：并联削波**（效果相同）；**左下：双端削波**（上下限）；**右下：Zener 削波**（精确 $\pm V_Z$ 限幅）

> [!EXAMPLE] 二极管 + 齐纳二极管保护运放输入
> - 正常输入：$-V_Z < v_{\text{in}} < V_Z$，运放正常工作
> - 过压：$|v_{\text{in}}| > V_Z$，Zener 导通，电压被钳在 $\pm V_Z$

### 4.2 钳位电路 (Clamper)

钳位把波形**整体上移或下移**（改变直流电平），但不改变波形形状：

> [!NOTE] 钳位的原理
> - 电容 $C$ 在输入波形的正峰值时充电至 $V_{\text{peak}} - V_D$
> - 充电后，电容作为**直流电压源**工作，将波形整体偏移
> - 二极管确保电容只能充电、不能放电（单向导通）

| 类型 | 效果 |
| :--- | :--- |
| **正向钳位 (+ clamper)** | 波形整体上移，负峰值接地 |
| **负向钳位 (− clamper)** | 波形整体下移，正峰值接 $-V_{\text{DC}}$ |
| **偏置钳位** | 钳位电平可调（加直流偏置） |

---

## 五、齐纳二极管 (Zener Diode) 与稳压

### 5.1 Zener 稳压原理

![[zener_regulator.svg]]

> ![[zener_regulator.svg]]
> **左：Zener I-V 特性**：反向击穿区 $V_Z$ 几乎恒定；**右：稳压特性**：输入变化时，输出稳定在 $V_Z$

| 区域 | 条件 | 特性 |
| :--- | :--- | :--- |
| **正向导通** | $V_D > 0.6$ V | 同普通二极管 |
| **反向截至** | $0 < V_D < V_Z$ | $I_D \approx 0$ |
| **Zener 击穿 (稳压区)** | $V_D < -V_Z$ | $V_D \approx -V_Z$（恒定），$I_D$ 在 $I_{Z,\min}$–$I_{Z,\max}$ 范围 |
| **热击穿** | $I_Z > I_{Z,\max}$ | 二极管过热损坏 |

### 5.2 Zener 稳压电路

$$V_{\text{out}} \approx V_Z \quad (\text{稳压区工作时})$$

$$R_{\text{series}} = \frac{V_{\text{in}} - V_Z}{I_{\text{load}} + I_Z}$$

> [!NOTE] 设计要点
> 1. **$I_Z$ 不能太小**：$I_Z > I_{Z,\min} \approx 1$–$5$ mA 才能进入稳压区
> 2. **$I_Z$ 不能太大**：$I_Z < I_{Z,\max}$ 防止过热（$P_Z = V_Z\cdot I_Z$）
> 3. **输入电压必须足够高**：$V_{\text{in}} > V_Z + I_{\text{load}}R_{\text{series}}$

> [!EXAMPLE] 设计 5.1 V 稳压电源
> - 目标：$V_Z = 5.1$ V，$I_{\text{load}} = 10$ mA，$V_{\text{in}} = 12$ V
> - $R_{\text{series}} = (12 - 5.1) / (10 + 5) \text{mA} \approx 460\ \Omega$
> - $P_R = I^2 R = (15\text{mA})^2 \times 460\ \Omega \approx 0.1$ W（选 $0.25$ W 电阻）

### 5.3 Zener 的应用场景

| 应用 | 原理 |
| :--- | :--- |
| **基准电压源** | $V_Z$ 作为精密参考（TL431 更精确）|
| **输入过压保护** | 与负载并联，限制电压不超过 $V_Z$ |
| **电平转移** | 利用 $V_Z$ 产生不同的参考电平 |
| **浪涌抑制** | 吸收瞬态电压尖峰（TVS 二极管）|

---

## 六、特殊二极管

| 类型 | 符号 | 特性 | 应用 |
| :--- | :--- | :--- | :--- |
| **发光二极管 (LED)** | 带箭头发光 | $V_F \approx 1.8$–$3.5$ V（颜色决定）| 指示灯、显示器 |
| **光电二极管 (Photodiode)** | 反向偏置 + 光 | $I_D$ 与光强成正比 | 光传感器、光通信 |
| **肖特基二极管 (Schottky)** | 金属-半导体结 | $V_F \approx 0.2$–$0.4$ V（更低）| 高速整流、射频 |
| **变容二极管 (Varactor)** | 带 | $C$ 与反向电压相关 | 调谐电路、压控振荡器 (VCO) |
| **TVS 二极管** | 双向箭头 | 瞬态电压钳位 | 防雷、ESD 保护 |

---

## 相关笔记

- [[Large-Signal Model]] —— PN 结的大信号行为（二极管方程来源）
- [[Capacitor]] —— 整流后滤波电容（纹波电压公式）
- [[Operational Amplifier]] —— 运放输入保护（Zener 削波）
- [[Impedance]] —— 二极管动态电阻 $r_D = nV_T/I_D$（小信号参数）
- [[Filters]] —— Zener 稳压后的电源滤波
- [[Amplifiers and Feedback]] —— 电源中的反馈设计
- [[Power Supplies]] —— 线性稳压器与开关电源（进阶）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
