---
tags:
  - 电路学
  - 动态电路
  - 暂态分析
  - 例题
date: 2026-10-18
updated: 2026-10-19
aliases:
  - Second-Order Circuit Worked Examples
  - 二阶电路例题
  - 二阶暂态例题
  - RLC Worked Examples
---

# Second-Order Circuit Worked Examples（二阶电路例题）

本笔记把 ECE 2001 Lecture 6 的换路、自然响应 (natural response)、阶跃响应 (step response) 与一般二阶电路练习串起来。通用公式、阻尼分类及系数表统一见 [[Second-Order Transients]]，这里保留电路图、关键推导、数值结果与检查方法。

**约定**：$t$ 以 s 计，所有结果针对 $t>0$；$u(t)$ 为单位阶跃。电路参考方向按各题原图，不能跨题沿用符号。$\dot x$ 表示对时间的一阶导数；$V_0,I_0$ 表示换路瞬间的电容电压与电感电流。

| 题目 | 练习重点 | 原讲义 |
| :--- | :--- | :--- |
| 例 1 | 初态连续，但导数须用新拓扑求 | pp.5–7 |
| 例 2 | 负电容电压、非状态量的初始导数 | pp.8–12 |
| 例 3 | 开关隔离电源后的串联自然响应 | pp.30–35 |
| 例 4 | 并联自然响应与参考方向 | pp.43–46 |
| 例 5 | 同一串联电路的三种阻尼；求电压与电流 | pp.48–53 |
| 例 6 | 并联电流阶跃、状态已有储能 | pp.54–56 |
| 例 7 | 双电感的 KVL 消元 | pp.58–61 |
| 运放例 | 两个电容的有源二阶系统 | pp.62–63 |

## 例 1：先求状态，再求斜率 (Initial Conditions)

![[l6-example-1.png|550]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=5|PDF p.5]]。开关原先闭合很久，$t=0$ 断开 $2\,\Omega$ 支路。$i$ 向右流经 L，$v_C$ 上正下负。*

换路前，L 短路、C 开路：

$$I_0=\frac{12}{4+2}=2\ \mathrm A,\qquad V_0=2I_0=4\ \mathrm V.$$

状态连续，所以 $i(0^+)=2\,\mathrm A$、$v_C(0^+)=4\,\mathrm V$。换路后只剩 $12\,\mathrm V$、$4\,\Omega$、$0.25\,\mathrm H$、$0.1\,\mathrm F$ 的串联回路：

$$\dot i(0^+)=\frac{12-4(2)-4}{0.25}=0\ \mathrm{A/s},$$

$$\dot v_C(0^+)=\frac{2}{0.1}=20\ \mathrm{V/s}.$$

稳定终态为 $i(\infty)=0$、$v_C(\infty)=12\,\mathrm V$。

**检查**：换路前 $\dot v_C(0^-)=0$，换路后变为 $20\,\mathrm{V/s}$；$v_C$ 连续不要求其导数连续。$0^+$ 的 KVL 为 $12=8+0+4$ V。

## 例 2：非状态量的初值与导数 (Non-State Output)

![[l6-example-2.png|620]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=8|PDF pp.8–12]]。电流源 $3u(t)\,\mathrm A$ 向上注入；$v_R$ 是左侧 $2\,\Omega$ 上端电压，$i_L$ 沿右侧电感向下；$v_C$ 取电容上正下负，电容下端接 $+20\,\mathrm V$。*

换路前电流源为零，右节点因 L 短路而为 0 V：

$$i_L(0^+)=0,\qquad v_C(0^+)=0-20=-20\ \mathrm V.$$

设 $v_o$ 为上方 $4\,\Omega$ 电阻左正右负的电压。$0^+$ 时有

$$v_R=v_o+v_C+20,\qquad 3=\frac{v_R}{2}+\frac{v_o}{4}.$$

代入 $v_C=-20$ 得 $v_o=v_R=4\,\mathrm V$，故

$$\dot i_L(0^+)=\frac{v_C(0^+)+20}{0.6}=0\ \mathrm{A/s},$$

$$\dot v_C(0^+)=\frac{3-v_R(0^+)/2-i_L(0^+)}{0.5}
=2\ \mathrm{V/s}.$$

对 $t>0$，左节点的 KCL 可化为

$$3v_R=v_C+32\ \mathrm V,$$

因此

$$\dot v_R(0^+)=\frac13\dot v_C(0^+)=\frac23\ \mathrm{V/s}.$$

稳定终态下，电感再次短路、电容开路，3 A 按 $2\,\Omega$ 与 $4\,\Omega$ 分流：

$$i_L(\infty)=3\frac{2}{2+4}=1\ \mathrm A,\qquad
v_C(\infty)=-20\ \mathrm V,\qquad v_R(\infty)=4\ \mathrm V.$$

**检查**：$v_R(0^+)$ 与终值相等，并不表示过程中恒定；它的初始斜率不为零。这里负的电容电压由所选极性决定，不是计算错误。

## 例 3：串联自然响应与相反的电容电流方向 (Series Natural Response)

![[l6-example-3.png|460]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=30|PDF pp.30–35]]。开关断开后，左侧电源与 $4\,\Omega$ 被隔离；右侧剩余回路的总电阻为 $3+6=9\,\Omega$。*

换路前的直流稳态给出

$$I_0=\frac{10}{4+6}=1\ \mathrm A,\qquad V_0=6I_0=6\ \mathrm V.$$

原图中 $i$ 流入 L，却流出电容正端，所以本题的关系是 $i=-C\dot v_C$，KVL 为

$$0.5\dot i+9i-v_C=0.$$

由此

$$\dot i(0^+)=\frac{6-9(1)}{0.5}=-6\ \mathrm{A/s}.$$

$L=0.5\,\mathrm H$、$C=0.02\,\mathrm F$，因此

$$\alpha=9\ \mathrm{s}^{-1},\quad\omega_0=10\ \mathrm{rad/s},\quad
\omega_d=\sqrt{19}\approx4.35890\ \mathrm{rad/s}.$$

令 $i=e^{-9t}(B_1\cos\omega_dt+B_2\sin\omega_dt)$，由两个初值得

$$B_1=1\ \mathrm A,\qquad B_2=\frac{-6+9}{\sqrt{19}}\ \mathrm A.$$

$$\boxed{i(t)=e^{-9t}\left(\cos\sqrt{19}t+\frac3{\sqrt{19}}\sin\sqrt{19}t\right)\ \mathrm A.}$$

**检查**：$i(0)=1$ A、$\dot i(0)=-6$ A/s、$i(\infty)=0$；根为 $-9\pm j\sqrt{19}\ \mathrm{s}^{-1}$，代入 $s^2+18s+100=0$ 成立。自由振荡频率是 $\sqrt{19}/(2\pi)\approx0.694$ Hz，不能把 $4.359$ rad/s 写成 $4.359$ Hz。

## 例 4：并联零输入响应 (Parallel Natural Response)

![[l6-example-4.png|620]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=43|PDF pp.43–46]]。开关闭合后，右侧 $50\,\Omega$、$0.4\,\mathrm H$、$20\,\mu\mathrm F$ 构成无源并联网络；左侧电源支路被理想短路与右侧动态网络隔开。*

换路前：

$$V_0=40\frac{50}{30+50}=25\ \mathrm V.$$

原图的电感电流参考方向向左，与换路前实际电流相反，故

$$I_0=-\frac{40-25}{30}=-0.5\ \mathrm A.$$

换路后按并联参考方向取电感电流从上节点流向参考节点：

$$\dot v_C(0^+)=-\frac{V_0/R+I_0}{C}
=-\frac{25/50-0.5}{20\times10^{-6}}=0\ \mathrm{V/s}.$$

$$\alpha=\frac1{2RC}=500\ \mathrm{s}^{-1},\qquad
\omega_0=\sqrt{125000}\ \mathrm{rad/s}<\alpha.$$

这是过阻尼。取慢根 $s_1=-500+\sqrt{125000}$、快根 $s_2=-500-\sqrt{125000}$，约为 $-146.4466,-853.5534\ \mathrm{s}^{-1}$：

$$v_C(t)=\frac{-25s_2}{s_1-s_2}e^{s_1t}
+\frac{25s_1}{s_1-s_2}e^{s_2t}.$$

数值形式为

$$\boxed{v_C(t)\approx(30.17767e^{-146.44661t}-5.17767e^{-853.55339t})\ \mathrm V.}$$

**检查**：精确系数之和为 25 V，初始斜率为零，终值为零。讲义先将根四舍五入为 $-146,-854$，因此其系数与保留精确根的结果略有差异。

## 例 5：串联阶跃的三种阻尼 (Three Damping Cases)

![[l6-example-5.png|570]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=48|PDF pp.48–53]]。$V_S=24\,\mathrm V$、$L=1\,\mathrm H$、$C=0.25\,\mathrm F$。开关原先闭合很久，$t=0$ 断开右侧 $1\,\Omega$ 支路。$i$ 流入电容电压 $v$ 的正端。*

换路前的串联负载为 $R+1\,\Omega$；换路后是标准串联 RLC：

$$I_0=\frac{24}{R+1}\ \mathrm A,\quad
V_0=(1\,\Omega)I_0,\quad
\dot v(0^+)=\frac{I_0}{0.25\,\mathrm F},\quad
v(\infty)=24\ \mathrm V.$$

这里 $R$ 的数值以 $\Omega$ 代入。换路后的方程为

$$\ddot v+R\dot v+4v=96,$$

其中导数系数在数值式中分别带有隐含的 $\mathrm{s}^{-1}$、$\mathrm{s}^{-2}$，$t$ 按 s 代入。物理形式是 $\ddot v+(R/L)\dot v+v/(LC)=V_S/(LC)$。

| $R$ | $v(0^+)$ | $i(0^+)$ | $\dot v(0^+)$ | $\alpha$ | 根 $s_{1,2}$，单位 $\mathrm{s}^{-1}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $5\,\Omega$ | 4 V | 4 A | 16 V/s | $2.5\,\mathrm{s}^{-1}$ | $-1,-4$，过阻尼 |
| $4\,\Omega$ | 4.8 V | 4.8 A | 19.2 V/s | $2\,\mathrm{s}^{-1}$ | $-2,-2$，临界阻尼 |
| $1\,\Omega$ | 12 V | 12 A | 48 V/s | $0.5\,\mathrm{s}^{-1}$ | $-0.5\pm j\sqrt{15}/2$，欠阻尼 |

三种情形的 $\omega_0$ 均为 $2\,\mathrm{rad/s}$。把相应的初值代入[[Second-Order Transients#5.2 通用系数表|系数表]]，得到以下电压和电流。

### $R=5\,\Omega$：过阻尼

$$\boxed{v(t)=\left(24-\frac{64}3e^{-t}+\frac43e^{-4t}\right)\ \mathrm V,}$$

$$\boxed{i(t)=C\dot v(t)=\left(\frac{16}3e^{-t}-\frac43e^{-4t}\right)\ \mathrm A.}$$

### $R=4\,\Omega$：临界阻尼

$$\boxed{v(t)=\left[24-19.2(1+t)e^{-2t}\right]\ \mathrm V,}$$

$$\boxed{i(t)=4.8(1+2t)e^{-2t}\ \mathrm A.}$$

这里 $1+t$、$1+2t$ 是按 $t$ 的秒数写出的数值表达；完整量纲分别为 $1+(1\,\mathrm{s}^{-1})t$、$1+(2\,\mathrm{s}^{-1})t$。

### $R=1\,\Omega$：欠阻尼

令 $\omega_d=\sqrt{15}/2\approx1.9364917\,\mathrm{rad/s}$。下面三角函数的自变量为 $\omega_dt$，系数取相应 SI 数值：

$$\boxed{v(t)=\left[24+e^{-t/2}\left(-12\cos\omega_dt+
\frac{42}{\omega_d}\sin\omega_dt\right)\right]\ \mathrm V,}$$

$$\boxed{i(t)=e^{-t/2}\left(12\cos\omega_dt+
\frac6{\omega_d}\sin\omega_dt\right)\ \mathrm A.}$$

其中正弦系数的数值分别为 $21.68871$ V 和 $3.09839$ A。

> [!WARNING] 原讲义频率笔误
> PDF pp.52–53 的特征根使用 $1.936j$，但后续三角函数多处写成 $19.36t$。正确角频率是 $\sqrt{15}/2\approx1.93649$ rad/s；其正弦系数应按同一频率重新求出。只检查初值和斜率不够，还须代入原 ODE。

**统一检查**：三种 $v,i$ 均满足 $i=0.25\dot v$、$\dot i+Ri+v=24$；初值与表格相符，$\dot i(0^+)=0$，终值为 $v=24$ V、$i=0$。由于换路前初态随 $R$ 改变，这三条曲线不能直接用来比较“同一初态下谁最快”。

## 例 6：并联电流阶跃与已有初态 (Parallel Step Response)

![[l6-example-6.png|620]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=54|PDF pp.54–56]]。开关原先断开，$t=0$ 闭合；$30u(-t)$ V 同时从 30 V 变为 0 V。右侧两个 $20\,\Omega$ 对动态网络等效并联。$i$ 沿电感向下，$v$ 上正下负。*

换路前，电感由左侧电流源维持 $I_0=4$ A；右侧电容由两只相等电阻分压充到 $V_0=15$ V。换路后

$$R=20\parallel20=10\,\Omega,\quad L=20\,\mathrm H,\quad
C=8\,\mathrm{mF},\quad I_S=4\,\mathrm A.$$

$$i(0^+)=4\ \mathrm A,\qquad
\dot i(0^+)=\frac{15}{20}=0.75\ \mathrm{A/s},\qquad i(\infty)=4\ \mathrm A.$$

$$\alpha=\frac1{2RC}=6.25\ \mathrm{s}^{-1},\qquad
\omega_0=\frac1{\sqrt{LC}}=2.5\ \mathrm{rad/s}.$$

令 $s_s=-6.25+\sqrt{6.25^2-2.5^2}$ 为慢根，$s_f=-6.25-\sqrt{6.25^2-2.5^2}$ 为快根，分别约为 $-0.5217804,-11.9782196\ \mathrm{s}^{-1}$。定义

$$K=\frac{0.75\ \mathrm{A/s}}{s_s-s_f}\approx0.06546537\ \mathrm A.$$

则精确形式为

$$\boxed{i(t)=4\ \mathrm A+K(e^{s_st}-e^{s_ft}),\qquad
v(t)=LK(s_se^{s_st}-s_fe^{s_ft}).}$$

数值形式：

$$i(t)\approx\left[4+0.0654654(e^{-0.521780t}-e^{-11.978220t})\right]\ \mathrm A,$$

$$v(t)\approx(15.68317e^{-11.978220t}-0.68317e^{-0.521780t})\ \mathrm V.$$

两只 $20\,\Omega$ 上的向下支路电流相同，**每只**均为

$$i_R(t)=\frac{v(t)}{20\,\Omega}
\approx(0.784159e^{-11.978220t}-0.034159e^{-0.521780t})\ \mathrm A.$$

**检查**：$i(0)=4$ A、$\dot i(0)=0.75$ A/s、$v(0)=15$ V，且 $2i_R+C\dot v+i=4$ A；$\dot v(0^+)=(4-15/10-4)/0.008=-187.5$ V/s。$i$ 的初值和终值虽然相同，中间仍有暂态。

> [!WARNING] 原讲义小数点勘误
> PDF p.56 的最终电流式写有 $0.655$，与前页求得的约 $0.0655$ 以及 $v=L\dot i$ 不一致；正确量级为 $0.0655$ A。每只 $20\,\Omega$ 支路的慢项系数约为 $-0.0342$ A；页面中的 $-0.342$ 亦有小数点问题，并附有更正标注。上式采用未提前舍入的根重算。

## 例 7：双电感一般二阶电路 (Two-Inductor Circuit)

![[l6-example-7.png|460]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=58|PDF pp.58–61]]。两个电感 $L_1=0.5$ H、$L_2=0.2$ H，因中间有 $1\,\Omega$ 分流支路而不能串联合并。两个网孔电流 $i_1,i_2$ 顺时针，输出 $v_o$ 为 $1\,\Omega$ 上正下负的电压。*

对于 $t>0$，保留全部电阻与电感，列 KVL：

$$0.5\dot i_1+3i_1+(i_1-i_2)=7,$$

$$0.2\dot i_2+(i_2-i_1)=0,\qquad v_o=(1\,\Omega)(i_1-i_2).$$

换路前输入为零且已稳态，故 $i_1(0)=i_2(0)=0$，由新拓扑得 $\dot i_1(0)=14$ A/s、$\dot i_2(0)=0$。稳态两电感短路，$i_1(\infty)=i_2(\infty)=7/3$ A、$v_o(\infty)=0$。

按 SI 数值消元，第一式给出 $i_2=4i_1+0.5\dot i_1-7$；代入第二式得到

$$\boxed{\ddot i_1+13\dot i_1+30i_1=70.}$$

其中各数值系数携带使方程量纲一致的 SI 单位。齐次特征式为

$$s^2+13s+30=(s+3)(s+10)=0.$$

代入初值与终值得

$$\boxed{i_1(t)=\left(\frac73-\frac43e^{-3t}-e^{-10t}\right)\ \mathrm A,}$$

$$\boxed{i_2(t)=\left(\frac73-\frac{10}3e^{-3t}+e^{-10t}\right)\ \mathrm A,}$$

$$\boxed{v_o(t)=2(e^{-3t}-e^{-10t})\ \mathrm V.}$$

**检查**：$i_1(0)=i_2(0)=0$、$\dot i_1(0)=14$ A/s、$\dot i_2(0)=0$，两网孔原始 KVL 均成立。这也是“非振荡”不等于“所有输出单调”的例子：$v_o$ 从零上升后回到零。

## 运放例：两个电容的二阶系统 (Second-Order Op-Amp Circuit)

![[l6-opamp.png|580]]

*原图：[[ECE2001/L6 Second-order Circuits 20261018.pdf#page=62|PDF pp.62–63]]。理想运放接成电压跟随器 (voltage follower)，$C_1$ 从同相端节点接地，$C_2$ 从两电阻中点接输出。*

令 $v_1$ 为两电阻中点电压、$v_o$ 为输出电压；讲义的 $v_2=v_1-v_o$ 是 $C_2$ 两端电压，**并不是标号“2”的节点电压**。按理想运放线性负反馈模型，输入电流为零、同相端电压等于 $v_o$：

$$\frac{v_s-v_1}{R_1}=C_2\frac{d(v_1-v_o)}{dt}+\frac{v_1-v_o}{R_2},\qquad
\frac{v_1-v_o}{R_2}=C_1\dot v_o.$$

消元得

$$\boxed{\ddot v_o+\left(\frac1{R_1C_2}+\frac1{R_2C_2}\right)\dot v_o
+\frac{v_o}{R_1R_2C_1C_2}=\frac{v_s}{R_1R_2C_1C_2}.}$$

零初态、$v_s=V_Su(t)$ 时，$v_o(0^+)=0$、$\dot v_o(0^+)=0$、稳定终值为 $V_S$，可直接按主笔记的通用系数表求解。参数识别、与现有 Sallen-Key 标号的换算及数值例子见 [[Operational Amplifier#4.4 二阶运放电路的时域方程 (Second-Order Op-Amp Dynamics)|运放笔记 §4.4]]。

## 自检清单 (Recall)

- 初态是否来自 $0^-$，导数是否来自 $0^+$ 的新拓扑？
- 电容电流是否流入所定义电压的正端？例 3 的方向与标准串联公式相反。
- 能否直接从新拓扑识别串联或并联？不能时应列 KCL/KVL 消元。
- 是否先扣除常数特解，再确定暂态系数？
- 特征根之和、之积是否与 ODE 相符？
- 除初值与终值外，是否检查了原始微分方程及 $i_C=C\dot v_C$、$v_L=L\dot i_L$？

## 来源与关联

- CUHK-Shenzhen，ECE 2001 *Basic Circuit Theory*，Lecture 6，[[ECE2001/L6 Second-order Circuits 20261018.pdf|L6 Second-order Circuits 20261018]]，文件日期 2026-10-18，PDF pp.5–12、30–35、43–63。图为讲义电路图摘录；推导与数值重算按图示参考方向。
- [[Second-Order Transients]] —— 主概念、系数速算与适用条件
- [[First-Order Transients]] —— 换路与状态连续性
- [[Basic Circuit Analysis Method]] / [[Kirchhoff's Laws]] —— 节点与网孔消元
- [[Operational Amplifier]] / [[Filters]] —— 二阶有源电路
- [[cs6.002x.1]] / [[Circuit Theory Glossary]] —— 知识树与术语
