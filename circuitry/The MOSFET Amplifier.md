---
tags:
  - 电路学
  - 放大器
  - MOSFET
  - 课程笔记
date: 2026-09-08
aliases:
  - The MOSFET Amplifier
  - MOSFET 放大器
  - 共源放大器
  - 共漏放大器
  - 共栅放大器
  - Common-Source Amplifier
  - Source Follower
  - Common-Gate Amplifier
---

# The MOSFET Amplifier（MOSFET 放大器）

> [!NOTE] 本笔记定位
> 放大器的**完整分析**：从 [[Large-Signal Model|大信号直流偏置]]（确定 Q 点）到 [[Small Signal Circuit Representation|小信号交流分析]]（计算 $A_v$、$R_{in}$、$R_{out}$），覆盖共源 (CS)、共漏 (CD / Source Follower)、共栅 (CG) 三种经典组态。
> 三种组态是 [[Small Signal Circuit Representation]] 中参数汇总的具体实现。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、放大器的基本指标

| 指标 | 定义 | 理想值 |
| :--- | :--- | :--- |
| 电压增益 $A_v$ | $v_{\text{out}}/v_{\text{in}}$ | 越大越好 |
| 输入电阻 $R_{in}$ | $v_{\text{in}}/i_{\text{in}}$（看进去的阻抗） | $\infty$ |
| 输出电阻 $R_{out}$ | 从输出端看进去的戴维南电阻 | $0$ |
| 线性范围 | 输出不进入失真的最大输入摆幅 | 越大越好 |
| 功耗 $P$ | $V_{DD}\cdot I_D$ | 越小越好 |

> [!NOTE] 设计核心矛盾
> $|A_v|=g_mR_D$，而 $g_m=\sqrt{2KI_D}$——想高增益就要大电流，但大电流增加功耗。**增益–功耗–带宽**的折中是模拟电路设计的永恒主题。

---

## 二、共源放大器 (Common-Source Amplifier)

### 2.1 电路结构

![[cs_amplifier_stage.svg]]

| 端子 | 角色 | 特点 |
| :--- | :--- | :--- |
| 源极 (S) | 公共端（接地） | 输入输出的共同参考 |
| 栅极 (G) | 输入端 | 高阻抗（绝缘栅） |
| 漏极 (D) | 输出端 | 通过 $R_D$ 接 VDD |

### 2.2 直流偏置（大信号分析）

对电路列 KVL（$V_{SS}=0$）：
$$V_{DD} = I_D R_D + V_{DS}$$

MOSFET 饱和区方程（忽略沟道调制 $\lambda$）：
$$I_D = \frac{K}{2}(V_{GS} - V_t)^2$$

联立两式，在 $V_{GS}$ 已知时（偏置电路决定），可解出 $I_D$ 与 $V_{DS}$。

> [!TIP] 图解法
> 也可用 [[Analysis of Nonlinear Circuits|非线性电路图解法]] 中的**负载线**：直线 $I_D = -\frac{1}{R_D}V_{DS} + \frac{V_{DD}}{R_D}$ 与 MOSFET $I_D$–$V_{DS}$ 特性曲线族的交点即为 Q 点。

### 2.3 小信号参数（饱和区）

$$g_m = \frac{\partial i_D}{\partial v_{GS}}\Big|_Q = 2K(V_{GS}-V_t) = \frac{2I_D}{V_{GS}-V_t} = \sqrt{2KI_D}$$

$$r_o = \frac{1}{\lambda I_D} \quad(\text{沟道长度调制，}\lambda\neq 0\text{ 时保留})$$

### 2.4 电压增益

从栅–漏小信号方程：
$$\frac{v_{\text{out}}}{R_D} + \frac{v_{\text{out}}}{r_o} + g_m v_{\text{in}} = 0 \quad\Longrightarrow\quad \boxed{A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = -g_m\,(R_D\| r_o)}$$

> [!IMPORTANT] 负号 = 反相
> 共源放大器是**反相放大器**（$180^\circ$ 相移）。这是最常用的电压放大组态。

### 2.5 输入 / 输出电阻

$$\boxed{R_{in} = \infty \quad (\text{理想绝缘栅})}$$
$$\boxed{R_{out} = R_D \| r_o \approx R_D \quad (r_o \gg R_D)}$$

### 2.6 密勒效应（高频限制）

$C_{gd}$（栅–漏电容）在反向放大器中等效放大：
$$C_{\text{Miller}} = C_{gd}(1+|A_v|)$$

- 限制了输入端的高频响应
- 解决：[[Small Signal Circuit Representation#五-密勒效应]] 中用 **CG 共栅** 或 **cascode** 抑制密勒效应

---

## 三、共漏放大器 (Common-Drain / Source Follower)

### 3.1 电路特点

| 端子 | 角色 | 意义 |
| :--- | :--- | :--- |
| 漏极 (D) | 公共端（接 VDD） | AC 接地 |
| 栅极 (G) | 输入端 | 高阻抗 |
| 源极 (S) | 输出端 | 跟随栅压（略低 $V_t$） |

**核心功能：阻抗变换**——高输入阻抗、低输出阻抗，是优秀的缓冲级。

### 3.2 直流分析

$$V_{DD} = I_D R_S + V_{DS} + V_{GS} \quad(\text{源极有电阻 } R_S)$$

简化（无 $R_S$，$V_{DS}=V_{DD}-V_{GS}$）：
$$I_D = \frac{K}{2}(V_{GS} - V_t)^2, \quad V_{DS} = V_{DD} - V_{GS}$$

### 3.3 小信号增益

从源极输出的小信号方程：
$$\boxed{A_v \approx \frac{g_m R_S \| r_o}{1 + g_m R_S \| r_o} \approx 1 \quad (\text{当 } g_m R_S \gg 1\text{)})}$$

> [!TIP] "源极跟随器"的名称来源
> $v_{\text{out}} = v_S \approx v_G - V_t$——输出电压"跟随"输入电压（低 $V_t$ 偏移），且**同相**（无反相）。

### 3.4 输入 / 输出电阻

$$\boxed{R_{in} = \infty \quad (\text{绝缘栅})}$$
$$\boxed{R_{out} = \frac{1}{g_m} \| R_S \approx \frac{1}{g_m} \quad (\text{低输出阻抗})}$$

> [!NOTE] 阻抗变换的物理
> $R_{out}=1/g_m$ 典型值约 100Ω–1kΩ（$g_m=1$–$10\text{mS}$）。这比 $R_D$（通常 kΩ–10kΩ）小得多，能驱动更重的负载。

---

## 四、共栅放大器 (Common-Gate Amplifier)

### 4.1 电路特点

| 端子 | 角色 |
| :--- | :--- |
| 栅极 (G) | 公共端（AC 接地，通过大电容） |
| 源极 (S) | 输入端 |
| 漏极 (D) | 输出端 |

**核心优势：无密勒效应，高频性能好。**

### 4.2 电压增益

$$\boxed{A_v = g_m (R_D \| r_o) \quad (\text{同相放大})}$$

> [!NOTE] 共栅 vs 共源
> | 属性 | CS（共源） | CG（共栅） |
> | :--- | :--- | :--- |
> | $A_v$ | $-g_mR_D$（反相） | $+g_mR_D$（同相） |
> | $R_{in}$ | $\infty$（高） | $\approx 1/g_m$（低） |
> | 密勒效应 | 有（$C_{gd}$ 放大） | 无（$C_{gd}$ 直接接地） |
> | 高频性能 | 受密勒效应限制 | 更好 |

### 4.3 输入电阻

$$R_{in} \approx \frac{1}{g_m} \quad (\text{源极看进去的阻抗很低})$$

> [!WARNING] 共栅的输入阻抗问题
> 低 $R_{in}$ 是共栅的缺点——它需要低阻抗信号源驱动（或前置驱动级）。通常 CG 与 CS 级联（cascode）来兼顾两者优点。

---

## 五、Cascode 结构（级联 CS+CG）

把 CG（共栅）堆在 CS（共源）之上：

```mermaid
graph TD
    VDD["VDD"] --> RD["RD"]
    RD --> M2["M2 (CG)"]
    M2 --> M1["M1 (CS)"]
    M1 --> SS["VSS / GND"]
    subgraph ""
    G1["vin → G1"]
    S1["→ S1 (output)"]
    end
    M2 -.-> G1
    M1 -.-> S1
```

**Cascode 的好处：**
1. M2 的 $V_{DS}$ 几乎恒定（抑制密勒效应）——$C_{gd}$ 不再放大
2. M1 的 $V_{DS}$ 由 M2 偏置决定，更稳定
3. 高增益（CS 的 $g_m$ × CG 的高输出阻抗）

---

## 六、偏置电路：如何稳定 Q 点？

### 6.1 电流镜偏置（工业标准）

$$I_{REF} = I_D = \frac{K_1}{2}(V_{GS}-V_t)^2 \quad\Longrightarrow\quad I_D \text{ 与绝对 } V_t/K \text{ 解耦（相对稳定）}$$

详见 [[Current Sources and Mirrors]]。

### 6.2 源极负反馈电阻 $R_S$

加入 $R_S$ 后：
$$V_{GS} = V_{GG} - I_D R_S$$

负反馈自动调节 $I_D$——当 $I_D$ 偏大时，$I_DR_S$ 增大，$V_{GS}$ 减小，$I_D$ 回落。

**代价：** $R_S$ 降低交流增益（源极电阻不旁路时）。

---

## 七、三种组态总结与选型

| 应用需求 | 推荐组态 | 原因 |
| :--- | :--- | :--- |
| 通用电压放大 | CS（共源） | 高增益、适中 $R_{in}$ |
| 阻抗变换 / 缓冲 | CD（源极跟随器） | 高 $R_{in}$、低 $R_{out}$ |
| 高频 / 无密勒 | CG（共栅）或 Cascode | 无 $C_{gd}$ 放大 |
| 电流放大 | CG（共栅） | $R_{in}\approx 1/g_m$，可直接电流驱动 |

> [!NOTE] 模拟电路的"工具箱"
> CS / CD / CG 各有优劣，工程师根据需求组合使用。cascode（CS+CG）是最经典的组合之一——CS 提供增益，CG 提供高输出阻抗和抑制密勒效应。

---

## 相关笔记

- [[Large-Signal Model]] —— 直流偏置与 Q 点分析
- [[Small Signal Circuit Representation]] —— 三种组态的完整小信号参数表
- [[Small Signal Analysis]] —— BJT 侧放大器对比（$g_m$、$r_\pi$、$r_o$）
- [[MOSFET]] —— 器件物理（饱和区、三极管、截止）
- [[Current Sources and Mirrors]] —— 电流镜偏置（工业标准 Q 点稳定方案）
- [[Analysis of Nonlinear Circuits]] —— 负载线图解法（Q 点图解）
- [[First-Order Transients]] —— 放大器的瞬态响应与建立时间
- [[Resonance]] —— 高频放大器中的 LC 谐振（窄带放大器）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
