import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length (int): Desired length of the password.
      include_uppercase (bool): Include uppercase letters (A-Z).
      include_lowercase (bool): Include lowercase letters (a-z).
      include_numbers (bool): Include numbers (0-9).
      include_symbols (bool): Include symbols (e.g., !@#$%^&*).

  Returns:
      str: The generated random password.
  """

  # Define character sets based on user preferences
  char_sets = []
  if include_uppercase:
    char_sets.append(string.ascii_uppercase)
  if include_lowercase:
    char_sets.append(string.ascii_lowercase)
  if include_numbers:
    char_sets.append(string.digits)
  if include_symbols:
    char_sets.append(string.punctuation)

  # Validate at least one character set is chosen
  if not char_sets:
    print("Error: Please choose at least one character type for the password.")
    return

  # Combine all chosen character sets
  all_chars = ''.join(char_sets)

  # Generate random password using choices and join
  password = ''.join(random.choices(all_chars, k=length))
  return password

# Get user input for password length and character types
while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      print("Password length must be at least 8 characters.")
      continue
    include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
    include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
    include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    include_symbols = input("Include symbols (y/n)? ").lower() == 'y'
    break
  except ValueError:
    print("Invalid input. Please enter a number for password length.")

# Generate and print the password
password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols)
print(f"Your generated password is: {password}")
