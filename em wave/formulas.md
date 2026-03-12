# Electromagnetic Waves — Complete Formula Sheet

Formulas for **UPH013 Physics – Electromagnetic Waves**

---

## 1. Maxwell's Equations (Integral Form)

### Gauss's Law for Electric Field

```
∯ E · dS = q / ε₀
```

### Gauss's Law for Magnetic Field

```
∯ B · dS = 0
```

> This implies **magnetic monopoles do not exist**.

### Ampère–Maxwell Law

```
∮ B · dl = μ₀ × ( i + ε₀ × dΦ_E/dt )
```

### Faraday's Law of Electromagnetic Induction

```
∮ E · dl = −dΦ_B/dt
```

---

## 2. Maxwell's Equations (Differential Form)

### Gauss's Law (Electric)

```
div(E) = ρ / ε₀
```

### Gauss's Law (Magnetic)

```
div(B) = 0
```

### Faraday's Law

```
curl(E) = −∂B/∂t
```

### Ampère–Maxwell Law

```
curl(B) = μ₀ × ( J + ε₀ × ∂E/∂t )
```

---

## 3. Electromagnetic Waves in Vacuum

In vacuum: `ρ = 0`, `J = 0`

### Simplified Maxwell Equations

```
div(E) = 0

div(B) = 0

curl(E) = −∂B/∂t

curl(B) = μ₀ε₀ × ∂E/∂t
```

---

## 4. Wave Equations

**Electric field:**

```
∇²E = μ₀ε₀ × ∂²E/∂t²
```

**Magnetic field:**

```
∇²B = μ₀ε₀ × ∂²B/∂t²
```

**Standard form:**

```
∇²y = (1/v²) × ∂²y/∂t²
```

---

## 5. Plane Wave Solutions

**Electric field:**

```
E(r, t) = E₀ × exp[i(k·r − ωt)]
```

**Magnetic field:**

```
B(r, t) = B₀ × exp[i(k·r − ωt)]
```

---

## 6. Wave Vector

```
k = 2π / λ
```

---

## 7. Speed of Electromagnetic Waves

```
v = 1 / sqrt(μ₀ε₀) = 3 × 10⁸ m/s
```

> This equals the **speed of light**.

---

## 8. Transverse Nature of EM Waves

From divergence equations:

```
div(E) = 0  -->  k is perpendicular to E

div(B) = 0  -->  k is perpendicular to B
```

### Cross Product Relations

```
k x E = ωB   -->  B is perpendicular to both E and k

k x B = −ωE  -->  E is perpendicular to both B and k
```

---

## 9. Intrinsic Impedance of Free Space

Assume: E along x-axis, B along y-axis, propagation along z-axis.

```
k × Ex = μ₀ω × Hy   -->   Ex/Hy = μ₀ω/k
```

Since `ω/k = c`:

```
Z = sqrt(μ₀/ε₀) = 377 Ω
```

---

## 10. EM Waves in Conducting Medium

**Material properties:**

```
ε = εᵣ × ε₀
μ = μᵣ × μ₀
```

**Current density:**

```
J = σE
```

### Modified Ampère–Maxwell Law

```
curl(B) = μ × ( J + ε × ∂E/∂t )
```

---

## 11. Wave Equations in Conductors

**Electric field:**

```
∇²E = μσ × ∂E/∂t  +  με × ∂²E/∂t²
```

**Magnetic field:**

```
∇²B = μσ × ∂B/∂t  +  με × ∂²B/∂t²
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
2ab     = μσω
```

---

## 13. Phase Constant

```
a = ω × sqrt( (εμ/2) × [ sqrt(1 + (σ/εω)²) + 1 ] )
```

---

## 14. Attenuation Constant

```
b = ω × sqrt( (εμ/2) × [ sqrt(1 + (σ/εω)²) − 1 ] )
```

---

## 15. Good Conductors

> Condition: `σ >> ωε`

```
a = b = sqrt(μσω / 2)
```

**Phase shift:**

```
φ = arctan(b/a) = π/4
```

**Skin depth:**

```
δ = 1/b = sqrt(2 / μσω)
```

---

## 16. Poor Conductors

> Condition: `σ << ωε`

```
a = ω × sqrt(εμ)

b = (σ/2) × sqrt(μ/ε)
```

**Phase shift:**

```
φ = arctan( σ / (2εω) )
```

**Skin depth:**

```
δ = 1/b = (2/σ) × sqrt(ε/μ)
```

---

## 17. Attenuation of EM Waves

Inside a conductor, amplitudes decay exponentially:

```
E(r) = E₀ × exp(−br)

B(r) = B₀ × exp(−br)
```

---

## 18. Skin Depth

Skin depth is the distance at which amplitude reduces by `1/e`:

```
δ = 1/b
```

At `r = 1/b`:

```
E = E₀ / e
```

---

## 19. Phase Difference Between E and B

In a conducting medium, E and B are **not in phase**.

```
k = |k| × exp(iφ)

|k| = sqrt(a² + b²)
```

Where `φ` is the **phase shift between electric and magnetic fields**.

---

*End of Electromagnetic Waves Formula Sheet*
