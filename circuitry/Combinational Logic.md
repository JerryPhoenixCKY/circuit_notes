---
aliases:
  - 组合逻辑
  - Combinational Logic
  - 组合门
  - 布尔逻辑
  - Boolean Logic
  - 逻辑门
  - Logic Gates
tags: [电路原理, 数字电路, 6.002]
---

# Combinational Logic（组合逻辑）

> [!NOTE] 本讲定位
> MIT 6.002 Lecture 4 后半。把数字信号（0/1）当作布尔变量，用逻辑门实现任意组合函数。门作为「黑箱」，对外只暴露接口、内部无需关心——前提是它**遵守 [[Static Discipline|静态纪律]]**。

## 一、数字信号 → 布尔逻辑

- 两个离散值自然映射到布尔代数：$1 \leftrightarrow \text{TRUE (T)}$，$0 \leftrightarrow \text{FALSE (F)}$。
- 也可表示数字（多位二进制）；本讲聚焦「组合」——输出只由**当前输入**决定（无记忆、无时序）。

## 二、基本逻辑门 (Basic Logic Gates)

![[logic_gates.svg]]

| 门 | 布尔式 | 语义 |
| :--- | :--- | :--- |
| AND | $Z = X \cdot Y$ | 仅当 $X=1$ 且 $Y=1$ 时 $Z=1$（两者皆真） |
| OR | $Z = X + Y$ | 任一为 1 则 $Z=1$（至少一真） |
| NOT (Inverter) | $Z = \overline{X}$ | 取反：$X=0\Rightarrow Z=1$，$X=1\Rightarrow Z=0$ |
| NAND | $Z = \overline{X \cdot Y}$ | AND 后再取反（「非与」） |

> [!NOTE] 符号约定
> 「·」表示 AND，「+」表示 OR，上划线 $\overline{(\cdot)}$ 表示 NOT。NAND = AND 输出端加气泡 (bubble)。

**真值表示例（AND，枚举全部 $2^n$ 输入组合）：**

| X | Y | Z |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

> [!TIP] 真值表 = 函数的完整定义
> 一个 $n$ 输入的组合函数，穷举 $2^n$ 行即可唯一确定。它是门电路最底层的「真理表」。

## 三、组合门抽象 (Combinational Gate Abstraction)

> [!IMPORTANT] 组合门的两大契约
> 1. **遵守静态纪律**：输入在合法区 ⇒ 输出必在合法区（见 [[Static Discipline]]）。
> 2. **输出仅为输入的函数**：$Z = f(X, Y, \dots)$，与过去无关、无内部状态。

- 于是数字逻辑设计者**不需要知道门内部是什么**（课件第 16 页小猫黑箱图）：只看接口。
- 这把「电路物理」彻底抽象成「逻辑函数」，是能搭出 CPU 的关键一步。

## 四、噪声免疫演示 (Noise Demo)

课件第 17 页演示：输入 $X$ 被刻意注入噪声（高/低电平上都叠加锯齿毛刺），只要没越过阈值进入禁区，AND 门输出 $Z = X \cdot Y$ 仍然**干净**。

> [!NOTE] 这就是静态纪律的回报
> 模拟加法器（见 [[The Digital Abstraction]] 的 $V_0$ 例子）会被噪声污染；而一个遵守纪律的数字门，能「滤掉」不越界的噪声，输出标准 0/1。

## 五、布尔恒等式 (Boolean Identities)

| 恒等式 | 说明 |
| :--- | :--- |
| $X \cdot 1 = X$ | 与恒真相与 |
| $X \cdot 0 = 0$ | 与恒假相与 |
| $X + 1 = 1$ | 与恒真相或 |
| $X + 0 = X$ | 与恒假相或 |
| $\overline{1} = 0,\ \overline{0} = 1$ | 取反 |
| $AB + AC = A(B + C)$ | 分配律（提取公因子） |

> [!NOTE] 课件笔误提醒
> Lecture 4 第 20 页把 $X \cdot 0$ 误写为 $X \cdot 0 = X$，正确应为 $X \cdot 0 = 0$。上表已修正。

## 六、门级电路实现 (Gate-level Implementation)

例（课件第 20 页）：实现

$$\text{output} = A + \overline{B \cdot C}$$

两级结构：

1. 第一级 **NAND** 门对 $B, C$ 求与非：$\overline{B \cdot C}$。
2. 第二级 **OR** 门把 $A$ 与 $\overline{B \cdot C}$ 求或：$\text{output} = A + \overline{B \cdot C}$。

> [!TIP] 任何组合函数都可 gate-level 实现
> 由布尔恒等式 + 基本门（尤其 NAND 是「通用门」），任意真值表都能综合成门电路。这是从「抽象」到「可制造芯片」的桥梁。

## 相关笔记

- [[The Digital Abstraction]] —— 数字抽象动机与系统模型
- [[Static Discipline]] —— 门能当黑箱的前提（输入合法 ⇒ 输出合法）
- [[Superposition Theorem]] / [[Basic Circuit Analysis Method]] —— 真正的门内部仍是模拟电路，分析方法仍是这些线性工具
