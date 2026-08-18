---
tags:
  - 数学工具
  - 电路学
  - 信号与系统
  - 课程笔记
date: 2026-08-15
aliases:
  - 复数与欧拉公式
  - 欧拉公式
  - 欧拉恒等式
  - 反欧拉公式
  - 复数
  - 复平面
  - Euler's Formula and Complex Numbers
  - Euler's Formula
  - Euler's Identity
  - Inverse Euler Formula
  - Complex Number
  - Complex Numbers
  - Complex Representation
---

# 复数与欧拉公式 (Complex Numbers and Euler's Formula)

> [!IMPORTANT] 为什么电路课要学复数？
> 交流 (AC) 电路的稳态分析中，电压、电流都是**同频率的正弦量**，直接解微分方程非常繁琐。复数与欧拉公式把"正弦运算"转化为"复指数代数运算"，将微积分问题变成代数问题——这就是 **相量法 (Phasor Method)** 与 **阻抗 (Impedance)** 概念的数学根基。时域里解微分方程，频域里做代数运算，二者通过欧拉公式连通。

---

## 一、复数 (Complex Number)

> [!NOTE] 定义
> 复数 $z$ 是形如 $x + jy$ 的数，其中 $x, y$ 为实数，$j$ 为虚数单位，满足 $j^2 = -1$（电路领域习惯用 $j$ 而非 $i$，避免与电流 $i$ 混淆）。
> $$z = x + jy$$
> - $x = \operatorname{Re}(z)$ —— 实部 (Real Part)
> - $y = \operatorname{Im}(z)$ —— 虚部 (Imaginary Part)

**几何意义**：复数对应复平面 (Complex Plane) 上的一个点 $(x, y)$，横轴为实轴 (Real Axis)，纵轴为虚轴 (Imaginary Axis)。复数既有"大小"又有"方向"，这正是它能表示正弦量幅值与相位的原因。

---

## 二、复数的三种表示形式 (Complex Representation)

同一复数 $z$ 有三种等价表示，可互相转换：

| 形式                               | 表达式                               | 适用场景    |
| :------------------------------- | :-------------------------------- | :------ |
| **代数形式** (Rectangular)           | $z = x + jy$                      | 加减运算    |
| **三角形式** (Trigonometric)         | $z = r(\cos\theta + j\sin\theta)$ | 理解几何意义  |
| **极坐标/指数形式** (Polar/Exponential) | $z = r e^{j\theta}$               | 乘除、幂与开方 |

三种形式的关系：

$$z = x + jy = r(\cos\theta + j\sin\theta) = r e^{j\theta}$$

```mermaid
graph LR
    A["代数形式 x + jy"] <-->|"x = r cosθ, y = r sinθ"| B["三角形式 r(cosθ + j sinθ)"]
    B <-->|"欧拉公式"| C["指数形式 r e^{jθ}"]
    C <-->|"e^{jθ} = cosθ + j sinθ"| A
```

---

## 三、欧拉公式 (Euler's Formula)

> [!MATH] 欧拉公式
> $$e^{j\theta} = \cos\theta + j\sin\theta$$

这是数学中最优美的公式之一，它将**指数函数**与**三角函数**统一起来。欧拉公式可由泰勒展开 (Taylor Series) 推导：$e^x$、$\cos\theta$、$\sin\theta$ 的麦克劳林级数中，把 $x = j\theta$ 代入 $e^x$ 的展开式，实部恰为 $\cos\theta$ 的展开、虚部恰为 $\sin\theta$ 的展开。

### 运算性质

- **指数相乘**（同底数幂相加）：
  $$e^{j(\alpha+\beta)} = e^{j\alpha} \cdot e^{j\beta}$$
- **微分性质**（求导后乘以 $j$，即相位超前 $90°$）：
  $$\frac{d}{d\theta} e^{j\theta} = j e^{j\theta}$$

> [!TIP] 微分性质的电路含义
> $\dfrac{d}{dt} e^{j\omega t} = j\omega e^{j\omega t}$：对复指数信号求导 = 乘以 $j\omega$。这正是**电容、电感元件的频域阻抗**（$Z_C = \frac{1}{j\omega C}$、$Z_L = j\omega L$）的由来——微分关系在频域中退化为代数关系。

---

## 四、欧拉恒等式 (Euler's Identity)

> [!MATH] 欧拉恒等式
> $$e^{j\pi} + 1 = 0$$

将 $\theta = \pi$ 代入欧拉公式：$e^{j\pi} = \cos\pi + j\sin\pi = -1 + 0$，移项即得。它把数学中五个最重要的常数联系在同一个式子中：$e$、$j$、$\pi$、$1$、$0$。

---

## 五、反欧拉公式 (Inverse Euler Formula)

由欧拉公式解出三角函数：

> [!MATH] 反欧拉公式
> $$\cos\theta = \frac{e^{j\theta} + e^{-j\theta}}{2}, \qquad \sin\theta = \frac{e^{j\theta} - e^{-j\theta}}{2j}$$

**推导**：欧拉公式给出 $e^{j\theta} = \cos\theta + j\sin\theta$ 与 $e^{-j\theta} = \cos\theta - j\sin\theta$，两式相加、相减即可分别解出 $\cos\theta$、$\sin\theta$。

> [!NOTE] 使用价值
> 反欧拉公式把**实信号**分解为**共轭对称的两个复指数**（正频率 + 负频率）。傅里叶分析、调幅信号、滤波器设计都建立在这一分解之上。

---

## 六、模与相角 (Magnitude & Phase)

> [!NOTE] 定义
> 复数的**模** (Magnitude/Modulus) 是它到原点的距离，**相角** (Phase/Argument) 是它与实轴正方向的夹角：
> $$r = |z| = \sqrt{x^2 + y^2}, \qquad \theta = \arg z = \arctan\frac{y}{x}$$

- **模**：对应正弦量的**幅值**。
- **相角**：对应正弦量的**初相位**。
- 注意象限判断：$\theta$ 需根据 $(x, y)$ 所在的**象限**确定，不能只看 $\arctan\frac{y}{x}$（例如 $(-1, -1)$ 与 $(1, 1)$ 的 $\arctan$ 相同，但相角相差 $\pi$）。

**共轭复数** (Conjugate)：$\bar{z} = x - jy$，模不变、相角取反。利用 $z \cdot \bar{z} = |z|^2$ 可进行复数除法。

---

## 七、复数的运算规则

| 运算 | 代数形式 | 极坐标形式 |
| :--- | :--- | :--- |
| 加减 | 实部、虚部分别相加减 | 不适用（须转回代数形式） |
| 乘法 | 展开 $(x_1+jy_1)(x_2+jy_2)$ | $r_1 r_2 e^{j(\theta_1+\theta_2)}$，模相乘、相角相加 |
| 除法 | 乘以共轭 $\frac{z_1}{z_2} = \frac{z_1 \bar{z_2}}{\|z_2\|^2}$ | $\frac{r_1}{r_2} e^{j(\theta_1-\theta_2)}$，模相除、相角相减 |
| 幂/开方 | 较繁琐 | $z^n = r^n e^{jn\theta}$ |

> [!TIP] 记忆要点
> - **加减**用代数形式（实虚部分开算）
> - **乘除幂**用极坐标形式（模相运算、相角加减）——这正是 $e^{j\theta}$ 表示法在频域分析中大放异彩的原因。

---

## 八、典型示例

> [!EXAMPLE] 例题 1：代数 ↔ 极坐标转换
> 将 $z = 1 + j\sqrt{3}$ 化为极坐标形式。

$$r = \sqrt{1^2 + (\sqrt{3})^2} = 2, \qquad \theta = \arctan\frac{\sqrt{3}}{1} = \frac{\pi}{3}$$
$$z = 2e^{j\pi/3}$$

> [!EXAMPLE] 例题 2：欧拉公式验证
> 验证 $e^{j\pi} + 1 = 0$。

由欧拉公式：$e^{j\pi} = \cos\pi + j\sin\pi = -1 + j \cdot 0 = -1$，故 $e^{j\pi} + 1 = 0$ ✓

> [!EXAMPLE] 例题 3：复数乘法（极坐标）
> 计算 $(2e^{j\pi/3})(3e^{-j\pi/6})$。

模相乘、相角相加：
$$2 \times 3 \cdot e^{j(\pi/3 - \pi/6)} = 6e^{j\pi/6}$$

---

## 九、在电路中的典型应用

- **相量表示**：正弦量 $A\cos(\omega t + \phi)$ 对应相量 $A e^{j\phi}$，时域微分方程 → 频域代数方程。
- **阻抗**：$Z_R = R$，$Z_L = j\omega L$，$Z_C = \frac{1}{j\omega C}$，串联/并联阻抗按复数规则运算。
- **频域响应**：$H(j\omega) = \dfrac{V_{out}}{V_{in}}$ 是复函数，其模为增益、相角为相移 —— 这正是滤波器与频域分析的基础。

---

## 相关笔记

- [[cs6.002x.1]] —— 电路原理知识树（主笔记）
- [[Circuit Theory Glossary]] —— 术语表（Mathematical Tools 一节）
- [[Kirchhoff's Laws]] / [[Thevenin's Theorem]] —— 频域版本（阻抗电路）中同样适用
