---
tags:
  - 电路学
  - 正弦稳态
  - 阻抗
  - 课程笔记
date: 2026-09-08
aliases:
  - Impedance
  - 阻抗
  - 阻抗分析
  - 复阻抗
  - Electrical Impedance
  - 复数阻抗
  - AC Resistance
  - 交流阻抗
---

# Impedance（阻抗）

> [!NOTE] 本笔记定位
> 正弦稳态分析的**核心工具**：把电阻的欧姆定律 $V=RI$ 推广到交流，引入**阻抗 $Z$**（复数），使 KVL/KCL 在频域成立，从而用熟悉的直流电路分析方法（串并联、分压分流、戴维南/诺顿）来分析交流电路。
> 承上：[[Sinusoidal Steady State]]（相量法基础）；启下：[[Frequency Response]]（传递函数）/ [[Filters]]（滤波器设计）/ [[Resonance]]（谐振）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、阻抗的定义

### 1.1 从欧姆定律推广

直流电路：$V = R\,I$

正弦稳态（相量形式）：$\boxed{\tilde{V} = Z\,\tilde{I}}$

其中 $Z$ 是**阻抗 (Impedance)**，单位欧姆 (Ω)。

> [!IMPORTANT] $Z$ 是复数
> $Z = R + jX$，含：
> - **实部 $R$**：电阻分量（耗能），与频率无关
> - **虚部 $X$**：电抗分量（储能/释能），与频率有关
> - **幅值 $|Z|$**：电压幅值与电流幅值之比
> - **相角 $\angle Z$**：电压相对于电流的相位差

### 1.2 三种基本元件的阻抗

![[impedance_frequency.svg]]

| 元件 | 阻抗 $Z$ | 幅值 $|Z|$ | 相角 $\angle Z$ | 物理含义 |
| :--- | :--- | :--- | :--- | :--- |
| **电阻 R** | $Z_R = R$ | $R$ | $0^\circ$ | 耗能元件，电流与电压同相 |
| **电容 C** | $Z_C = \dfrac{1}{j\omega C} = -\dfrac{j}{\omega C}$ | $\dfrac{1}{\omega C}$ | $-90^\circ$ | 储能元件，电流**超前**电压 90° |
| **电感 L** | $Z_L = j\omega L$ | $\omega L$ | $+90^\circ$ | 储能元件，电压**超前**电流 90° |

> [!NOTE] 频率对阻抗的影响
> ![[impedance_frequency.svg]]
> - **电容**：$\omega\uparrow \Rightarrow |Z_C|\downarrow$ → 高频时趋向短路（开路 $\omega\to 0$，短路 $\omega\to\infty$）
> - **电感**：$\omega\uparrow \Rightarrow |Z_L|\uparrow$ → 高频时趋向开路（短路 $\omega\to 0$，开路 $\omega\to\infty$）
> - **电阻**：与频率无关，始终 $Z_R=R$

### 1.3 导纳 (Admittance)

阻抗的倒数称为**导纳 (Admittance)** $Y$：
$$Y = \frac{1}{Z}, \quad Y = G + jB$$

| 元件 | 导纳 $Y$ |
| :--- | :--- |
| 电阻 | $Y_R = 1/R = G$ |
| 电容 | $Y_C = j\omega C$（纯虚，正电纳） |
| 电感 | $Y_L = 1/(j\omega L) = -j/(\omega L)$（纯虚，负电纳） |

> [!NOTE] 导纳视角下的并联分析
> 并联时用导纳相加更方便：$Y_{\text{eq}} = Y_1 + Y_2 + \cdots$（与直流电导并联形式完全相同）。

---

## 二、阻抗的串并联

### 2.1 串联

$$Z_{\text{eq}} = Z_1 + Z_2 + \cdots$$

> [!NOTE] 与电阻串联公式形式相同
> $Z$ 是复数，但加减规则相同：实部相加、虚部相加。

### 2.2 并联

$$\frac{1}{Z_{\text{eq}}} = \frac{1}{Z_1} + \frac{1}{Z_2} + \cdots \quad\Longleftrightarrow\quad Y_{\text{eq}} = Y_1 + Y_2 + \cdots$$

> [!TIP] 并联时用导纳 $Y$ 更简单
> - $R\parallel R$: $G_{\text{eq}}=G_1+G_2$
> - $C\parallel C$: $Y_C$ 直接相加 $\Rightarrow C_{\text{eq}}=C_1+C_2$（并联电容值相加）
> - $L\parallel L$: $Y_L$ 直接相加 $\Rightarrow 1/L_{\text{eq}} = 1/L_1 + 1/L_2$（与串联电感公式对偶）

### 2.3 串并联化简实例

> [!EXAMPLE] RC 串联 → 等效阻抗
> $Z_{RC} = R + \frac{1}{j\omega C} = R - \frac{j}{\omega C}$
> - 幅值：$|Z_{RC}| = \sqrt{R^2 + \left(\frac{1}{\omega C}\right)^2}$
> - 相角：$\angle Z_{RC} = -\arctan\!\left(\frac{1}{\omega RC}\right)$（电压滞后电流）

> [!EXAMPLE] RL 并联 → 等效阻抗
> $Y_{RL} = \frac{1}{R} + \frac{1}{j\omega L} = \frac{1}{R} - \frac{j}{\omega L}$
> - $|Z| = \dfrac{1}{\sqrt{(1/R)^2 + (1/(\omega L))^2}}$

---

## 三、分压与分流（频域形式）

### 3.1 分压公式

串联阻抗上，电压按阻抗幅值比例分配（注意：相角也各自不同）：

$$\tilde{V}_k = \tilde{V}_{\text{total}} \cdot \frac{Z_k}{Z_1+Z_2+\cdots}$$

> [!WARNING] 这里的除法是复数除法
> 幅值上：$|V_k| = |V_{\text{total}}|\cdot \dfrac{|Z_k|}{|Z_{\text{total}}|}$
> 相位上：$\phi_k = \phi_{\text{total}} + \angle Z_k - \angle Z_{\text{total}}$

### 3.2 分流公式

并联导纳上，电流按导纳幅值比例分配：

$$\tilde{I}_k = \tilde{I}_{\text{total}} \cdot \frac{Y_k}{Y_1+Y_2+\cdots} = \tilde{I}_{\text{total}} \cdot \frac{Z_{\text{eq}}}{Z_k}$$

> [!EXAMPLE] 电阻 $R$ 与电容 $C$ 并联的分流
> $\tilde{I}_R = \tilde{I}_{\text{total}} \cdot \dfrac{j\omega C}{1/R + j\omega C}$
> - 低频（$\omega\to 0$）：$Y_C\to 0$ → 电流几乎全部流经 $R$
> - 高频（$\omega\to\infty$）：$Y_C\to\infty$ → 电流几乎全部流经 $C$

---

## 四、阻抗三角形与功率

### 4.1 阻抗三角形

$$Z = R + jX \quad\Longrightarrow\quad |Z| = \sqrt{R^2+X^2}, \quad \theta_Z = \arctan\frac{X}{R}$$

在复平面上，$R$ 为横轴、$X$ 为纵轴，$Z$ 是从原点到点 $(R,X)$ 的向量。

### 4.2 复功率 (Complex Power)

$$S = \tilde{V}\,\tilde{I}^* = P + jQ$$

| 量 | 定义 | 含义 |
| :--- | :--- | :--- |
| **复功率 $S$** | $\tilde{V}\,\tilde{I}^*$（VA） | 总视在功率 |
| **有功功率 $P$** | $\Re\{S\}=|V||I|\cos\theta_Z$（W） | 实际消耗的功率（电阻耗能） |
| **无功功率 $Q$** | $\Im\{S\}=|V||I|\sin\theta_Z$（VAR） | 储能元件来回交换的功率 |
| **功率因数 $\cos\theta_Z$** | $P/|S|$ | 电压与电流相位差余弦 |

> [!NOTE] 功率的物理分解
> - **电阻**（$X=0$）：$P=|V||I|\cos 0 = |V||I|$，$Q=0$（全部转化为热能）
> - **电容/电感**（$R=0$）：$P=0$，$Q=|V||I|$（功率在电源与储能元件之间来回交换，不消耗）

> [!EXAMPLE] 计算 RC 串联电路的功率
> $Z = R - j/(\omega C)$，$\theta_Z = -\arctan(1/(\omega RC))$
> - $P = |V||I|\cos\theta_Z = |V|^2 \dfrac{R}{R^2+(1/\omega C)^2}$
> - $Q = |V||I|\sin\theta_Z = -|V|^2 \dfrac{1/\omega C}{R^2+(1/\omega C)^2}$（负无功 = 容性）

---

## 五、戴维南/诺顿等效（交流形式）

所有直流电路分析方法都适用于交流阻抗电路：

### 5.1 戴维南等效

$$\boxed{Z_{\text{Th}} = Z_{\text{oc}}/\tilde{I}_{\text{sc}}, \quad \tilde{V}_{\text{Th}} = \tilde{V}_{\text{oc}}}$$

其中 $\tilde{V}_{\text{oc}}$ 是开路电压相量，$\tilde{I}_{\text{sc}}$ 是短路电流相量。

### 5.2 最大功率传输（交流）

$$P_L = \frac{|\tilde{V}_{\text{Th}}|^2}{4R_{\text{Th}}}\quad\text{当 } R_L = R_{\text{Th}} \text{ 且 } X_L = -X_{\text{Th}}$$

> [!IMPORTANT] 交流最大功率条件
> 负载阻抗必须**共轭匹配**：$Z_L = Z_{\text{Th}}^*$（实部相等、虚部相反）
> 若只要求实部匹配（$R_L=R_{\text{Th}}$），则在电抗为零时成立。

---

## 六、阻抗分析实例：RC 低通滤波器

![[impedance_frequency.svg]]
> ![[filter_magnitude.svg]]（见 [[Filters]]）

输入 $v_{\text{in}}$ 加在 RC 串联电路上，输出 $v_{\text{out}}$ 取自电容两端：

$$H(j\omega) = \frac{\tilde{V}_{\text{out}}}{\tilde{V}_{\text{in}}} = \frac{Z_C}{R+Z_C} = \frac{1/j\omega C}{R+1/j\omega C} = \frac{1}{1+j\omega RC}$$

- $|H(j\omega)| = \dfrac{1}{\sqrt{1+(\omega RC)^2}}$ → 低频 $|H|\to 1$，高频 $|H|\to 0$（低通）
- $\angle H = -\arctan(\omega RC)$ → 输出相位滞后输入（电流超前电压）

> [!NOTE] 这正是 [[Filters]] 中一阶低通滤波器的传递函数

---

## 相关笔记

- [[Sinusoidal Steady State]] —— 相量法的引入（$\tilde{V}=Z\tilde{I}$ 的推导来源）
- [[Capacitor]] —— 电容阻抗 $Z_C=1/(j\omega C)$ 的物理解释
- [[Inductor]] —— 电感阻抗 $Z_L=j\omega L$ 的物理解释
- [[Frequency Response]] —— 传递函数 $H(j\omega)$ 与 Bode 图
- [[Filters]] —— 四种滤波器（LP/HP/BP/Notch）的传递函数与设计
- [[Resonance]] —— 串联/并联 RLC 的阻抗特性与谐振
- [[Maximum Power Transfer Theorem]] —— 交流阻抗的共轭匹配条件
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
