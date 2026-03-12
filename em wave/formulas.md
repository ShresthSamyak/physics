# Electromagnetic Waves — Complete Formula Sheet

Formulas for **UPH013 Physics – Electromagnetic Waves**

---

# 1. Maxwell’s Equations (Integral Form)

## Gauss's Law for Electric Field
$$
\iint \vec{E} \cdot d\vec{S} = \frac{q}{\epsilon_0}
$$

## Gauss's Law for Magnetic Field
$$
\iint \vec{B} \cdot d\vec{S} = 0
$$
This implies **magnetic monopoles do not exist**.

## Ampère–Maxwell Law
$$
\oint \vec{B} \cdot d\vec{l} = \mu_0 \left( i + \epsilon_0 \frac{d\Phi_E}{dt} \right)
$$

## Faraday's Law of Electromagnetic Induction
$$
\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}
$$

---

# 2. Maxwell’s Equations (Differential Form)

## Gauss’s Law (Electric)
$$

\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}
$$

## Gauss’s Law (Magnetic)
$$

\nabla \cdot \vec{B} = 0
$$

## Faraday’s Law
$$

\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
$$

## Ampère–Maxwell Law
$$

\nabla \times \vec{B} = \mu_0 \left( \vec{J} + \epsilon_0 \frac{\partial \vec{E}}{\partial t} \right)
$$

---

# 3. Electromagnetic Waves in Vacuum

In vacuum: $\rho = 0$, $\vec{J} = 0$.

## Simplified Maxwell Equations
$$
\nabla \cdot \vec{E} = 0
$$
$$
\nabla \cdot \vec{B} = 0
$$
$$
\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}
$$
$$
\nabla \times \vec{B} = \mu_0 \epsilon_0 \frac{\partial \vec{E}}{\partial t}
$$

---

# 4. Wave Equations

Electric field wave equation:
$$
\nabla^2 \vec{E} = \mu_0 \epsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}
$$

Magnetic field wave equation:
$$
\nabla^2 \vec{B} = \mu_0 \epsilon_0 \frac{\partial^2 \vec{B}}{\partial t^2}
$$

## Standard Wave Equation
$$
\nabla^2 y = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}
$$

---

# 5. Plane Wave Solutions

Electric field:
$$
\vec{E}(\vec{r},t) = \vec{E}_0 e^{i(\vec{k}\cdot\vec{r} - \omega t)}
$$

Magnetic field:
$$
\vec{B}(\vec{r},t) = \vec{B}_0 e^{i(\vec{k}\cdot\vec{r} - \omega t)}
$$

---

# 6. Wave Vector

Magnitude of propagation vector:
$$
k = \frac{2\pi}{\lambda}
$$

---

# 7. Speed of Electromagnetic Waves

$$
v = \frac{1}{\sqrt{\mu_0 \epsilon_0}}
$$
Substituting constants:
$$
v = 3 \times 10^8 \; m/s
$$
This equals the **speed of light**.

---

# 8. Transverse Nature of EM Waves

From divergence equations:
$$
\nabla \cdot \vec{E} = i\vec{k}\cdot\vec{E} = 0 \implies \vec{k} \perp \vec{E}
$$
Similarly:
$$
\nabla \cdot \vec{B} = i\vec{k}\cdot\vec{B} = 0 \implies \vec{k} \perp \vec{B}
$$

## Cross Product Relations
$$
\vec{k} \times \vec{E} = \omega \vec{B} \implies \vec{B} \perp \vec{E}, \vec{k}
$$
$$
\vec{k} \times \vec{B} = -\omega \vec{E} \implies \vec{E} \perp \vec{B}, \vec{k}
$$

---

# 9. Intrinsic Impedance of Free Space

Assume:
- $E$ along x
- $B$ along y
- propagation along z

From Maxwell equations:
$$
kE_x = \mu_0 \omega H_y \implies \frac{E_x}{H_y} = \frac{\mu_0 \omega}{k}
$$
Since $\frac{\omega}{k} = c$, we obtain:
$$
Z = \sqrt{\frac{\mu_0}{\epsilon_0}}
$$
Numerically:
$$
Z = 377 \; \Omega
$$

---

# 10. EM Waves in Conducting Medium

Material properties:
$$
\epsilon = \epsilon_r \epsilon_0, \quad \mu = \mu_r \mu_0
$$
Current density:
$$
\vec{J} = \sigma \vec{E}
$$

## Modified Ampère–Maxwell Law
$$
\nabla \times \vec{B} = \mu \left( \vec{J} + \epsilon \frac{\partial \vec{E}}{\partial t} \right)
$$

---

# 11. Wave Equations in Conductors

Electric field:
$$
\nabla^2 \vec{E} = \mu\sigma \frac{\partial \vec{E}}{\partial t} + \mu\epsilon \frac{\partial^2 \vec{E}}{\partial t^2}
$$

Magnetic field:
$$
\nabla^2 \vec{B} = \mu\sigma \frac{\partial \vec{B}}{\partial t} + \mu\epsilon \frac{\partial^2 \vec{B}}{\partial t^2}
$$

---

# 12. Complex Wave Vector

Assume $k = a + ib$.
Wave relation:
$$
k^2 = i\mu\sigma\omega + \mu\epsilon\omega^2
$$
Expanding $k^2 = (a^2 - b^2) + i(2ab)$, thus:
$$
a^2 - b^2 = \mu\epsilon\omega^2
$$
$$
2ab = \mu\sigma\omega
$$

---

# 13. Phase Constant

$$
a = \omega \sqrt{ \frac{\epsilon\mu}{2} \left[ \sqrt{1 + \left(\frac{\sigma}{\epsilon\omega}\right)^2} + 1 \right] }
$$

---

# 14. Attenuation Constant

$$
b = \omega \sqrt{ \frac{\epsilon\mu}{2} \left[ \sqrt{1 + \left(\frac{\sigma}{\epsilon\omega}\right)^2} - 1 \right] }
$$

---

# 15. Good Conductors

Condition: $\sigma \gg \omega\epsilon$.
Then:
$$
a = b = \sqrt{\frac{\mu\sigma\omega}{2}}
$$

## Phase Shift
$$
\phi = \tan^{-1}\left(\frac{b}{a}\right) = \frac{\pi}{4}
$$

## Skin Depth
$$
\delta = \frac{1}{b} = \sqrt{\frac{2}{\mu\sigma\omega}}
$$

---

# 16. Poor Conductors

Condition: $\sigma \ll \omega\epsilon$.
Then:
$$
a = \omega\sqrt{\epsilon\mu}
$$
$$
b = \frac{\sigma}{2} \sqrt{\frac{\mu}{\epsilon}}
$$

## Phase Shift
$$
\phi = \tan^{-1} \left( \frac{\sigma}{2\epsilon\omega} \right)
$$

## Skin Depth
$$
\delta = \frac{1}{b} = \frac{2}{\sigma} \sqrt{\frac{\epsilon}{\mu}}
$$

---

# 17. Attenuation of EM Waves

Inside a conductor amplitudes decay exponentially.

Electric field:
$$
\vec{E}_0^*(r) = \vec{E}_0 e^{-br}
$$

Magnetic field:
$$
\vec{B}_0^*(r) = \vec{B}_0 e^{-br}
$$

---

# 18. Skin Depth

Skin depth is the distance where amplitude reduces by factor $1/e$.
$$
\delta = \frac{1}{b}
$$
At $r = 1/b$:
$$
E = \frac{E_0}{e}
$$

---

# 19. Phase Difference Between E and B

In conducting medium $\vec{E} \not\parallel \vec{B}$.

Wave vector:
$$
k = |k|e^{i\phi}
$$
Where:
$$
|k| = \sqrt{a^2 + b^2}
$$
and $\phi$ represents the **phase shift between electric and magnetic fields**.

---

# End of Electromagnetic Waves Formula Sheet