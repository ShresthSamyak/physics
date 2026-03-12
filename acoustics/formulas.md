# Acoustics — Complete Formula Sheet
*Summarized from Acoustics chapter (UPH013 Physics)*

## 1. Basic Acoustics and Reverberation

### Reverberation Time ($T$)
Defined as the time required for the sound intensity to fall to **one millionth** of its initial value after the source is stopped.

$$ I = \frac{I_0}{10^6} $$

*   **$I_0$**: Initial sound intensity
*   **$I$**: Final sound intensity

### Absorption Coefficient ($\alpha$)
Measures how much sound energy a surface absorbs.

$$ \alpha = \frac{\text{Sound energy absorbed}}{\text{Total energy incident}} $$

**Range:** $0 \leq \alpha \leq 1$
*   $\alpha = 0$: Perfectly reflecting (e.g., marble)
*   $\alpha = 1$: Perfectly absorbing (e.g., open window)

---

## 2. Sabine's Formula
Used for rooms with **low absorption** ($\alpha < 0.2$).

### General Formula
$$ T = K \frac{V}{A} $$

### Effective Absorbing Area ($A$)
$$ A = \sum \alpha_n S_n = \alpha_1 S_1 + \alpha_2 S_2 + \dots $$

### Unit Variations

| System | Velocity of Sound ($v$) | Constant ($K$) | Formula |
| :--- | :--- | :--- | :--- |
| **FPS (Feet)** | $1120 \text{ ft/s}$ | **0.05** | $T = \frac{0.05V}{\sum \alpha S}$ |
| **MKS (SI Meters)** | $340 \text{ m/s}$ | **0.161** | $T = \frac{0.161V}{\sum \alpha S}$ |

---

## 3. Eyring's Formula
Used for **highly absorbent** rooms (Dead rooms) where $\alpha > 0.2$.

### Formula
$$ T = \frac{K V}{-S \ln(1-\alpha_{avg})} $$

**Where:**
*   $S$: Total surface area of the room
*   $K$: $0.05$ (for Feet) or $0.161$ (for Meters)

> **Note:** When $\alpha = 1$ (perfect absorption), Sabine's formula incorrectly gives a finite time, whereas Eyring's correctly gives $T=0$.

---

## 4. Measuring Absorption Coefficient

### Method 1: Change of Absorption
Calculate $\alpha$ by measuring Reverberation Time ($T$) with and without a test material.

**Final Formula:**
$$ \alpha_m = \frac{K V}{S_m} \left( \frac{1}{T_1} - \frac{1}{T_2} \right) $$

*   **$T_1$**: Time *without* material
*   **$T_2$**: Time *with* material
*   **$S_m$**: Surface area of test material
*   **$K$**: $0.05$ or $0.161$

### Method 2: Decay of Intensity
Used when comparing two sound sources with different maximum intensities ($I_m$ and $I'_m$).

**Final Formula:**
$$ \alpha = \frac{K V (\ln I_m - \ln I'_m)}{S(T_1 - T_2)} $$

*   **$I_m, I'_m$**: Maximum intensities of the two sources
*   **$T_1, T_2$**: Decay times for the two sources