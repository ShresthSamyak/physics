# Acoustics — Complete Derivations

Step-by-step derivations for **UPH013 Physics – Acoustics**.

## Table of Contents
1. [Sabine Formula for Reverberation Time](#1-sabine-formula-for-reverberation-time)
2. [Eyring Formula](#2-eyring-formula)
3. [Reverberation Chamber Methods](#3-reverberation-chamber-methods)

---

## 1. Sabine Formula for Reverberation Time

Reverberation time ($T$) depends on:
- Volume of the hall ($V$)
- Effective absorbing surface ($A_{eff}$)

The relationship is given by:
$$ T \propto \frac{V}{A_{eff}} $$

Introducing a proportionality constant $K$:
$$ T = \frac{KV}{A_{eff}} $$

### Effective Absorbing Surface

$$ A_{eff} = \sum \alpha S $$

Where:
- $\alpha$ = absorption coefficient
- $S$ = geometrical surface area

For a room with multiple surfaces ($n$):
$$ A_{eff} = \alpha_1S_1 + \alpha_2S_2 + ... + \alpha_nS_n = \sum_{i=1}^{n} \alpha_i S_i $$

Thus, the Sabine formula becomes:
$$ T = \frac{K V}{\sum \alpha_i S_i} $$

### Constants

For different unit systems:
- **Feet units:** $K = 0.05$
- **Meters (SI):** $K = 0.162$

**Final Equation:**
$$ T = \frac{0.162V}{\sum \alpha_i S_i} \quad \text{(SI Units)} $$

---

## 2. Eyring Formula

This formula is used for **highly absorbent rooms**.

### Derivation

1. **Distance Between Reflections:**
   The average distance traveled between reflections is:
   $$ d = \frac{4V}{S} $$
   Where $V$ is volume and $S$ is total surface area.

2. **Time Between Reflections:**
   If $v$ is the velocity of sound:
   $$ t_{ref} = \frac{d}{v} = \frac{4V}{Sv} $$

3. **Number of Reflections:**
   The number of reflections ($n$) in total time $t$:
   $$ n = \frac{t}{t_{ref}} = \frac{Svt}{4V} $$

4. **Intensity Decay:**
   Let the average absorption coefficient be $\bar{\alpha}$. The fraction of energy reflected per impact is $(1-\bar{\alpha})$.
   After $n$ reflections, the intensity $I_t$ is:
   $$ I_t = I_0 (1-\bar{\alpha})^n $$
   Substituting $n$:
   $$ \frac{I_t}{I_0} = (1-\bar{\alpha})^{\frac{Svt}{4V}} $$

5. **Reverberation Time Definition:**
   Reverberation time $T$ is the time when intensity drops to $10^{-6}$ of the original value.
   $$ 10^{-6} = (1-\bar{\alpha})^{\frac{SvT}{4V}} $$

   Taking the natural log ($\ln$):
   $$ \ln(10^{-6}) = \frac{SvT}{4V} \ln(1-\bar{\alpha}) $$

   Solving for $T$:
   $$ T = \frac{4V \ln(10^{-6})}{Sv \ln(1-\bar{\alpha})} $$

### Final Eyring Formula

Substituting constants for velocity $v$:

- **Feet units:**
  $$ T = \frac{-0.05V}{S\ln(1-\bar{\alpha})} $$

- **SI units:**
  $$ T = \frac{-0.162V}{S\ln(1-\bar{\alpha})} $$

**Reduction to Sabine Formula:**
For small $\alpha$, $\ln(1-\bar{\alpha}) \approx -\bar{\alpha}$.
$$ T \approx \frac{0.162V}{S\bar{\alpha}} $$
This recovers Sabine’s formula.

---

## 3. Reverberation Chamber Methods

Used to determine **absorption coefficient** experimentally.

### A. Open Window Method

The sound absorption by the object is compared to that of an open window (perfect absorber).
$$ \alpha = \frac{\text{Area of window}}{\text{Total area of object}} $$

### B. Change in Reverberation Time Method

We measure reverberation time without and with the object.

1. **Without Object ($T_1$):**
   $$ T_1 = \frac{0.05V}{\sum \alpha_i S_i} $$

2. **With Object ($T_2$):**
   $$ T_2 = \frac{0.05V}{\sum \alpha_i S_i + cS} $$
   Where $c$ is the object's absorption coefficient and $S$ is its area.

**Calculation:**
Taking reciprocals and subtracting:
$$ \frac{1}{T_2} - \frac{1}{T_1} = \frac{cS}{0.05V} $$

Solving for $c$:
$$ c = \frac{0.05V}{S} \left( \frac{1}{T_2} - \frac{1}{T_1} \right) $$

### C. Decay of Intensity Method

Starting from the intensity relation:
$$ I_t = I_0 e^{-\frac{Svt\bar{\alpha}}{4V}} $$
(Using the approximation $\ln(1-\bar{\alpha}) \approx -\bar{\alpha}$)

**Two Source Method:**
Consider two conditions with sources generating intensities $I_0$ and $I_1$ that decay to a measured intensity $I_m$ over times $T_0$ and $T_1$.

$$ I_m = I_0 e^{-\frac{SvT_0\bar{\alpha}}{4V}} $$
$$ I_m = I_1 e^{-\frac{SvT_1\bar{\alpha}}{4V}} $$

Equating and rearranging:
$$ \frac{I_0}{I_1} = e^{\frac{\bar{\alpha}Sv(T_0-T_1)}{4V}} $$

Taking natural log and solving for $\bar{\alpha}$:
$$ \ln\left(\frac{I_0}{I_1}\right) = \frac{\bar{\alpha}Sv(T_0-T_1)}{4V} $$

$$ \bar{\alpha} = \frac{4V \ln(I_0/I_1)}{Sv(T_0-T_1)} $$

Since $\frac{I_0}{I_1} = \frac{P_0}{P_1}$ (Power Ratio):

$$ \boxed{ \bar{\alpha} = \frac{4V\ln(P_0/P_1)}{Sv(T_0-T_1)} } $$