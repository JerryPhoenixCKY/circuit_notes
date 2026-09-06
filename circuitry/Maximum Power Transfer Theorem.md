---
tags:
  - 电路学
  - 网络定理
  - 电路分析
date: 2026-09-06
aliases:
  - 最大功率传输定理
  - 最大功率传输
  - 最大功率定理
  - Maximum Power Transfer Theorem
  - Maximum Power Transfer
  - 阻抗匹配
---

# Maximum Power Transfer Theorem（最大功率传输定理）

> [!NOTE] 一句话
> 对**线性含源网络**（经 [[Thevenin's Theorem|戴维南等效]] 为 $V_{Th}$ 与 $R_{Th}$ 串联），当**负载电阻等于等效内阻** $R_L = R_{Th}$ 时，负载获得的**功率最大**。

$$\boxed{R_L = R_{Th} \quad\Longrightarrow\quad P_{L,\max} = \frac{V_{Th}^{2}}{4R_{Th}}}$$

> [!IMPORTANT] 最大功率 ≠ 最高效率
> 在匹配点 $R_L = R_{Th}$ 处，源内阻与负载各分一半电压，**传输效率恰好 50%**。最大功率传输追求的是"负载拿到尽可能多"，而不是"效率高"——这是通信/功放前端常用的准则；电力系统则相反，追求高效率，故意让 $R_L \gg R_{Th}$。

---

## 一、推导（基于戴维南等效）

把任意线性网络对端口等效为戴维南电路，外接负载 $R_L$：

![[thevenin_original.svg]]

回路电流：

$$i = \frac{V_{Th}}{R_{Th} + R_L}$$

负载功率：

$$P_L = i^{2}R_L = \frac{V_{Th}^{2}\,R_L}{(R_{Th} + R_L)^{2}}$$

对 $R_L$ 求极值（令 $\dfrac{dP_L}{dR_L}=0$）：

$$\frac{d}{dR_L}\!\left[\frac{R_L}{(R_{Th}+R_L)^2}\right] = \frac{(R_{Th}+R_L)^2 - R_L\cdot 2(R_{Th}+R_L)}{(R_{Th}+R_L)^4} = 0$$

分子为 0 ⇒ $(R_{Th}+R_L) - 2R_L = 0$ ⇒ $\boxed{R_L = R_{Th}}$。

代回得最大功率：

$$P_{L,\max} = \frac{V_{Th}^{2}\,R_{Th}}{(2R_{Th})^{2}} = \frac{V_{Th}^{2}}{4R_{Th}}$$

---

## 二、功率随 $R_L$ 的变化曲线

![[max_power_curve.svg]]

> [!NOTE] 曲线形状解读
> - $R_L \to 0$：负载短路，$V_{load}\to 0$，功率 $P\to 0$；
> - $R_L \to \infty$：负载开路，电流 $i\to 0$，功率 $P\to 0$；
> - 中间某处出现**单峰**，峰值严格在 $R_L = R_{Th}$。
>
> 因此"匹配 (matching)"即把负载调到峰点。

---

## 三、诺顿视角的等价表述

由 [[Norton's Theorem|诺顿等效]]（$I_N$ 与 $R_N$ 并联，$R_N = R_{Th}$），负载获得最大功率的条件同样是

$$R_L = R_N = R_{Th}$$

此时 $P_{L,\max} = \dfrac{I_N^{2}\,R_N}{4}$（因 $V_{Th}=I_N R_N$，两式等价）。

---

## 四、典型例题

> [!EXAMPLE] 求最大可传功率
> 某线性网络对端口的戴维南等效为 $V_{Th}=12\text{ V}$、$R_{Th}=3\,\Omega$，求接负载时的最大功率及匹配负载值。
>
> 匹配负载：$R_L = R_{Th} = 3\,\Omega$。
> 最大功率：$P_{L,\max} = \dfrac{12^{2}}{4\times 3} = \dfrac{144}{12} = 12\text{ W}$。
> 此时负载电流 $i = 12/(3+3) = 2\text{ A}$，负载电压 $V_L = 2\times 3 = 6\text{ V}$（恰为 $V_{Th}$ 的一半，效率 50%）。

---

## 五、与相关知识点的联系

- **依赖 [[Thevenin's Theorem|戴维南]] / [[Norton's Theorem|诺顿]]**：定理的前提是把网络先等效成单电源 + 单电阻；
- **建立在 [[Resistive Networks|线性电阻网络]] 上**：若网络含非线性元件（[[Analysis of Nonlinear Circuits|非线性电路分析]]），"等效电阻"概念失效，最大功率条件需重新推导；
- **与 [[Ohm's Law|欧姆定律]] 同源**：推导全程只用 $V=IR$ 与分压；
- **工程对照**：音频/射频**阻抗匹配**追求最大功率传输；电力传输追求高效率（故意失配，使 $R_L\gg R_{Th}$）。

---

## 相关笔记

- [[Thevenin's Theorem]] —— 定理的前提：端口等效为 $V_{Th}, R_{Th}$
- [[Norton's Theorem]] —— 诺顿视角下的等价匹配条件
- [[Resistive Networks]] —— 等效电阻、线性网络基础
- [[Ohm's Law]] —— 推导用的元件定律
- [[Superposition Theorem]] —— 同在 Ch.3 的网络定理
- [[Analysis of Nonlinear Circuits]] —— 非线性时本定理不再直接适用
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
