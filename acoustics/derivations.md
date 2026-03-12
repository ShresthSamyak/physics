# Acoustics — Complete Derivations

Step-by-step derivations for **UPH013 Physics – Acoustics**

---

# 1. Sabine Formula for Reverberation Time

Reverberation time ($T$) depends on two main factors:
1. **Volume of the hall** ($V$)
2. **Effective absorbing surface** ($A_{eff}$)

The relationship is proportional:
$$T \propto \frac{V}{A_{eff}}$$

Introducing a proportionality constant $K$:
$$T = K \frac{V}{A_{eff}}$$

### Effective Absorbing Surface
The effective absorbing surface is defined as:
$$A_{eff} = \alpha S$$

Where:
* $\alpha$ = absorption coefficient
* $S$ = geometrical surface area

### Multiple Surfaces
If the room has $n$ different surfaces (walls, floor, ceiling, etc.), the total absorption is the sum:
$$A_{eff} = \alpha_1S_1 + \alpha_2S_2 + \dots + \alpha_nS_n$$
$$A_{eff} = \sum_{i=1}^{n} \alpha_i S_i$$

Substituting this back into the main equation gives the general Sabine formula:
$$T = \frac{K V}{\sum \alpha_i S_i}$$

### Constants ($K$)
The value of $K$ changes based on the unit system:

* **Feet units:** $K \approx 0.05$
* **Meters (SI units):** $K \approx 0.162$

**Final Equations:**
* (Imperial) $T = \frac{0.05 V}{\sum \alpha_i S_i}$
* (SI) $T = \frac{0.162 V}{\sum \alpha_i S_i}$

---

# 2. Eyring Formula
*Used specifically for highly absorbent rooms ("dead" rooms).*  

### Step 1: Reflections
The average distance ($d$) sound travels between reflections is:
$$d = \frac{4V}{S}$$

The time ($t$) between reflections, given sound velocity $v$, is:
$$t = \frac{4V}{Sv}$$

Therefore, the number of reflections ($n$) in a given time $t$ is:
$$n = \frac{Svt}{4V}$$

### Step 2: Intensity Decay
Let the average absorption coefficient be $\bar{\alpha}$.  
The fraction of energy reflected is $(1 - \bar{\alpha})$.

After $n$ reflections, the intensity $I_t$ reduces from the initial intensity $I_0$:
$$I_t = I_0 (1 - \bar{\alpha})^n$$

Substituting $n$:
$$\frac{I_t}{I_0} = (1 - \bar{\alpha})^{\frac{Svt}{4V}}$$

### Step 3: Defining Reverberation Time
Reverberation time ($T$) is defined as the time it takes for intensity to drop to **one millionth** ($10^{-6}$) of its original value.

When $t = T$:
$$10^{-6} = (1 - \bar{\alpha})^{\frac{SvT}{4V}}$$

Taking the natural log ($\ln$) of both sides:
$$\ln(10^{-6}) = \frac{SvT}{4V} \ln(1 - \bar{\alpha})$$

Solving for $T$:
$$T = \frac{4V \ln(10^{-6})}{Sv \ln(1 - \bar{\alpha})}$$

### Final Eyring Formula
Using standard values for sound velocity and log conversion:

* **Feet units:** $T = \frac{-0.05 V}{S \ln(1 - \bar{\alpha})}$
* **SI units:** $T = \frac{-0.162 V}{S \ln(1 - \bar{\alpha})}$

> **Note:** For small values of $\alpha$, $\ln(1 - \bar{\alpha}) \approx -\bar{\alpha}$, which reduces the Eyring formula back to **Sabine’s formula**.

---

# 3. Reverberation Chamber Methods
*Methods used to determine the absorption coefficient experimentally.*

### A. Open Window Method
This method assumes an open window reflects no sound (perfect absorber).
$$\alpha = \frac{\text{Area of open window}}{\text{Total area of object}}$$

### B. Change in Reverberation Time Method
We measure the reverberation time of a room twice: once empty, and once with the test object.

1. **Without Object ($T_1$):**  
$$T_1 = \frac{0.05 V}{\sum \alpha_i S_i}$$

2. **With Object ($T_2$):**  
$$T_2 = \frac{0.05 V}{\sum \alpha_i S_i + cS}$$
*(Where $c$ is the object's coefficient and $S$ is its area)*

Taking the reciprocals and subtracting:
$$\frac{1}{T_2} - \frac{1}{T_1} = \frac{cS}{0.05 V}$$

**Final Formula for $c$:**
$$c = \frac{0.05 V}{S} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$

### C. Decay of Intensity Method
We use the intensity relation derived earlier:
$$I_t = I_0 (1 - \bar{\alpha})^{\frac{Svt}{4V}}$$

Taking the natural log and assuming small $\alpha$ (so $\ln(1-\bar{\alpha}) \approx -\bar{\alpha}$):
$$\ln\left(\frac{I_t}{I_0}\right) = - \frac{Svt \bar{\alpha}}{4V}$$

In exponential form:
$$I_t = I_0 e^{-\frac{Svt \bar{\alpha}}{4V}}$$

**Two Source Method:**  
If we have two sources with intensities $I_0$ and $I_1$ that decay to the same minimum audible intensity $I_m$ at times $T_0$ and $T_1$:

$$I_m = I_0 e^{-\frac{SvT_0 \bar{\alpha}}{4V}}$$
$$I_m = I_1 e^{-\frac{SvT_1 \bar{\alpha}}{4V}}$$

Equating them:
$$I_0 e^{-\frac{SvT_0 \bar{\alpha}}{4V}} = I_1 e^{-\frac{SvT_1 \bar{\alpha}}{4V}}$$

Rearranging and solving for $\bar{\alpha}$:
$$\frac{I_0}{I_1} = e^{\frac{\bar{\alpha} Sv (T_0 - T_1)}{4V}}$$

Taking the log:
$$\ln\left(\frac{I_0}{I_1}\right) = \frac{\bar{\alpha} Sv (T_0 - T_1)}{4V}$$

**Final Expression:**
Using Power ($P$) instead of Intensity ($I$):

$$ \boxed{\bar{\alpha} = \frac{4V \ln(P_0/P_1)}{Sv(T_0 - T_1)}} $$
