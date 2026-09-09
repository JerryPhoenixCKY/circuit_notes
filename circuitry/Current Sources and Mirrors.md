---
tags:
  - 电路学
  - 模拟电路
  - 电流源
  - 占位笔记
date: 2026-09-08
aliases:
  - Current Sources and Mirrors
  - 电流源与电流镜
  - Current Source
  - 电流源
  - Current Mirror
  - 电流镜
  - Bias Current
  - 偏置电流
  - Wilson Current Mirror
  - 威尔逊电流镜
  - Cascode Current Mirror
  - 共源共栅电流镜
---

# Current Sources and Mirrors（电流源与电流镜）

> [!NOTE] 本笔记定位
> 电流源（Current Source）是模拟 IC 设计的基础模块：为放大器提供**恒定偏置电流**（bias current），设定工作点 Q。电流镜（Current Mirror）利用匹配的晶体管把一个参考电流"复制"到多个支路，是 IC 中最常见的偏置技术。本笔记承上启下：[[MOSFET]]（器件特性）→ 电流源/镜（偏置电路）→ [[The MOSFET Amplifier]]（放大器偏置）/ [[Large-Signal Model]]（工作点分析）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、为什么需要电流源？

> [!IMPORTANT] 电流源在放大器中的两个核心作用
> 1. **偏置 (Biasing)**：设定晶体管的工作点 Q（DC operating point），使其工作在饱和区
> 2. **有源负载 (Active Load)**：用大交流输出阻抗 $r_o$ 替代电阻 $R_D$，在不提高电源电压的前提下获得大增益 $A_v = -g_m r_o$

### 1.1 理想电流源 vs 实际电流源

| 参数 | 理想 | 实际（MOSFET 电流源）|
| :--- | :--- | :--- |
| 输出阻抗 $R_{\text{out}}$ | $\infty$ | $r_o = 1/(\lambda I_D)$（有限）|
| 电流精度 | 精确 | 受工艺/温度偏差影响 |
| 面积 | 0 | 晶体管面积 $\propto W/L$ |

---

## 二、基本电流镜 (Basic Current Mirror)

### 2.1 原理

两只匹配的 MOSFET（$M_1$=二极管连接、$M_2$=输出管），$V_{GS}$ 相同 $\Rightarrow$ $I_{D1} = I_{D2}$（忽略沟道长调制）：

$$\boxed{I_{\text{out}} = I_{\text{ref}} \cdot \frac{(W/L)_2}{(W/L)_1}}$$

> [!NOTE] "二极管连接" (Diode-Connected MOSFET)
> 把 $M_1$ 的栅极和漏极短接：$V_G = V_D \Rightarrow V_{GS} = V_{DS}$，使其永远工作在饱和区（$V_{DS} \ge V_{GS} - V_T$）。$M_1$ 的 $I_D$-$V_{GS}$ 关系等同于一个平方律"二极管"。

### 2.2 误差来源

- **沟道长调制 $\lambda$**：$M_1$ 的 $V_{DS1} = V_{GS}$，$M_2$ 的 $V_{DS2}$ 由负载决定，$V_{DS1}\neq V_{DS2} \Rightarrow I_{\text{out}}\neq I_{\text{ref}}$
- **器件失配**：$V_T$ 和 $K$ 的工艺偏差导致 $I_{\text{out}}$ 偏离 $I_{\text{ref}}$

---

## 三、改进型电流镜

| 类型 | 改进点 | 输出阻抗 |
| :--- | :--- | :--- |
| **基本电流镜** | — | $r_{o2}$ |
| **Wilson 电流镜** | 加入反馈管 $M_3$，负反馈稳定 $I_{\text{out}}$ | $\approx g_{m3}r_{o3}r_{o2}$（高）|
| **Cascode 电流镜** | $M_3$ 叠在 $M_2$ 上方，屏蔽 $V_{DS2}$ 变化 | $\approx g_{m3}r_{o3}r_{o2}$（高）|
| **宽幅 Cascode** | 降低 $M_3$ 的 $V_{DS}$ 压降，节省 headroom | 同上但更低压 |

---

## 四、电流源作为有源负载

把放大器的漏极电阻 $R_D$ 换成电流源（PMOS 电流镜），输出阻抗从 $R_D$ 变为 $r_{o,\text{PMOS}} \parallel r_{o,\text{NMOS}}$：

$$A_v = -g_m (r_{o1} \parallel r_{o2})$$

> [!EXAMPLE] 共源放大器有源负载
> - NMOS 放大管 $M_1$：$g_m = 1\text{mS}$，$r_{o1} = 100\text{k}\Omega$
> - PMOS 电流源负载 $M_2$：$r_{o2} = 80\text{k}\Omega$
> - $A_v = -1\text{mS}\times(100\text{k}\parallel 80\text{k}) = -44.4$
> - 如果用 $R_D = 10\text{k}\Omega$：$A_v = -10$（差 4.4 倍）

---

## 相关笔记

- [[MOSFET]] —— MOSFET 器件特性（饱和区平方律、$r_o$）
- [[The MOSFET Amplifier]] —— 放大器偏置与工作点 Q
- [[Large-Signal Model]] —— 大信号模型与工作点计算
- [[Small Signal Circuit Representation]] —— 小信号参数 $g_m, r_o$ 与有源负载增益
- [[Operational Amplifier]] —— 运放内部差分级用电流镜做有源负载
- [[Amplifiers and Feedback]] —— 反馈与偏置稳定性
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）

---

> [!WARNING] 本笔记为占位骨架
> 当前为框架占位，待深入学习 MIT 6.002x 对应章节后填充正文（Wilson/Cascode 推导、失配分析、Bandgap 基准等）。
