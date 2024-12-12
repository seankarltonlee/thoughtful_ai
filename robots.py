"""
Package Sorting System
"""

def sort_package(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages based on their dimensions and mass.
    
    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Mass of the package in kilograms
    
    Returns:
        str: 'STANDARD', 'SPECIAL', or 'REJECTED'
    
    Raises:
        ValueError: If any input dimension or mass is negative
    """
    
    if any(dim < 0 for dim in [width, height, length, mass]):
        raise ValueError("Dimensions and mass must be non-negative")
    
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20
    
    return "REJECTED" if (is_bulky and is_heavy) else "SPECIAL" if (is_bulky or is_heavy) else "STANDARD"