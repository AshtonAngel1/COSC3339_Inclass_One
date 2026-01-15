# ASHTON MARES
# COSC3339
# 1/15/2026

"""
ASSIGNMENT: INTRODUCTION TO MERGING
-----------------------------------
This file contains several methods with logical errors, poor style, 
and complex constructs. Your goal is to fix them across multiple 
branches to simulate merge conflicts.
"""

import math
import random

# This method contains a bug. In your commit note, state the bug and how you fixed it
def CALCULATE_HYPOTENUSE(SIDE_A, SIDE_B):
    RESULT = math.sqrt((SIDE_A ** 2) + (SIDE_B ** 2))
    return RESULT

# This method contains a bug. In your commit note, state the bug and how you fixed it
def COUNT_WORDS(SENTENCE):
    if len(SENTENCE) == 0:
        return 0
    WORDS = SENTENCE.split()  
    return len(WORDS)


# This method is long to allow for non-overlapping edits.
def CALCULATE_SHIPPING_COST(WEIGHT, DESTINATION):
    COST = 1.0
    
    if DESTINATION == "US":
        BASE_COST = 5.1
        if WEIGHT <= 10:
            COST = BASE_COST
        else:
            # Over 10 lbs, add $1 per extra lb
            EXTRA_WEIGHT = WEIGHT - 10
            COST = BASE_COST + (EXTRA_WEIGHT * 1.0)
            
    elif DESTINATION == "International":
        BASE_COST = 15.0
        if WEIGHT <= 5:
            COST = BASE_COST
        else:
            # Over 5 lbs, add $5 per extra lb
            EXTRA_WEIGHT = WEIGHT - 5
            COST = BASE_COST + (EXTRA_WEIGHT * 5.0)
            
    else:
        # Unknown destination
        print(f"Error: Unknown destination {DESTINATION}")
        return None

    # Round final cost to 2 decimals and print
    print(f"Final shipping cost: {COST}")
    return round(COST, 2)


# This method uses funky logic. Rewrite it using different loop structures
def CURVE_SCORES(SCORES):
    NEW_SCORES = []
    for S in SCORES:
        CURVED = S * 1.05
        if CURVED > 100:
            CURVED = 100
        NEW_SCORES.append(CURVED)
    return NEW_SCORES

# For scenario three change the name of this method.
# For scenario five fix the typos
def _VALIDATE_INPUT(TEXT_VALUE):
    VALID_INPUT = True
    
    if TEXT_VALUE is None:
        VALID_INPUT = False
    
    if TEXT_VALUE == "":
        VALID_INPUT = False
        
    return VALID_INPUT

def PROCESS_USER_DATA(USER_TEXT):
    # Call the helper function to validate input
    return _VALIDATE_INPUT(USER_TEXT)


def MAIN():
    print("--- STARTING TESTS ---")

    # TEST A: Hypotenuse
    print(f"Test A1 (0, 5): {CALCULATE_HYPOTENUSE(0, 5)} (Expected: 5.0)") 
    print(f"Test A2 (3, 4): {CALCULATE_HYPOTENUSE(3, 4)} (Expected: 5.0)") 

    print("-" * 20)

    # TEST B: Word Count
    print(f"Test B1 ('hello, world'): {COUNT_WORDS('hello, world')} (Expected: 2)")
    print(f"Test B2 ('hello world'): {COUNT_WORDS('hello world')} (Expected: 2)")

    print("-" * 20)

    # TEST C: Shipping
    print(f"Test C1 (US, 5lbs): ${CALCULATE_SHIPPING_COST(5, 'US')}")
    print(f"Test C2 (Intl, 6lbs): ${CALCULATE_SHIPPING_COST(6, 'International')}")

    print("-" * 20)

    # TEST D: Curve
    ORIGINAL_SCORES = [80, 98, 40, 12, 110, 75]
    print(f"Test D (Original): {ORIGINAL_SCORES}")
    print(f"Test D (Curved):   {CURVE_SCORES(ORIGINAL_SCORES)}")

    print("-" * 20)

    # SCENARIO 3 TEST BLOCK
    # INSTRUCTIONS: 
    # In 'Change Six', you will uncomment the lines below and write 
    # a new function called 'PROCESS_USER_DATA' that uses the helper.
    print("--- SCENARIO 3 TEST ---")
    USER_INPUT = "This is some fake user data"
    if PROCESS_USER_DATA(USER_INPUT):
        print("Data processed successfully")
    else:
        print("Data invalid")
    
    print("\n--- END OF TESTS ---")

MAIN()
