import os
import subprocess
import sys

def main():
    print("Starting Hermes Agent Gateway...")
    try:
        subprocess.run([sys.executable, "-m", "hermes.gateway", "start"], check=False)
    except KeyboardInterrupt:
        print("\nStopping Hermes Agent...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
