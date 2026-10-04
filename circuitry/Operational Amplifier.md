---
tags:
  - 电路学
  - 有源器件
  - 运算放大器
  - 课程笔记
date: 2026-09-08
aliases:
  - Operational Amplifier
  - Op Amp
  - 运算放大器
  - 运放
  - Operational Amplifier Abstraction
  - Op-Amp Model
  - 虚短
  - 虚断
  - Virtual Short
  - Virtual Open
---

# Operational Amplifier（运算放大器）

> [!NOTE] 本笔记定位
> 运算放大器（operational amplifier, op amp）是差分输入、单端输出的有源器件。其开环增益通常很高，但数值随器件、频率和工作条件变化；用**负反馈**（negative feedback）可在稳定、未饱和的工作区内，由外接网络设定较可预测的闭环关系。
> 承上：[[Small Signal Circuit Representation]]（输入/输出电阻、增益）/ [[Impedance]]（阻抗）；启下：[[Diode]]（整流后的信号要用运放滤波/缓冲）/ [[Filters]]（有源滤波器）/ [[Amplifiers and Feedback]]（反馈理论）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、运放符号与端口

![[opamp_generic_symbol.svg|536]]

> **运放电路符号**（5 个功能端口）：同相输入 $v_+$、反相输入 $v_-$、输出 $v_o$、正供电 $V_{S+}$、负供电 $V_{S-}$。供电端在简化图中常省略，实际电路必须连接。

图中是通用电路符号，不代表某一型号的封装脚位；实际供电脚和允许的输入、输出范围须按所选器件的数据手册确定。

| 端口 | 符号 | 功能 |
| :--- | :--- | :--- |
| **同相输入 $v_+$** | `+` | 输入电压与输出同相（$v_{\text{out}}\propto +v_+$）|
| **反相输入 $v_-$** | `−` | 输入电压与输出反相（$v_{\text{out}}\propto -v_-$）|
| **输出 $v_{\text{out}}$** | — | 放大后的电压输出 |
| **正供电 $V_{S+}$** | — | 由具体器件及供电方案规定，不存在通用的 $+15$ V 上限 |
| **负供电 $V_{S-}$** | — | 可以为负电压，也可以在允许单电源工作的器件中接地 |

供电脚和信号输入脚的符号要区分：$V_{S+},V_{S-}$ 是电源，$v_+,v_-$ 是相对参考地测得的输入电位。有些器件封装还有失调调零脚或未连接脚；这些不是所有运放的通用引脚定义，布线按器件数据手册核对。

---

## 二、理想与非理想运放模型

> [!IMPORTANT] 理想运放的两条黄金规则
> 1. **虚短 (Virtual Short)**：$v_+ \approx v_-$（两个输入端电压几乎相等）
> 2. **虚断 (Virtual Open)**：$i_+ = i_- \approx 0$（两个输入端近似不汲取电流）
>
> **虚断**来自理想输入电阻无穷大，即使开环也成立；**虚短**还要求负反馈闭合、闭环稳定且输出没有饱和。虚短表示电位相等，绝不表示两个输入端短接并能互相流过电流。

### 2.1 理想基线与主要非理想量

| 参数 | 理想值 | 实际器件 | 影响 |
| :--- | :--- | :--- | :--- |
| **开环电压增益 $A$** | $\infty$ | 有限且随频率变化 | 决定闭环误差和稳定性 |
| **差分输入电阻 $R_i$** | $\infty$ | 有限，器件类型差异很大 | 输入负载与偏置 |
| **开环输出电阻 $R_o$** | $0$ | 有限 | 负载对输出的影响 |
| **带宽** | 无穷大 | 有限，须结合开环频率响应 | 高频闭环误差 |
| **输入偏置电流 $I_B$** | $0$ | 由输入级及温度决定 | 经源电阻产生直流误差 |
| **输入失调电压 $V_{OS}$** | $0$ | 由器件及温度决定 | 零差分输入时的输出偏移 |

前三项构成一个基本等效电路：电压控制电压源（voltage-controlled voltage source, VCVS）给出内部电压 $v_x=A(v_+-v_-)$，输入端之间接 $R_i$，输出串联 $R_o$。它是[[Dependent Sources|受控源]]模型；负载电流经过 $R_o$ 时，端口电压 $v_o$ 可以不同于 $v_x$。理想运放取 $A\to\infty, R_i\to\infty, R_o\to0$。

### 2.2 开环传输特性

- 若闭环使 $v_o$ 保持有限且在线性区，$A\to\infty$ 才推出 $v_+-v_-\to0$。
- **饱和**（voltage saturation）：当线性式要求的电压超出输出摆幅范围，实际输出被限制在 $V_{OL}$ 与 $V_{OH}$ 之间。简化模型可取 $V_{OL}=V_{S-}, V_{OH}=V_{S+}$；真实限幅由器件、供电和负载决定。

> [!NOTE] 饱和的物理含义
> 输出接近其可达的正/负摆幅边界时，线性受控源式不再适用，虚短也须重新检查。若采用简化对称限幅 $\pm V_{sat}$，可写 $v_o=\operatorname{clip}(A(v_+-v_-),-V_{sat},+V_{sat})$；这是电路分析模型，不是任意运放的精确数据手册曲线。

### 2.3 有限增益为什么仍可用虚短近似

以一个反相电路为例：取 $v_s=2\,\mathrm V$，输入电阻 $10\,\mathrm{k}\Omega$，反馈电阻 $20\,\mathrm{k}\Omega$；运放等效参数为 $A=2\times10^5$、$R_i=2\,\mathrm{M}\Omega$、$R_o=50\,\Omega$。同相端接地，令反相端电位为 $v_n$，内部受控源电压为 $-Av_n$，KCL 为

$$\frac{v_s-v_n}{10\,\mathrm{k}\Omega}=\frac{v_n-v_o}{20\,\mathrm{k}\Omega}+\frac{v_n}{2\,\mathrm{M}\Omega},\qquad
\frac{v_n-v_o}{20\,\mathrm{k}\Omega}=\frac{v_o+Av_n}{50\,\Omega}.$$

联立得 $v_n\approx20.05\,\mathrm{\mu V}$、$v_o\approx-3.99994\,\mathrm V$，所以闭环增益约 $-1.99997$，与理想结果 $-20/10=-2$ 很接近。若反馈电流正方向定义为**求和节点 $\to$ 输出**，则 $i_f=(v_n-v_o)/(20\,\mathrm{k}\Omega)\approx+0.200\,\mathrm{mA}$；若反向定义则为 $-0.200\,\mathrm{mA}$。列式时须始终使用同一电流参考方向。

---

## 三、七种基本运放电路

每种接法的电路图都放在对应的小节，可边看接线边看推导。图中电源引脚为便于读图而省略；所列关系以理想运放、稳定负反馈且输出未饱和为前提。交叉处的跨线弧表示两根导线不相连，实心圆点表示电气连接。本节的 $v_o$ 与图中的 `v_out` 是同一输出电压，所有输入、输出电压均相对于图中的地。不要先背增益公式：**先看输入接在哪个端口，再看输出怎样反馈到反相端，最后对节点列电流方程**。

> [!IMPORTANT] 通用分析步骤 / Analysis recipe
> 1. 确认输出经电阻、电容或导线接回**反相端**，并先假定闭环稳定、输出在线性摆幅内。
> 2. 用理想模型 $i_+=i_-=0$（**虚断，no input current**）及 $v_+=v_-$（**虚短，equal input potentials**）。只有 $v_+$ 真正接地时，才可进一步写 $v_-\approx0$。
> 3. 给每条支路选定电流方向，用[[Kirchhoff's Laws|节点电流定律（KCL）]]及 $i=(v_a-v_b)/R$ 列式。电流可以算出负值，这只说明实际方向与约定相反。
> 4. 求出 $v_o$ 后，检查符号、单位和器件允许的输入/输出范围；若发生饱和，前面的虚短假设就要重审。

对单输入的纯电阻电路，电压增益（voltage gain）是 $A_v=v_o/v_{\mathrm{in}}$，无量纲；多输入电路要分别看每一路的系数。积分器和微分器随时间或频率变化，不能用一个固定的直流增益概括。

### 3.1 同相放大器 (Non-Inverting Amplifier)

![[opamp_non_inverting_amplifier.svg|442]]

**看上图。** $v_{\mathrm{in}}$ 直接接同相端，$R_f$ 从输出接到反相端，$R_1$ 从反相端接地。令反相节点电压为 $v_n$。因为输入端不取电流，$R_f$ 与 $R_1$ 构成输出到地的分压器：

$$v_n=\frac{R_1}{R_1+R_f}v_o.$$

负反馈使 $v_n=v_+=v_{\mathrm{in}}$。将它代回分压式并移项：

$$v_{\mathrm{in}}=\frac{R_1}{R_1+R_f}v_o
\quad\Longrightarrow\quad
\boxed{A_v=\frac{v_o}{v_{\mathrm{in}}}=1+\frac{R_f}{R_1}.}$$

直觉是：输出必须比同相输入更大，才能在分压后让反相端“追上”输入。$R_1,R_f>0$ 时 $A_v\ge1$；信号极性不翻转。理想模型下运放输入电阻无穷大、闭环输出电阻趋近零；真实器件只有“高输入、低输出”的近似，仍受带宽和负载限制。

> [!EXAMPLE] 增益为 10 的放大器
> 取 $R_f=9\,\mathrm{k}\Omega$、$R_1=1\,\mathrm{k}\Omega$、$v_{\mathrm{in}}=0.5\,\mathrm V$。则 $A_v=1+9/1=10$，$v_o=5\,\mathrm V$。核对分压：$v_n=5\times1/(1+9)=0.5\,\mathrm V$，确实等于 $v_+$；两只电阻中的电流均为 $0.5\,\mathrm{mA}$。这个结果还要求所选运放在当前供电和负载下能输出 $5\,\mathrm V$。

**English recall:** The feedback divider sets the gain; essentially no signal current enters the op-amp input.

### 3.2 反相放大器 (Inverting Amplifier)

![[opamp_inverting_amplifier.svg|486]]

**看上图。** $v_{\mathrm{in}}$ 经过 $R_1$ 接反相端，同相端接地。令反相节点电压为 $v_n$；由于 $v_+=0$ 且有稳定负反馈，$v_n\approx0$，称为**虚地（virtual ground）**。它只有电位接近地，**并没有用导线接地**。

约定输入电阻电流从输入源流向求和节点，反馈电阻电流从求和节点流向输出：

$$i_1=\frac{v_{\mathrm{in}}-v_n}{R_1},\qquad
i_f=\frac{v_n-v_o}{R_f}.$$

运放反相输入端不取电流，故 KCL 为 $i_1=i_f$。代入 $v_n=0$：

$$\frac{v_{\mathrm{in}}}{R_1}=\frac{-v_o}{R_f}
\quad\Longrightarrow\quad
\boxed{A_v=\frac{v_o}{v_{\mathrm{in}}}=-\frac{R_f}{R_1}.}$$

负号表示输出相对于输入反相；$R_f<R_1$ 时幅值也可以缩小。信号源看到的输入电阻约为 $R_1$，**不是**运放芯片本身很高的输入电阻，因为电流确实经过 $R_1$ 流入反馈支路。

> [!EXAMPLE] 从电流验证负号
> 取 $R_1=10\,\mathrm{k}\Omega$、$R_f=20\,\mathrm{k}\Omega$、$v_{\mathrm{in}}=+0.6\,\mathrm V$。$i_1=0.6/10\,\mathrm{k}\Omega=60\,\mathrm{\mu A}$，必须有同样的 $i_f$ 流向输出。于是 $v_o=-i_fR_f=-1.2\,\mathrm V$；反算 $i_f=(0-(-1.2))/20\,\mathrm{k}\Omega=60\,\mathrm{\mu A}$。要实现它，器件必须允许负向输出摆幅。

**English recall:** The inverting node is a virtual ground, and input current flows through the feedback resistor, not into the op amp.

若把电压源和 $R_1$ 换成**注入反相求和节点的电流源** $i_{in}$，同一 KCL 给出 $v_o=-i_{in}R_f$：这是跨阻放大器（transimpedance amplifier）的理想关系，单位检查为 $\mathrm A\cdot\Omega=\mathrm V$。输入电流方向若改为从节点流出，输出符号也相反。

### 3.3 电压跟随器 (Voltage Follower / Buffer)

![[opamp_voltage_follower.svg|418]]

**看上图。** 输入直接接同相端，输出用导线直接接反相端；它是同相放大器把 $R_f$ 短接、$R_1$ 去掉的极限接法。由导线可知 $v_-=v_o$，由虚短可知 $v_-=v_+=v_{\mathrm{in}}$，因此

$$\boxed{v_o=v_{\mathrm{in}},\qquad A_v=\frac{v_o}{v_{\mathrm{in}}}=1.}$$

“没有放大电压”不等于“没有作用”：理想跟随器几乎不从信号源取电流，却可从自己的电源向负载供电流，所以常作**缓冲器（buffer）**，隔离高源电阻与低负载电阻。

> [!EXAMPLE] 为什么 1 倍增益仍有用？
> 把传感器等效成开路电压 $V_s=1.0\,\mathrm V$、串联源电阻 $R_s=100\,\mathrm{k}\Omega$，负载 $R_L=10\,\mathrm{k}\Omega$。直接相接时，分压得到 $v_L=V_sR_L/(R_s+R_L)=1.0\times10/110\approx0.091\,\mathrm V$。若插入理想跟随器，输入不取电流，传感器端保持约 $1.0\,\mathrm V$，于是输出也约 $1.0\,\mathrm V$，向负载提供 $i_L\approx1.0/10\,\mathrm{k}\Omega=0.10\,\mathrm{mA}$。真实器件还须检查输出电流能力、摆幅与稳定性。

同理，高输出阻抗传感器接 ADC 时，跟随器可减轻采样电容造成的负载影响；是否能在采样时间内建立到所需精度，仍要按 ADC 和运放的实际参数验证。

**English recall:** A voltage follower copies voltage while buffering the source from the load.

### 3.4 差分放大器 (Differential Amplifier)

![[opamp_difference_amplifier.svg|453]]

**看上图（difference amplifier / subtractor）。** $R_1$ 从 $v_1$ 接反相端，$R_2$ 从输出反馈到反相端；$R_3$ 从 $v_2$ 接同相端，$R_4$ 从同相端接地。令同相节点为 $v_b$、反相节点为 $v_a$。要看懂它，先求同相端的电位，再算反相端的反馈。

1. 同相输入不取电流，所以 $R_3,R_4$ 对 $v_2$ 分压：$v_b=\dfrac{R_4}{R_3+R_4}v_2$。
2. 虚短给出 $v_a=v_b$；**这并不表示两节点之间有电流流动**。
3. 对 $v_a$ 列 KCL：$\dfrac{v_1-v_a}{R_1}=\dfrac{v_a-v_o}{R_2}$，移项得到 $v_o=\left(1+\dfrac{R_2}{R_1}\right)v_a-\dfrac{R_2}{R_1}v_1$。
4. 代入 $v_a=v_b$：

$$\boxed{v_o=\frac{R_4(R_1+R_2)}{R_1(R_3+R_4)}v_2-\frac{R_2}{R_1}v_1.}$$

只有两组**电阻比匹配（ratio matching）**，即 $R_2/R_1=R_4/R_3=k$，$v_2$ 的系数才也化为 $k$。此时

$$\boxed{v_o=k(v_2-v_1),\qquad k=\frac{R_2}{R_1}=\frac{R_4}{R_3}.}$$

> [!EXAMPLE] 从节点电位算到输出
> 取 $R_1=R_3=10\,\mathrm{k}\Omega$、$R_2=R_4=20\,\mathrm{k}\Omega$，故 $k=2$。若 $v_1=1.2\,\mathrm V$、$v_2=1.5\,\mathrm V$，先算 $v_b=1.5\times20/(10+20)=1.0\,\mathrm V$，于是 $v_a=1.0\,\mathrm V$。KCL 成为 $(1.2-1.0)/10\,\mathrm{k}\Omega=(1.0-v_o)/20\,\mathrm{k}\Omega$，解得 $v_o=0.6\,\mathrm V$；用简式核对，$2(1.5-1.2)=0.6\,\mathrm V$。若两个输入同时增加相同电压，理想输出仍由差值决定。

四只电阻全相等只是 $k=1$ 的特例。实际电阻比失配和运放本身的共模误差会使共同变化的电压泄漏到输出；弱差分信号测量通常用输入阻抗更高的[[Instrumentation Amplifier|仪表放大器]]。

**English recall:** Matched resistor *ratios* reject the common-mode part and amplify the difference $v_2-v_1$.

### 3.5 加法器 (Summing Amplifier)

![[opamp_summing_amplifier.svg|483]]

上图是三输入**反相加法器（inverting summing amplifier）**。三个信号分别经过 $R_1,R_2,R_3$ 到达同一个反相**求和节点（summing node）** $N$；同相端接地，故 $v_N\approx0$。这不是“三个运放输入端”，而是**一个节点上的三条输入支路**。

约定每路电流从信号源流向 $N$，反馈电流从 $N$ 流向输出：

$$i_1=\frac{v_1-v_N}{R_1},\quad i_2=\frac{v_2-v_N}{R_2},\quad
i_3=\frac{v_3-v_N}{R_3},\quad i_f=\frac{v_N-v_o}{R_f}.$$

输入端不取电流，KCL 给出 $i_1+i_2+i_3=i_f$。将 $v_N=0$ 代入并整理：

$$\frac{v_1}{R_1}+\frac{v_2}{R_2}+\frac{v_3}{R_3}=\frac{-v_o}{R_f}
\quad\Longrightarrow\quad
\boxed{v_o=-\frac{R_f}{R_1}v_1-\frac{R_f}{R_2}v_2-\frac{R_f}{R_3}v_3.}$$

每一路的“增益”是自己的权重 $-R_f/R_i$；例如 $R_2$ 较小，第二路同样电压会产生较大的电流和输出贡献。三路电阻相同且等于 $R_f$ 时，$v_o=-(v_1+v_2+v_3)$。

> [!EXAMPLE] 三路带正负号的输入
> 取 $R_f=20\,\mathrm{k}\Omega$，$R_1=20\,\mathrm{k}\Omega$、$R_2=10\,\mathrm{k}\Omega$、$R_3=40\,\mathrm{k}\Omega$；令 $v_1=0.5\,\mathrm V$、$v_2=-0.2\,\mathrm V$、$v_3=0.4\,\mathrm V$。三路电流依次为 $25\,\mathrm{\mu A}$、$-20\,\mathrm{\mu A}$、$10\,\mathrm{\mu A}$，总和 $15\,\mathrm{\mu A}$，所以 $v_o=-R_f(15\,\mathrm{\mu A})=-0.30\,\mathrm V$。第二路负电流表示它实际上从节点流向第二个信号源；按权重式复算为 $-(0.5-0.4+0.2)=-0.30\,\mathrm V$。

**English recall:** Each input contributes a weighted current; the feedback resistor converts their sum to an inverted output voltage.

同一求和节点还可做电阻加权[[Resistor-Weighted Digital-to-Analog Converter|数模转换器]]；每路输入在 $0$ 和同一参考电压间切换，电阻比决定二进制权重。

### 3.6 积分器 (Integrator)

![[opamp_integrator_basic.svg]]

**看上图。** 输入经电阻 $R$ 接反相节点 $N$，输出通过电容 $C$ 反馈到 $N$，同相端接地。令电阻电流从输入流向 $N$，电容电流从 $N$ 流向输出，并将电容两端电压定义为 $v_C=v_N-v_o$。元件定律与 KCL 给出

$$i_R=\frac{v_{\mathrm{in}}-v_N}{R},\qquad
i_C=C\frac{d(v_N-v_o)}{dt},\qquad i_R=i_C.$$

在线性负反馈的理想模型下 $v_N=0$，因此 $v_{\mathrm{in}}/R=-C\,dv_o/dt$，也就是

$$\boxed{\frac{dv_o}{dt}=-\frac{v_{\mathrm{in}}}{RC},\qquad
v_o(t)=v_o(t_0)-\frac{1}{RC}\int_{t_0}^{t}v_{\mathrm{in}}(\tau)\,d\tau.}$$

这里 $t_0$ 是起始时刻，$v_o(t_0)$ 由电容初始电压决定；$RC$ 的单位为秒。**恒定正输入使输出按固定负斜率下降**，并不是输出等于一个固定倍数的输入。若取零初始条件并作拉普拉斯变换（Laplace transform），则 $sV_o(s)=-V_{\mathrm{in}}(s)/(RC)$，所以 $H(s)=V_o(s)/V_{\mathrm{in}}(s)=-1/(sRC)$。

若输入是频率为 $f$ 的正弦波，代入 $s=j\omega$、$\omega=2\pi f$，得到**幅值增益（magnitude gain）** $|H(j\omega)|=1/(\omega RC)$；频率越高，输出幅值相对越小。例如下例的 $RC=0.10\,\mathrm s$，在 $f=1\,\mathrm{Hz}$ 时，$|H|=1/(2\pi\times1\times0.10)\approx1.59$。这是该频率下的稳态幅值比，不是任意输入的固定增益。

> [!EXAMPLE] 电压如何随时间累积？
> 取 $R=10\,\mathrm{k}\Omega$、$C=10\,\mathrm{\mu F}$，故 $RC=0.10\,\mathrm s$。设 $v_o(0)=0$，在 $0$ 至 $0.10\,\mathrm s$ 内施加恒定 $v_{\mathrm{in}}=+0.50\,\mathrm V$，则斜率 $dv_o/dt=-0.50/0.10=-5.0\,\mathrm{V/s}$，末端输出为 $v_o(0.10\,\mathrm s)=-0.50\,\mathrm V$。单位核对：$(1/RC)\int v_{\mathrm{in}}dt$ 为 $\mathrm{s}^{-1}\cdot\mathrm{V\,s}=\mathrm V$。这个短时结果要求输出仍处在线性摆幅内。

理想积分器对直流失调也不断累积，迟早可能饱和；实际常给反馈电容并联电阻以建立直流反馈，详见 §4.1。

**English recall:** An integrator turns input voltage into output *slope*; the initial output value is part of the answer.

### 3.7 微分器 (Differentiator)

![[opamp_differentiator_basic.svg]]

**看上图。** 把积分器的输入、反馈元件对调：输入先经过电容 $C$ 到反相节点 $N$，输出经电阻 $R$ 反馈。仍约定输入电容电流流向 $N$、反馈电阻电流流向输出：

$$i_C=C\frac{d(v_{\mathrm{in}}-v_N)}{dt},\qquad
i_R=\frac{v_N-v_o}{R},\qquad i_C=i_R.$$

由于 $v_N=0$，输入电压的**变化率（rate of change）**决定电容电流：

$$C\frac{dv_{\mathrm{in}}}{dt}=\frac{-v_o}{R}
\quad\Longrightarrow\quad
\boxed{v_o(t)=-RC\frac{dv_{\mathrm{in}}(t)}{dt}.}$$

$RC$ 的单位为秒，而 $dv_{\mathrm{in}}/dt$ 的单位为 $\mathrm{V/s}$，相乘得到 V。零初始条件下，拉普拉斯变换给出 $H(s)=V_o(s)/V_{\mathrm{in}}(s)=-sRC$；因此它也没有固定的直流电压增益。

对频率为 $f$ 的正弦波，$|H(j\omega)|=\omega RC=2\pi fRC$；频率越高，输出幅值相对越大。例如下例的 $RC=0.10\,\mathrm s$，在 $f=1\,\mathrm{Hz}$ 时，$|H|=2\pi\times1\times0.10\approx0.628$。它与积分器的频率趋势相反，但高频结果仍受实际运放带宽限制。

> [!EXAMPLE] 斜坡输入产生恒定输出
> 取 $R=10\,\mathrm{k}\Omega$、$C=10\,\mathrm{\mu F}$，故 $RC=0.10\,\mathrm s$。在一段时间内让输入以 $1.0\,\mathrm{V/s}$ 匀速上升，例如从 $0$ 到 $0.20\,\mathrm s$，输入由 $0$ 变为 $0.20\,\mathrm V$。在斜坡内部，$v_o=-0.10\times1.0=-0.10\,\mathrm V$；若输入改为保持不变，理想输出回到 $0$。符号为负，因为输入正在上升。

理想微分器会不断放大更高频率的噪声；真实电路的有限带宽使 $-sRC$ 不可能在所有频率成立，实际设计常加输入串联电阻和反馈电容限制高频增益，见 §4.2。

**English recall:** A differentiator responds to input *slope*: a rising ramp gives a negative output, while a flat input gives zero.

### 3.8 带参考电位的反相电路与饱和检查

这是 §3.2 的延伸：若同相端接参考电位 $v_b$ 而非地，输入 $v_a$ 经 $R_{in}$ 接反相端，$R_f$ 从输出反馈到反相端，则虚短给出 $v_-=v_b$，**不能再把反相端写成 $0\,\mathrm V$**。对反相节点列 KCL，$(v_a-v_b)/R_{in}=(v_b-v_o)/R_f$；移项得线性区关系

$$\boxed{v_o=\left(1+\frac{R_f}{R_{in}}\right)v_b-\frac{R_f}{R_{in}}v_a.}$$

**步骤是先假设线性，再验算摆幅。** 例如取 $R_{in}=25\,\mathrm{k}\Omega$、$R_f=100\,\mathrm{k}\Omega$、供电 $\pm10\,\mathrm V$，故 $v_o=5v_b-4v_a$。当 $v_a=1\,\mathrm V$ 时，$v_b=0\,\mathrm V$ 给出 $v_o=-4\,\mathrm V$，$v_b=2\,\mathrm V$ 给出 $v_o=6\,\mathrm V$；两者都在简化模型的 $(-10,10)\,\mathrm V$ 线性范围内。当 $v_a=1.5\,\mathrm V$，要严格避免到达限幅边界，须 $-10<5v_b-6<10$，即 $-0.8\,\mathrm V<v_b<3.2\,\mathrm V$。端点对应理想化的限幅边界，实际器件还须留裕量。

**七种接法速查 / Seven-circuit quick reference**（均以稳定负反馈、未饱和的理想模型为前提）：

| 电路 | Look for this connection | 推导结果 |
| :--- | :--- | :--- |
| 同相 Non-inverting | Signal to `+`; resistor divider to `−` | $A_v=1+R_f/R_1$ |
| 反相 Inverting | Signal through $R_1$ to `−`; `+` grounded | $A_v=-R_f/R_1$ |
| 跟随器 Follower | Output wired directly to `−` | $A_v=1$ |
| 差分 Difference | Two inputs, two matched resistor ratios | $v_o=k(v_2-v_1)$，须 $R_2/R_1=R_4/R_3=k$ |
| 加法器 Summing | Several resistors meet at one `−` node | $v_o=-R_f\sum_i v_i/R_i$ |
| 积分器 Integrator | Input $R$, feedback $C$ | $H(s)=-1/(sRC)$（零初始条件）|
| 微分器 Differentiator | Input $C$, feedback $R$ | $H(s)=-sRC$（零初始条件）|

前三种的 $A_v$ 是单输入电压增益；差分与加法电路有多个输入，应看各路系数；最后两种要看时间响应或频率响应。**Quick check:** 先认接线，再列 KCL，最后才用速查式核对。

---

## 四、运放 RC 电路（积分器 / 微分器 / Sallen-Key）

![[opamp_rc_sallen_key_schematics.svg|576]]

> **运放 RC 电路**：左上为电容反馈的理想积分器，右上为电容输入的理想微分器；下排为单位增益（$K=1$）的 Sallen–Key 低通与高通。实心圆点表示电气连接；各图省略了运放供电脚，电压均以图中地为参考。

### 4.1 积分器（Op-Amp Integrator）

$$\boxed{H(s) = \frac{v_{\text{out}}}{v_{\text{in}}}(s) = -\frac{1}{sRC}}$$

> [!NOTE] 频率域含义
> $H(j\omega) = -1/(j\omega RC) = +j/( \omega RC)$，即：
> - $|H|\propto1/\omega$（幅值随频率升高而衰减）；理想积分器在 $\omega\to0$ 时增益无界，不能当作普通稳定的一阶低通滤波器。
> - 相位恒为 $+90^\circ$（输出超前输入 $90^\circ$）
> 实际积分器常加并联反馈电阻限制直流增益，相关设计见 [[Filters]]。

> [!WARNING] 积分器漂移问题
> 理想积分器对微小输入失调电压与偏置电流也会持续积分，最终使运放饱和。实际常在反馈电容两端并联电阻，给直流提供反馈通路并限制低频增益。

### 4.2 微分器（Op-Amp Differentiator）

$$\boxed{H(s) = \frac{v_{\text{out}}}{v_{\text{in}}}(s) = -sRC}$$

> [!NOTE] 频率域含义
> $|H| \propto \omega$（幅值随频率升高而增加；这是理想微分器的高频加权，不是具有有限通带增益的普通高通滤波器）
> 相位恒为 $-90^\circ$（输出滞后输入 $90^\circ$）
> 高频增益无穷大（实际被运放带宽限制）——容易放大高频噪声，**实际很少使用**。

### 4.3 Sallen-Key 有源滤波器

对标准两电阻、两电容的 Sallen-Key 低通拓扑（[[Filters]] §4），常写成：

$$\boxed{H_{\text{LP}}(s)=\frac{K\omega_0^2}{s^2+s(\omega_0/Q)+\omega_0^2},\qquad \omega_0=\frac{1}{\sqrt{R_1R_2C_1C_2}}.}$$

其中 $K$ 为通带增益，$Q$ 由电容接法、阻值比和 $K$ 共同决定；必须先固定具体电路拓扑及元件标号再写 $Q$ 的元件公式。原先笔记中的 $Q$ 表达式量纲不为 1，不能使用。

对于上图所画的**单位增益**版本，低通的 $C_1$ 从两只串联电阻的中点接到输出，$C_2$ 从同相输入节点接地；高通的 $R_1$ 从两只串联电容的中点接到输出，$R_2$ 从同相输入节点接地。按图中标号，理想运放模型给出

$$H_{\mathrm{LP}}(s)=\frac{1}{1+sC_2(R_1+R_2)+s^2R_1R_2C_1C_2},\qquad
H_{\mathrm{HP}}(s)=\frac{s^2R_1R_2C_1C_2}{1+sR_1(C_1+C_2)+s^2R_1R_2C_1C_2}.$$

当 $R_1=R_2=R$ 且 $C_1=C_2=C$ 时，两者分母都化为 $1+2sRC+s^2R^2C^2$，因此 $\omega_0=1/(RC)$、$Q=1/2$；不能把旧图中的 $1+sRC+s^2R^2C^2$ 当作等值元件、单位增益电路的结果。图中的积分器、微分器接法参照 [Texas Instruments, *Handbook of Operational Amplifier Applications*, Rev. B, Fig. 21–22](https://www.ti.com/lit/an/sboa092b/sboa092b.pdf)；Sallen–Key 拓扑参照 [Analog Devices, *Phase Relations in Active Filters*, Fig. 10–11](https://www.analog.com/en/resources/analog-dialogue/articles/phase-relations-in-active-filters.html)，元件标号与公式按本图定义。

> [!NOTE] Sallen-Key 的优势
> - **有源滤波**（比无源 RLC 少电感）：易于集成、阻抗匹配好
> - **可调 $Q$**：通过调整电阻比 $R_1/R_2$ 或电容比 $C_1/C_2$ 控制谐振峰
> - **单位增益**（$K=1$）或**带增益**版本（[[Filters]] §4.1）

---

## 五、饱和、正反馈与振荡器

### 5.1 开环比较器与饱和

在开环或比较器（comparator）应用中，输出通常由差分输入的**符号**决定，而非遵守虚短：若 $v_+>v_-$，趋向高电平 $V_{OH}$；若 $v_+<v_-$，趋向低电平 $V_{OL}$。接近阈值时，输入失调、噪声、传播延迟等会影响翻转。例如低电压报警器把参考电压接同相端、待测电压接反相端：$v_{in}<v_{ref}$ 时输出趋向高电平。实际比较用途应核查器件能否在相应输入范围与供电条件下工作，以及输出是否能驱动负载。

> [!IMPORTANT] 输出限幅要按器件与负载核对
> - 当线性模型要求的输出超出该器件在当前供电与负载下允许的输出摆幅时，输出接近电源轨并削顶；例如某些采用 $\pm15$ V 供电的运放可能只到约 $\pm14$ V，具体应查数据手册。
> - 内部晶体管退出线性放大区，进入大信号模式
> - $v_{\text{out}}$ 被电源轨夹断，不再跟随 $v_+-v_-$
> - 失真：正弦波变成削顶波形（[[Diode]] §削波）

### 5.2 正反馈 (Positive Feedback)

负反馈可在合适的相位裕量下稳定闭环；正反馈会放大微小扰动，可用于迟滞与振荡。下式是静态代数模型，尚未包含运放带宽、延迟和饱和：

以一个理想求和模型说明，令 $v_+=v_{\text{in}}+\beta v_{\text{out}}$、$v_-=0$，并在未饱和时取 $v_{\text{out}}=A(v_+-v_-)$，则

$$\Rightarrow\quad v_{\text{out}} = \frac{A}{1-A\beta}\,v_{\text{in}}$$

- 当 $A\beta \to 1$ 时，理想线性式的分母趋零，说明该线性工作点不可继续沿用；实际输出受电源轨限制，动态行为须另行分析。
- **Barkhausen 振荡条件**：
$$\boxed{|A\beta|=1, \quad \angle A + \angle \beta = 0^\circ}$$

> [!NOTE] RC 振荡器
> RC 相移振荡器需在目标频率同时满足**总环路相位为 $0^\circ$**及足够的环路增益；RC 网络自身有衰减，因此放大器所需增益不能一律设为 1。MIT Lecture 21 的例子则是另一类**迟滞比较器 + RC 充放电**的松弛振荡器，阈值和周期推导见 [[Amplifiers and Feedback]]。

### 5.3 滞回比较器（Hysteresis Comparator）

对输入接反相端、同相端经 $R_f$ 接输出并经 $R_g$ 接地的电路，令 $\beta=R_g/(R_f+R_g)$、对称饱和电平为 $\pm V_{sat}$：

$$V_{\text{H}} = +\beta V_{sat}, \qquad V_{\text{L}} = -\beta V_{sat}.$$

正反馈引入**滞回 (hysteresis)**：两个阈值 $V_H>V_L$，避免比较器在噪声附近反复切换（Schmitt Trigger）。状态转移方向及 RC 振荡应用见 [[Amplifiers and Feedback]]。

另一种**偏置阈值**版本让同相端由正、负电源分压，并经电阻从输出获得正反馈；阈值公式依接线和电阻位置而变，不能直接套用上式的对称 $\pm\beta V_{sat}$。拓扑、上下阈值及例子见[[Amplifiers and Feedback#3.2 迟滞比较器 (Schmitt Trigger)|反馈笔记]]。

---

## 六、运放的二端口模型

### 6.1 闭环输入 / 输出电阻

| 电路 | $R_{\text{in,cl}}$ | $R_{\text{out,cl}}$ |
| :--- | :--- | :--- |
| **同相放大器** | $R_{\text{in}}(1+A\beta)$（极高）| $R_{\text{out}}/(1+A\beta)$（极低）|
| **反相放大器** | $R_1$ | 负反馈降低；具体值取决于反馈网络和开环输出电阻 |
| **电压跟随器** | 很高（理想极限 $\infty$）| 很低（理想极限 $0$）|

> [!NOTE] 公式的拓扑前提
> 上表的 $R_{in}(1+A\beta)$ 与 $R_{out}/(1+A\beta)$ 是**电压串联反馈**且其简化模型适用时的近似关系；反相放大器从信号源看到的输入电阻仍约为 $R_1$。$A\beta$ 随频率变化，带宽与稳定性也须按具体反馈网络判断。详见 [[Amplifiers and Feedback]]。

### 6.2 带宽扩展（Gain-Bandwidth Product, GBW）

对于**单主极点补偿、且处于增益随频率近似按 $1/f$ 下降的区间**，开环增益幅值与频率的乘积近似为常数：

$$\boxed{|A(j2\pi f)|\,f\approx\mathrm{GBW}.}$$

- 同相放大器在相同近似下：闭环带宽 $f_{\text{cl}}\approx\mathrm{GBW}/|A_{\text{cl}}|$；反相放大器应按噪声增益估算。
- 增益越高，带宽越窄（ tradeoff）

### 6.3 多级级联 (Cascaded Op Amps)

理想缓冲条件下，两级串接且前一级输出直接驱动后一级输入，整体电压增益为 $A_{v,\mathrm{total}}=A_{v1}A_{v2}$；若三级则继续相乘。每一级的有限输入/输出阻抗、带宽、输出摆幅、失调和负载都可能改变乘积关系，应逐级验算，不能只检查最终输出。

---

## 相关笔记

- [[Small Signal Circuit Representation]] —— 运放开环增益 / 输入输出阻抗的物理来源
- [[Impedance]] —— 运放的输入阻抗（虚断）与输出阻抗（负反馈降低）
- [[Frequency Response]] —— 运放 GBW / 带宽限制 / 相位补偿
- [[Filters]] —— Sallen-Key 有源滤波器；区分实际低通与理想积分器
- [[Diode]] —— 运放饱和时的削波（与二极管削波的联系）
- [[Large-Signal Model]] —— 运放的饱和模型（非线性特性）
- [[Amplifiers and Feedback]] —— 负反馈理论 / 振荡器（Barkhausen 条件）
- [[Instrumentation Amplifier]] —— 三运放仪表放大器、差分增益与共模抑制
- [[Resistor-Weighted Digital-to-Analog Converter]] —— 电阻加权求和的 4 bit DAC
- [[Complex Numbers and Euler's Formula]] —— 相量法在运放交流分析中的应用
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
