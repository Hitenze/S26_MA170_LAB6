"""
MATH 170 - Lab 06: Root Finding (Bisection + Newton)
Spring 2026

Instructions
------------
1) Implement the bisection method (robust, guaranteed if bracketed).
2) Implement Newton's method (fast, but can fail).
3) Use bisection to solve a small real application (loan interest rate).

Core restriction (for this lab's submission):
- Do NOT call SciPy root finders (e.g., scipy.optimize.bisect/newton).
  Implement the algorithms yourself.
"""


def bisection(f, a, b, tol=1e-10, max_iter=100):
    """
    Find a root of f in [a, b] using the bisection method.

    Parameters
    ----------
    f : callable
        Function to find a root of (solve f(x) = 0).
    a, b : float
        Interval endpoints. Must have a sign change: f(a) * f(b) < 0.
    tol : float
        Convergence tolerance (stop when interval width < tol OR |f(m)| < tol).
    max_iter : int
        Maximum number of iterations.

    Returns
    -------
    tuple
        (root, iterations, history)
        - root: approximate root
        - iterations: number of iterations performed
        - history: list of midpoints (length == iterations)
    """
    # TODO:
    # - Check bracket validity (sign change on [a, b]); raise ValueError if not.
    # - Repeatedly bisect the interval and keep the half that contains the root.
    # - Track midpoints in `history`.
    # - Return (root, iterations, history).

    return None  # Replace with your code


def newton(f, df, x0, tol=1e-10, max_iter=50):
    """
    Find a root of f using Newton's method.

    Newton update:
        x_{n+1} = x_n - f(x_n) / f'(x_n)

    Parameters
    ----------
    f : callable
        Function to find a root of.
    df : callable
        Derivative of f.
    x0 : float
        Initial guess.
    tol : float
        Convergence tolerance (stop when |f(x)| < tol).
    max_iter : int
        Maximum number of iterations.

    Returns
    -------
    tuple
        (root, iterations, history)
        - root: approximate root
        - iterations: number of iterations performed
        - history: list of iterates x_1, x_2, ... (length == iterations)
    """
    # TODO:
    # - Iterate Newton updates starting at x0.
    # - Stop when |f(x)| < tol.
    # - If the derivative is too small, raise ValueError.
    # - Track iterates in `history` and return (root, iterations, history).

    return None  # Replace with your code


def loan_payment_residual(rate, principal, payment, n_months):
    """
    Residual (remaining balance) after n_months payments for a simple loan model.

    We model monthly compounding and fixed monthly payments:
      balance_{k+1} = balance_k * (1 + r_monthly) - payment

    If the residual is:
    - 0: exactly paid off
    - positive: underpaid (still owe money)
    - negative: overpaid (paid too much)

    Parameters
    ----------
    rate : float
        Annual interest rate (e.g., 0.12 for 12%).
    principal : float
        Initial loan amount.
    payment : float
        Fixed monthly payment.
    n_months : int
        Number of payments.

    Returns
    -------
    float
        Remaining balance after n_months payments.
    """
    # TODO:
    # - Handle the special case rate == 0.0.
    # - Otherwise simulate month-by-month as described in the docstring.

    return None  # Replace with your code


def find_interest_rate(principal, payment, n_months):
    """
    Find the annual interest rate that makes the loan residual ~ 0.

    Uses bisection on a reasonable interval of annual rates.

    Parameters
    ----------
    principal : float
        Initial loan amount.
    payment : float
        Fixed monthly payment.
    n_months : int
        Number of payments.

    Returns
    -------
    float
        Annual interest rate (e.g., 0.10 for 10%).
    """
    # TODO:
    # - Define g(rate) = loan_payment_residual(rate, principal, payment, n_months)
    # - Use bisection to find a root of g on an interval like [0.0, 0.50].

    return None  # Replace with your code
