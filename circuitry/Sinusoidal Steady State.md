---
tags:
  - 电路学
  - 正弦稳态
  - 相量法
  - 课程笔记
date: 2026-09-08
aliases:
  - Sinusoidal Steady State
  - 正弦稳态
  - 稳态响应
  - Sinusoidal Steady-State Response
  - 复指数激励
  - 相量
  - Phasor
  - Phasor Method
  - 复数激励
---

# Sinusoidal Steady State（正弦稳态）

> [!NOTE] 本笔记定位
> **动态电路分析的核心入口**：当输入是**正弦激励**（$v(t)=V_m\cos(\omega t+\phi)$）时，线性时不变 (LTI) 电路达到稳态后，**所有支路电压电流都是同频率 $\omega$ 的正弦波**，只是幅值和相位不同。这使得我们可以用**相量 (Phasor)** 把微分方程变成复数代数方程——这是 [[Impedance]] 和整个频域分析的起点。
> 承上：[[First-Order Transients]]（时域暂态）与 [[Second-Order Transients]]（LC/RLC 振荡）；启下：[[Impedance]]（复阻抗）/ [[Frequency Response]]（频率响应）/ [[Resonance]]（谐振）。
> 与 [[cs6.002x.1|知识树]] 互链。

---

## 一、为什么研究正弦稳态？

### 1.1 正弦波的普遍性

自然界和工程中的交流信号几乎都是正弦波（或叠加多个正弦波）：

| 来源 | 频率范围 | 典型应用 |
| :--- | :--- | :--- |
| 电力系统 | 50/60 Hz | 家庭/工业电网 |
| 音频 | 20 Hz–20 kHz | 音响、语音 |
| 射频 (RF) | kHz–GHz | 无线通信 |
| 载波调制 | MHz–GHz | AM/FM/数字调制 |

> [!IMPORTANT] 傅里叶定理
> **任意周期信号**都可以分解为一系列**不同频率的正弦波叠加**（直流分量 + 基波 + 谐波）。因此：只要会分析**单一频率正弦激励**下的响应，就能用叠加原理处理**任意周期信号**。

### 1.2 从暂态到稳态

![[rc_first_order.svg]]
> 典型 RC 一阶电路对正弦激励的响应：$v_{in}(t)$ → $v_{out}(t)$
> 初始的**暂态分量**（指数衰减）消失后，剩余的**稳态分量**就是正弦稳态响应。

$$v_{out}(t) = \underbrace{V_{\text{transient}}(t)}_{\text{暂态：随时间衰减} \to 0} + \underbrace{V_{\text{steady}}(t)}_{\text{稳态：永存的正弦波}}$$

> [!NOTE] 稳态 vs 暂态
> 暂态（Transient）来自**初始条件**，会随时间衰减；稳态（Steady-State）是**强制响应**，由输入信号持续驱动，与初始条件无关。正弦稳态研究的就是这部分。

---

## 二、复指数表示法 (Complex Exponential Representation)

### 2.1 欧拉公式的回响

$$e^{j\theta} = \cos\theta + j\sin\theta, \qquad e^{-j\theta} = \cos\theta - j\sin\theta$$

由此可得：
$$\cos\theta = \frac{e^{j\theta}+e^{-j\theta}}{2}, \qquad \sin\theta = \frac{e^{j\theta}-e^{-j\theta}}{2j}$$

> [!NOTE] 正弦 ↔ 复指数的对应
> $$V_m\cos(\omega t+\phi) = \Re\{V_m e^{j(\omega t+\phi)}\} = \Re\{(V_m e^{j\phi})\,e^{j\omega t}\}$$
> 括号里的 $V_m e^{j\phi}$ 就是**相量 (Phasor)**，不含时间 $t$。

### 2.2 相量的定义

$$\boxed{\tilde{V} = V_m e^{j\phi} = V_m\angle\phi}$$

- **相量 (Phasor)**：复数，携带正弦波的**幅值 $V_m$** 和**相位 $\phi$**
- **频率 $\omega$** 不包含在相量里（因为所有信号共享同一 $\omega$）
- 上标波浪 `~` 或粗体表示相量

> [!TIP] 相量的物理直觉
> 相量是复平面上一根**旋转的矢量**：
> - 长度 = 幅值 $V_m$
> - 角度 = 初相 $\phi$
> - 角速度 = $\omega$（所有相量以相同速度旋转，相对位置不变）
>
> ![[phasor.svg]]

### 2.3 相量的时域恢复

给定相量 $\tilde{V}=V_m\angle\phi$ 和频率 $\omega$：
$$v(t) = \Re\{\tilde{V}\,e^{j\omega t}\} = V_m\cos(\omega t+\phi)$$

---

## 三、元件的相量关系

把 $v(t)=\Re\{\tilde{V}e^{j\omega t}\}$ 代入各元件的本构关系，得到**相量代数方程**：

| 元件 | 时域关系 | 相量关系（代入 $v=\Re\{\tilde{V}e^{j\omega t}\}$） |
| :--- | :--- | :--- |
| **电阻 R** | $v_R = Ri_R$ | $\tilde{V}_R = R\,\tilde{I}_R$（同相） |
| **电容 C** | $i_C = C\,dv_C/dt$ | $\tilde{V}_C = \dfrac{1}{j\omega C}\,\tilde{I}_C = -j\frac{1}{\omega C}\,\tilde{I}_C$（电流超前 90°） |
| **电感 L** | $v_L = L\,di_L/dt$ | $\tilde{V}_L = j\omega L\,\tilde{I}_L$（电压超前 90°） |

> [!IMPORTANT] 相量关系即欧姆定律的推广
> $\tilde{V}=Z\,\tilde{I}$，其中 $Z$ 是**阻抗 (Impedance)**，见 [[Impedance]]。
> - 电阻：$Z_R = R$（实数，同相）
> - 电容：$Z_C = 1/(j\omega C) = -j/\omega C$（纯虚数，电流超前）
> - 电感：$Z_L = j\omega L$（纯虚数，电压超前）

---

## 四、正弦稳态求解步骤（相量法）

### 4.1 标准流程

1. **写出时域电路**，确定输入 $v_s(t)=V_m\cos(\omega t+\phi_s)$
2. **写出相量**：$\tilde{V}_s = V_m\angle\phi_s$
3. **把所有元件替换为阻抗** $Z_R=R$、$Z_C=1/(j\omega C)$、$Z_L=j\omega L$
4. **用直流电路分析方法**（KCL/KVL、串并联化简、戴维南/诺顿）求解相量 $\tilde{V}$、$\tilde{I}$
5. **恢复时域**：$v(t)=\Re\{\tilde{V}e^{j\omega t}\}$

> [!NOTE] 为什么相量法有效？
> 线性时不变系统对正弦激励的响应，稳态部分仍是同频率 $\omega$ 的正弦波。相量变换把**微分方程**（含 $d/dt$）变成**复数代数方程**（不含微分），大大简化分析。

### 4.2 电路定律的相量形式

$$\boxed{\sum\tilde{V}=0 \quad\text{(相量形式的 KVL)}}$$
$$\boxed{\sum\tilde{I}=0 \quad\text{(相量形式的 KCL)}}$$

> [!WARNING] 注意：相量相加须用**复数加法**（实部+实部，虚部+虚部）
> 不是幅值直接相加！相位不同（相位差非零）时，代数和的幅值小于各幅值之和。

---

## 五、齐次解 + 特解 = 完整解

线性常系数微分方程的全解：
$$v(t) = \underbrace{v_h(t)}_{\text{齐次解（暂态）}} + \underbrace{v_p(t)}_{\text{特解（稳态）}}$$

### 5.1 齐次解 $v_h(t)$

由特征方程决定，对应**固有响应 (natural response)**：
- RC 一阶：$v_h(t)=A\,e^{-t/(RC)}$（衰减到 0）
- RL 一阶：$v_h(t)=A\,e^{-Rt/L}$
- LC/RLC：振荡衰减（详见 [[Second-Order Transients]]）

> [!NOTE] 关键：暂态分量一定衰减
> 稳定 LTI 系统的齐次解，指数项的指数**实部为负**（电阻耗能），最终 $v_h(t)\to 0$。只剩稳态特解。

### 5.2 特解 $v_p(t)$

用相量法求得：设 $v_p(t)=V_m\cos(\omega t+\phi)$，代入微分方程解得 $V_m,\phi$。

**特解 = 正弦稳态响应**（与输入同频率的正弦波）。

### 5.3 图示：暂态 → 稳态

$$\boxed{v(t) = \underbrace{A\,e^{-\alpha t}\cos(\omega_d t+\psi)}_{\text{齐次解（指数衰减）}} + \underbrace{V_m\cos(\omega t+\phi)}_{\text{特解（永存）}}}$$

其中 $\alpha$ 是阻尼系数（与 [[Second-Order Transients]] 中的 $\alpha = R/(2L)$ 一致）。

---

## 六、与时域解的对比

| 方法 | 工具 | 方程类型 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **时域微分方程** | $d/dt$ → 特征方程 | 常系数 ODE | 暂态分析、初始条件 |
| **相量法（频域）** | $j\omega$ → 复数代数 | 代数方程 | 正弦稳态（$\omega$ 已知） |
| **拉普拉斯变换** | $s$ → 代数 | 代数方程（通用） | 任意输入、含初始条件 |

> [!NOTE] 相量法是拉普拉斯变换在 $s=j\omega$（纯虚轴）上的特例
> 拉普拉斯把 $d/dt\to s$，相量法把 $d/dt\to j\omega$。两者都是把微分方程变成代数方程——相量法更简洁，但只适用于正弦稳态。

---

## 相关笔记

- [[First-Order Transients]] —— RC / RL 暂态（一阶微分方程）
- [[Second-Order Transients]] —— LC / RLC 暂态（固有振荡、阻尼）
- [[Impedance]] —— 阻抗的定义、RC/RL/LC 的阻抗、相量欧姆定律
- [[Frequency Response]] —— 频率响应 $H(j\omega)$、Bode 图
- [[Resonance]] —— LC 谐振的物理（$\omega_0=1/\sqrt{LC}$）
- [[Complex Numbers and Euler's Formula]] —— 欧拉公式（相量法的数学基础）
- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
