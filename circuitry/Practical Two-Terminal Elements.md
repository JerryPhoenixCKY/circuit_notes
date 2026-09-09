---
tags:
  - 电路学
  - 电路抽象
  - 元件
  - 课程笔记
date: 2026-09-06
aliases:
  - 实际二端元件
  - 实际两端元件
  - 实际元件
  - 实际电压源
  - Practical Two-Terminal Elements
  - Practical Elements
  - 电池
  - Battery
  - 线性电阻
  - Linear Resistor
  - 关联变量约定
  - AVD
  - Associated Variables Discipline
---

# Practical Two-Terminal Elements（实际二端元件）

> [!NOTE] 本笔记定位
> 对应教材 Ch.1.5 *Practical Two-Terminal Elements*。承接 [[The Circuit Abstraction|电路抽象]] 与 [[Lumped Matter Discipline|LMD]]，介绍**尽量贴近真实器件**的二端元件模型：电池（含内阻）、线性电阻，以及贯穿全书的**关联变量约定 (AVD, Associated Variables Discipline)**。
> 与 [[cs6.002x.1|知识树]] 互链；理想化版本见 [[Ideal Two-Terminal Elements]]。

---

## 一、实际电压源：电池 (Battery with Internal Resistance)

真实电池**不是**理想电压源——它有内阻 $R_{int}$。工程模型 = 一个理想电压源 $V_s$ **串联**内阻 $R_{int}$，再接负载 $R_L$：

列回路方程（设电流 $i$ 顺时针）：

$$V_s = i\,R_{int} + i\,R_L = i(R_{int}+R_L)$$

端口（负载两端）实际电压：

$$V_{out} = V_s - iR_{int} = V_s\frac{R_L}{R_{int}+R_L}$$

> [!IMPORTANT] 带载特性
> - $R_L \to \infty$（开路）：$V_{out} = V_s$（端电压最高）
> - $R_L \to 0$（短路）：$i \to V_s/R_{int}$，端电压塌为 0
> - **负载越重（电流越大），端电压跌得越多** —— 这是实际电源与理想电源（电压纹丝不动）的本质区别。

---

## 二、线性电阻 (Linear Resistor)

实际电阻在额定范围内满足**线性欧姆关系**：

$$v = iR \qquad \text{或} \qquad i = Gv,\; G=1/R$$

其 V–I 特性是过原点的**直线**，斜率为 $R$。所有电阻/电源/电容/电感的 v–i 关系总表见 [[Two-Terminal Element Laws]]。

---

## 三、关联变量约定 (Associated Variables Discipline, AVD)

> [!IMPORTANT] AVD 定义
> 规定**电流 $i$ 的正方向为：从元件标注"+"号的电压端流入元件**。在这个统一约定下：
> $$p = v\,i$$
> 表示元件**吸收 (absorb)** 的功率；若算得 $p<0$，则元件实际在**发出 (deliver)** 功率。

![[avd_element.svg]]

上图：电压 $v$ 定义为上正下负，电流 $i$ 箭头从上端（"+"端）流入元件——这就是 AVD 的标准画法。

> [!TIP] 为什么要有 AVD？
> 没有统一约定，电源、电阻、电容各用各的电流方向，功率符号会乱套。AVD 让"**谁在耗能、谁在供电**"有了唯一判据，是后续所有功率分析（含 [[Maximum Power Transfer Theorem|最大功率传输]]、放大器效率）的基础。

---

## 四、实际元件 → 理想元件

把实际元件的寄生/非理想因素逐步剥离，就得到 [[Ideal Two-Terminal Elements|理想二端元件]]：
- 电池去掉内阻 → 理想电压源
- 电阻忽略温漂/非线性 → 理想电阻
- 导线电阻视为 0 → 理想导线

这种"先理想、后修正"的建模思路，是电路抽象的核心方法论。

---

## 相关笔记

- [[The Circuit Abstraction]] —— 电路抽象（本笔记的框架来源）
- [[Ideal Two-Terminal Elements]] —— 理想二端元件（极限模型）
- [[Two-Terminal Element Laws]] —— 二端元件定律总表（v–i 关系）
- [[Ohm's Law]] —— 欧姆定律（电阻的 v–i 关系）
- [[Lumped Matter Discipline]] —— LMD（抽象成立的约束）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
