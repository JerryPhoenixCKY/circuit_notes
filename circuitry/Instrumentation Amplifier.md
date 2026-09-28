---
tags:
  - 电路学
  - 运算放大器
  - 测量电路
  - 课程笔记
date: 2026-09-28
aliases:
  - Instrumentation Amplifier
  - 仪表放大器
  - In-Amp
---

# Instrumentation Amplifier（仪表放大器）

仪表放大器（instrumentation amplifier, in-amp）用于从较大的共模电位中提取微弱的**差分电压**（differential voltage）。三运放结构的前两级提供高输入阻抗并放大差分信号，末级用电阻匹配的[[Operational Amplifier#3.4 差分放大器 (Differential Amplifier)|差分放大器]]相减。典型应用是[[Wheatstone Bridge and Wye-Delta Transformation|电桥]]、传感器与小信号测量。

![[opamp_instrumentation_three_stage.svg]]

图中同名网络标签 `N1`、`N2` 各表示同一电气节点。$V_1,V_2$ 相对同一参考地；$V_1',V_2'$ 是前级输出，$V_o$ 是末级输出。$R_{gain}$ 是两个反相节点之间的增益电阻，上下两只前级反馈电阻同为 $R_1$；末级两只输入电阻同为 $R_2$，反馈/接地电阻同为 $R_3$。供电脚在信号示意图中省略，实际电路必须连接。

## 差分增益推导

先假设三个运放都处于**稳定的负反馈线性区**，且可用理想模型 $i_+=i_-=0$、$v_+=v_-$。前级两个反相节点因而分别为 $V_1$、$V_2$。沿 $R_{gain}$ 从上到下定义电流

$$i_g=\frac{V_1-V_2}{R_{gain}}.$$

由于输入端不汲取电流，同一电流还必须流经上下两个 $R_1$，故

$$V_1'-V_1=i_gR_1,\qquad V_2-V_2'=i_gR_1,$$

$$\boxed{V_1'-V_2'=\left(1+\frac{2R_1}{R_{gain}}\right)(V_1-V_2).}$$

末级是**匹配比值** $R_3/R_2$ 的差分放大器，输出为 $V_o=(R_3/R_2)(V_2'-V_1')$。因此，以 $V_d=V_2-V_1$ 为输入差分电压，整体增益为

$$\boxed{V_o=A_dV_d,\qquad A_d=\left(1+\frac{2R_1}{R_{gain}}\right)\frac{R_3}{R_2}.}$$

括号与电阻比都无量纲，故 $A_d$ 无量纲；交换 $V_1,V_2$ 时 $V_o$ 应翻转符号。若 $R_{gain}\to\infty$，前级退化为两个缓冲器，整体增益为 $R_3/R_2$。这一极限也验证了式子的形式。

## 共模抑制与适用边界

定义**共模电压**（common-mode voltage）$V_{cm}=(V_1+V_2)/2$，真实电路更一般地写为

$$V_o=A_d(V_2-V_1)+A_{cm}V_{cm}+V_{off},\qquad
\mathrm{CMRR}=\left|\frac{A_d}{A_{cm}}\right|,\qquad
\mathrm{CMRR}_{dB}=20\log_{10}\mathrm{CMRR}.$$

$A_{cm}$ 是共模到输出的增益，$V_{off}$ 是汇总的输出失调电压；若 $A_{cm}=0$，理想 CMRR 趋于无穷大。末级的两组 $R_3/R_2$ 若失配，输入共模即使在理想运放模型下也不能完全抵消；运放本身的 CMRR、失调与输入偏置电流又会叠加误差。测量前还须检查**输入共模范围**（input common-mode range）、两个前级输出的摆幅、末级输出摆幅、供电、频率和负载。高输入阻抗不能消除这些限制，也不能在超出范围时继续套用虚短。

> [!example] 10 mV 差分信号
> 令 $R_1=10\,\mathrm{k}\Omega$、$R_{gain}=2\,\mathrm{k}\Omega$、$R_2=10\,\mathrm{k}\Omega$、$R_3=20\,\mathrm{k}\Omega$，理想差分增益 $A_d=(1+2\cdot10/2)(20/10)=22$。若 $V_1=1.002\,\mathrm V$、$V_2=1.012\,\mathrm V$，则 $V_d=10\,\mathrm{mV}$、$V_{cm}=1.007\,\mathrm V$，有 $V_o=22\times10\,\mathrm{mV}=0.220\,\mathrm V$。
> 前级分别为 $V_1'=0.952\,\mathrm V$、$V_2'=1.062\,\mathrm V$，差为 $110\,\mathrm{mV}$；末级再放大 2 倍。输出的符号和量级均与推导相符。仍须按所选器件确认各节点没有超出输入/输出允许范围。

## 复习检查

1. 为什么 $R_{gain}$ 越小，差分增益越高？当 $V_1=V_2$ 时它流过电流吗？
2. 哪些电阻需要**比值匹配**，而不是要求所有电阻绝对阻值相同？
3. 给定供电与共模电压时，是否检查了**每一只**运放的线性范围？

相关：[[Operational Amplifier]]、[[Amplifiers and Feedback]]、[[Wheatstone Bridge and Wye-Delta Transformation]]、[[Kirchhoff's Laws]]、[[cs6.002x.1]]。
