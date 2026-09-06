---
tags:
  - 电路学
  - 电路抽象
  - 元件
  - 课程笔记
date: 2026-09-06
aliases:
  - 理想二端元件
  - 理想两端元件
  - 理想元件
  - Ideal Two-Terminal Elements
  - Ideal Elements
  - 理想电压源
  - Ideal Voltage Source
  - 理想导线
  - Ideal Wire
  - 理想电阻
  - Ideal Resistor
  - 理想电流源
  - Ideal Current Source
  - 元件定律
  - Element Laws
---

# Ideal Two-Terminal Elements（理想二端元件）

> [!NOTE] 本笔记定位
> 对应教材 Ch.1.6 *Ideal Two-Terminal Elements*。给出四类**极限模型**：理想电压源、理想导线（短路）、理想电阻、理想电流源，并给出各自**元件定律 (element law)**。实际版本见 [[Practical Two-Terminal Elements]]，v–i 总表见 [[Two-Terminal Element Laws]]。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、四类理想二端元件

![[ideal_elements.svg]]

| 元件 | 元件定律 (Element Law) | 关键特征 |
| :--- | :--- | :--- |
| 理想电压源 Ideal Voltage Source | $v = V_s$（恒定） | 电压被锁定；电流由外电路决定；内阻 $0$ |
| 理想导线 Ideal Wire（短路） | $v = 0$（电阻 $0\ \Omega$） | 两端等电位，是"短接"的数学理想 |
| 理想电阻 Ideal Resistor | $v = iR$ | 线性欧姆关系，见 [[Ohm's Law]] |
| 理想电流源 Ideal Current Source | $i = I_s$（恒定） | 电流被锁定；电压由外电路决定；内阻 $\infty$ |

> [!IMPORTANT] 理想源的"约束"本质
> 理想电压源**强行固定电压**——电流想多大就多大（由外电路决定）；理想电流源**强行固定电流**——电压想多高就多高。它们不是"提供"固定量，而是对外**施加约束**。这是初学者最容易混淆的点。

---

## 二、元件定律 (Element Laws)

每个理想元件由一条**本构关系 (constitutive relation / element law)** 完全定义。它与 KCL/KVL 并列，是列电路方程的"原材料"：

- 电阻 / 电源：**代数关系**（瞬时 $v,i$ 直接互相决定，无记忆）
- 电容 / 电感：**微分关系**（能储能、产生暂态，详见 [[Two-Terminal Element Laws]] 与后续储能元件章节）

> [!TIP] 理想化建模的方法论
> 真实器件千变万化，但抽象成理想元件后：
> 1. 先用理想模型抓住**主效应**（如放大、开关）；
> 2. 再把非理想因素（内阻、寄生电容/电感）作为**修正项**加回去。
> 这种"理想骨架 + 非理想修正"的思路贯穿全书（如 [[MOSFET]]、[[Operational Amplifier]]）。

---

## 三、理想源的开路 / 短路

- 理想电压源**不允许短路**（短路 ⇒ 电流无限大，物理上不可能，属建模失效）；
- 理想电流源**不允许开路**（开路 ⇒ 电压无限大，同样失效）。
- 实际电源有内阻/饱和，故短路/开路电流电压有限——这正是 [[Practical Two-Terminal Elements|实际元件]] 更"安全"的原因。

---

## 相关笔记

- [[Practical Two-Terminal Elements]] —— 实际二端元件（含内阻电池、AVD）
- [[Two-Terminal Element Laws]] —— 所有元件的 v–i 关系总表
- [[Ohm's Law]] —— 欧姆定律
- [[Superposition Theorem]] —— 电流源在叠加时的置零规则（开路）
- [[The Circuit Abstraction]] —— 电路抽象（理想化是抽象的核心）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
