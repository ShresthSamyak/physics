# Acoustics — Complete Derivations

Step-by-step derivations for **UPH013 Physics – Acoustics**

---

# 1. Sabine Formula for Reverberation Time

Reverberation time \(T\) depends on:

- volume of the hall
- effective absorbing surface

Thus

\[
T \propto \frac{\text{Volume of hall}}{\text{Effective absorbing surface}}
\]

or

\[
T \propto \frac{V}{A_{eff}}
\]

Introducing proportionality constant \(K\):

\[
T = K\frac{V}{A_{eff}}
\]

---

## Effective Absorbing Surface

\[
A_{eff} = \alpha S
\]

Where

- \( \alpha \) = absorption coefficient
- \( S \) = geometrical surface area

---

## Multiple Surfaces

If the room has \(n\) surfaces:

\[
A_{eff} = \alpha_1S_1 + \alpha_2S_2 + \alpha_3S_3 + ... + \alpha_nS_n
\]

or

\[
A_{eff} = \sum_{i=1}^{n} \alpha_i S_i
\]

Thus Sabine formula becomes

\[
T = \frac{K V}{\sum \alpha_i S_i}
\]

---

## Constants

For different unit systems

Feet units:

\[
K = 0.05
\]

Meters (SI):

\[
K = 0.162
\]

Thus

\[
T = \frac{0.05V}{\sum \alpha_i S_i}
\]

or

\[
T = \frac{0.162V}{\sum \alpha_i S_i}
\]

---

# 2. Eyring Formula

Used for **highly absorbent rooms**.

---

## Distance Between Reflections

Average distance travelled between reflections

\[
d = \frac{4V}{S}
\]

Where

- \(V\) = volume of hall
- \(S\) = total surface area

---

## Time Between Reflections

If \(v\) is velocity of sound

\[
t = \frac{4V}{Sv}
\]

---

## Number of Reflections

Number of reflections in time \(t\):

\[
n = \frac{Svt}{4V}
\]

---

## Intensity After Reflections

Let average absorption coefficient be

\[
\bar{\alpha}
\]

Fraction reflected:

\[
1-\bar{\alpha}
\]

After \(n\) reflections:

\[
I_t = I_0 (1-\bar{\alpha})^n
\]

Substitute \(n\):

\[
I_t = I_0 (1-\bar{\alpha})^{\frac{Svt}{4V}}
\]

Thus

\[
\frac{I_t}{I_0} =
(1-\bar{\alpha})^{\frac{Svt}{4V}}
\]

---

## Definition of Reverberation Time

When \(t = T\)

\[
\frac{I_t}{I_0} = 10^{-6}
\]

Thus

\[
10^{-6} =
(1-\bar{\alpha})^{\frac{SvT}{4V}}
\]

---

## Taking Natural Log

\[
\ln(10^{-6})
=
\ln(1-\bar{\alpha})\frac{SvT}{4V}
\]

---

## Solving for Reverberation Time

\[
T =
\frac{\ln(10^{-6})4V}{Sv\ln(1-\bar{\alpha})}
\]

---

## Final Eyring Formula

Feet units:

\[
T =
\frac{-0.05V}{S\ln(1-\bar{\alpha})}
\]

SI units:

\[
T =
\frac{-0.162V}{S\ln(1-\bar{\alpha})}
\]

---

## Reduction to Sabine Formula

For small \(\alpha\)

\[
\ln(1-\bar{\alpha}) \approx -\bar{\alpha}
\]

Thus

\[
T = \frac{0.05V}{S\bar{\alpha}}
\]

which is Sabine’s formula.

---

# 3. Reverberation Chamber Methods

Used to determine **absorption coefficient** experimentally.

---

# A. Open Window Method

Sound absorption by the object equals that of an open window.

\[
\alpha =
\frac{\text{Area of window}}
{\text{Total area of object}}
\]

---

# B. Change in Reverberation Time Method

### Without Object

\[
T_1 =
\frac{0.05V}{\sum \alpha_i S_i}
\]

---

### With Object

\[
T_2 =
\frac{0.05V}{\sum \alpha_i S_i + cS}
\]

Where

- \(c\) = absorption coefficient of object
- \(S\) = surface area of object

---

## Taking Reciprocals

\[
\frac{1}{T_2} - \frac{1}{T_1}
=
\frac{cS}{0.05V}
\]

---

## Final Formula

\[
c =
\frac{0.05V}{S}
\left(
\frac{1}{T_2} - \frac{1}{T_1}
\right)
\]

---

# C. Decay of Intensity Method

Start from intensity relation

\[
I_t =
I_0(1-\bar{\alpha})^{\frac{Svt}{4V}}
\]

---

## Taking Logarithm

\[
\ln\left(\frac{I_t}{I_0}\right)
=
\frac{Svt}{4V}\ln(1-\bar{\alpha})
\]

For small \(\alpha\)

\[
\ln(1-\bar{\alpha}) \approx -\bar{\alpha}
\]

Thus

\[
\ln\left(\frac{I_t}{I_0}\right)
=
\frac{-Svt\bar{\alpha}}{4V}
\]

---

## Exponential Form

\[
I_t =
I_0 e^{-\frac{Svt\bar{\alpha}}{4V}}
\]

---

## Two Source Method

Source 1:

\[
I_m =
I_0 e^{-\frac{SvT_0\bar{\alpha}}{4V}}
\]

Source 2:

\[
I_m =
I_1 e^{-\frac{SvT_1\bar{\alpha}}{4V}}
\]

---

## Equating Both

\[
I_0 e^{-\frac{SvT_0\bar{\alpha}}{4V}}
=
I_1 e^{-\frac{SvT_1\bar{\alpha}}{4V}}
\]

---

## Rearranging

\[
\frac{I_0}{I_1}
=
e^{\frac{\bar{\alpha}Sv(T_0-T_1)}{4V}}
\]

---

## Taking Log

\[
\ln\left(\frac{I_0}{I_1}\right)
=
\frac{\bar{\alpha}Sv(T_0-T_1)}{4V}
\]

---

## Solving for Average Absorption Coefficient

\[
\bar{\alpha}
=
\frac{4V}{Sv}
\frac{\ln(I_0/I_1)}{(T_0-T_1)}
\]

---

## Using Power Ratio

Since

\[
\frac{I_0}{I_1} = \frac{P_0}{P_1}
\]

Final expression becomes

\[
\boxed{
\bar{\alpha}
=
\frac{4V\ln(P_0/P_1)}{Sv(T_0-T_1)}
}
\]

---

# End of Acoustics Derivations