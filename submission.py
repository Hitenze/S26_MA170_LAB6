"""
MATH 170 - Lab 06: Root Finding -- Reference Solution
Spring 2026

This file is for instructor/reference use.
"""

from __future__ import annotations


def bisection(f, a, b, tol=1e-10, max_iter=100):
    if tol <= 0:
        raise ValueError("tol must be positive")
    if max_iter <= 0:
        raise ValueError("max_iter must be positive")

    # Ensure a <= b
    if a > b:
        a, b = b, a

    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0, []
    if fb == 0:
        return b, 0, []

    if fa * fb > 0:
        raise ValueError("Need sign change on [a, b]")

    history: list[float] = []

    for i in range(max_iter):
        m = (a + b) / 2
        fm = f(m)
        history.append(m)

        if abs(fm) < tol or abs(b - a) < tol:
            return m, i + 1, history

        # Keep the half interval with the sign change.
        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    return m, max_iter, history


def newton(f, df, x0, tol=1e-10, max_iter=50):
    if tol <= 0:
        raise ValueError("tol must be positive")
    if max_iter <= 0:
        raise ValueError("max_iter must be positive")

    x = float(x0)
    history: list[float] = []

    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i, history

        dfx = df(x)
        if abs(dfx) < 1e-15:
            raise ValueError("Derivative too small")

        x = x - fx / dfx
        history.append(x)

    return x, max_iter, history


def loan_payment_residual(rate, principal, payment, n_months):
    if n_months < 0:
        raise ValueError("n_months must be non-negative")

    if rate == 0.0:
        return float(principal) - float(payment) * int(n_months)

    r_monthly = rate / 12
    balance = float(principal)

    for _ in range(int(n_months)):
        balance *= 1 + r_monthly
        balance -= payment

    return float(balance)


def find_interest_rate(principal, payment, n_months):
    def residual(rate):
        return loan_payment_residual(rate, principal, payment, n_months)

    root, iters, history = bisection(residual, 0.0, 0.50, tol=1e-10, max_iter=200)
    return root
