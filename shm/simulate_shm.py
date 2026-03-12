"""
simulate_shm.py
---------------
Visualises the physics equations derived in shm/derivations.md.

Four subplots are produced and saved to shm_plots.png:
  1. Simple Harmonic Motion          – x(t) = A cos(ωt + φ)
  2. Phase Space (velocity vs disp.) – v = ±ω √(A² − x²)
  3. Damped Harmonic Motion          – underdamped solution
  4. Forced Oscillations / Resonance – amplitude vs driving frequency ω
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")          # non-interactive backend; works without a display
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------------------------------
# Shared parameters
# ---------------------------------------------------------------------------
A      = 1.0          # amplitude  (m)
omega0 = 2.0 * np.pi  # natural angular frequency (rad/s)  →  T = 1 s
phi    = 0.0          # phase constant (rad)
m      = 1.0          # mass (kg)
b      = 0.5          # damping coefficient (kg/s)
F0     = 1.0          # driving force amplitude (N)

t = np.linspace(0, 3, 1000)   # time array (s)

# ---------------------------------------------------------------------------
# 1. Simple Harmonic Motion  x(t) = A cos(ωt + φ)
# ---------------------------------------------------------------------------
x_shm = A * np.cos(omega0 * t + phi)

# ---------------------------------------------------------------------------
# 2. Phase Space  v = ±ω √(A² − x²)
#    We parametrise over x ∈ [−A, A] to get the ellipse directly.
# ---------------------------------------------------------------------------
x_phase = np.linspace(-A, A, 1000)
v_pos   =  omega0 * np.sqrt(np.maximum(A**2 - x_phase**2, 0))
v_neg   = -omega0 * np.sqrt(np.maximum(A**2 - x_phase**2, 0))

# ---------------------------------------------------------------------------
# 3. Damped Harmonic Motion (underdamped)
#    ω' = √(ω₀² − (b/2m)²)
#    x(t) = A e^(−bt/2m) cos(ω't + φ)
# ---------------------------------------------------------------------------
gamma   = b / (2 * m)                         # damping ratio
omega_d = np.sqrt(np.maximum(omega0**2 - gamma**2, 0))  # damped frequency
x_damp  = A * np.exp(-gamma * t) * np.cos(omega_d * t + phi)
envelope_pos =  A * np.exp(-gamma * t)
envelope_neg = -A * np.exp(-gamma * t)

# ---------------------------------------------------------------------------
# 4. Forced Oscillations / Resonance
#    A(ω) = (F₀/m) / √[(ω² − ω₀²)² + (bω/m)²]
# ---------------------------------------------------------------------------
omega_drive = np.linspace(0.1, 4 * np.pi, 1000)  # driving frequency range
amplitude_resonance = (F0 / m) / np.sqrt(
    (omega_drive**2 - omega0**2)**2 + (b * omega_drive / m)**2
)

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle("Simple Harmonic Motion – Visualisation of Derivations", fontsize=14)

# --- subplot 1: SHM ---
ax1 = axes[0, 0]
ax1.plot(t, x_shm, color="steelblue", linewidth=1.8)
ax1.axhline(0, color="black", linewidth=0.6, linestyle="--")
ax1.set_title("Simple Harmonic Motion")
ax1.set_xlabel("Time t (s)")
ax1.set_ylabel("Displacement x (m)")
ax1.text(0.02, 0.92, r"$x(t)=A\cos(\omega t+\phi)$",
         transform=ax1.transAxes, fontsize=10)
ax1.grid(True, alpha=0.3)

# --- subplot 2: phase space ---
ax2 = axes[0, 1]
ax2.plot(x_phase, v_pos, color="darkorange", linewidth=1.8)
ax2.plot(x_phase, v_neg, color="darkorange", linewidth=1.8)
ax2.set_title("Phase Space (Velocity vs Displacement)")
ax2.set_xlabel("Displacement x (m)")
ax2.set_ylabel("Velocity v (m/s)")
ax2.text(0.02, 0.92, r"$v=\pm\omega\sqrt{A^2-x^2}$",
         transform=ax2.transAxes, fontsize=10)
ax2.grid(True, alpha=0.3)

# --- subplot 3: damped motion ---
ax3 = axes[1, 0]
ax3.plot(t, x_damp,        color="forestgreen",  linewidth=1.8, label="x(t)")
ax3.plot(t, envelope_pos,  color="red",           linewidth=1,   linestyle="--", label="Envelope")
ax3.plot(t, envelope_neg,  color="red",           linewidth=1,   linestyle="--")
ax3.axhline(0, color="black", linewidth=0.6, linestyle="--")
ax3.set_title("Damped Harmonic Motion (Underdamped)")
ax3.set_xlabel("Time t (s)")
ax3.set_ylabel("Displacement x (m)")
ax3.text(0.02, 0.92, r"$x(t)=Ae^{-bt/2m}\cos(\omega' t+\phi)$",
         transform=ax3.transAxes, fontsize=10)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# --- subplot 4: resonance ---
ax4 = axes[1, 1]
ax4.plot(omega_drive, amplitude_resonance, color="mediumpurple", linewidth=1.8)
ax4.axvline(omega0, color="red", linewidth=1, linestyle="--", label=r"$\omega_0$")
ax4.set_title("Forced Oscillations & Resonance")
ax4.set_xlabel(r"Driving Frequency $\omega$ (rad/s)")
ax4.set_ylabel("Amplitude A (m)")
ax4.text(0.02, 0.92,
         r"$A=\frac{F_0/m}{\sqrt{(\omega^2-\omega_0^2)^2+(b\omega/m)^2}}$",
         transform=ax4.transAxes, fontsize=9)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.tight_layout()

# Save next to this script so the output is predictable regardless of cwd
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shm_plots.png")
plt.savefig(output_path, dpi=150)
print(f"Plots saved to {output_path}")
