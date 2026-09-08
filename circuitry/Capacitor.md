---
tags:
  - 电路学
  - 能量存储元件
  - 课程笔记
date: 2026-09-07
aliases:
  - 电容
  - 电容器
  - Capacitor
  - Capacitance
  - 本构关系
  - 隔直电容
  - 旁路电容
---

# Capacitor（电容）

> [!NOTE] 本笔记定位
> [[Two-Terminal Element Laws|二端元件定律]] 中的**储能元件**之一。核心是**本构关系 (constitutive relation)** $q=Cv$，以及由此导出的电流关系、串并联、储能与"电压不能突变"的**状态变量**特性。
> 与 [[Inductor|电感]] 对偶，与 [[Energy and Charge Conservation|能量/电荷守恒]] 紧密关联。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、本构关系 (Constitutive Relation)

$$q = C\,v \qquad\text{(电荷正比于两端电压)}$$

- $C$：**电容值 (capacitance)**，单位法拉 (F)；物理上 $C=\dfrac{\varepsilon A}{d}$（平行板）。
- 对时间求导得**电流–电压关系**：
  $$i = \frac{dq}{dt} = C\,\frac{dv}{dt}$$

> [!IMPORTANT] 一句话记忆
> **电容电流正比于"电压的变化率"**——电压不变（直流稳态）则电流为 0（开路）；电压变化越快，电流越大。

由此反解电压（含历史积分，说明电容**有记忆**）：
$$v(t) = v(t_0) + \frac{1}{C}\int_{t_0}^{t} i(\tau)\,d\tau$$

---

## 二、两个关键性质

### 2.1 电压不能突变（状态变量）

由 $v(t)=v(t_0)+\frac{1}{C}\int i\,dt$ 可知：除非流过**冲击电流**（无穷大），否则 $v_C$ 连续：
$$v_C(0^+) = v_C(0^-)$$
$v_C$ 称为电容的**状态变量 (state variable)**——它记住了"过去的积分历史"。

> [!TIP] 与电感对偶
> 电容"电压连续" ⇄ 电感"电流连续"（见 [[Inductor]]）。这是动态电路 [[First-Order Transients|一阶暂态]] 的初始条件来源。

### 2.2 直流开路 / 交流导通

- **直流稳态**：$dv/dt=0 \Rightarrow i=0$ ⇒ 电容等效**开路**（隔直, **coupling / blocking**）。
- **高频交流**：$|Z_C|=1/(\omega C)$ 很小 ⇒ 电容近似**短路**（旁路, **bypass / decoupling**）。

---

## 三、串并联 (Series / Parallel)

![[capacitor_parallel.svg]]
![[capacitor_series.svg]]

| 连接 | 等效电容 | 记忆法 |
| :--- | :--- | :--- |
| **并联 Parallel** | $C_{\text{eq}} = C_1 + C_2 + \cdots$ | 同电压、面积相加 ⇒ 电容相加 |
| **串联 Series** | $\dfrac{1}{C_{\text{eq}}} = \dfrac{1}{C_1} + \dfrac{1}{C_2} + \cdots$ | 同电荷、总电压分压 ⇒ 倒数相加 |

> [!NOTE] 与电阻串并联"反着来"
> 电容并联相加、串联取倒数和——正好和 [[Resistive Networks|电阻]] 的串联相加 / 并联倒数和**相反**（因为电容是 $1/C$ 参与分压，类似电导 $G$）。

---

## 四、储能 (Stored Energy)

电容把能量存在**电场**里，理想电容不耗能：
$$E_C = \frac12 C v^2, \qquad p = v\,i = \frac{d}{dt}\!\left(\frac12 C v^2\right)$$

- 充电时从外电路吸收能量存入电场；放电时释放。
- 能量守恒角度见 [[Energy and Charge Conservation|能量 / 电荷守恒]]。

---

## 五、典型应用

| 应用 | 作用 | 关联笔记 |
| :--- | :--- | :--- |
| 隔直 / 耦合 (coupling) | 通交流、隔直流 | [[Small Signal Analysis]] |
| 旁路 / 去耦 (bypass/decoupling) | 给交流信号提供低阻通路、稳定电源 | [[The MOSFET Amplifier]] |
|  timing / 积分 | 与 $R$ 构成 RC 时间常数 | [[First-Order Transients]] |
| 滤波 (filter) | 与 $R/L$ 构成低通 / 高通 | [[Filters]] |
| 调谐 | 与 $L$ 构成谐振回路 | [[Resonance]] |

---

## 六、物理实现：MOS 栅电容（承上启下）

在 [[MOSFET|MOSFET]] 中，**栅极 – 氧化层 – 沟道**构成了一个平行板电容（详见 [[Capacitive and Magnetic Devices|电容与磁器件]]）。栅电容 $C_{ox}=\varepsilon_{ox}/t_{ox}$ 决定了器件的输入电容与开关速度，是数字与模拟电路速度的物理瓶颈之一。

---

## 相关笔记

- [[Two-Terminal Element Laws]] —— 电容的 $i=C\,dv/dt$ 在 v–i 关系总表中
- [[Inductor]] —— 对偶储能元件（电流连续、磁场储能）
- [[Energy and Charge Conservation]] —— 电荷守恒 ⇒ 电压连续、电场储能
- [[First-Order Transients]] —— RC 一阶暂态（时间常数 $\tau=RC$）
- [[Second-Order Transients]] —— LC / RLC 二阶（与电感共振荡）
- [[MOSFET]] / [[Capacitive and Magnetic Devices]] —— 栅电容等物理实现
- [[Resistive Networks]] —— 串并联化简（与电容"反着来"）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
