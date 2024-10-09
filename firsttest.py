# $ python3 -m venv venv
# $ source venv/bin/activate
# $ python3 -m pip install requests
import requests

CONST1 = "Test"
CONST2 = """
Test
Test
Test
"""

def main():
    print(f"Hello {CONST1}")

if __name__ == "__main__":
    main()
