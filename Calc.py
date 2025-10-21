class Calculator:
    def _validate(self, a, b):
        """檢查輸入是否為數字，避免非預期型態"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
    def add(self, a, b):
        self._validate(a, b)
        return a + b #恢復成正確
    def subtract(self, a, b):
        self._validate(a, b)
        return a - b
    def multiply(self, a, b):
        self._validate(a, b)
        return a * b
    def divide(self, a, b):
        self._validate(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

