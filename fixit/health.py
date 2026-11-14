def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Calculate BMI using weight in kg and height in cm."""
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers")

    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)