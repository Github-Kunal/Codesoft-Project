def add(num1, num2):
  """Adds two numbers and returns the result."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers and returns the result."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers and returns the result."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers and handles division by zero error."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

while True:
  # Get user input for numbers and operator
  num1 = float(input("Enter the first number: "))
  operator = input("Enter an operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  # Perform calculation based on operator
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    result = "Invalid operator."

  # Print the result
  print(f"Result: {result}")

  # Ask if user wants to continue
  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != 'y':
    break

print("Exiting calculator...")
