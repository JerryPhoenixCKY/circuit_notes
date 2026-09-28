---
tags:
  - 电路学
  - 运算放大器
  - 数模转换
  - 课程笔记
date: 2026-09-28
aliases:
  - Resistor-Weighted Digital-to-Analog Converter
  - Binary-Weighted Resistor DAC
  - 电阻加权数模转换器
  - 电阻加权 DAC
---

# Resistor-Weighted Digital-to-Analog Converter（电阻加权数模转换器）

电阻加权数模转换器（resistor-weighted digital-to-analog converter, DAC）把各数字位对应的电压经不同电阻送入[[Operational Amplifier#3.5 加法器 (Summing Amplifier)|反相求和放大器]]。每一位为 $0$ 或同一参考电压 $V_{ref}$，输入电阻依次加倍，因而电流及输出贡献依次减半。以下分析课件[[L4 Op-amp 20260928.pdf#page=46|EIE 2001 Lecture 4，PDF 页 46–47]]的**4 bit 教学电路**，不把它当成所有 DAC 的结构。

![[opamp_resistor_weighted_dac.svg]]

图中四个输入端口代表开关输出：$b_3$（最高有效位，MSB）至 $b_0$（最低有效位，LSB）分别取 $V_{ref}$ 或 $0\,\mathrm V$；同相输入接地，输出经 $R_f$ 反馈至求和节点 $N$。为让后文电阻下标与位号一致，记四支路为 $R_3,R_2,R_1,R_0$，分别对应课件的 $R_1,R_2,R_3,R_4$；图中则直接标阻值比 $R,2R,4R,8R$。实际开关、电源和参考源虽在示意图中简化，仍是电路的一部分。

## 权重与输出公式

假设运放有稳定负反馈、输出未饱和、输入电流可忽略，节点 $N$ 为虚地 $v_N\approx0$。定义 $b_k\in\{0,1\}$，位为 1 时对应支路电压 $v_k=b_kV_{ref}$。对 $N$ 列 [[Kirchhoff's Laws|KCL]]：

$$\sum_{k=0}^{3}\frac{b_kV_{ref}}{R_k}=\frac{-V_o}{R_f}.$$

对课件的取值 $R_f=R_3=10\,\mathrm{k}\Omega$、$R_2=20\,\mathrm{k}\Omega$、$R_1=40\,\mathrm{k}\Omega$、$R_0=80\,\mathrm{k}\Omega$，得到

$$\boxed{V_o=-V_{ref}\left(b_3+\frac{b_2}{2}+\frac{b_1}{4}+\frac{b_0}{8}\right)=-\frac{V_{ref}}8D,\quad D=8b_3+4b_2+2b_1+b_0.}$$

$D$ 是 0–15 的无量纲二进制码；输出负号来自反相结构。$V_o$ 与 $V_{ref}$ 都用 V，电阻比无量纲。若需要正极性输出，可在后级再反相，但应逐级检查摆幅和带宽。

> [!example] $V_{ref}=1\,\mathrm V$
> 相邻码的输出差为 $\Delta V_o=-V_{ref}/8=-0.125\,\mathrm V$，步长幅值为 $0.125\,\mathrm V$。码 `0000` 给 $0\,\mathrm V$，`0001` 给 $-0.125\,\mathrm V$，`0101`（$D=5$）给 $-0.625\,\mathrm V$，`1111` 给 $-1.875\,\mathrm V$。最大码输出幅值为 $15/8\,\mathrm V=1.875\,\mathrm V$，不是 $2.000\,\mathrm V$。课件[[L4 Op-amp 20260928.pdf#page=47|PDF 页 47]]的表头列的是 $-V_o$，所以表内正数对应这里的负输出电压。若所选运放达不到所需负向输出摆幅，大码会削顶而不再线性。

## 从教学电路到实际器件

- **电阻比与位权**：这里要求相邻支路阻值准确呈 $1:2:4:8$；误差会改变位权与码间步长。位数增加时阻值跨度也迅速增大，输入偏置和漏电对高阻 LSB 支路更敏感。
- **开关与参考源**：真实数字位通过开关在 $0$ 与 $V_{ref}$ 之间切换。开关导通电阻、漏电、电平兼容性及参考源输出阻抗都可能改变支路电流。
- **动态性能**：输出建立时间受运放带宽、转换速率（slew rate）、输出负载及切换瞬态限制；本静态公式不预测毛刺或建立时间。
- **范围**：先算全部码的 $V_o$，再按数据手册检查供电、输入共模范围、输出摆幅、负载和所需精度。例如单电源供电且输出不能低于 $0\,\mathrm V$ 的运放，不能直接产生上式所需的负输出。虚地近似只在闭环线性时可用。

相关：[[Operational Amplifier]]、[[Amplifiers and Feedback]]、[[Kirchhoff's Laws]]、[[cs6.002x.1]]。

来源：*EIE 2001 Basic Circuit Theory, Lecture 4: Operational Amplifier*，[[L4 Op-amp 20260928.pdf#page=46|PDF 页 46–47]]；图据课件的电阻加权求和拓扑重绘，公式与数值独立验算。
