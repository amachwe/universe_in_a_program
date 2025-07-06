import time
import sys

def increment_from_min():
    """
    Starts at the lowest integer value and increments by 1 every second.
    This demonstrates counting from the minimum possible integer value.
    """
    # Get the minimum integer value in Python
    min_int = -sys.maxsize - 1
    print(f"Starting from minimum integer value: {min_int}")
    print("Press Ctrl+C to stop the counter\n")
    
    current_value = min_int
    counter = 0
    
    try:
        while True:
            print(f"Second {counter:4d}: {current_value}")
            current_value += 1
            counter += 1
            time.sleep(1)
            
            # Optional: Add a safety check to prevent infinite loop
            # Uncomment the lines below to stop after a certain number of increments
            # if counter >= 20:
            #     print("Demo complete - stopping after 20 increments")
            #     break
                
    except KeyboardInterrupt:
        print(f"\n\nStopped at value: {current_value}")
        print(f"Total increments: {counter}")
        print(f"Started from: {min_int}")
        print(f"Difference: {current_value - min_int}")

def show_integer_limits():
    """
    Display information about integer limits in Python
    """
    print("Python Integer Limits:")
    print(f"sys.maxsize: {sys.maxsize}")
    print(f"Minimum integer: {-sys.maxsize - 1}")
    print(f"Maximum integer: Python has arbitrary precision integers!")
    print()

if __name__ == "__main__":
    print("🌌 Welcome to the Universe Counter! 🌌")
    print("=" * 50)
    
    show_integer_limits()
    
    print("This program will start counting from the lowest possible integer value.")
    print("Each second, the counter will increment by 1.")
    print()
    
    start = input("Press Enter to start counting, or 'q' to quit: ").strip().lower()
    
    if start != 'q':
        increment_from_min()
    else:
        print("Goodbye! 👋")
