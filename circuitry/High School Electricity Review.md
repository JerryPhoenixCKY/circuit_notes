---
tags:
  - 电路学
  - 前置复习
  - 高中物理
  - 课程笔记
date: 2026-08-18
aliases:
  - 高中电学复习
  - 高中物理电学
  - 前置知识复习
  - 高中电学总结
  - 高中电磁学复习
  - High School Electricity Review
  - High School Physics Electricity
---

# 高中电学复习 (High School Electricity Review)

> [!NOTE] 本文件定位
> 在学习大学「电路原理」(6.002x) 之前的**前置知识复习总结**，系统回顾高中阶段接触的电学知识，作为衔接大学课程（[[Lumped Matter Discipline|集总事物理论]]、 [[Maxwell's Equations|麦克斯韦方程组]]、交流分析等）的地基。
> 高中电学以**定性理解 + 基本计算**为主；大学电路原理则是**系统化的定量分析**。前者是"认识现象"，后者是"建立方程"。

---

## 一、静电场 (Electrostatics)

### 1. 电荷 (Charge) 与库仑定律 (Coulomb's Law)

- **电荷**：物体带电的多少，单位库仑 (C)。自然界存在正、负两种电荷，**电荷守恒**。
- **元电荷**：$e = 1.6 \times 10^{-19}\ \text{C}$，所有电荷都是元电荷的整数倍。
- **库仑定律**（真空中的点电荷）：
$$F = k\frac{q_1q_2}{r^2},\qquad k = \frac{1}{4\pi\epsilon_0}\approx 9\times 10^9\ \text{N·m}^2/\text{C}^2$$

> [!TIP] 与大学课程的衔接
> 库仑定律是 [[Maxwell's Equations|麦克斯韦方程组]] 中**高斯定律**的源头。高中用点电荷公式，大学用通量积分 $\oint \mathbf{E}\cdot d\mathbf{S} = q/\epsilon_0$ 统一描述。

### 2. 电场 (Electric Field) 与电场强度

- **电场强度** $E = F/q$，单位 N/C 或 V/m。方向为正电荷受力方向。
- **电场线**：从正电荷出发、终止于负电荷，疏密表示场强大小，永不相交。
- **匀强电场**：$E = U/d$（平行板电容器）。

### 3. 电势 (Potential)、电势差 (Voltage) 与电势能

- **电势差（电压）** $U_{AB}=\varphi_A-\varphi_B$，单位伏特 (V)。沿电场线方向电势降低。
- **电场力做功**：$W_{AB}=qU_{AB}$，与路径无关（静电力是保守力）。
- **电势能** $E_p=q\varphi$。

> [!IMPORTANT] 高中"电势差" = 大学"电压 (Voltage)"
> 高中语境下的"电势差 $U$"就是电路分析中的"电压 $V$"。**电压本质是两点间的电势差**，这是连接高中静电学与大学电路理论的核心桥梁。

### 4. 静电平衡与导体特性

- 导体放入电场后，内部自由电子在电场力作用下移动，重新分布，**内部合场强为零**。
- 特性：① $E_{\text{合}}=0$；② 导体是**等势体**（$U_{\text{内}}=Ed=0$）；③ 电荷只分布在外表面；④ **静电屏蔽**（外不影响内，内能影响外）。

### 5. 电容 (Capacitor)

- **电容定义**：$C = Q/U$，单位法拉 (F)。换算：$1\ \text{F}=10^6\ \mu\text{F}=10^{12}\ \text{pF}$。
- **平行板电容器**：$C = \dfrac{\varepsilon_r S}{4\pi kd}=\dfrac{Q}{U}$，其中 $S$ 为正对面积，$d$ 为板间距，$\varepsilon_r$ 为相对介电常数。
- 电容是**储能元件**，存储电场能：$E = \dfrac{1}{2}CU^2 = \dfrac{Q^2}{2C} = \dfrac{1}{2}QU$。

> [!NOTE] 电容器动态分析
> - **U 不变（接电源）**：极板间距增大 $\Rightarrow C\downarrow\Rightarrow Q\downarrow\Rightarrow E\downarrow$（$E=U/d$，$U$ 不变而 $d\uparrow$ 故 $E\downarrow$）。
> - **Q 不变（断开电源）**：$C\downarrow\Rightarrow U\uparrow$，但 $E = \dfrac{Q}{\varepsilon_r S}\cdot 4\pi k$ **与 $d$ 无关**，$E$ 不变。

### 6. 带电粒子在电场中的运动

#### 6.1 加速电场（直线）

粒子从静止经电压 $U$ 加速：
$$qU = \frac{1}{2}mv^2 \Rightarrow v = \sqrt{\frac{2qU}{m}}$$
（运动学方法或能量方法均可）

#### 6.2 类平抛运动（偏转电场）

- **加速度**：$a = \dfrac{qU}{md}$（$d$ 为极板间距）
- **偏转位移**：
$$y = \frac{1}{2}at^2 = \frac{qUL^2}{2mdv_0^2},\qquad \tan\theta = \frac{v_y}{v_0} = \frac{qUL}{mdv_0^2}$$

> [!IMPORTANT] 偏转位移与比荷无关
> $y = \dfrac{U_2L^2}{4U_1d}$，**与粒子比荷 $q/m$ 无关**——这意味着不同荷质比的带电粒子在相同加速+偏转电场中有相同的偏转位移，是**示波管**的工作原理。

#### 6.3 等效重力场

电场与重力场叠加：将电场力与重力合力视为"等效重力"，带电粒子在复合场中的运动可等效为"重力场"中的运动。典型应用：**单摆模型**、**类单摆**。

---

## 二、恒定电流 (Direct Current)

### 1. 电流 (Current) 与电动势 (EMF)

- **电流**：$I = \dfrac{q}{t} = nqSv$（$n$ 为单位体积电荷数，$v$ 为漂移速度，$S$ 为横截面积），方向为正电荷定向移动方向。
- **电动势 (EMF)** $\mathcal{E}$：电源将其他形式能量转化为电能的本领，$\mathcal{E} = \dfrac{W_{\text{非}}}{q}$，数值上等于断路电压。
- **铭牌参数**：$1\ \text{A·h}=3600\ \text{C}$；$1\ \text{kWh}=3.6\times 10^6\ \text{J}$（**能量单位，不是电功单位**）。

### 2. 电阻与欧姆定律 (Ohm's Law)

- **电阻定义式**：$R = U/I$
- **电阻决定式**：$R = \rho\dfrac{l}{S}$（$\rho$ 为电阻率，与温度正相关）
- **欧姆定律（部分电路）**：$I = U/R$，仅适用于**纯电阻**。
- **U-I 图像**：线性元件为过原点直线（$k=R$）；小灯泡非线性（温度升高 $\rho\uparrow\Rightarrow R\uparrow$，曲线上凸）。

### 3. 闭合电路欧姆定律

$$I = \frac{\mathcal{E}}{R+r},\qquad U_{\text{外}} = \mathcal{E} - Ir$$

- **电源 U-I 特性曲线**：纵截距为 $\mathcal{E}$，横截距为短路电流 $I_{\text{短}}=\mathcal{E}/r$，斜率 $k=-r$。

### 4. 串并联电路

| 连接 | 电流 | 电压 | 等效电阻 |
| :--- | :--- | :--- | :--- |
| 串联 Series | $I$ 相同 | $U=U_1+U_2$ | $R=R_1+R_2$ |
| 并联 Parallel | $I=I_1+I_2$ | $U$ 相同 | $\dfrac{1}{R}=\dfrac{1}{R_1}+\dfrac{1}{R_2}$ |

### 5. 电功、电功率与焦耳定律

- **电功** $W=UIt=I^2Rt=\dfrac{U^2}{R}t$
- **电功率** $P=UI=I^2R=\dfrac{U^2}{R}$（纯电阻）
- **焦耳定律**：$Q=I^2Rt$
- **非纯电阻（电动机）**：$P_{\text{总}}=UI$，$P_{\text{热}}=I^2r$，$P_{\text{输出}}=P_{\text{总}}-P_{\text{热}}$，效率 $\eta=\dfrac{P_{\text{输出}}}{P_{\text{总}}}$

> [!IMPORTANT] 电源输出功率
> $P_{\text{输出}} = UI = \dfrac{\mathcal{E}^2}{R+r}-\left(\dfrac{\mathcal{E}}{R+r}\right)^2r$，当且仅当 $R_{\text{外}}=r$ 时 $P_{\text{输出}}$ 最大，$P_{\text{max}}=\dfrac{\mathcal{E}^2}{4r}$。

### 6. 电路实验专题

#### 6.1 电表读数规则

电表读数精度以"1"结尾，**往下估读一位**：
- 量程 0.6A $\Rightarrow$ 分度值 0.02A
- 量程 3A $\Rightarrow$ 分度值 0.1A
- 量程 3V $\Rightarrow$ 分度值 0.1V
- 量程 15V $\Rightarrow$ 分度值 0.5V

#### 6.2 伏安法测电阻（电流表内外接）

| 接法 | 测量值 | 误差来源 | 适用条件 |
| :--- | :--- | :--- | :--- |
| 内接法（电流表在内） | $R_{\text{测}}=R_X+R_A$ | 电流表分压，$R_{\text{测}}>R_{\text{真}}$ | $R_A\ll R_X$（大电阻） |
| 外接法（电压表在外） | $R_{\text{测}}=\dfrac{R_XR_V}{R_X+R_V}$ | 电压表分流，$R_{\text{测}}<R_{\text{真}}$ | $R_V\gg R_X$（小电阻） |

> [!TIP] 记忆口诀
> **大内偏大，小外偏小**：待测电阻**远大于**电流表内阻用内接法（测量值偏大）；**远小于**电压表内阻用外接法（测量值偏小）。
>
> **阻值已知时**：电流表内阻已知 $\Rightarrow$ 内接；电压表内阻已知 $\Rightarrow$ 外接。

#### 6.3 滑动变阻器接法

| 接法 | 电路特点 | 测量范围 | 适用场景 |
| :--- | :--- | :--- | :--- |
| 限流接法 | 变阻器与负载串联 | $\dfrac{R_X}{R_P+R_X}\mathcal{E}\sim\mathcal{E}$ | 大多数情况，$R_P\approx(3\sim 10)R_X$ |
| 分压接法 | 变阻器两端并联，输出电压从滑片取 | $0\sim\mathcal{E}$（全范围） | 需从 0 调、待测电阻 $\gg R_P$、描绘伏安特性曲线 |

#### 6.4 替代法测电阻

电路：待测电阻 $R_X$ 与电阻箱 $R_0$ 通过单刀双掷开关交替接入电路，保持电流表示数相同，则 $R_X=R_0$。

#### 6.5 半偏法测电表内阻

| 方法 | 电路 | 步骤 | 误差来源 | 结论 |
| :--- | :--- | :--- | :--- | :--- |
| **电流表半偏法** | 电流表与电阻箱并联，串联大电阻 | 先满偏 $\Rightarrow$ 并 $R_0$ 使半偏 $\Rightarrow R_A=R_0$ | 并联后总电阻减小，$I_{\text{总}}\uparrow$ | $R_{\text{测}}<R_{\text{真}}$ |
| **电压表半偏法** | 电压表与电阻箱串联 | 先满偏 $\Rightarrow$ 串 $R_0$ 使半偏 $\Rightarrow R_V=R_0$ | 串联后分压增大 | $R_{\text{测}}>R_{\text{真}}$ |

> 两种半偏法均需满足**变阻器阻值远大于电表内阻**以减小对总电路的影响。

#### 6.6 电桥法（惠斯通电桥）

平衡条件（检流计示数为零）：
$$\frac{R_1}{R_2} = \frac{R_3}{R_4} \quad\Leftrightarrow\quad U_{cd}=0,\ I_G=0$$

实际应用中，将 $R_3$ 换为标准电阻 $R_s$，$R_4$ 换为待测电阻 $R_X$，平衡时 $\dfrac{R_s}{R_X} = \dfrac{R_{2\text{左}}}{R_{2\text{右}}}$。

#### 6.7 测电源电动势和内阻

| 方法 | 电路 | 原理 | U-I 图像 |
| :--- | :--- | :--- | :--- |
| 伏安法（电流表内接） | 电流表相对电源内接 | $U=\mathcal{E}-I(r+R_A)$ | $\mathcal{E}_{\text{测}}=\mathcal{E}_{\text{真}}$，$r_{\text{测}}>r_{\text{真}}$ |
| 伏安法（电流表外接） | 电流表相对电源外接 | $U=\mathcal{E}-\left(I+\dfrac{U}{R_V}\right)r$ | $\mathcal{E}_{\text{测}}<\mathcal{E}_{\text{真}}$，$r_{\text{测}}<r_{\text{真}}$ |
| **安阻法** | 电流表 + 电阻箱 | $E=I(R+r)$，作 $1/I-R$ 图像（斜率 $=1/\mathcal{E}$，截距 $=r/\mathcal{E}$） | $\mathcal{E}_{\text{测}}=\mathcal{E}_{\text{真}}$，$r_{\text{测}}>r_{\text{真}}$ |
| **伏阻法** | 电压表 + 电阻箱 | $E=U\left(1+\dfrac{r}{R}\right)$，作 $1/U-1/R$ 图像 | $\mathcal{E}_{\text{测}}<\mathcal{E}_{\text{真}}$，$r_{\text{测}}<r_{\text{真}}$ |

#### 6.8 多用电表（欧姆档）

**原理电路**：电源 $\mathcal{E}$、调零电阻 $R_P$、表头 $G$、待测电阻 $R_X$ 串联。

- **机械调零**：指针指最左端（$I=0$）。
- **欧姆调零**：短接两表笔，调旋钮使指针指最右端（$R=0$）。
- **中值电阻**：$R_{\text{内}} = R_g+r+R_p$（当 $R_X=R_{\text{内}}$ 时指针指中央）。
- **读数规律**：欧姆表刻度**右密左疏**，每次换档均需重新调零。
- **电流红进黑出**：电流从红表笔流入多用电表，从黑表笔流出。
- **注意**：测电阻时必须**与其他电路断开**，手不能接触表笔触头。

### 7. 动态电路分析

滑动变阻器滑片移动时，电路各部分电流电压的变化。核心规律：**串反并同**（变化电阻与谁串联则其电流电压变化趋势相反；与谁并联则其电流电压变化趋势相同）。

> [!NOTE] 适用条件
> 只有一个电阻变化，且电源有内阻（内阻需等效计入）。

### 8. 电表改装

| 改装目标 | 电路 | 扩程电阻公式 | 说明 |
| :--- | :--- | :--- | :--- |
| 灵敏电流计 $\Rightarrow$ 电压表 | 灵敏电流计与 $R$ **串联** | $R=(n-1)R_g$（$n=U_{\text{总}}/U_g$） | 串联大电阻分压 |
| 灵敏电流计 $\Rightarrow$ 电流表 | 灵敏电流计与 $R$ **并联** | $R=\dfrac{R_g}{n-1}$（$n=I_{\text{总}}/I_g$） | 并联小电阻分流 |

> 记忆口诀：**串大，并小**（电压表串联大电阻，电流表并联小电阻）。

---

## 三、磁场 (Magnetic Field)

### 1. 磁场基础与磁感线

- 磁感线是闭合曲线，外部 N$\rightarrow$S，内部 S$\rightarrow$N。
- **安培定则（右手螺旋定则）**：判断通电直导线/环形电流周围的磁场方向。
- **地磁场**：地理北极 $\approx$ 地磁南极；赤道处 $B$ 平行地面；北半球 $B$ 斜向下。

### 2. 磁感应强度

$$B = \frac{F}{IL}\quad \text{（单位：特斯拉 T）}$$

方向：小磁针 N 极受力方向。

### 3. 安培力 (Ampère Force)

$$F_A = BIL\sin\theta,\quad \theta\text{ 为导线与磁场夹角}$$

- 方向由**左手定则**判断：四指 $\Rightarrow I$ 方向，掌心 $\Rightarrow B$ 穿入，大拇指 $\Rightarrow F$ 方向。
- **有效长度**：导线的起点到终点连线长度。

### 4. 洛伦兹力 (Lorentz Force)

$$F_{\text{洛}} = qvB\sin\theta$$

- 方向：正电荷由左手定则判断；**负电荷则方向相反**。
- 关键性质：$F_{\text{洛}}\perp v$，永不做功，只改变速度方向。

> [!TIP] 与大学课程的衔接
> 高中用"左手定则"记忆方向，大学用**叉积** $\mathbf{F}=q\mathbf{v}\times\mathbf{B}$ 统一表达。安培力的微观本质即洛伦兹力。

### 5. 带电粒子在磁场中的运动

仅受洛伦兹力 $\Rightarrow$ **匀速圆周运动**：

$$qvB = \frac{mv^2}{r} \Rightarrow r = \frac{mv}{qB},\qquad T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}$$

> [!IMPORTANT] 周期与半径的特点
> - **周期**：$T = \dfrac{2\pi m}{qB}$，**与速度 $v$ 无关**（速度大半径大，但周期相同）。
> - **半径**：$r = \dfrac{mv}{qB}$，**与速度 $v$ 有关**（速度越大，半径越大）。

#### 几何关系（直线边界入射）

入射角 $\theta$、弦长 $d$、半径 $r$ 的关系：$2r\sin\theta = d$，圆心角 $=2\theta$（入射偏转角）。

#### 磁场动态圆

| 类型 | 条件 | 特点 |
| :--- | :--- | :--- |
| **放缩圆** | $v$ 大小变，方向不变 | 圆心在入射方向的垂线上，半径随 $v$ 等比缩放 |
| **旋转圆（打板问题）** | $v$ 大小不变，方向变 | 圆心分布在以入射点为圆心、半径为 $r$ 的圆上 |
| **平移圆** | 入射点平移，$v$ 不变 | 轨迹圆平移 |
| **双磁场** | 两区域磁场强度不同 | 三点（两圆心 + 切点）共线，$B_1L_1 = B_2L_2$ |
| **圆形磁场** | 径向入/径向出 | 几何约束：$d^2+r^2=(R-r)^2$ |

### 6. 霍尔效应 (Hall Effect)

导体中电流方向与磁场垂直时，上下表面产生电势差：
$$U = \frac{BI}{nqd}$$

> [!NOTE] 霍尔效应的物理本质
> 洛伦兹力使载流子偏转，在横向积累形成电场，直至 $F_{\text{洛}}=F_{\text{电}}$ 达到平衡。
> - **导体**：载流子为电子，上表面积累**负电荷**。
> - **半导体**：载流子为正电荷（空穴），上表面积累**正电荷**。

### 7. 三大电磁应用装置

#### 速度选择器

电场 $E$ 与磁场 $B$ 垂直，只有速度 $v=E/B$ 的粒子能直线通过（与粒子种类无关）。

$$\boxed{qE = qvB \Rightarrow v = \frac{E}{B}}$$

> **只能单向工作**：从电、磁一方入射的特定速度粒子可选择。

#### 质谱仪

加速电场使粒子获得初速度，再进入磁场偏转：
$$r = \frac{mv}{qB} = \sqrt{\frac{2Um}{B^2q}} \propto \sqrt{\frac{m}{q}}$$

底片位置 $X=2r$，可测量**比荷** $q/m$。

#### 回旋加速器

- **最大动能**：$E_{\text{kmax}} = \dfrac{q^2B^2R^2}{2m}$（**与加速电压 $U$ 无关**！）。
- **回旋频率**：$f = \dfrac{qB}{2\pi m}$（与粒子比荷相关，不同粒子需调整频率）。
- 粒子的螺旋轨迹半径逐渐增大，最终达到盒半径 $R$。

> [!WARNING] 相对论效应
> 当 $v$ 接近光速时，$m$ 增大，周期变化，回旋加速器失效——这就是**同步加速器**出现的原因（MIT 6.002x 中会涉及）。

### 8. 磁聚焦与磁发散

- **磁发散**：带电粒子从圆形磁场圆心入射，$r=R$ 时各方向发散。
- **磁聚焦**：平行粒子束进入圆形磁场，$r=R$ 时汇聚于一点。
- **螺距**（螺旋线轴向位移）：$\Delta x = v_x\cdot T = v_x\cdot\dfrac{2\pi m}{qB}$。

### 9. 电磁组合场

#### 先电场后磁场

1. 电场中：类平抛 $\Rightarrow$ 求出射速度 $v$ 和偏角 $\theta$；
2. 磁场中：几何关系 $\Rightarrow$ 求半径 $r$，再求其他量。

---

## 四、电磁感应 (Electromagnetic Induction)

### 1. 磁通量 (Magnetic Flux)

$$\Phi = BS\cos\theta = BS_{\perp}$$

> [!TIP] 磁通量变化的两类来源
> - **面积变化**（$B$ 不变）：$\Delta\Phi = B\cdot\Delta S$
> - **磁场变化**（$S$ 不变）：$\Delta\Phi = \Delta B\cdot S$

### 2. 法拉第电磁感应定律 (Faraday's Law)

$$E = n\frac{\Delta\Phi}{\Delta t}$$

> [!IMPORTANT] 与大学课程的衔接
> 高中法拉第定律是 [[Maxwell's Equations|麦克斯韦方程组]] 中**法拉第定律积分形式** $\oint\mathbf{E}\cdot d\mathbf{l} = -\dfrac{\partial\Phi_B}{\partial t}$ 的特例。[[Kirchhoff's Laws|KVL]] 由"磁通变化率为零"这一 [[Lumped Matter Discipline|LMD 假设]] 导出——高中法拉第定律是大学 KVL 的理论根源。

### 3. 楞次定律 (Lenz's Law)

> 感应电流的方向，总是**阻碍**引起感应电流的磁通量的变化。

判断步骤：① 确定原磁场方向及增减 $\Rightarrow$ ② "增反减同"确定感应磁场方向 $\Rightarrow$ ③ 右手螺旋确定电流方向。

> 推广：**增缩减扩**（线圈面积趋向减小）、**来拒去留**（导体运动被阻碍）。

### 4. 导线切割磁感线

$$E = BLv\sin\theta\quad \text{（$v$ 与 $B$ 夹角为 $\theta$）}$$

方向由**右手定则**判断。

### 5. 电磁感应综合模型

#### 5.1 单杆切割（含外力）

| 待求量 | 方法 |
| :--- | :--- |
| $a(v)$ | 牛顿第二定律：$F-F_{\text{安}} = ma$，$F_{\text{安}} = \dfrac{B^2L^2v}{R+r}$ |
| $v_{\text{max}}$ | 稳态时 $a=0$，$F=F_{\text{安}}$ |
| $q$（电荷量） | 动量定理：$-F_{\text{安}}\cdot t = m\Delta v \Rightarrow BLq = m\Delta v$ |
| $x$（位移） | $q = \dfrac{BLx}{R+r}$ |
| $Q$（焦耳热） | 能量守恒：$W_{\text{外}} = Q + \Delta E_k$ |

> [!IMPORTANT] 核心方法论
> $a\Rightarrow$ 动力学；$Q\Rightarrow$ 能量观点；$v_{\text{末}}\Rightarrow$ 动量守恒/动量定理；$q,x,t\Rightarrow$ 动量定理（$x\Leftrightarrow q$，求 $x$ 先求 $q$）。

#### 5.2 含源切割（导体棒在磁场中切割 + 电源）

- 稳定条件：$E_{\text{反}} = 0$，即 $BLv = \mathcal{E}$，$v_{\text{max}} = \dfrac{\mathcal{E}}{BL}$。
- 电荷量仍由动量定理 $BLq = m(v_m-v_0)$ 求得。

#### 5.3 含容切割（导体棒 + 电容器）

- 电容器两端电压：$U_C = q/C = BLv$（稳态时 $U_C=\mathcal{E}$）。
- 联立 $\begin{cases}U_C = q/C = BLv\\ BLq = m(v_m-v_0)\end{cases}$ 解 $q$、$v$。

> 含容切割可形成**简谐运动**（安培力提供回复力），等效劲度系数 $k = \dfrac{B^2d^2}{L}$，周期 $T = 2\pi\sqrt{\dfrac{m}{k}}$。

#### 5.4 含感切割（导体棒 + 电感）

电感产生反向电动势 $\mathcal{E}_L = L\dfrac{\Delta I}{\Delta t}$，系统做**简谐运动**。

#### 5.5 旋转切割

导体棒绕轴旋转（角速度 $\omega$）切割磁感线：
- 盘状导体：$E = \dfrac{1}{2}B\omega L^2$
- 环形导体（内外半径）：$E = \dfrac{1}{2}B\omega(L_2^2-L_1^2)$

### 6. 双杆模型

#### 等长双杆（无外力）

- **动量守恒**：$m_1v_0 = (m_1+m_2)v_{\text{共}}$
- 稳定时 $v_1=v_2$（共速），电流为零，安培力为零。
- 总焦耳热：$Q = \dfrac{1}{2}m_1v_0^2 - \dfrac{1}{2}(m_1+m_2)v_{\text{共}}^2$

#### 不等长双杆

- 稳定时 $Bl_a v_a = Bl_b v_b$（$v_a$ 与 $v_b$ **成比例，不共速**）。
- 每根杆均需用动量定理：$-Bl_a q = m_a(v_a-v_{a0})$，$Bl_b q = m_b(v_b-0)$。

### 7. 自感现象 (Self-Induction)

$$\mathcal{E}_L = -L\frac{\Delta I}{\Delta t}$$

- **通电自感**：电流增大，自感电动势阻碍电流增大，灯泡后亮。
- **断电自感**：电流减小，自感电动势维持电流，灯泡缓缓熄灭。
- 电感特性：**通直流，阻交流；通低频，阻高频**（感抗 $X_L=2\pi fL$）。

---

## 五、交变电流 (Alternating Current)

### 1. 正弦交流电

- 瞬时值：$e = NBS\omega\sin\omega t$，$u=U_m\sin\omega t$
- **峰值**：$E_m=NBS\omega$（电容器击穿电压由峰值决定）
- **有效值**：$U=U_m/\sqrt{2}$（热效应等效）

> [!NOTE] 不同波形的有效值
> - 正弦半波：$I_{\text{有}}=I_m/2$
> - 矩形脉冲（脉宽 $t$，周期 $T$）：$I_{\text{有}}=\sqrt{t/T}\cdot I_m$

> [!TIP] 求电荷量用平均值
> $q = \bar{I}\cdot t = \dfrac{n\Delta\Phi}{R}$（注意：有效值代入不成立！）

### 2. 变压器 (Transformer)

$$\frac{U_1}{U_2} = \frac{n_1}{n_2},\qquad I_1n_1 = I_2n_2$$

- **能量损耗**：铜损（线圈发热）、铁损（涡流 $\Rightarrow$ 硅钢片）、漏损（漏磁 $\Rightarrow$ 闭合铁芯）。
- **等效电阻法**：将副边电阻 $R$ 等效到原边，$R_{\text{等效}} = \left(\dfrac{n_1}{n_2}\right)^2R$。

### 3. 远距离输电

$$\mathcal{E}_2 = U_3 + I_2r,\qquad P_r = I_2^2r = \left(\frac{P_2}{U_2}\right)^2r$$

> **减小输电损耗的方法**：① 减小导线电阻（$R=\rho L/S$）；② **提高输电电压**（最有效，降低电流）。

### 4. LC 电磁振荡电路

| 阶段 | 电容 | 电感 |
| :--- | :--- | :--- |
| 充电完毕 | $q=q_m$，$U$ 最大 | $i=0$，磁场能为零 |
| 放电过程 | $q\downarrow$，$i\uparrow$ | 电场能 $\rightarrow$ 磁场能 |
| 放电完毕 | $q=0$ | $i=i_m$，磁场能最大 |
| 充电过程 | $q\uparrow$，$i\downarrow$ | 磁场能 $\rightarrow$ 电场能 |

$$T = 2\pi\sqrt{LC}$$

> [!IMPORTANT] 充放电周期特性
> 一个周期内，电容器有**两次充放电**（电场能 $\leftrightarrow$ 磁场能往返两次）。

---

## 六、高中 → 大学 知识衔接对照表

| 高中概念 | 大学深化 |
| :--- | :--- |
| 电势差 $U$ | 电压 $V$（电路分析的基本变量） |
| 欧姆定律 $I=U/R$ | 一般本构关系 + 电容/电感动态关系 |
| 串并联电阻 | 节点/网孔 + [[Kirchhoff's Laws\|KCL/KVL]] 系统分析 |
| 左手定则 | 叉积 $\mathbf{F}=q\mathbf{v}\times\mathbf{B}$ |
| 法拉第定律 $E=n\dfrac{\Delta\Phi}{\Delta t}$ | [[Maxwell's Equations\|麦克斯韦方程]] + KVL 理论根源 |
| 交流有效值 | [[Complex Numbers and Euler's Formula\|相量法 + 阻抗 + 频域分析]] |
| 洛伦兹力永不做功 | $v$ 大则半径大、周期相同（回旋加速器基础） |
| 电磁振荡 $T=2\pi\sqrt{LC}$ | [[Complex Numbers and Euler's Formula\|阻抗]] $Z_L=j\omega L$，$Z_C=1/j\omega C$ |
| 电场能 $E=\frac{1}{2}CU^2$ | 电容储能，交流功率 $P=UI\cos\varphi$ 的无功分量 |
| 楞次定律（阻碍磁通变化） | [[Maxwell's Equations\|法拉第定律]]的负号（能量守恒体现） |

---

## 相关笔记

- [[cs6.002x.1]] —— 电路原理知识树（主笔记，衔接目标）
- [[Maxwell's Equations]] —— 高中静电/磁/感应定律的大学统一形式
- [[Lumped Matter Discipline]] —— 从"电磁场"到"电路"的桥梁
- [[Kirchhoff's Laws]] —— KCL/KVL（高中串并联规律的推广）
- [[Complex Numbers and Euler's Formula]] —— 高中交流电的数学工具升级
