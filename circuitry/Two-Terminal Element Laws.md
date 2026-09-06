---
tags:
  - 电路学
  - 电路抽象
  - 元件
  - 课程笔记
date: 2026-09-06
aliases:
  - 二端元件定律
  - 元件定律
  - 二端元件法则
  - Two-Terminal Element Laws
  - Element Laws
  - 本构关系
  - Constitutive Relation
  - 伏安特性
  - V-I Characteristic
---

# Two-Terminal Element Laws（二端元件定律）

> [!NOTE] 本笔记定位
> 汇总所有二端元件的**本构关系 (constitutive relation / element law)**，即各自的 $v\text{–}i$ 关系。这是列 KCL/KVL 方程时的"原材料"。配合 [[Ideal Two-Terminal Elements]] 与 [[Practical Two-Terminal Elements]] 使用。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、元件符号速查

![[element_laws.svg]]

---

## 二、v–i 关系总表

| 元件 | 时域定律 (Element Law) | 特性 |
| :--- | :--- | :--- |
| 电阻 Resistor | $v = iR$ | 线性、无记忆、耗能 |
| 理想电压源 Ideal V-Source | $v = V_s$（常数） | 电压锁定，电流由外电路定 |
| 理想电流源 Ideal I-Source | $i = I_s$（常数） | 电流锁定，电压由外电路定 |
| 电容 Capacitor | $i = C\dfrac{dv}{dt}$ | 储能于电场，微分关系 |
| 电感 Inductor | $v = L\dfrac{di}{dt}$ | 储能于磁场，微分关系 |

> [!IMPORTANT] 代数 vs 微分
> - **电阻、电源**是**代数关系**：瞬时 $v,i$ 互相直接决定（**无记忆**）。
> - **电容、电感**是**微分关系**：$v,i$ 互相积分/微分，因而能**储能**、产生暂态（详见 [[First-Order Transients]]、[[Second-Order Transients]]）。

---

## 三、功率与能量

在 AVD 约定下（见 [[Practical Two-Terminal Elements]]），元件吸收功率 $p = vi$：

- 电阻：$p = i^2R \ge 0$，永远耗能
- 电容储能：$E_C = \tfrac12 C v^2$
- 电感储能：$E_L = \tfrac12 L i^2$

> [!TIP] 记忆法
> "电阻/电源管**瞬时**，电容/电感管**历史**"——后者因为含微分/积分，状态依赖过去，所以能存能量、撑起动态电路。

---

## 相关笔记

- [[Ideal Two-Terminal Elements]] —— 理想元件的极限模型
- [[Practical Two-Terminal Elements]] —— 实际元件（含内阻电池、AVD 约定）
- [[Ohm's Law]] —— 欧姆定律详述
- [[Capacitor]] / [[Inductor]] —— 储能元件专题（待建）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
