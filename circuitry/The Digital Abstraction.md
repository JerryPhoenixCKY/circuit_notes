---
aliases:
  - 数字抽象
  - 数字抽象概述
  - Digital Abstraction
  - 离散化取值
  - 数字化
tags: [电路原理, 数字电路, 6.002]
---

# The Digital Abstraction（数字抽象）

> [!NOTE] 本讲定位
> MIT 6.002 Lecture 4。在「集总电路抽象 ([[Lumped Matter Discipline|LMD]])」与「线性电路分析工具箱（[[Superposition Theorem|叠加]] / [[Thevenin's Theorem|戴维南]] / [[Norton's Theorem|诺顿]]，见 [[Basic Circuit Analysis Method]]）」之后，本讲把**取值**也离散化，从模拟世界跨入数字世界。核心问题只有一个：**如何用会出错的模拟电压，可靠地表示 0 与 1？**

## 一、为什么需要数字抽象？（动机）

模拟信号处理的例子（课件第 4 页）：两个电压源 $V_1, V_2$ 各经电阻 $R_1, R_2$ 接到输出节点 $V_0$，由叠加原理：

$$V_0 = \frac{R_2}{R_1+R_2}V_1 + \frac{R_1}{R_1+R_2}V_2$$

当 $R_1 = R_2$ 时 $V_0 = (V_1 + V_2)/2$ —— 一个纯电阻「加法器」。

> [!WARNING] 模拟的根本弱点：噪声
> 噪声（课件第 5 页的红色毛刺）会叠加在导线上。模拟电压取值连续，**噪声让我们难以区分 3.1V 与 3.2V 这样的微小差别**——只要噪声幅度接近信号差值，接收方就「啊？」无法判断。工具的精度被噪声死死限制。

## 二、取值离散化 (Value Discretization)

**关键一步：把取值限制为两种之一**（课件第 6 页）：

| 编码 | HIGH | LOW |
| :--- | :--- | :--- |
| 电压 | 5V | 0V |
| 逻辑 | TRUE (T) | FALSE (F) |
| 二进制 | 1 | 0 |

- 多 bit 的 0/1 串可表示任意大的数（正如多个十进制位表示 >9 的数）：二进制 `101` = 十进制 `5`。
- 于是「模拟加法器」升级为「数字门」：输入/输出退化为 0/1，噪声只需「不把 0 推成 1、不把 1 推成 0」即可。

## 三、数字系统模型 (Digital System)

```mermaid
flowchart LR
    S[sender<br/>发送端 V_S] -->|noise V_N| R[receiver<br/>接收端 V_R]
```

- 发送端输出 $V_S$，经过带噪声的导线（噪声电压叠加 $V_N$，例如 $V_N = 0.2\text{V}$），接收端得到 $V_R = V_S + V_N$。
- 只要 $V_R$ 仍落在接收端判读的合法区间（HIGH 或 LOW），0/1 就被正确还原。

> [!TIP] 抗噪能力的来源
> 模拟：3.1V 与 3.2V 要靠精度分辨。数字：只要 5V 的 0.2V 抖动仍 > 2.5V 阈值，就还是「1」。**把「精确比较」换成「区间判读」，噪声容限就诞生了。**

## 四、电压阈值与禁区 (Voltage Thresholds & Forbidden Region)

「1」与「0」并非单点电压，而是**电压区间**（课件第 9–10 页）：

- 设电源电压 5V、阈值 2.5V：则 $V \ge 2.5\text{V} \Rightarrow 1$，$V \le 2.5\text{V} \Rightarrow 0$。此时高/低噪声容限各 2.5V。
- 更稳健：为 1 设区间 $V_H \in [3\text{V}, 5\text{V}]$，为 0 设区间 $V_L \in [0\text{V}, 2\text{V}]$，中间 $2\text{V}\sim3\text{V}$ 划为 **forbidden region（禁区 / 无主之地）**。

> [!IMPORTANT] 禁区是「容错缓冲区」
> 发送端只承诺输出落在 $V_H$ 或 $V_L$ 内、绝不进入禁区；接收端也只在禁区之外判读。**两者之间的缝隙就是噪声容限的物理载体。**

## 五、两条延伸主线

数字抽象的正确性，由两个更严格的工程框架保证：

1. **静态纪律 ([[Static Discipline]])**：用四个阈值（$V_{OH}, V_{IH}, V_{IL}, V_{OL}$）把「区间判读」量化成可计算的噪声容限，并用电压传输特性 (VTC) 解释增益如何「再生」信号。
2. **组合逻辑 ([[Combinational Logic]])**：把 0/1 当作布尔变量，用门电路（AND/OR/NOT/NAND）实现任意组合函数，且门作为「黑箱」遵守静态纪律。

## 相关笔记

- [[Lumped Matter Discipline]] —— 本讲建立在「集总电路抽象」之上（课件第 2 页 Review）
- [[Superposition Theorem]] / [[Basic Circuit Analysis Method]] —— 模拟加法器即由叠加原理求出
- [[Static Discipline]] / [[Combinational Logic]] —— 本讲延伸出的两条主线
