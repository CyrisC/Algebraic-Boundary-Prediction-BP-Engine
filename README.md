# Pure Algebraic Boundary Prediction (BP) Engine

This repository contains the foundational Python implementation of the **Algebraic Boundary Prediction (BP) Algorithm** for Finite Operator Calculus.

Unlike traditional holonomic methods (like Zeilberger's algorithm) that rely on solving dense linear systems over rational function fields, the BP algorithm treats the universal degree law ($D = kr + 2m$) and its multivariate extensions as deterministic geometric oracles. This eliminates expression swell and operates in strictly bounded $\mathcal{O}(D \log^2 D)$ time.

## Corresponding Paper
**Universal Degree Laws and Algebraic Boundary Prediction in Finite Operator Calculus**  
**Author**: Cyris C.  
**Publication Date**: April 11, 2026  
**ResearchGate Preprint**: [DOI 10.13140/RG.2.2.13370.35527](https://www.researchgate.net/publication/403724592_Universal_Degree_Laws_and_Algebraic_Boundary_Prediction_in_Finite_Operator_Calculus)

This repository provides the official, reproducible implementation of the Algebraic Boundary Prediction (BP) algorithm and the Generalized Cyris Scaling Law presented in the paper.

## Core Features
- **Generalized Univariate BP**: Reconstructs exact closed-form polynomials for any analytic delta operator of singularity order `k`.
- **Multivariate Ray Projection**: Handles adversarial entangled weights (e.g., $P(x,y,z) = (x-y+z)^m$) across mixed-singularity configurations ($k_1=1, k_2=2, k_3=3$).
- **Sentinel Safeguard**: Enforces a strict cross-validation step by evaluating the reconstructed polynomial at $n = D+1$ to mathematically certify the geometric boundary.

## Dependencies
- `sympy` (>= 1.10)
- `numpy`

## Installation
```bash
git clone https://github.com/CyrisC/Algebraic-Boundary-Prediction-BP-Engine.git
cd Algebraic-Boundary-Prediction-BP-Engine
pip install -r requirements.txt