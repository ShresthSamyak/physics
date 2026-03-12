# Acoustics — Complete Formula Sheet

All formulas summarized from the **Acoustics chapter (UPH013 Physics)**.

---

# 1. Basic Acoustics and Reverberation Time

## Reverberation Time Definition

Reverberation time is the **time required for the sound intensity to fall to one millionth of its initial value** after the source is stopped.

$$
I = \frac{I_0}{10^6}
$$

Where:

- \(I_0\) = Initial sound intensity  
- \(I\) = Final sound intensity after reverberation  

---

## Absorption Coefficient

The absorption coefficient measures how much sound energy is absorbed by a surface.

$$
\alpha =
\frac{\text{Sound energy absorbed by surface}}
{\text{Total sound energy incident on surface}}
$$

Range:

$$
0 \leq \alpha \leq 1
$$

- \( \alpha = 0 \) → perfectly reflecting surface  
- \( \alpha = 1 \) → perfectly absorbing surface  

---

# 2. Sabine's Formula

Sabine derived a relation between reverberation time and hall properties.

## General Sabine Formula

$$
T = K \frac{V}{A}
$$

Where:

- \(T\) = Reverberation time  
- \(V\) = Volume of hall  
- \(A\) = Effective absorbing surface area  
- \(K\) = Constant depending on unit system  

---

## Effective Absorbing Surface Area

$$
A = \alpha_1 S_1 + \alpha_2 S_2 + \alpha_3 S_3 + \dots + \alpha_n S_n
$$

or

$$
A = \sum_{n=1}^{N} \alpha_n S_n
$$

Where:

- \(S_n\) = surface area of nth material  
- \( \alpha_n \) = absorption coefficient of that material  

---

## Sabine Formula (Feet Units)

Velocity of sound:

$$
v = 1120 \; ft/s
$$

Constant:

$$
K = 0.05
$$

Thus

$$
T = \frac{0.05V}{A}
$$

or

$$
T = \frac{0.05V}{\sum_{n=1}^{N} \alpha_n S_n}
$$

---

## Sabine Formula (SI Units)

Velocity of sound:

$$
v = 340 \; m/s
$$

Constant:

$$
K = 0.161
$$

Thus

$$
T = \frac{0.161V}{A}
$$

---

# 3. Eyring's Formula

Eyring’s formula is used for **highly absorbent rooms** where

$$
\alpha > 0.2
$$

---

## Energy Fractions

Fraction absorbed:

$$
\alpha
$$

Fraction reflected:

$$
1 - \alpha
$$

---

## Eyring Formula (Feet)

$$
T = \frac{0.05V}{-S \ln(1-\alpha)}
$$

---

## Eyring Formula (Meters)

$$
T = \frac{0.161V}{-S \ln(1-\alpha)}
$$

Where:

- \(S\) = total surface area of the room

---

## Important Note

For large values of \( \alpha \):

Sabine formula incorrectly gives:

$$
T = \frac{0.05V}{S}
$$

But Eyring formula correctly gives:

$$
T = 0
$$

when

$$
\alpha = 1
$$

---

# 4. Methods to Measure Absorption Coefficient

Two experimental methods are commonly used.

---

# Method 1 — Change of Absorption

Reverberation time is measured:

- Without absorbing material → \(T_1\)
- With absorbing material → \(T_2\)

---

## Without Absorbing Material

$$
T_1 = \frac{0.05V}{\alpha S}
$$

---

## With Absorbing Material

$$
T_2 =
\frac{0.05V}
{\alpha S + \alpha_m S_m}
$$

Where:

- \( \alpha_m \) = absorption coefficient of unknown material  
- \( S_m \) = surface area of that material  

---

## Final Formula

$$
\alpha_m =
\frac{0.05V}{S_m}
\left(
\frac{T_1 - T_2}{T_1T_2}
\right)
$$

---

# Method 2 — Decay of Intensity Method

Used when two sound sources produce different maximum intensities.

---

## Intensity Decay Law

$$
I = I_m e^{-Ct}
$$

Where:

- \(I_m\) = maximum intensity  
- \(C\) = decay constant  

---

## Constant C

$$
C = \frac{\alpha S v}{4V}
$$

Where:

- \(v\) = velocity of sound  

---

## Threshold Intensity Equations

For first source:

$$
I_{Th} = I_m e^{-CT_1}
$$

For second source:

$$
I_{Th} = I'_m e^{-CT_2}
$$

---

## Intensity Ratio

$$
\frac{I_m}{I'_m}
=
e^{C(T_1 - T_2)}
$$

---

## Final Absorption Coefficient Formula

$$
\alpha =
\frac{0.05V(\ln I_m - \ln I'_m)}
{S(T_1 - T_2)}
$$

---

# End of Acoustics Formula Sheet