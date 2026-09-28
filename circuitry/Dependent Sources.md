---
tags:
  - 电路学
  - 受控源
  - 放大器
  - 课程笔记
aliases:
  - Dependent Sources
  - Dependent Source
  - 受控源
  - 控制源
---

# Dependent Sources（受控源）

受控源的输出电压或电流由**电路中的另一个电压或电流**决定。它把输入端的控制量与输出端的供能能力分开，因此是连接 [[Basic Circuit Analysis Method|电路求解]]、[[The MOSFET Amplifier|MOSFET 放大器]] 和 [[Small Signal Circuit Representation|小信号模型]] 的桥梁。

## 一、控制关系与端口

| 模型 | 控制关系 | 系数单位 |
| :--- | :--- | :--- |
| 电压控制电流源 (VCCS) | $i_o=g v_c$ | $g$：S（西门子） |
| 电流控制电流源 (CCCS) | $i_o=\beta i_c$ | $\beta$：无量纲 |
| 电压控制电压源 (VCVS) | $v_o=\mu v_c$ | $\mu$：无量纲 |
| 电流控制电压源 (CCVS) | $v_o=r_m i_c$ | $r_m$：$\Omega$ |

$v_c,i_c$ 是控制端的电压、电流；$v_o,i_o$ 是输出端的参考电压、电流。先标出各自正方向，再写 KCL/KVL。控制关系也可以是非线性的，例如 $i_o=f(v_c)$；只有 $f$ 为线性函数时，才能直接套用线性叠加。MIT Lecture 8 重点使用 VCCS 说明放大器，见 [[05fef0ad87134781c8f285e47973023b_6002_l8.pdf#page=3|L8，页 3–10]]。

受控源的输出功率可以来自器件的**供电端口**。放大器常画成输入、输出两个信号端口，但还需要电源端口；“信号增益”不等于凭空产生能量。若把有源器件误当作无源受控源，计算出的工作区可能在物理上不可达，见 [[05fef0ad87134781c8f285e47973023b_6002_l8.pdf#page=17|L8，页 17、23–24]]。

## 二、节点法例题：电压控制的电流下拉

设输出节点通过 $R_L=1\,\mathrm{k}\Omega$ 接 $V_S=10\,\mathrm V$，一只 VCCS 从输出节点向参考地吸收 $i_o=g v_c$，其中 $g=2\,\mathrm{mS}$，控制电压 $v_c=2\,\mathrm V$。对输出节点列 KCL：

$$\frac{V_S-v_o}{R_L}=g v_c
\quad\Longrightarrow\quad
v_o=V_S-gR_Lv_c=10\,\mathrm V-4\,\mathrm V=6\,\mathrm V.$$

检查：$i_o=4\,\mathrm{mA}$，电阻压降为 $i_oR_L=4\,\mathrm V$；$v_o$ 介于地和电源之间，与这个下拉模型的工作区相容。功率也闭合：电源提供 $40\,\mathrm{mW}$，电阻消耗 $16\,\mathrm{mW}$，受控源吸收 $24\,\mathrm{mW}$。若公式给出 $v_o<0$，不能继续假定真实 MOSFET 仍遵从相同的电流关系；应重新检查器件工作区。

## 三、从非线性器件到小信号受控源

对于偏置在饱和区的 MOSFET，忽略沟道长度调制，设 $V_{OV}=V_{GS}-V_T>0$：

$$I_D=\frac K2 V_{OV}^{2},\qquad
g_m=\left.\frac{\partial i_D}{\partial v_{GS}}\right|_Q=K V_{OV}=\frac{2I_D}{V_{OV}}.$$

$K$ 的单位为 $\mathrm{A/V^2}$，$g_m$ 的单位为 S。若输入扰动 $|v_{gs}|\ll V_{OV}$，在固定偏置点 $Q$ 附近有 $i_d\approx g_m v_{gs}$：非线性的晶体管在**小信号电路**里成为 VCCS。电源的恒定直流分量在增量电路中为零，偏置电流与电压仍决定 $g_m$。偏置点及饱和条件见 [[The MOSFET Amplifier]]，建模步骤见 [[Small Signal Circuit Representation]]；对应 [[5d9288b54aceb1737d8f831d3c66739b_6002_l9.pdf#page=8|L9，页 8、17–21]] 与 [[223a71c6e0b77090a6bdfd3b28aa1d5f_6002_l11.pdf#page=6|L11，页 6–12]]。

## 四、使用受控源时的检查

1. **控制量必须仍可定义**：做 [[Source Transformation|电源变换]] 时，不要把用于定义 $v_c$ 或 $i_c$ 的支路消掉。
2. **只关闭独立源**：用 [[Superposition Theorem|叠加法]] 或求端口等效电阻时，受控源保持在方程中；必要时加测试源，见 [[Thevenin's Theorem]]。
3. **检查模型工作区和功率**：数学上的 VCCS 可以输出任意功率，真实晶体管受电源轨、截止和饱和区边界约束。

## 来源与关联

- MIT 6.002 *Circuits and Electronics*, Lecture 8, “Dependent Sources and Amplifiers”，[[05fef0ad87134781c8f285e47973023b_6002_l8.pdf|本地课件]]，页 3–10、17、23–24。
- MIT 6.002, Lecture 9 “MOSFET Amplifier: Large Signal Analysis” 与 Lecture 11 “Small Signal Circuits”，见上文对应页。
- [[Circuit Theory Glossary]] · [[cs6.002x.1]]
