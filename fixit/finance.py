"""Loan EMI calculation utilities."""


def calculate_emi(principal: float, annual_rate: float, years: int) -> float:
    """Calculate and return the monthly loan EMI.

    Args:
        principal: Total loan amount.
        annual_rate: Annual interest rate in percentage.
        years: Loan duration in years.

    Returns:
        Monthly EMI amount.
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero")

    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative")

    if years <= 0:
        raise ValueError("Loan duration must be greater than zero")

    months = years * 12

    if annual_rate == 0:
        return principal / months

    monthly_rate = annual_rate / (12 * 100)

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

    return emi