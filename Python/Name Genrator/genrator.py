import random

def generate_strings(number_of_strings):
    letters = "abcdefghijklmnopqrstuvwxyz"
    generated_strings = []
    for i in range(number_of_strings):
      #  first_letter = random.choice(letters)
      #  second_letter = random.choice(letters)
        third_letter = random.choice(letters)
        forth_letter = random.choice(letters)
        generated_strings.append("Z" + "O" + third_letter + forth_letter )
    return generated_strings

def display_skull():
    skull = """
           _____
         .'     '.
        /  o   o  \
       |    (_)    |
        \ '._ _.' /
         '._____.'   
    """
    print(skull)

if __name__ == "__main__":
    try:
        number_of_strings = int(input("Enter the number of strings to generate: "))
    except ValueError:
        print("Please provide a valid integer.")
        exit(1)

    generated_strings = generate_strings(number_of_strings)
    display_skull()
    for string in generated_strings:
        print(string)

    

