import os
import subprocess
import sys

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("Starting Hermes Agent Gateway...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "hermes.gateway", "start"],
            check=False
        )
        return result.returncode
    except KeyboardInterrupt:
        print("\nStopping Hermes Agent...")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
