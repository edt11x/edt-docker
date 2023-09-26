FROM arm32v7/python:3.9

WORKDIR /tmp

COPY .  prime_calculator.py
COPY .  __main__.py

# For some weird reason, we need to force the main module
# CMD ["python", "prime_calculator.py"]
# CMD ["python", "-c", "print('hi')"]
# CMD ["python", "-c", "import os; print(os.listdir('.'))"]
# CMD ["python", "--version"]
CMD ["python3", "/tmp/__main__.py"]

