#!/usr/bin/env python3
"""
Differential Setup Calculator
-----------------------------
A tool to assist in calculating pinion depth, checking distance, mounting distance, 
and carrier preload/shims. It supports two modes of operation:
1. Current / Pre-existing setup calculations (from physical measurements).
2. Desired / Manufacturing specifications setup calculations (from specs & new parts).

This script fixes the formula errors (column/row index shifts) found in the original 
Excel spreadsheet and provides clear, physically accurate shimming directions.
"""

import sys

# ANSI Colors for beautiful console output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(title):
    print("\n" + "=" * 60)
    print(f"{BOLD}{CYAN}{title.center(60)}{RESET}")
    print("=" * 60)

def print_step(step_num, text):
    print(f"\n{BOLD}{BLUE}Step {step_num}:{RESET} {text}")

def get_float_input(prompt, default=None):
    while True:
        try:
            val_str = input(prompt).strip()
            if not val_str and default is not None:
                return default
            val = float(val_str)
            if val < 0:
                print(f"{RED}Error: Value cannot be negative. Please enter a valid number.{RESET}")
                continue
            return val
        except ValueError:
            print(f"{RED}Error: Invalid numeric input. Please enter a number.{RESET}")

def calculate_pre_existing():
    print_header("Mode 1: Pre-existing / Current Setup Calculator")
    print("Enter measurements taken from your differential housing and carrier bearings.")
    
    # Inputs
    f_race = get_float_input("1. Face to Race (diff face to top of carrier bearing race) [inches]: ")
    od_race = get_float_input("2. Race Outer Diameter (outer diameter of the carrier bearing race) [inches]: ")
    f_pinion = get_float_input("3. Face to Pinion (diff face to front face of pinion head) [inches]: ")
    m_target = get_float_input("4. Pinion Etched Marking / Target Mounting Distance [inches]: ")
    
    calc_carrier = input("Do you want to calculate carrier shims? (y/n) [n]: ").strip().lower() == 'y'
    w_housing, w_carrier, p_desired = 0.0, 0.0, 0.008
    if calc_carrier:
        w_housing = get_float_input("5. Housing Internal Width (distance between bearing bulkheads) [inches]: ")
        w_carrier = get_float_input("6. Carrier + Races Width (total width without shims) [inches]: ")
        p_desired = get_float_input("7. Desired Preload [inches] (default 0.008): ", default=0.008)

    # Calculations
    print_header("Calculation Results")
    
    # 1. Axle Centerline
    axle_centerline = f_race + (od_race / 2.0)
    print_step(1, "Calculate Axle Centerline (Target)")
    print(f"   Formula: Face to Race + (Race Outer Diameter / 2)")
    print(f"   Math   : {f_race:.4f} + ({od_race:.4f} / 2)")
    print(f"   Result : {BOLD}{GREEN}{axle_centerline:.4f} inches{RESET} from differential cover face")

    # 2. Current Checking Distance
    checking_dist = f_pinion - axle_centerline
    print_step(2, "Calculate Current Checking Distance (Pinion Face to Centerline)")
    print(f"   Formula: Face to Pinion - Axle Centerline")
    print(f"   Math   : {f_pinion:.4f} - {axle_centerline:.4f}")
    print(f"   Result : {BOLD}{GREEN}{checking_dist:.4f} inches{RESET}")

    # Positive diff = pinion too far out → ADD shim to push deeper
    # Negative diff = pinion too deep → REMOVE shim to pull back
    shim_diff = checking_dist - m_target
    print_step(3, "Calculate Shim Adjustment")
    print(f"   Formula: Current Checking Distance - Target (Etched Marking)")
    print(f"   Math   : {checking_dist:.4f} - {m_target:.4f}")

    if shim_diff > 0:
        adjustment_text = f"{BOLD}{YELLOW}ADD {abs(shim_diff):.4f} inches{RESET} of shim thickness to move the pinion deeper."
    elif shim_diff < 0:
        adjustment_text = f"{BOLD}{YELLOW}REMOVE {abs(shim_diff):.4f} inches{RESET} of shim thickness to pull the pinion further out."
    else:
        adjustment_text = f"{BOLD}{GREEN}No adjustment needed.{RESET} Pinion depth is exactly on target."

    print(f"   Difference: {shim_diff:+.4f} inches")
    print(f"   Action Required: {adjustment_text}")

    # 4. Carrier Shim Stack
    if calc_carrier:
        total_shims = (w_housing - w_carrier) + p_desired
        print_step(4, "Calculate Total Carrier Shim Stack Required")
        print(f"   Formula: (Housing Internal Width - Carrier Width) + Desired Preload")
        print(f"   Math   : ({w_housing:.4f} - {w_carrier:.4f}) + {p_desired:.4f}")
        print(f"   Result : {BOLD}{GREEN}{total_shims:.4f} inches{RESET} total shims (split between left and right sides to set backlash)")
    
    print("\n" + "=" * 60)

def calculate_manufacturing():
    print_header("Mode 2: Manufacturing Numbers / Desired Setup Calculator")
    print("Enter specs for new gears and parts to calculate required setup shims.")
    
    # Inputs
    f_race = get_float_input("1. Face to Race (diff face to top of carrier bearing race) [inches]: ")
    od_race = get_float_input("2. Race Outer Diameter (outer diameter of the carrier bearing race) [inches]: ")
    cd_target = get_float_input("3. Manufacturer Checking Distance (spec pinion face to centerline) [inches]: ")
    t_head = get_float_input("4. Pinion Head Thickness (front face of pinion to bearing shoulder) [inches]: ")
    m_target = get_float_input("5. Pinion Etched Marking / Target Mounting Distance [inches]: ")
    
    calc_carrier = input("Do you want to calculate carrier shims? (y/n) [n]: ").strip().lower() == 'y'
    w_housing, w_carrier, p_desired = 0.0, 0.0, 0.008
    if calc_carrier:
        w_housing = get_float_input("6. Housing Internal Width (distance between bearing bulkheads) [inches]: ")
        w_carrier = get_float_input("7. Carrier + Races Width (total width without shims) [inches]: ")
        p_desired = get_float_input("8. Desired Preload [inches] (default 0.008): ", default=0.008)

    # Calculations
    print_header("Calculation Results")
    
    # 1. Axle Centerline
    axle_centerline = f_race + (od_race / 2.0)
    print_step(1, "Calculate Axle Centerline (Target)")
    print(f"   Formula: Face to Race + (Race Outer Diameter / 2)")
    print(f"   Math   : {f_race:.4f} + ({od_race:.4f} / 2)")
    print(f"   Result : {BOLD}{GREEN}{axle_centerline:.4f} inches{RESET} from differential cover face")

    # 2. Target Pinion Face to Differential Face
    f_pinion_target = cd_target + axle_centerline
    print_step(2, "Calculate Target Pinion Face to Differential Face")
    print(f"   Formula: Manufacturer Checking Distance + Axle Centerline")
    print(f"   Math   : {cd_target:.4f} + {axle_centerline:.4f}")
    print(f"   Result : {BOLD}{GREEN}{f_pinion_target:.4f} inches{RESET}")

    # 3. Current Mounting Distance
    current_mounting_dist = cd_target + t_head
    print_step(3, "Calculate Current Mounting Distance (Back of head to axle centerline)")
    print(f"   Formula: Manufacturer Checking Distance + Pinion Head Thickness")
    print(f"   Math   : {cd_target:.4f} + {t_head:.4f}")
    print(f"   Result : {BOLD}{GREEN}{current_mounting_dist:.4f} inches{RESET}")

    # 4. Shim Adjustment
    shim_diff = current_mounting_dist - m_target
    print_step(4, "Calculate Shim Adjustment to Reach Mounting Distance")
    print(f"   Formula: Current Mounting Distance - Target (Etched Marking)")
    print(f"   Math   : {current_mounting_dist:.4f} - {m_target:.4f}")
    
    if shim_diff > 0:
        adjustment_text = f"{BOLD}{YELLOW}ADD {abs(shim_diff):.4f} inches{RESET} of shim thickness to move the pinion deeper."
    elif shim_diff < 0:
        adjustment_text = f"{BOLD}{YELLOW}REMOVE {abs(shim_diff):.4f} inches{RESET} of shim thickness to pull the pinion further out."
    else:
        adjustment_text = f"{BOLD}{GREEN}No adjustment needed.{RESET} Pinion depth is exactly on target."

    print(f"   Difference: {shim_diff:+.4f} inches")
    print(f"   Action Required: {adjustment_text}")

    # 5. Carrier Shim Stack
    if calc_carrier:
        total_shims = (w_housing - w_carrier) + p_desired
        print_step(5, "Calculate Total Carrier Shim Stack Required")
        print(f"   Formula: (Housing Internal Width - Carrier Width) + Desired Preload")
        print(f"   Math   : ({w_housing:.4f} - {w_carrier:.4f}) + {p_desired:.4f}")
        print(f"   Result : {BOLD}{GREEN}{total_shims:.4f} inches{RESET} total shims (split between left and right sides to set backlash)")

    print("\n" + "=" * 60)

def main():
    while True:
        print_header("Differential Setup Calculator")
        print("Please choose a calculation mode:")
        print("1. Pre-existing / Current Setup Measurements (Mode 1)")
        print("2. Manufacturing Numbers / Desired Specs Setup (Mode 2)")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        if choice == '1':
            calculate_pre_existing()
        elif choice == '2':
            calculate_manufacturing()
        elif choice == '3':
            print("Exiting calculator. Good luck with your differential setup!")
            break
        else:
            print(f"{RED}Invalid choice. Please select 1, 2, or 3.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCalculator terminated by user. Goodbye!")
        sys.exit(0)
