import math

def sort(width, height, length, mass):
    try:
        width = float(width)
        height = float(height)
        length = float(length)
        mass = float(mass)
    except (TypeError, ValueError):
        return "Type Error"
    
    if width < 0 or height < 0 or length < 0 or mass < 0:
        return "Negative Value Error"
    
    if (math.isnan(width) or math.isnan(height) or math.isnan(length) or math.isnan(mass) or
        math.isinf(width) or math.isinf(height) or math.isinf(length) or math.isinf(mass)):
        return "Infinity Value Error"
    
    if width == 0 or height == 0 or length == 0:
        volume = 0
        return "Zero Value Error, No package"
    else:
        volume = width * height * length
    
    is_bulky = False
    if volume >= 1000000:
        is_bulky = True
    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True
    
    is_heavy = False
    if mass >= 20:
        is_heavy = True
    
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"


if __name__ == "__main__":
    print("\n" + "="*60)
    print("STANDARD TEST CASES")
    print("="*60)
    
    # Basic test cases
    test_cases = [
        ("Standard package", 50, 50, 50, 10),
        ("Heavy package", 50, 50, 50, 25),
        ("Bulky package (by volume)", 100, 100, 100, 10),
        ("Bulky package (by dimension)", 160, 50, 50, 10),
        ("Rejected package", 160, 50, 50, 25),
        ("Edge case", 150, 50, 50, 20),
    ]
    
    for name, w, h, l, m in test_cases:
        result = sort(w, h, l, m)
        print(f"\n{name}:")
        print(f"Package ({w}x{h}x{l} cm, {m} kg) -> {result}")
    
    print("\n" + "="*60)
    print("ERROR HANDLING TESTS")
    print("="*60)
    
    error_cases = [
        ("Negative dimensions", -10, 50, 50, 10),
        ("Negative mass", 50, 50, 50, -5),
        ("Zero width", 0, 50, 50, 10),
        ("String input", "50", "50", "50", "10"),
        ("Invalid string", "abc", 50, 50, 10),
        ("None input", None, 50, 50, 10),
        ("Infinite dimension", float('inf'), 50, 50, 10),
        ("NaN dimension", float('nan'), 50, 50, 10),
    ]
    
    for name, w, h, l, m in error_cases:
        result = sort(w, h, l, m)
        print(f"\n{name}:")
        print(f"Package ({w}x{h}x{l} cm, {m} kg) -> {result}")

