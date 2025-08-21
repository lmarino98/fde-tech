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
    
    print("\nStandard package:")
    result1 = sort(50, 50, 50, 10)
    print(f"Package (50x50x50 cm, 10 kg) -> {result1}")
    
    print("\nHeavy package:")
    result2 = sort(50, 50, 50, 25)
    print(f"Package (50x50x50 cm, 25 kg) -> {result2}")
    
    print("\nBulky package (by volume):")
    result3 = sort(100, 100, 100, 10)
    print(f"Package (100x100x100 cm, 10 kg) -> {result3}")
    
    print("\nBulky package (by dimension):")
    result4 = sort(160, 50, 50, 10)
    print(f"Package (160x50x50 cm, 10 kg) -> {result4}")
    
    print("\nRejected package:")
    result5 = sort(160, 50, 50, 25)
    print(f"Package (160x50x50 cm, 25 kg) -> {result5}")
    
    print("\nEdge case:")
    result6 = sort(150, 50, 50, 20)
    print(f"Package (150x50x50 cm, 20 kg) -> {result6}")
    
    print("\nMicroscopic package:")
    result7 = sort(0.001, 0.001, 0.001, 0.001)
    print(f"Package (0.001x0.001x0.001 cm, 0.001 kg) -> {result7}")
    
    print("\nGiant spaghetti box:")
    result8 = sort(500, 5, 5, 2)
    print(f"Package (500x5x5 cm, 2 kg) -> {result8}")
    
    print("\nBalloon package:")
    result9 = sort(300, 300, 300, 0.5)
    print(f"Package (300x300x300 cm, 0.5 kg) -> {result9}")

    print("\nPaper-thin wide package:")
    result10 = sort(1000, 1000, 0.01, 5)
    print(f"Package (1000x1000x0.01 cm, 5 kg) -> {result10}")
    
    print("\nTheoretical zero-width package:")
    result11 = sort(0, 100, 100, 10)
    print(f"Package (0x100x100 cm, 10 kg) -> {result11}")

    print("\nAlmost heavy package:")
    result12 = sort(50, 50, 50, 19.999999)
    print(f"Package (50x50x50 cm, 19.999999 kg) -> {result12}")
    
    print("\nTelephone pole package:")
    result13 = sort(2000, 20, 20, 100)
    print(f"Package (2000x20x20 cm, 100 kg) -> {result13}")
    
    print("\nWeird shape at volume threshold:")
    result14 = sort(1000, 10, 100, 8)
    print(f"Package (1000x10x100 cm, 8 kg) -> {result14}")
    
    print("\n" + "="*60)
    print("EDGE CASES AND INPUT VALIDATION TESTS")
    print("="*60)
    
    print("\nNegative dimensions:")
    result15 = sort(-10, 50, 50, 10)
    print(f"Package (-10x50x50 cm, 10 kg) -> {result15}")
    
    print("\nNegative mass:")
    result16 = sort(50, 50, 50, -5)
    print(f"Package (50x50x50 cm, -5 kg) -> {result16}")
    
    print("\nZero width:")
    result17 = sort(0, 50, 50, 10)
    print(f"Package (0x50x50 cm, 10 kg) -> {result17}")
    
    print("\nZero mass:")
    result18 = sort(50, 50, 50, 0)
    print(f"Package (50x50x50 cm, 0 kg) -> {result18}")
    
    print("\nAll zeros:")
    result19 = sort(0, 0, 0, 0)
    print(f"Package (0x0x0 cm, 0 kg) -> {result19}")
    
    print("\nString input:")
    result20 = sort("50", "50", "50", "10")
    print(f"Package ('50'x'50'x'50' cm, '10' kg) -> {result20}")
    
    print("\nInvalid string:")
    result21 = sort("abc", 50, 50, 10)
    print(f"Package ('abc'x50x50 cm, 10 kg) -> {result21}")
    
    print("\nNone input:")
    result22 = sort(None, 50, 50, 10)
    print(f"Package (None x 50 x 50 cm, 10 kg) -> {result22}")
    
    print("\nInfinite dimension:")
    result23 = sort(float('inf'), 50, 50, 10)
    print(f"Package (inf x 50 x 50 cm, 10 kg) -> {result23}")
    
    print("\nInfinite mass:")
    result24 = sort(50, 50, 50, float('inf'))
    print(f"Package (50x50x50 cm, inf kg) -> {result24}")
    
    print("\nNaN dimension:")
    result25 = sort(float('nan'), 50, 50, 10)
    print(f"Package (NaN x 50 x 50 cm, 10 kg) -> {result25}")
    
    print("\nExtremely large dimension:")
    result26 = sort(1e20, 1e20, 1e20, 10)
    print(f"Package (1e20 x 1e20 x 1e20 cm, 10 kg) -> {result26}")
    
    print("\nInteger inputs:")
    result27 = sort(100, 100, 100, 15)
    print(f"Package (100x100x100 cm, 15 kg) -> {result27}")
    
    print("\nMixed valid/invalid:")
    result28 = sort(50, "invalid", 50, 10)
    print(f"Package (50 x 'invalid' x 50 cm, 10 kg) -> {result28}")
    
    print("\nBoolean inputs:")
    result29 = sort(True, False, True, True)
    print(f"Package (True x False x True cm, True kg) -> {result29}")

