# Pure Algebraic Boundary Prediction (BP) Engine

This repository contains the foundational Python implementation of the **Algebraic Boundary Prediction (BP) Algorithm** for Finite Operator Calculus. 

Unlike traditional holonomic methods (like Zeilberger's algorithm) that rely on solving dense linear systems over rational function fields, the BP algorithm treats the universal degree law ($D = kr + 2m$) and its multivariate extensions as deterministic geometric oracles. This eliminates expression swell and operates in strictly bounded $\mathcal{O}(D \log^2 D)$ time.

## Core Features
* **Generalized Univariate BP:** Reconstructs exact closed-form polynomials for any analytic delta operator of singularity order `k`.
* **Multivariate Ray Projection:** Handles adversarial entangled weights (e.g., $P(x,y,z) = (x-y+z)^m$) across mixed-singularity configurations ($k_1=1, k_2=2, k_3=3$).
* **Sentinel Safeguard:** Enforces a strict cross-validation step by evaluating the reconstructed polynomial at $n = D+1$ to mathematically certify the geometric boundary.

## Dependencies
* `sympy` (>= 1.10)
* `numpy`

## Usage

Run the symbolic engine directly to see the exact parametric polynomial extraction for both univariate and multivariate operator configurations:

```bash
python bp_engine_core.py