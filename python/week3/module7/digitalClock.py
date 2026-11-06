import time

def digital_clock():
    print("Press Ctrl+C to stop the clock.\n")
    try:
        while True:
            # Fetch and format current local time
            current_time = time.strftime("%H:%M:%S %p")
            
            # \r moves cursor to start of line, end="" prevents a new line
            print(f"Current Time: {current_time}", end="\r", flush=True)
            
            # Wait for 1 second before updating
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

if __name__ == "__main__":
    digital_clock()