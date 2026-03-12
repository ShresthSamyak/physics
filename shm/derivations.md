## Differential Equation of Simple Harmonic Motion

Starting from Newton's Second Law:

$$
F = ma
$$

For a spring obeying Hooke's Law:

$$
F = -kx
$$

Therefore,

$$
ma = -kx
$$

Dividing both sides by $m$:

$$
a = -\frac{k}{m}x
$$

Acceleration can also be written as:

$$
a = \frac{d^2x}{dt^2}
$$

Substituting this into the equation gives:

$$
\frac{d^2x}{dt^2} = -\frac{k}{m}x
$$

Define angular frequency:

$$
\omega^2 = \frac{k}{m}
$$

Thus the differential equation becomes:

$$
\boxed{\frac{d^2x}{dt^2} + \omega^2 x = 0}
$$

The general solution is:

$$
x(t) = A\cos(\omega t + \phi)
$$

where:

* $A$ = Amplitude
* $\omega$ = Angular frequency
* $\phi$ = Phase constant

---

## Velocity in Simple Harmonic Motion

The total mechanical energy in SHM is constant.

$$
E = KE + PE
$$

Potential energy of a spring:

$$
PE = \frac{1}{2}kx^2
$$

Kinetic energy:

$$
KE = \frac{1}{2}mv^2
$$

Total energy at maximum displacement $A$:

$$
E = \frac{1}{2}kA^2
$$

At position $x$:

$$
\frac{1}{2}kA^2 = \frac{1}{2}kx^2 + \frac{1}{2}mv^2
$$

Rearranging:

$$
\frac{1}{2}kA^2 - \frac{1}{2}kx^2 = \frac{1}{2}mv^2
$$

Multiply both sides by $2$:

$$
kA^2 - kx^2 = mv^2
$$

Factor $k$:

$$
k(A^2 - x^2) = mv^2
$$

Divide by $m$:

$$
v^2 = \frac{k}{m}(A^2 - x^2)
$$

Since

$$
\omega^2 = \frac{k}{m}
$$

we obtain

$$
v^2 = \omega^2(A^2 - x^2)
$$

Therefore

$$
\boxed{v = \pm \omega \sqrt{A^2 - x^2}}
$$

---

## Differential Equation of a Simple Pendulum

For a pendulum of mass $m$ and length $L$:

Arc length:

$$
s = L\theta
$$

Restoring force:

$$
F = -mg\sin\theta
$$

Using Newton's second law:

$$
m\frac{d^2s}{dt^2} = -mg\sin\theta
$$

For small angles:

$$
\sin\theta \approx \theta
$$

Thus:

$$
m\frac{d^2(L\theta)}{dt^2} = -mg\theta
$$

Simplifying:

$$
mL\frac{d^2\theta}{dt^2} = -mg\theta
$$

Divide by $mL$:

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta
$$

Comparing with

$$
\frac{d^2x}{dt^2} = -\omega^2 x
$$

we obtain

$$
\boxed{\omega = \sqrt{\frac{g}{L}}}
$$

---

## LC Circuit Oscillation

Applying Kirchhoff's Voltage Law:

$$
V_L + V_C = 0
$$

Inductor voltage:

$$
V_L = L\frac{dI}{dt}
$$

Capacitor voltage:

$$
V_C = \frac{Q}{C}
$$

Thus

$$
L\frac{dI}{dt} + \frac{Q}{C} = 0
$$

Since

$$
I = \frac{dQ}{dt}
$$

we obtain

$$
L\frac{d^2Q}{dt^2} + \frac{Q}{C} = 0
$$

Rearranging:

$$
\boxed{\frac{d^2Q}{dt^2} + \frac{1}{LC}Q = 0}
$$

Comparing with SHM equation:

$$
\frac{d^2x}{dt^2} + \omega^2x = 0
$$

we obtain

$$
\boxed{\omega = \frac{1}{\sqrt{LC}}}
$$

---

## Damped Harmonic Motion

Retarding force proportional to velocity:

$$
R = -bv
$$

Total force:

$$
F = -kx - bv
$$

Applying Newton's second law:

$$
m\frac{d^2x}{dt^2} = -kx - b\frac{dx}{dt}
$$

Rearranging:

$$
\boxed{m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = 0}
$$

Divide by $m$:

$$
\boxed{\frac{d^2x}{dt^2} + \frac{b}{m}\frac{dx}{dt} + \frac{k}{m}x = 0}
$$

Assume solution:

$$
x = Ae^{\alpha t}
$$

Substitute:

$$
\alpha^2 + \frac{b}{m}\alpha + \frac{k}{m} = 0
$$

Characteristic equation:

$$
\boxed{\alpha^2 + \frac{b}{m}\alpha + \frac{k}{m} = 0}
$$

Roots:

$$
\alpha = -\frac{b}{2m} \pm \sqrt{\left(\frac{b}{2m}\right)^2 - \frac{k}{m}}
$$

General solution:

$$
x = A_1 e^{\left[-\frac{b}{2m} + \sqrt{\left(\frac{b}{2m}\right)^2 - \frac{k}{m}}ight]t} + A_2 e^{\left[-\frac{b}{2m} - \sqrt{\left(\frac{b}{2m}\right)^2 - \frac{k}{m}}ight]t}
$$

---

## Damped LCR Circuit

Applying Kirchhoff's Law:

$$
L\frac{dI}{dt} + IR + \frac{Q}{C} = 0
$$

Substitute

$$
I = \frac{dQ}{dt}
$$

Thus

$$
\boxed{L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{Q}{C} = 0}
$$

Divide by $L$:

$$
\boxed{\frac{d^2Q}{dt^2} + \frac{R}{L}\frac{dQ}{dt} + \frac{1}{LC}Q = 0}
$$

Solution for underdamped case:

$$
Q(t) = Q_{max} e^{-\frac{Rt}{2L}} \cos(\omega t + \phi)
$$

where

$$
\boxed{\omega = \sqrt{\frac{1}{LC} - \left(\frac{R}{2L}\right)^2}}
$$

---

## Logarithmic Decrement

For successive amplitudes:

$$
\delta = \ln\left(\frac{x_a}{x_b}\right)
$$

Using exponential decay:

$$
x_a = Ae^{-\frac{b}{2m}t_a}
$$

$$
x_b = Ae^{-\frac{b}{2m}t_b}
$$

Thus

$$
\frac{x_a}{x_b} = e^{-\frac{bT}{2m}}
$$

Taking logarithm:

$$
\delta = \frac{bT}{2m}
$$

Since

$$
T = \frac{2\pi}{\omega}
$$

$$
\boxed{\delta = \frac{b\pi}{m\omega}}
$$

For LCR circuit:

$$
\boxed{\delta = \frac{R}{2L}\left(\frac{2\pi}{\omega}\right)}
$$

---

## Quality Factor

Definition:

$$
Q = 2\pi \frac{\text{Energy Stored}}{\text{Energy Lost per Cycle}}
$$

Energy decay:

$$
E = E_0 e^{-\frac{b}{m}t}
$$

Rate of energy loss:

$$
\frac{dE}{dt} = -\frac{b}{m}E
$$

Thus

$$
Q = 2\pi \frac{E}{-dE}
$$

Substituting:

$$
Q = \frac{2\pi m}{Tb}
$$

Since

$$
T = \frac{2\pi}{\omega}
$$

we obtain

$$
\boxed{Q = \frac{\omega m}{b}}
$$

For LCR circuit:

$$
\boxed{Q = \frac{\omega L}{R}}
$$

---

## Forced Oscillations

External driving force:

$$
F(t) = F_0 \sin(\omega t)
$$

Equation of motion:

$$
m\frac{d^2x}{dt^2} + b\frac{dx}{dt} + kx = F_0\sin(\omega t)
$$

Steady-state amplitude:

$$
\boxed{ A = \frac{F_0/m} {\sqrt{(\omega^2 - \omega_0^2)^2 + \left(\frac{b\omega}{m}\right)^2}} }
$$

where

$$
\omega_0 = \sqrt{\frac{k}{m}}
$$

---

## Resonance

When driving frequency equals natural frequency:

$$
\omega = \omega_0
$$

Amplitude becomes very large.

This phenomenon is known as

$$
\boxed{\text{Resonance}}