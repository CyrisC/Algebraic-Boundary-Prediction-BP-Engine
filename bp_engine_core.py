### 2. `bp_engine_core.py`

```python
# ==============================================================================
# PURE ALGEBRAIC BOUNDARY PREDICTION (BP) SYMBOLIC ENGINE
# ==============================================================================
# Theory: Universal Degree Laws and Algebraic Boundary Prediction in 
#         Finite Operator Calculus
# ==============================================================================

import sympy as sp
from sympy.polys.polyfuncs import interpolate

# ==============================================================================
# 1. Generalized Univariate BP Algorithm (For any singularity order k)
# ==============================================================================

def evaluate_operator_action_dk(weight_expr, var_x, r, gamma, n_val, k_order):
    """
    Computes the scalar value of the operator action for a generalized 
    singularity order k. Uses the Puiseux-umbral basis expansion.
    """
    x = sp.Symbol('x')
    P_x = weight_expr.subs(var_x, x)
    idx = n_val + r
    
    if idx < 0:
        return sp.Rational(0)
        
    y = x + gamma * n_val
    seq_expr = (y ** (k_order * idx)) / sp.factorial(k_order * idx)
    target_expr = P_x * seq_expr
    
    if k_order * n_val == 0:
        deriv = target_expr
    else:
        deriv = sp.diff(target_expr, x, k_order * n_val)
        
    return sp.simplify(deriv.subs(x, 0))

def umbral_bp_sum(weight_expr, var_x, k_order, r, m, n_symbol, gamma=1):
    """
    Reconstructs the exact closed-form polynomial utilizing the 
    Universal Degree Law: D = k*r + 2*m.
    """
    # The BP Geometric Oracle
    D = k_order * r + 2 * m
    points = []
    
    # Generate D+2 sample points for exact polynomial reconstruction + Sentinel
    for i in range(D + 2):
        val = evaluate_operator_action_dk(weight_expr, var_x, r, gamma, i, k_order)
        points.append((i, val))
        
    # Fast reconstruction via interpolation over the integer grid
    closed_form = sp.simplify(interpolate([p for p in points[:-1]], n_symbol))
    
    # Cross-validation Sentinel Safeguard (The BP Guarantee)
    if sp.simplify(closed_form.subs(n_symbol, D + 1)) != points[-1][1]:
        raise ValueError("Error: Oracle Boundary Violated!")
        
    return sp.collect(closed_form, n_symbol)


# ==============================================================================
# 2. Multivariate Ray Projection BP (Adversarial Entanglement)
# ==============================================================================

def evaluate_multivariate_action_ray(m_weight, n_val):
    """
    Evaluates the multivariate action for mixed singularities:
    k1 = 1 (D), k2 = 2 (D^2), k3 = 3 (D^3).
    Target adversarial weight: P(x,y,z) = (x - y + z)^m
    """
    x, y, z = sp.symbols('x y z')
    P_xyz = (x - y + z)**m_weight
    
    if n_val == 0:
        return P_xyz.subs({x: 0, y: 0, z: 0})
        
    seq_x = (x + n_val)**n_val / sp.factorial(n_val)
    seq_y = (y + n_val)**(2 * n_val) / sp.factorial(2 * n_val)
    seq_z = (z + n_val)**(3 * n_val) / sp.factorial(3 * n_val)
    
    target = P_xyz * seq_x * seq_y * seq_z
    
    # Independent coordinate-wise annihilation
    deriv = sp.diff(target, x, n_val)
    deriv = sp.diff(deriv, y, 2 * n_val)
    deriv = sp.diff(deriv, z, 3 * n_val)
    
    return sp.simplify(deriv.subs({x: 0, y: 0, z: 0}))

def multivariate_bp_verification(m_weight):
    """
    Reconstructs the multivariate polynomial using a diagonal ray projection.
    Verifies the Anisotropic Algebraic Stretching phenomenon.
    """
    n_symbol = sp.Symbol('n')
    
    # Diagonal ray projection dynamically locks D = 2m
    D = 2 * m_weight 
    points = []
    
    for i in range(D + 2):
        points.append((i, evaluate_multivariate_action_ray(m_weight, i)))
        
    closed_form = sp.simplify(interpolate(points[:-1], n_symbol))
    
    # Cross-validation Sentinel Safeguard
    if sp.simplify(closed_form.subs(n_symbol, D + 1)) != points[-1][1]:
        raise ValueError("Error: Multivariate Oracle Boundary Violated!")
        
    return sp.collect(closed_form, n_symbol)


# ==============================================================================
# Execution Entry Point
# ==============================================================================
if __name__ == "__main__":
    x, n = sp.symbols('x n')
    
    print("=" * 60)
    print(" PURE BP SYMBOLIC ENGINE EXECUTION")
    print("=" * 60 + "\n")

    # --------------------------------------------------------------------------
    # Test 1: Generalized Univariate Test
    # --------------------------------------------------------------------------
    print("1. Univariate Test: k=2, m=3, P(x)=x^3, r=0")
    print("   Evaluating...")
    R_1D = umbral_bp_sum(weight_expr=x**3, var_x=x, k_order=2, r=0, m=3, n_symbol=n)
    print(f"   => Exact Result: {R_1D}\n")

    # --------------------------------------------------------------------------
    # Test 2: Multivariate Entanglement & Anisotropic Algebraic Stretching
    # --------------------------------------------------------------------------
    print("2. Multivariate Entanglement Test: P(x,y,z)=(x-y+z)^2")
    print("   Mixed Singularities: k1=1, k2=2, k3=3 | Projection: m=2")
    print("   Evaluating...")
    R_Multi = multivariate_bp_verification(m_weight=2)
    print(f"   => Exact Result: {R_Multi}\n")
    
    print("=" * 60)
    print(" ALL SENTINEL SAFEGUARDS PASSED.")
    print("=" * 60)