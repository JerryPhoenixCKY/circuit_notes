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

![[opamp_symbol.svg]]

> **运放电路符号**（5 个功能端口）：同相输入 $v_+$、反相输入 $v_-$、输出 $v_o$、正供电 $V_{S+}$、负供电 $V_{S-}$。供电端在简化图中常省略，实际电路必须连接。

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

$$v_o=A(v_+-v_-)\qquad\text{（开环、未饱和、输出无负载的简化式）}$$

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

![[opamp_basic_circuits.svg]]

> **四种基本运放电路**：同相放大、反相放大、电压跟随器、差分放大器

### 3.1 同相放大器 (Non-Inverting Amplifier)

> 上排左图

$$\boxed{A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = 1 + \frac{R_f}{R_1}}$$

- **增益**：永远 $\ge 1$（最小值是 $1$，即电压跟随器）
- **输入阻抗**：$R_{\text{in}} \approx \infty$（虚断）
- **输出阻抗**：$R_{\text{out}} \approx 0$（负反馈降低输出阻抗）
- **相位**：同相（$v_{\text{out}}$ 与 $v_{\text{in}}$ 同方向）

> [!EXAMPLE] $R_f=9\text{k}\Omega,\ R_1=1\text{k}\Omega \Rightarrow A_v=10$
> $v_{\text{out}} = 10\times v_{\text{in}}$，输入 $0.5$ V $\to$ 输出 $5$ V（在线性范围内）

### 3.2 反相放大器 (Inverting Amplifier)

> 上排右图

$$\boxed{A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = -\frac{R_f}{R_1}}$$

- **增益**：可大可小，符号为负（输出与输入反相 $180^\circ$）
- **输入阻抗**：$R_{\text{in}} = R_1$（电流从 $v_{\text{in}}$ 经 $R_1$ 流入运放虚地）
- **"虚地 (Virtual Ground)"**：$v_-$ 被强制到接近 $0$ V（虚短 + $v_+=0$）

> [!NOTE] 虚地
> 反相放大器中 $v_+=0$（接地），虚短 $\Rightarrow v_-\approx 0$。因此 $v_-$ 是一个"虚假的接地"，称为**虚地 (Virtual Ground)**。输入电流 $i_{\text{in}} = v_{\text{in}}/R_1$，全部流入 $R_f$。

若把电压源和 $R_1$ 换成**注入反相求和节点的电流源** $i_{in}$，同一 KCL 给出 $v_o=-i_{in}R_f$：这是跨阻放大器（transimpedance amplifier）的理想关系，单位检查为 $\mathrm A\cdot\Omega=\mathrm V$。输入电流方向若改为从节点流出，输出符号也相反。

### 3.3 电压跟随器 (Voltage Follower / Buffer)

> 下排左图（同相放大器的特例：$R_f=0,\ R_1=\infty$）

$$\boxed{A_v = 1 \qquad v_{\text{out}} = v_{\text{in}}}$$

- **单位增益缓冲器**：输入阻抗极高、输出阻抗极低
- **作用**：隔离前后级（不让低阻抗后级拉低前级的信号）

> [!EXAMPLE] 高输出阻抗传感器驱动有采样电容的 ADC
> 若传感器的输出阻抗使 ADC 采样瞬间不能在规定时间内建立到所需精度，可插入跟随器：传感器 $\to$ **跟随器** $\to$ ADC。
> - 跟随器不汲取传感器电流（$R_{\text{in}}=\infty$）
> - 跟随器为 ADC 提供低阻抗驱动（$R_{\text{out}}\approx 0$）

### 3.4 差分放大器 (Differential Amplifier)

> 下排右图（减法器）

对差分放大器取如下标号：$R_1$ 从 $v_1$ 接反相端，$R_2$ 从输出反馈到反相端；$R_3$ 从 $v_2$ 接同相端，$R_4$ 从同相端接地。忽略输入电流并假设负反馈线性，则同相端电位 $v_b=R_4v_2/(R_3+R_4)$，反相端 $v_a=v_b$。对 $v_a$ 列 KCL 得

$$\boxed{v_o=\frac{R_4(R_1+R_2)}{R_1(R_3+R_4)}v_2-\frac{R_2}{R_1}v_1.}$$

要让相同的共模电压在理想模型下抵消，须匹配**电阻比** $R_2/R_1=R_4/R_3$，此时

$$\boxed{v_o=\frac{R_2}{R_1}(v_2-v_1).}$$

- 全部四只电阻相等只是增益为 $1$ 的一个特例，不是差分公式的唯一条件。
- 电阻比失配和运放本身的共模增益都会使共模信号泄漏到输出。弱差分信号测量通常采用高输入阻抗的[[Instrumentation Amplifier|仪表放大器]]；它的推导与共模抑制比见独立笔记。

### 3.5 加法器 (Summing Amplifier)

$$v_{\text{out}} = -\frac{R_f}{R_1}v_1 - \frac{R_f}{R_2}v_2 - \frac{R_f}{R_3}v_3$$

- **虚地原理**：所有输入端被强制到 $v_- \approx 0$（虚地），各路电流独立相加

> [!EXAMPLE] 音频混音器
> 三个音频信号 $v_1,v_2,v_3$ 按权重 $R_f/R_1$ 混合输出，实现混音效果。

同一求和节点还可做电阻加权[[Resistor-Weighted Digital-to-Analog Converter|数模转换器]]；每路输入在 $0$ 和同一参考电压间切换，电阻比决定二进制权重。

### 3.6 积分器 (Integrator)

> 详见 §四·运放 RC 电路

$$v_{\text{out}}(t) = -\frac{1}{RC}\int_0^t v_{\text{in}}(\tau)\,d\tau + v_{\text{out}}(0)$$

### 3.7 微分器 (Differentiator)

$$v_{\text{out}}(t) = -RC\,\frac{dv_{\text{in}}}{dt}$$

### 3.8 带参考电位的反相电路与饱和检查

若反相放大器的同相端接参考电位 $v_b$ 而非地，输入 $v_a$ 经 $R_{in}$ 接反相端，$R_f$ 从输出反馈到反相端，则线性区有

$$\boxed{v_o=\left(1+\frac{R_f}{R_{in}}\right)v_b-\frac{R_f}{R_{in}}v_a.}$$

**步骤是先假设线性，再验算摆幅。** 例如取 $R_{in}=25\,\mathrm{k}\Omega$、$R_f=100\,\mathrm{k}\Omega$、供电 $\pm10\,\mathrm V$，故 $v_o=5v_b-4v_a$。当 $v_a=1\,\mathrm V$ 时，$v_b=0\,\mathrm V$ 给出 $v_o=-4\,\mathrm V$，$v_b=2\,\mathrm V$ 给出 $v_o=6\,\mathrm V$；两者都在简化模型的 $(-10,10)\,\mathrm V$ 线性范围内。当 $v_a=1.5\,\mathrm V$，要严格避免到达限幅边界，须 $-10<5v_b-6<10$，即 $-0.8\,\mathrm V<v_b<3.2\,\mathrm V$。端点对应理想化的限幅边界，实际器件还须留裕量。

---

## 四、运放 RC 电路（积分器 / 微分器 / Sallen-Key）

![[opamp_active_filter.svg]]

> **运放 RC 电路**：积分器（C 反馈）/ 微分器（C 输入）/ Sallen-Key LP / Sallen-Key HP

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
