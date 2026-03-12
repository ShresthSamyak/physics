# Oscillations & Waves – Complete Formula Sheet

All formulas compiled from the **UPH013 Physics – Oscillations and Waves slides**.

---

# 1. Simple Harmonic Motion (Spring Oscillations)

## Restoring Force (Hooke's Law)

\[
F = -kx
\]

---

## Newton's Second Law Applied

\[
F = ma
\]

\[
-kx = ma
\]

\[
a = -\frac{k}{m}x
\]

---

## Differential Equation of SHM

\[
\frac{d^2x}{dt^2} = -\frac{k}{m}x
\]

\[
\frac{d^2x}{dt^2} = -\omega^2 x
\]

---

## Angular Frequency

\[
\omega^2 = \frac{k}{m}
\]

\[
\omega = \sqrt{\frac{k}{m}}
\]

---

## Displacement Equation

\[
x(t) = A \cos(\omega t + \phi)
\]

Where:

- \(A\) = Amplitude  
- \(\omega\) = Angular frequency  
- \(\phi\) = Phase constant  

---

## Velocity

\[
v = \frac{dx}{dt}
\]

\[
v = -\omega A \sin(\omega t + \phi)
\]

### Maximum Velocity

\[
v_{max} = \omega A
\]

\[
v_{max} = \sqrt{\frac{k}{m}}A
\]

---

## Acceleration

\[
a = \frac{d^2x}{dt^2}
\]

\[
a = -\omega^2 A \cos(\omega t + \phi)
\]

### Maximum Acceleration

\[
a_{max} = \omega^2 A
\]

\[
a_{max} = \frac{k}{m}A
\]

---

## Period and Frequency

\[
T = 2\pi\sqrt{\frac{m}{k}}
\]

\[
f = \frac{1}{T}
\]

\[
f = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
\]

---

# 2. Energy in Simple Harmonic Motion

## Total Mechanical Energy

\[
E = K + U
\]

---

## Potential Energy

\[
U = \frac{1}{2}kx^2
\]

---

## Kinetic Energy

\[
K = \frac{1}{2}mv^2
\]

---

## Total Energy Equation

\[
E = \frac{1}{2}mv^2 + \frac{1}{2}kx^2
\]

\[
E = \frac{1}{2}kA^2
\]

---

## Maximum Kinetic Energy

\[
K_{max} = \frac{1}{2}mA^2\omega^2
\]

\[
K_{max} = \frac{1}{2}kA^2
\]

---

# 3. Simple Pendulum

## Restoring Force

\[
F = -mg\sin\theta
\]

---

## Arc Length Relation

\[
s = L\theta
\]

---

## Tangential Force Equation

\[
F_t = -mg\sin\theta
\]

\[
F_t = m\frac{d^2s}{dt^2}
\]

---

## Exact Differential Equation

\[
\frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin\theta
\]

---

## Small Angle Approximation

\[
\frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta
\]

---

## Angular Frequency

\[
\omega = \sqrt{\frac{g}{L}}
\]

---

## Period of Pendulum

\[
T = 2\pi\sqrt{\frac{L}{g}}
\]

---

# 4. Electrical Oscillations (LC Circuit)

## Voltage Equation

\[
\frac{Q}{C} + L\frac{d^2Q}{dt^2} = 0
\]

---

## Current Relation

\[
I = \frac{dQ}{dt}
\]

---

## Differential Equation

\[
\frac{d^2Q}{dt^2} = -\frac{1}{LC}Q
\]

---

## Charge Oscillation

\[
Q = Q_{max}\cos(\omega t + \phi)
\]

---

## Angular Frequency

\[
\omega = \frac{1}{\sqrt{LC}}
\]

---

## Energy in Capacitor

\[
U_C = \frac{Q^2}{2C}
\]

---

## Energy in Inductor

\[
U_L = \frac{1}{2}LI^2
\]

---

## Total Energy

\[
U = U_C + U_L
\]

\[
U = \frac{Q^2}{2C} + \frac{1}{2}LI^2
\]

---

## Maximum Energy Equivalence

\[
\frac{Q_{max}^2}{2C} = \frac{LI_{max}^2}{2}
\]

---

# 5. Damped Harmonic Motion (Mechanical)

## Forces

Retarding force:

\[
R = -bv
\]

Restoring force:

\[
F = -kx
\]

---

## Equation of Motion

\[
m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0
\]

---

## Underdamped Solution

\[
x = Ae^{-\frac{b}{2m}t}\cos(\omega t + \phi)
\]

Amplitude decay:

\[
A(t) = Ae^{-\frac{b}{2m}t}
\]

---

## Damped Angular Frequency

\[
\omega = \sqrt{\frac{k}{m} - \left(\frac{b}{2m}\right)^2}
\]

Natural frequency:

\[
\omega_0 = \sqrt{\frac{k}{m}}
\]

---

## Damping Conditions

### Underdamped

\[
\frac{k}{m} > \left(\frac{b}{2m}\right)^2
\]

### Critical Damping

\[
\frac{k}{m} = \left(\frac{b}{2m}\right)^2
\]

### Overdamped

\[
\frac{k}{m} < \left(\frac{b}{2m}\right)^2
\]

---

# 6. Damped Electrical Oscillations (LCR Circuit)

## Circuit Equation

\[
L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{Q}{C} = 0
\]

---

## Charge Solution

\[
Q = Q_{max}e^{-Rt/2L}\cos(\omega_d t)
\]

---

## Damped Frequency

\[
\omega_d =
\sqrt{
\frac{1}{LC}
-
\left(\frac{R}{2L}\right)^2
}
\]

---

## Critical Resistance

\[
R_c = \sqrt{\frac{4L}{C}}
\]

---

## Electrical Damping Conditions

### Underdamped

\[
R < R_c
\]

### Critical Damping

\[
R = R_c
\]

### Overdamped

\[
R > R_c
\]

---

# 7. Damping Measurements

## Logarithmic Decrement

\[
\delta = \ln\left(\frac{x_{n-1}}{x_n}\right)
\]

Alternative form:

\[
\delta = rT
\]

Where:

\[
r = \frac{b}{2m}
\]

---

## Relaxation Time

Time for amplitude to decay to \(1/e\).

\[
\tau_a = \frac{1}{r}
\]

Relation with decrement:

\[
\delta = rT = \frac{T}{\tau_a}
\]

---

# 8. Quality Factor

Definition:

\[
Q =
2\pi
\frac{\text{Energy Stored}}
{\text{Energy Lost per Cycle}}
\]

---

## Energy Form

\[
Q = 2\pi \left(\frac{E}{-dE}\right)
\]

---

## Energy Decay

\[
E = E_0 e^{-2rt}
\]

---

## Rate of Energy Loss

\[
-dE = 2rE_0 e^{-2rt}dt
\]

---

## Simplified Quality Factor

\[
Q = \frac{\omega}{2r}
\]

---

# End of Formula Sheet