---
tags:
  - 电路学
  - 器件
  - 半导体
date: 2026-09-06
aliases:
  - MOSFET
  - 金属-氧化物半导体场效应管
  - 场效应管
  - MOS 场效应晶体管
  - Metal–Oxide–Semiconductor Field-Effect Transistor
---

# MOSFET（金属-氧化物半导体场效应管）

> [!NOTE] 占位骨架
> 本笔记对应教材 Ch.6（The MOSFET Switch）与 Ch.7（The MOSFET Amplifier）的器件基础，待按学习进度填充：MOSFET 物理结构、符号（增强/耗尽、N/P 沟道）、三种工作区（截止 Cutoff / 饱和 Saturation / 线性 Triode）、SRC 大信号模型、作为开关的电阻特性、作为放大器的偏置与负载线。
> 详细推导将沉淀于此；当前为框架占位。

## 待填充内容
- 物理结构：栅 (Gate) / 氧化层 / 沟道 (Channel) / 源 (Source) / 漏 (Drain)
- 符号与分类：NMOS / PMOS、增强型 / 耗尽型
- 大信号模型（SRC 模型）：
  - 截止区：$v_{GS} < V_T$，$i_{DS} = 0$
  - 饱和区：$v_{GS} \ge V_T$ 且 $v_{DS} \ge v_{GS}-V_T$，$i_{DS} = \frac{K}{2}(v_{GS}-V_T)^2$
  - 线性区（三极管区）：$v_{DS} < v_{GS}-V_T$，$i_{DS} = K\left[(v_{GS}-V_T)v_{DS} - \frac{v_{DS}^2}{2}\right]$
- 阈值电压 $V_T$、跨导参数 $K$
- 作为开关：导通电阻 $R_{on}$、截止（开路）
- 与 [[Small Signal Analysis|小信号分析]] 的衔接（跨导 $g_m = K(v_{GS}-V_T)$）

---

## 相关笔记
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
- [[The MOSFET Switch]] —— MOSFET 开关（Ch.6 专题，待建）
- [[The MOSFET Amplifier]] —— MOSFET 放大器（Ch.7 专题，待建）
- [[Small Signal Analysis]] —— 小信号分析
- [[Diode]] —— 二极管（Ch.16，待建）
