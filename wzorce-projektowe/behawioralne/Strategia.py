# Strategy interface
class Strategy:
    def execute(self, a, b):
        pass

# Concrete Strategy classes implementing the Strategy interface
class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b

class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b

class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b

# Context class that uses the Strategy
class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def setStrategy(self, strategy: Strategy):
        self.strategy = strategy

    def executeStrategy(self, a, b):
        return self.strategy.execute(a, b)

# Example client code
class ExampleApplication:
    def main(self):
        # Creating the context object
        context = Context(ConcreteStrategyAdd())  # Initial strategy: addition

        # Simulating user input
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        action = input("Enter the operation (add, subtract, multiply): ").lower()

        # Selecting the strategy based on user input
        if action == "add":
            context.setStrategy(ConcreteStrategyAdd())
        elif action == "subtract":
            context.setStrategy(ConcreteStrategySubtract())
        elif action == "multiply":
            context.setStrategy(ConcreteStrategyMultiply())
        else:
            print("Invalid operation")
            return

        # Execute the strategy
        result = context.executeStrategy(first_number, second_number)
        print(f"Result: {result}")

# Running the application
app = ExampleApplication()
app.main()
