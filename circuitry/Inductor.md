---
tags:
  - 电路学
  - 能量存储元件
  - 课程笔记
date: 2026-09-08
aliases:
  - 电感
  - 电感器
  - Inductor
  - Inductance
  - 磁通链
  - 绕组电感
---

# Inductor（电感）

> [!NOTE] 本笔记定位
> [[Two-Terminal Element Laws|二端元件定律]] 中的**储能元件**之一（对偶于 [[Capacitor|电容]]）。核心是**本构关系 (constitutive relation)** $\phi = Li$，以及由此导出的电压关系、串并联、储能与"电流不能突变"的**状态变量**特性。
> 与 [[Capacitor|电容]] 对偶；与 [[Energy and Charge Conservation|能量/电荷守恒]] 中的磁通守恒紧密关联。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、本构关系 (Constitutive Relation)

$$\phi = L\,i \qquad\text{(磁通链正比于电流)}$$

- $\phi$：**磁通链 (flux linkage)**，单位韦伯 (Wb)；物理上 $L = N^2\mu A/\ell$（螺线管）。
- 对时间求导得**电压–电流关系**（法拉第定律的直接形式）：
  $$v = \frac{d\phi}{dt} = L\,\frac{di}{dt}$$

> [!IMPORTANT] 一句话记忆
> **电感电压正比于"电流的变化率"**——电流不变（直流稳态）则电压为 0（短路）；电流变化越快，两端电压越大。

由此反解电流（含历史积分，说明电感**有记忆**）：
$$i(t) = i(t_0) + \frac{1}{L}\int_{t_0}^{t} v(\tau)\,d\tau$$

---

## 二、两个关键性质

### 2.1 电流不能突变（状态变量）

由 $i(t)=i(t_0)+\frac{1}{L}\int v\,dt$ 可知：除非两端出现**冲击电压**（无穷大），否则 $i_L$ 连续：
$$i_L(0^+) = i_L(0^-)$$
$i_L$ 称为电感的**状态变量 (state variable)**——它记住了"过去的磁通链历史"。

> [!TIP] 与电容对偶
> | 性质 | 电容 (Capacitor) | 电感 (Inductor) |
> | :--- | :--- | :--- |
> | 状态变量 | $v_C$ | $i_L$ |
> | 本构关系 | $q=Cv$ | $\phi=Li$ |
> | 导数形式 | $i=C\,dv/dt$ | $v=L\,di/dt$ |
> | 连续性 | $v_C$ 连续 | $i_L$ 连续 |
> | 直流稳态 | 开路 ($i=0$) | 短路 ($v=0$) |
> | 储能 | $E_C=\frac12Cv^2$ | $E_L=\frac12Li^2$ |

### 2.2 直流短路 / 交流高阻抗

- **直流稳态**：$di/dt=0 \Rightarrow v=0$ ⇒ 电感等效**短路**（理想导线）。
- **高频交流**：$|Z_L|=\omega L$ 很大 ⇒ 电感近似**开路**（阻断高频）。

---

## 三、串并联 (Series / Parallel)

![[inductor_parallel.svg]]
![[inductor_series.svg]]

| 连接 | 等效电感 | 记忆法 |
| :--- | :--- | :--- |
| **串联 Series** | $L_{\text{eq}} = L_1 + L_2 + \cdots$ | 磁通链相加（同一电流、磁通相加） |
| **并联 Parallel** | $\dfrac{1}{L_{\text{eq}}} = \dfrac{1}{L_1} + \dfrac{1}{L_2} + \cdots$ | 同一电压、各支路电流分流，$\frac{1}{L}$ 加和 |

> [!NOTE] 与电容串并联"正相反"
> 电感串联相加、并联取倒数和——与 [[Capacitor|电容]] 正好相反（因为电感的物理量是 $L$ 直接参与叠加，而电容是 $1/C$ 参与分压）。

---

## 四、储能 (Stored Energy)

电感把能量存在**磁场**里，理想电感不耗能：
$$E_L = \frac12 L i^2, \qquad p = v\,i = \frac{d}{dt}\!\left(\frac12 L i^2\right)$$

- 电流增大时从外电路吸收能量存入磁场；电流减小时释放。
- 与 [[Capacitor|电容]] 的电场能共同构成 **LC 振荡**（见下节）。

---

## 五、LC 振荡：磁场能与电场能的交换

把 [[Capacitor|电容]] 与电感并联构成 **LC 谐振腔 (tank)**：

- 电容放电 → 电流增大 → 电感存磁场
- 电感续流 → 电容反向充电 → 电场回升

$$\text{总电磁能量：}\quad E_{\text{tot}} = \tfrac12 C v^2 + \tfrac12 L i^2 = \text{const（守恒）}$$

详见 [[Energy and Charge Conservation|能量/电荷守恒]] 与 [[Second-Order Transients|二阶暂态]]。

---

## 六、耦合电感与互感 (Coupled Inductors / Mutual Inductance)

当两个线圈靠近时，一线圈电流变化产生的磁通会穿过另一线圈，产生**互感电压**：

$$v_2 = M\,\frac{di_1}{dt}, \qquad M = k\sqrt{L_1 L_2}$$

其中 $k\in[0,1]$ 是**耦合系数**，$k=1$ 为理想全耦合（[[Capacitive and Magnetic Devices|变压器]]）。

> [!NOTE] 变压器是耦合电感的直接应用
> 见 [[Capacitive and Magnetic Devices|电容与磁器件]]。

---

## 七、典型应用

| 应用 | 作用 | 关联笔记 |
| :--- | :--- | :--- |
| 滤波 (inductive choke) | 阻断高频、只让直流通过 | [[Filters]] |
| 储能释放 | 开关电源、Boost/Buck 转换器 | [[DC-DC Converter]] |
| 谐振 | 与 C 构成 LC 振荡回路 | [[Resonance]] / [[Second-Order Transients]] |
| 磁耦合 / 变压器 | 隔离、变压、阻抗匹配 | [[Capacitive and Magnetic Devices]] |
| 延迟 | 与 R 构成 RL 时间常数 | [[First-Order Transients]] |

---

## 相关笔记

- [[Two-Terminal Element Laws]] —— 电感的 $v=L\,di/dt$ 在 v–i 关系总表中
- [[Capacitor]] —— 对偶储能元件（电压连续、电场储能）
- [[Energy and Charge Conservation]] —— 磁通守恒 ⇒ 电流连续、磁场储能
- [[First-Order Transients]] —— RL 一阶暂态（时间常数 $\tau=L/R$）
- [[Second-Order Transients]] —— LC / RLC 二阶（与电容共振荡）
- [[Capacitive and Magnetic Devices]] —— 耦合电感 / 变压器的物理实现
- [[Resonance]] —— LC 能量守恒的频域表现（谐振）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
