# Electromagnetic Waves — Complete Formula Sheet

Formulas for **UPH013 Physics – Electromagnetic Waves**

---

## 1. Maxwell's Equations (Integral Form)

### Gauss's Law for Electric Field

```
∯ E⃗ · dS⃗ = q / ε₀
```

### Gauss's Law for Magnetic Field

```
∯ B⃗ · dS⃗ = 0
```

> This implies **magnetic monopoles do not exist**.

### Ampère–Maxwell Law

```
∮ B⃗ · dl⃗ = μ₀ ( i + ε₀ · dΦ_E/dt )
```

### Faraday's Law of Electromagnetic Induction

```
∮ E⃗ · dl⃗ = −dΦ_B/dt
```

---

## 2. Maxwell's Equations (Differential Form)

### Gauss's Law (Electric)

```
∇ · E⃗ = ρ / ε₀
```

### Gauss's Law (Magnetic)

```
∇ · B⃗ = 0
```

### Faraday's Law

```
∇ × E⃗ = −∂B⃗/∂t
```

### Ampère–Maxwell Law

```
∇ × B⃗ = μ₀ ( J⃗ + ε₀ · ∂E⃗/∂t )
```

---

## 3. Electromagnetic Waves in Vacuum

In vacuum: `ρ = 0`, `J⃗ = 0`

### Simplified Maxwell Equations

```
∇ · E⃗ = 0

∇ · B⃗ = 0

∇ × E⃗ = −∂B⃗/∂t

∇ × B⃗ = μ₀ε₀ · ∂E⃗/∂t
```

---

## 4. Wave Equations

**Electric field wave equation:**

```
∇²E⃗ = μ₀ε₀ · ∂²E⃗/∂t²
```

**Magnetic field wave equation:**

```
∇²B⃗ = μ₀ε₀ · ∂²B⃗/∂t²
```

**Standard wave equation:**

```
∇²y = (1/v²) · ∂²y/∂t²
```

---

## 5. Plane Wave Solutions

**Electric field:**

```
E⃗(r⃗, t) = E⃗₀ · e^[i(k⃗·r⃗ − ωt)]
```

**Magnetic field:**

```
B⃗(r⃗, t) = B⃗₀ · e^[i(k⃗·r⃗ − ωt)]
```

---

## 6. Wave Vector

Magnitude of propagation vector:

```
k = 2π / λ
```

---

## 7. Speed of Electromagnetic Waves

```
v = 1 / √(μ₀ε₀)  =  3 × 10⁸ m/s
```

> This equals the **speed of light**.

---

## 8. Transverse Nature of EM Waves

From divergence equations:

```
∇ · E⃗ = ik⃗ · E⃗ = 0  →  k⃗ ⊥ E⃗

∇ · B⃗ = ik⃗ · B⃗ = 0  →  k⃗ ⊥ B⃗
```

### Cross Product Relations

```
k⃗ × E⃗ = ωB⃗   →   B⃗ ⊥ E⃗ and k⃗

k⃗ × B⃗ = −ωE⃗  →   E⃗ ⊥ B⃗ and k⃗
```

---

## 9. Intrinsic Impedance of Free Space

Assume: E along x, B along y, propagation along z.

From Maxwell equations:

```
k·Eₓ = μ₀ω·Hᵧ   →   Eₓ/Hᵧ = μ₀ω/k
```

Since `ω/k = c`:

```
Z = √(μ₀/ε₀)  =  377 Ω
```

---

## 10. EM Waves in Conducting Medium

**Material properties:**

```
ε = εᵣε₀     μ = μᵣμ₀
```

**Current density:**

```
J⃗ = σE⃗
```

### Modified Ampère–Maxwell Law

```
∇ × B⃗ = μ ( J⃗ + ε · ∂E⃗/∂t )
```

---

## 11. Wave Equations in Conductors

**Electric field:**

```
∇²E⃗ = μσ · ∂E⃗/∂t  +  με · ∂²E⃗/∂t²
```

**Magnetic field:**

```
∇²B⃗ = μσ · ∂B⃗/∂t  +  με · ∂²B⃗/∂t²
```

---

## 12. Complex Wave Vector

Assume `k = a + ib`

**Wave relation:**

```
k² = iμσω + μεω²
```

Expanding `k² = (a² − b²) + i(2ab)`:

```
a² − b² = μεω²

2ab = μσω
```

---

## 13. Phase Constant

```
a = ω √{ (εμ/2) · [ √(1 + (σ/εω)²) + 1 ] }
```

---

## 14. Attenuation Constant

```
b = ω √{ (εμ/2) · [ √(1 + (σ/εω)²) − 1 ] }
```

---

## 15. Good Conductors

> Condition: `σ >> ωε`

```
a = b = √(μσω / 2)
```

**Phase shift:**

```
φ = arctan(b/a) = π/4
```

**Skin depth:**

```
δ = 1/b = √(2 / μσω)
```

---

## 16. Poor Conductors

> Condition: `σ << ωε`

```
a = ω√(εμ)

b = (σ/2) · √(μ/ε)
```

**Phase shift:**

```
φ = arctan( σ / 2εω )
```

**Skin depth:**

```
δ = 1/b = (2/σ) · √(ε/μ)
```

---

## 17. Attenuation of EM Waves

Inside a conductor, amplitudes decay exponentially:

```
E⃗₀*(r) = E⃗₀ · e^(−br)

B⃗₀*(r) = B⃗₀ · e^(−br)
```

---

## 18. Skin Depth

Skin depth is the distance at which amplitude reduces by a factor of `1/e`:

```
δ = 1/b
```

At `r = 1/b`:

```
E = E₀ / e
```

---

## 19. Phase Difference Between E and B

In a conducting medium, `E⃗` and `B⃗` are **not in phase**.

**Wave vector:**

```
k = |k| · e^(iφ)

|k| = √(a² + b²)
```

Where `φ` is the **phase shift between electric and magnetic fields**.

---

*End of Electromagnetic Waves Formula Sheet*
