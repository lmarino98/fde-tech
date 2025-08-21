# Robotic Arm Package Sorting System

A Python function for automatically sorting packages into different handling categories based on their physical dimensions and mass.

## Overview

The `sort()` function classifies packages into three main categories plus error handling, enabling automated sorting for warehouse and logistics operations.

## Sorting Criteria

### Package Classifications

**STANDARD** - Normal handling

-   Not bulky AND not heavy
-   Can be processed automatically with standard equipment

**SPECIAL** - Requires special handling

-   Either heavy OR bulky
-   Needs specialized equipment or manual intervention

**REJECTED** - Cannot be processed

-   Both heavy AND bulky
-   Requires rejection from automated system

### Bulky Package Definition

A package is considered **bulky** if:

-   Volume ≥ 1,000,000 cm³ OR
-   Any dimension ≥ 150 cm

### Heavy Package Definition

A package is considered **heavy** if:

-   Mass ≥ 20 kg

## Function Signature

```python
def sort(width, height, length, mass) -> str
```

### Parameters

-   `width` (float): Package width in centimeters
-   `height` (float): Package height in centimeters
-   `length` (float): Package length in centimeters
-   `mass` (float): Package mass in kilograms

### Return Values

-   `"STANDARD"` - Normal packages for standard processing
-   `"SPECIAL"` - Packages requiring special handling
-   `"REJECTED"` - Packages that cannot be processed
-   `"Error"` - Different type of errors depending on the case (type, Infinite, None, etc...)

```
Input Validation
↓
Valid Input?
├─ No → Return Error Code
└─ Yes → Continue
↓
Calculate Volume
↓
Check if Bulky
(Volume ≥ 1M cm³ OR Any dimension ≥ 150cm)
↓
Check if Heavy
(Mass ≥ 20 kg)
↓
┌───────────────────────────┐
│ Heavy? │ Bulky? │ Result  │
├───────────────────────────┼
│ No  │ No    │ STANDARD    │
│ Yes │ No    │ SPECIAL     │
│ No  │ Yes   │ SPECIAL     │
│ Yes │ Yes   │ REJECTED    │
└─────────────┴─────────────┴

```

## Testing

The system includes comprehensive test cases covering:

### Standard Test Cases

-   Normal packages (all categories)
-   Edge cases at exact thresholds
-   Extreme dimension packages (microscopic, gigantic)
-   Unusual shapes (telephone pole, paper-thin)

### Input Validation Tests

-   Type validation (strings, None, booleans)
-   Range validation (negative values, zero values)
-   Special values (infinity, NaN)
-   Mixed valid/invalid inputs

### Running Tests

```bash
python package_sorter.py
```

This will run all test cases and display the results for verification.

## 🔧 Installation

1. Clone or download the `package_sorter.py` file
2. Ensure Python 3.6+ is installed
