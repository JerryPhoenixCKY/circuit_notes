---
tags:
  - 电磁学
  - 电路学
  - 课程笔记
date: 2026-08-15
aliases:
  - 麦克斯韦方程组
  - 麦克斯韦方程
  - 麦克斯韦四大方程
  - 麦克斯韦四个方程
  - Maxwell Equations
  - Maxwell's Equations
---

# 麦克斯韦方程组 (Maxwell's Equations)

> [!IMPORTANT] 核心地位
> 麦克斯韦方程组是**经典电磁学的统一理论**，将电场与磁场、电荷与电流统一到四个方程之中。
> 电路理论（KCL、KVL、欧姆定律）是它在 [[Lumped Matter Discipline|集总事物理论 (LMD)]] 条件下的**简化近似**——先把电磁学搞清楚，才能理解电路为什么"能用几条代数方程"描述。

---

## 一、四大方程总览

|  #  | 定律                                     | 微分形式                                                                                                   | 积分形式                                                                                                                   | 物理意义          |
| :-: | :------------------------------------- | :----------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :------------ |
|  1  | **高斯定律** (Gauss's Law)                 | $\nabla \cdot \mathbf{E} = \dfrac{\rho}{\epsilon_0}$                                                   | $\displaystyle\oint \mathbf{E} \cdot d\mathbf{S} = \dfrac{q_{enc}}{\epsilon_0}$                                        | 电荷是电场的"源"     |
|  2  | **磁场高斯定律** (Gauss's Law for Magnetism) | $\nabla \cdot \mathbf{B} = 0$                                                                          | $\displaystyle\oint \mathbf{B} \cdot d\mathbf{S} = 0$                                                                  | 不存在磁单极子，磁感线闭合 |
|  3  | **法拉第电磁感应定律** (Faraday's Law)          | $\nabla \times \mathbf{E} = -\dfrac{\partial \mathbf{B}}{\partial t}$                                  | $\displaystyle\oint \mathbf{E} \cdot d\mathbf{l} = -\dfrac{\partial \Phi_B}{\partial t}$                               | 变化的磁场产生电场     |
|  4  | **安培-麦克斯韦定律** (Ampère–Maxwell Law)     | $\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\epsilon_0\dfrac{\partial \mathbf{E}}{\partial t}$ | $\displaystyle\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{enc} + \mu_0\epsilon_0\dfrac{\partial \Phi_E}{\partial t}$ | 电流与变化的电场产生磁场  |

> [!NOTE] 符号约定
> - $\mathbf{E}$：电场强度；$\mathbf{B}$：磁感应强度；$\mathbf{J}$：电流密度；$\rho$：电荷密度。
> - $\epsilon_0$：真空介电常数；$\mu_0$：真空磁导率。
> - $q_{enc}$ / $I_{enc}$：闭合曲面内净电荷 / 闭合回路包围的净电流。

---

## 二、预备知识：场论工具

在推导四个方程之前，先掌握三个核心工具，否则后面每一步都会"知其然而不知其所以然"。

### 1. 通量 (Flux) 与环流 (Circulation)

- **通量**：矢量场穿过某一曲面的"总量"。
$$\Phi_F = \int_S \mathbf{F} \cdot d\mathbf{S} = \int_S F\cos\theta\, dS$$

  > 物理直觉：想象水流过一个渔网。水流垂直于网面穿过最多（$\theta=0$），平行于网面穿过为零（$\theta=90°$）。电场通量、磁场通量同理。

- **环流**：矢量场沿闭合回路的"绕圈总量"。
$$\oint_C \mathbf{F} \cdot d\mathbf{l}$$

  > 物理直觉：沿环路走一圈，场对单位电荷做了多少功（电场），或场"包裹"了多少电流（磁场）。

### 2. 散度 (Divergence) 与旋度 (Curl)

- **散度** $\nabla \cdot \mathbf{F}$：某点"向外发散"的程度，是**标量**。正散度=源（向外喷），负散度=汇（向内吸）。
- **旋度** $\nabla \times \mathbf{F}$：某点"旋转"的程度，是**矢量**。方向由右手定则确定。

### 3. 两条积分定理（微分形式与积分形式的桥梁）

- **高斯散度定理**（把体积分与面积分联系起来）：
$$\int_V \nabla \cdot \mathbf{F}\, dV = \oint_S \mathbf{F} \cdot d\mathbf{S}$$

- **斯托克斯定理**（把面积分与线积分联系起来）：
$$\int_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S} = \oint_C \mathbf{F} \cdot d\mathbf{l}$$

> [!TIP] 微分形式 vs 积分形式
> - **微分形式**：描述"空间中每一点"的场行为，是局域定律。
> - **积分形式**：描述"某个区域/回路"的总体行为，是全局定律。
> - 两者通过散度定理、斯托克斯定理**严格等价**。做题时：对称性高的问题用积分形式（配高斯面/安培回路），逐点分布的问题才需要微分形式。

---

## 三、各方程详解（含推导与计算）

### 方程 1：高斯定律（电场）—— 电荷是电场的源

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \quad\Longleftrightarrow\quad \oint \mathbf{E} \cdot d\mathbf{S} = \frac{q_{enc}}{\epsilon_0}$$

#### ① 推导原理

出发点只有两条：**库仑定律** + **叠加原理**。高斯定律不是独立假设，而是库仑定律的积分形式重写。

#### ② 推导过程

**Step 1：点电荷的电通量与立体角**

点电荷 $q$ 在距离 $r$ 处的电场（库仑定律）：
$$\mathbf{E} = \frac{q}{4\pi\epsilon_0}\frac{\hat{\mathbf{r}}}{r^2}$$

取包围 $q$ 的任意闭合曲面 $S$，面元 $d\mathbf{S}$ 处的外法线单位向量为 $\hat{\mathbf{n}}$。穿过面元的电通量：
$$d\Phi_E = \mathbf{E}\cdot d\mathbf{S} = \frac{q}{4\pi\epsilon_0}\frac{\hat{\mathbf{r}}\cdot\hat{\mathbf{n}}}{r^2}\, dS$$

引入**立体角**：面元在电荷处张开的立体角元为
$$d\Omega = \frac{\hat{\mathbf{r}}\cdot\hat{\mathbf{n}}}{r^2}\, dS$$

于是
$$d\Phi_E = \frac{q}{4\pi\epsilon_0}\, d\Omega$$

对整个闭合曲面积分，点电荷在曲面内部时张开的**总立体角为 $4\pi$**（整个球面方向）：
$$\Phi_E = \oint_S \mathbf{E}\cdot d\mathbf{S} = \frac{q}{4\pi\epsilon_0}\cdot 4\pi = \frac{q}{\epsilon_0}$$

> [!NOTE] 点电荷在曲面外部时
> 电荷在闭合曲面外，从电荷出发的电场线**穿入再穿出**，净通量为零（立体角正负相消），$\Phi_E = 0$。

**Step 2：叠加原理推广到多电荷/连续分布**

多个电荷时电通量线性叠加，只有**曲面内部**的电荷贡献：
$$\Phi_E = \frac{1}{\epsilon_0}\sum_i q_{i,\ \text{inside}} = \frac{q_{enc}}{\epsilon_0}$$

**Step 3：微分形式**

用高斯散度定理把左边写成体积分：
$$\int_V \nabla\cdot\mathbf{E}\, dV = \frac{1}{\epsilon_0}\int_V \rho\, dV$$

因对**任意体积** $V$ 都成立，被积函数必相等：
$$\boxed{\nabla\cdot\mathbf{E} = \frac{\rho}{\epsilon_0}}$$

#### ③ 物理量计算方法

核心思路：**先找对称性 → 选合适高斯面 → 让 $\mathbf{E}$ 在面上处处等大且垂直于面 → 把积分变成乘法**。

适用场景（高对称性）：

| 电荷分布 | 对称性 | 高斯面选择 | 结果 |
| :--- | :--- | :--- | :--- |
| 点电荷 / 均匀带电球 | 球对称 | 同心球面 | $E = \dfrac{q}{4\pi\epsilon_0 r^2}$（球外） |
| 无限长带电直线 | 柱对称 | 同轴圆柱面 | $E = \dfrac{\lambda}{2\pi\epsilon_0 r}$ |
| 无限大带电平面 | 面对称 | 跨越平面的"药盒" | $E = \dfrac{\sigma}{2\epsilon_0}$ |
| 平行板电容器 | 面对称 | 板间药盒 | $E = \dfrac{\sigma}{\epsilon_0} = \dfrac{U}{d}$ |

#### ④ 例题

**例 1.1** 均匀带电球体，半径 $R$，总电荷 $Q$，求球内、球外电场。

- **球外 $(r > R)$**：取半径 $r$ 的同心球面为高斯面，由球对称知 $E$ 处处等大且沿径向。
$$E\cdot 4\pi r^2 = \frac{Q}{\epsilon_0} \Rightarrow E = \frac{Q}{4\pi\epsilon_0 r^2} \quad (\text{等效于点电荷})$$

- **球内 $(r < R)$**：高斯面内只包围部分电荷 $q_{enc} = \rho\cdot\frac{4}{3}\pi r^3$，其中 $\rho = \dfrac{Q}{\frac{4}{3}\pi R^3}$。
$$E\cdot 4\pi r^2 = \frac{\rho\cdot\frac{4}{3}\pi r^3}{\epsilon_0} \Rightarrow E = \frac{\rho r}{3\epsilon_0} = \frac{Q r}{4\pi\epsilon_0 R^3} \quad (\text{随 } r \text{ 线性增长})$$

**例 1.2** 无限长均匀带电直线，线电荷密度 $\lambda$，求距离 $r$ 处电场。

取半径为 $r$、高为 $L$ 的同轴圆柱高斯面。侧面 $E$ 等大且垂直（$E\cdot 2\pi r L$），上下底面 $E$ 平行于面（贡献为零）：
$$E\cdot 2\pi r L = \frac{\lambda L}{\epsilon_0} \Rightarrow \boxed{E = \frac{\lambda}{2\pi\epsilon_0 r}}$$

> [!IMPORTANT] 高斯定律的深层含义
> 电场线**始于正电荷、终于负电荷**（有源有汇）。这是"电荷是电场源"的几何表述。

---

### 方程 2：磁场高斯定律 —— 无磁单极子

$$\nabla \cdot \mathbf{B} = 0 \quad\Longleftrightarrow\quad \oint \mathbf{B} \cdot d\mathbf{S} = 0$$

#### ① 推导原理

与电场不同，磁场没有"磁荷"（磁单极子）。实验上：无论怎样切割磁铁，永远得到同时带 N/S 的磁铁，而非孤立磁极。

#### ② 推导过程

磁感线永远是**闭合曲线**（从 N 极出发、经外部空间回到 S 极、再经磁铁内部回到 N 极）。因此穿过任意闭合曲面的磁感线**穿入条数 = 穿出条数**，净磁通量恒为零：
$$\oint_S \mathbf{B}\cdot d\mathbf{S} = 0$$

对任意闭合曲面成立，用散度定理：
$$\int_V \nabla\cdot\mathbf{B}\, dV = 0 \quad\Rightarrow\quad \boxed{\nabla\cdot\mathbf{B} = 0}$$

> [!NOTE] 与高斯定律（电场）对比
> - 电场：$\nabla\cdot\mathbf{E} = \rho/\epsilon_0$（有源）
> - 磁场：$\nabla\cdot\mathbf{B} = 0$（无源）
> - 这反映了电与磁的**不对称性**——这正是麦克斯韦方程组的深刻之处：电场有单极（电荷），磁场没有。

#### ③ 物理量计算方法

磁场高斯定律主要用于**判断磁场分布合理性**与**磁通量守恒**（如变压器铁芯中磁通量沿闭合磁路守恒），计算上常与安培定律配合。

---

### 方程 3：法拉第电磁感应定律 —— 变化的磁场产生电场

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \quad\Longleftrightarrow\quad \oint \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial \Phi_B}{\partial t}$$

#### ① 推导原理

感应电动势有两个物理来源，法拉第定律统一描述两者。

#### ② 推导过程

**来源 A：动生电动势（导体在磁场中运动）**

导体棒以速度 $\mathbf{v}$ 在磁场 $\mathbf{B}$ 中运动，棒内自由电荷受到**洛伦兹力**：
$$\mathbf{F} = q(\mathbf{v}\times\mathbf{B})$$

这等价于电荷感受一个"非静电场"：
$$\mathbf{E}_{\text{非}} = \mathbf{v}\times\mathbf{B}$$

沿棒长 $L$ 积分得电动势：
$$\mathcal{E} = \int (\mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$$

当 $\mathbf{v}\perp\mathbf{B}$ 且棒垂直于两者时：
$$\boxed{\mathcal{E} = BLv}$$

> [!NOTE] 洛伦兹力是动生电动势的本质
> 这里"非静电力"就是洛伦兹力，它把正电荷从棒的一端搬运到另一端，形成电势差。

**来源 B：感生电动势（磁场随时间变化）**

法拉第实验发现：即使导体不动，只要穿过回路的磁通量变化，也会产生电动势。此时洛伦兹力无法解释（$v=0$），必须引入**感生电场（涡旋电场）** $\mathbf{E}_{\text{感}}$。法拉第总结出统一规律：

感应电动势 = 磁通量变化率的负值：
$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$

对任意回路，感应电动势就是感生电场沿回路的环流：
$$\oint \mathbf{E}\cdot d\mathbf{l} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\int_S \mathbf{B}\cdot d\mathbf{S}$$

**负号的物理意义**：**楞次定律 (Lenz's Law)** —— 感应电流的方向总是**反抗**磁通量的变化（本质是能量守恒：若感应电流助长变化，就会"无中生有"地产生能量）。

**Step 3：微分形式**

用斯托克斯定理（若回路不随时间变形，可把 $\frac{d}{dt}$ 移进积分号，对固定面积分得 $\frac{\partial}{\partial t}$）：
$$\int_S (\nabla\times\mathbf{E})\cdot d\mathbf{S} = -\int_S \frac{\partial\mathbf{B}}{\partial t}\cdot d\mathbf{S}$$

对任意曲面成立，故：
$$\boxed{\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}}$$

> [!IMPORTANT] 涡旋电场与静电场不同
> - 静电场（高斯定律）：$\nabla\times\mathbf{E}=0$，是无旋场，可定义电势。
> - 感生电场（法拉第定律）：$\nabla\times\mathbf{E}\neq 0$，是**涡旋场**，无势函数。这也是 [[Kirchhoff's Laws|KVL]] 在时变磁场下失效的根源——[[Lumped Matter Discipline|LMD]] 正是通过"磁通变化率为 0"这一假设回避了这个问题。

#### ③ 物理量计算方法

| 场景 | 公式 | 说明 |
| :--- | :--- | :--- |
| 导体棒切割磁感线 | $\mathcal{E} = BLv\sin\theta$ | $\theta$ 为 $v$ 与 $B$ 夹角 |
| 转动导体棒 | $\mathcal{E} = \frac{1}{2}B\omega L^2$ | 用平均速度 $\bar{v}=\omega L/2$ |
| 线圈在匀强磁场中转动 | $\mathcal{E} = NBS\omega\sin\omega t$ | 交流发电机原理 |
| 任意磁通量变化 | $\mathcal{E} = -N\dfrac{d\Phi_B}{dt}$ | 通用 |

#### ④ 例题

**例 3.1** $N$ 匝线圈，面积 $S$，在匀强磁场 $B$ 中以角速度 $\omega$ 匀速转动，求电动势。

设 $t=0$ 时线圈平面垂直于磁场，则磁通量 $\Phi_B = BS\cos\omega t$。由法拉第定律：
$$\mathcal{E} = -N\frac{d\Phi_B}{dt} = -N\frac{d}{dt}(BS\cos\omega t) = NBS\omega\sin\omega t$$

这就是**正弦交流电**的起源，峰值为 $E_m = NBS\omega$。

**例 3.2** 导体棒长 $L=0.5\ \text{m}$，在 $B=0.2\ \text{T}$ 的磁场中以 $v=10\ \text{m/s}$ 垂直切割，求电动势。

$$\mathcal{E} = BLv = 0.2\times 0.5\times 10 = 1.0\ \text{V}$$

---

### 方程 4：安培-麦克斯韦定律 —— 电流 + 变化的电场产生磁场

$$\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\epsilon_0\frac{\partial \mathbf{E}}{\partial t} \quad\Longleftrightarrow\quad \oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{enc} + \mu_0\epsilon_0\frac{\partial \Phi_E}{\partial t}$$

#### ① 推导原理（麦克斯韦的"神来之笔"）

**安培定律**（静态形式）：
$$\oint \mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{enc}$$

#### ② 推导过程——从安培定律到位移电流

**Step 1：发现矛盾**

考虑一个**正在充电的平行板电容器**，导线中有传导电流 $I$。取一个环绕导线的安培回路 $C$，再取两个都以 $C$ 为边界的曲面：

- **曲面 $S_1$**（穿过导线）：穿过传导电流 $I$，故 $\oint_C \mathbf{B}\cdot d\mathbf{l} = \mu_0 I$。
- **曲面 $S_2$**（穿过电容器两极板之间）：此处**没有传导电流**，故 $\oint_C \mathbf{B}\cdot d\mathbf{l} = 0$。

同一个环路积分却得到两个不同结果——**安培定律自相矛盾**！磁场的环流不应依赖曲面的选取。

**Step 2：麦克斯韦的修正——位移电流 (Displacement Current)**

麦克斯韦注意到：电容器充电时，极板间**电场在随时间变化**。极板间电场 $E = \dfrac{\sigma}{\epsilon_0} = \dfrac{Q}{\epsilon_0 S}$，电通量：
$$\Phi_E = E\cdot S = \frac{Q}{\epsilon_0}$$

其变化率：
$$\epsilon_0\frac{d\Phi_E}{dt} = \epsilon_0\frac{d}{dt}\left(\frac{Q}{\epsilon_0}\right) = \frac{dQ}{dt} = I$$

**恰好等于导线中的传导电流！** 麦克斯韦因此假设：变化的电场也像电流一样产生磁场，称为**位移电流**：
$$I_d = \epsilon_0\frac{d\Phi_E}{dt}$$

于是取曲面 $S_2$ 时，虽然传导电流为零，但位移电流 $I_d = I$ 恰好补上，矛盾消除。

**Step 3：推广为安培-麦克斯韦定律**

$$\oint \mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{enc} + \mu_0\epsilon_0\frac{d\Phi_E}{dt}$$

**Step 4：微分形式**

用斯托克斯定理，并将 $I_{enc}$ 写成电流密度积分：
$$\int_S (\nabla\times\mathbf{B})\cdot d\mathbf{S} = \mu_0\int_S \mathbf{J}\cdot d\mathbf{S} + \mu_0\epsilon_0\int_S \frac{\partial\mathbf{E}}{\partial t}\cdot d\mathbf{S}$$

对任意曲面成立：
$$\boxed{\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t}}$$

> [!IMPORTANT] 位移电流的本质
> 位移电流 $\mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t}$ **不是真实的电荷流动**，但它在"产生磁场"这一点上与传导电流完全等效。它的存在保证了**电荷守恒与安培定律的自洽**。

#### ③ 物理量计算方法

| 场景 | 公式 | 说明 |
| :--- | :--- | :--- |
| 无限长直导线 | $B = \dfrac{\mu_0 I}{2\pi r}$ | 用圆形安培回路 |
| 无限长螺线管内部 | $B = \mu_0 n I$ | $n$ 为单位长度匝数 |
| 环形螺线管（螺绕环） | $B = \dfrac{\mu_0 NI}{2\pi r}$ | $N$ 为总匝数 |
| 含位移电流的磁场 | 用安培-麦克斯韦定律 | 传导电流 + 位移电流 |

#### ④ 例题

**例 4.1** 无限长直导线载流 $I$，求距离 $r$ 处磁感应强度。

取半径为 $r$ 的圆形安培回路，由对称性 $B$ 处处等大且沿切向：
$$B\cdot 2\pi r = \mu_0 I \Rightarrow \boxed{B = \frac{\mu_0 I}{2\pi r}}$$

**例 4.2** 平行板电容器，极板面积 $S = 0.01\ \text{m}^2$，充电电流 $I = 1\ \text{A}$，求极板间位移电流与位移电流密度。

- 极板间电场：$E = \dfrac{Q}{\epsilon_0 S}$，变化率 $\dfrac{\partial E}{\partial t} = \dfrac{1}{\epsilon_0 S}\dfrac{dQ}{dt} = \dfrac{I}{\epsilon_0 S}$。
- 位移电流密度：$J_d = \epsilon_0\dfrac{\partial E}{\partial t} = \epsilon_0\cdot\dfrac{I}{\epsilon_0 S} = \dfrac{I}{S} = \dfrac{1}{0.01} = 100\ \text{A/m}^2$。
- 位移电流：$I_d = J_d\cdot S = 100\times 0.01 = 1\ \text{A}$，**恰好等于传导电流 $I$**。

> [!NOTE] 这一结论的意义
> 电容器极板间"没有电荷流过"，却有位移电流 $I_d = I$，所以极板间同样能激发磁场——这正是安培-麦克斯韦定律对静态安培定律的修正。

---

## 四、电荷连续性方程 (Charge Conservation)

$$\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t} \quad\Longleftrightarrow\quad \oint \mathbf{J} \cdot d\mathbf{S} = -\frac{\partial q}{\partial t}$$

#### ① 推导过程

对**安培-麦克斯韦定律**两边取散度：
$$\nabla\cdot(\nabla\times\mathbf{B}) = \mu_0\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})$$

左边恒为零（**任何矢量场的旋度的散度恒为零**，这是矢量恒等式 $\nabla\cdot(\nabla\times\mathbf{F})\equiv 0$）：
$$0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\frac{\partial}{\partial t}(\nabla\cdot\mathbf{E})$$

代入高斯定律 $\nabla\cdot\mathbf{E} = \dfrac{\rho}{\epsilon_0}$：
$$0 = \mu_0\nabla\cdot\mathbf{J} + \mu_0\epsilon_0\frac{\partial}{\partial t}\left(\frac{\rho}{\epsilon_0}\right) = \mu_0\nabla\cdot\mathbf{J} + \mu_0\frac{\partial\rho}{\partial t}$$

消去 $\mu_0$：
$$\boxed{\nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}}$$

#### ② 物理意义

流出某区域的电流 = 该区域内电荷的减少速率，即**电荷守恒**的微分表述。

> [!IMPORTANT] 它不是独立的第五条方程
> 连续性方程是**高斯定律 + 安培-麦克斯韦定律**的必然推论。反过来看：麦克斯韦之所以要在安培定律中加上位移电流项，**正是为了让它与电荷守恒自洽**——没有位移电流，两边取散度会得到 $\nabla\cdot\mathbf{J}=0$（电流无源），这与电容充电时电荷在极板上积累的实事矛盾。
>
> **电路中的体现**：它是 [[Lumped Matter Discipline|LMD]] 推导 **KCL** 的直接物理基础（节点处电荷不积累 $\Rightarrow$ 流入 = 流出）。

---

## 五、与电路理论的关系（关键过渡）

麦克斯韦方程组是**偏微分方程**，描述空间中每一点、每一时刻的场。直接用它解电路，复杂度不可接受。

[[Lumped Matter Discipline|集总事物理论 (LMD)]] 通过三条假设，把"场的问题"降维成"电路元件之间连线的问题"：

| 麦克斯韦方程 | LMD 假设 | 降维结果 |
| :--- | :--- | :--- |
| 法拉第定律 $\dfrac{\partial \Phi_B}{\partial t}$ | 元件外部磁通变化率为 0 | **KVL（基尔霍夫电压定律）** |
| 连续性方程 $\dfrac{\partial q}{\partial t}$ | 节点处电荷积累率为 0 | **KCL（基尔霍夫电流定律）** |

> [!TIP] 一句话总结
> **电路理论不是"新的物理"，而是麦克斯韦方程在特定约束下的工程近似。** 理解了这一点，KCL/KVL 就不再是死记硬背的规则，而是"场论在集总条件下的必然结果"。

---

## 相关笔记

- [[Lumped Matter Discipline]] —— LMD 三条假设与 KCL/KVL 的推导
- [[Kirchhoff's Laws]] —— KCL/KVL 的具体应用
- [[Complex Numbers and Euler's Formula]] —— 麦克斯韦方程在交流稳态下的频域形式（相量法）
- [[High School Electricity Review]] —— 高中静电/磁/感应定律的直观引入
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
