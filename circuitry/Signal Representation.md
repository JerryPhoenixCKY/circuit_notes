---
tags:
  - 电路学
  - 信号与系统
  - 课程笔记
date: 2026-09-06
aliases:
  - 信号表示
  - 信号表达
  - 信号表征
  - Signal Representation
  - 模拟信号
  - Analog Signal
  - 数字信号
  - Digital Signal
  - 取值离散化
  - Value Discretization
---

# Signal Representation（信号表示）

> [!NOTE] 本笔记定位
> 对应教材 Ch.1.8 *Signal Representation*。电路处理的对象——**信号 (signal)**——如何被分类与抽象：模拟信号 vs 数字信号（取值离散化）。这是 [[The Digital Abstraction|数字抽象]] 的物理出发点。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、模拟信号 (Analog Signal)

取值**连续**的信号：在时间和幅度上都可取任意实数值。

$$x_a(t) \in \mathbb{R},\qquad \forall\,t$$

例：正弦波 $x(t)=A\sin(\omega t)$、温度、声音——任意中间值都有物理意义。

---

## 二、数字信号 (Digital Signal) — 取值离散化

> [!IMPORTANT] 取值离散化 (Value Discretization)
> 数字信号只允许取**有限个离散值**（典型 $0/1$，即 LOW / HIGH）。连续模拟量被**量化 (quantize)** 到最近的合法电平，**主动丢弃多余精度**，换取极强的抗噪声能力。

下图：同一信息的**模拟**表示（连续正弦，上）vs **数字**表示（仅取两电平、按采样点保持，下）：

![[signal_analog_digital.svg]]

---

## 三、为什么数字更抗噪？

模拟信号叠加噪声后，数值被**永久改变**；数字信号只要噪声未把电平推过**阈值 (threshold)**，接收端就能无错还原。

> [!TIP] 模拟 vs 数字
> - **模拟** = 保真但娇气（一点噪声就失真）
> - **数字** = 粗糙但皮实（只要不跨阈值就原样还原）
>
> 现代电子几乎全面数字化，根源就是这一步"取值离散化"。系统化的离散化理论与阈值设计见 [[Static Discipline|静态纪律]] 与 [[The Digital Abstraction|数字抽象]]。

---

## 相关笔记

- [[The Digital Abstraction]] —— 数字抽象（系统化的离散化理论）
- [[Static Discipline]] —— 静态纪律（阈值与噪声容限）
- [[Combinational Logic]] —— 组合逻辑（数字信号的函数处理）
- [[The Circuit Abstraction]] —— 信号是抽象要处理的"对象"
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
