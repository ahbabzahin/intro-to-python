class Expression:
    def __init__(self, expression: str):
        self.expression = expression

    def evaluate(self):
        try:

            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"

    def display(self):
        print(f"Expression: {self.expression}")
        print(f"Result: {self.evaluate()}")


if __name__ == "__main__":
    expr1 = Expression("10 + 20 * 3")
    expr1.display()

    expr2 = Expression("(50 - 20) / 5")
    expr2.display()
