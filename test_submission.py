"""
Test cases for Lab 06 - DO NOT MODIFY

Tests for root finding functions:
- bisection
- newton
- loan_payment_residual
- find_interest_rate
"""

from __future__ import annotations

import math

import pytest

from submission import bisection, find_interest_rate, loan_payment_residual, newton


# =============================================================================
# Tests for bisection
# =============================================================================


def test_bisection_returns_tuple():
    """Test that bisection returns (root, iterations, history)."""

    def f(x):
        return x**2 - 2

    result = bisection(f, 1, 2, tol=1e-6)
    assert isinstance(result, tuple)
    assert len(result) == 3


def test_bisection_sqrt2():
    """Test bisection finds sqrt(2) for f(x) = x^2 - 2."""

    def f(x):
        return x**2 - 2

    root, iters, history = bisection(f, 1, 2, tol=1e-10)
    assert root == pytest.approx(math.sqrt(2), rel=1e-9)


def test_bisection_iterations_reasonable():
    """Test that bisection converges in reasonable iterations."""

    def f(x):
        return x**2 - 2

    root, iters, history = bisection(f, 1, 2, tol=1e-10)
    # For interval [1, 2], need about 34 iterations for 1e-10 tolerance
    # log2(1 / 1e-10) = 33.2
    assert iters < 60
    assert iters > 10


def test_bisection_history_length():
    """Test that history length matches iterations."""

    def f(x):
        return x**2 - 2

    root, iters, history = bisection(f, 1, 2, tol=1e-6)
    assert len(history) == iters


def test_bisection_tolerance_check():
    """Test that bisection respects tolerance."""

    def f(x):
        return x**3 - x - 2  # root near 1.521

    root, iters, history = bisection(f, 1, 2, tol=1e-8)
    assert abs(f(root)) < 1e-7


def test_bisection_sin_pi():
    """Test bisection on sin(x) finds pi."""

    def f(x):
        return math.sin(x)

    root, iters, history = bisection(f, 3, 4, tol=1e-10)
    assert root == pytest.approx(math.pi, rel=1e-9)


def test_bisection_requires_sign_change():
    """Test that bisection raises if there is no sign change."""

    def f(x):
        return x**2 + 1  # always positive

    with pytest.raises(ValueError):
        bisection(f, -1, 1)


# =============================================================================
# Tests for newton
# =============================================================================


def test_newton_returns_tuple():
    """Test that newton returns (root, iterations, history)."""

    def f(x):
        return x**2 - 2

    def df(x):
        return 2 * x

    result = newton(f, df, 1.5, tol=1e-6)
    assert isinstance(result, tuple)
    assert len(result) == 3


def test_newton_sqrt2():
    """Test Newton finds sqrt(2) for f(x) = x^2 - 2."""

    def f(x):
        return x**2 - 2

    def df(x):
        return 2 * x

    root, iters, history = newton(f, df, 1.5, tol=1e-10)
    assert root == pytest.approx(math.sqrt(2), rel=1e-9)


def test_newton_fast_convergence():
    """Test that Newton converges much faster than bisection."""

    def f(x):
        return x**2 - 2

    def df(x):
        return 2 * x

    root, iters, history = newton(f, df, 1.5, tol=1e-10)
    assert iters < 10


def test_newton_history_length():
    """Test that history length matches iterations."""

    def f(x):
        return x**2 - 2

    def df(x):
        return 2 * x

    root, iters, history = newton(f, df, 1.5, tol=1e-6)
    assert len(history) == iters


def test_newton_cubic():
    """Test Newton on x^3 - x - 2."""

    def f(x):
        return x**3 - x - 2

    def df(x):
        return 3 * x**2 - 1

    root, iters, history = newton(f, df, 1.5, tol=1e-10)
    assert abs(f(root)) < 1e-9


def test_newton_derivative_too_small_raises():
    """Test that Newton guards against near-zero derivatives."""

    def f(x):
        return x**3 - 1  # f(0) != 0 but f'(0) = 0

    def df(x):
        return 3 * x**2

    with pytest.raises(ValueError):
        newton(f, df, 0.0)


# =============================================================================
# Tests for loan_payment_residual
# =============================================================================


def test_loan_payment_residual_zero_rate():
    """With 0% rate, monthly payments just subtract from principal."""
    residual = loan_payment_residual(0.0, 1200, 100, 12)
    assert residual == pytest.approx(0.0, abs=1e-6)


def test_loan_payment_residual_positive_when_underpaid():
    """Residual is positive when payment is too small."""
    residual = loan_payment_residual(0.12, 1000, 50, 12)
    assert residual > 0


def test_loan_payment_residual_negative_when_overpaid():
    """Residual is negative when payment is too large."""
    residual = loan_payment_residual(0.12, 1000, 200, 12)
    assert residual < 0


# =============================================================================
# Tests for find_interest_rate
# =============================================================================


def test_find_interest_rate_basic():
    """$10k loan, $879.16/mo for 12 months is ~10% annual rate."""
    rate = find_interest_rate(10000, 879.16, 12)
    assert rate == pytest.approx(0.10, rel=0.01)


def test_find_interest_rate_returns_annual():
    """Returned rate is annual (not monthly)."""
    rate = find_interest_rate(1000, 100, 12)
    assert 0 <= rate <= 1


def test_find_interest_rate_low():
    """Finding a low interest rate (near 0%)."""
    rate = find_interest_rate(1200, 100.5, 12)
    assert rate < 0.05
