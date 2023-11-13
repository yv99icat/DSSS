import random

def generate_random_integer(min_val, max_val):
    """Generate a random integer between min_val and max_val."""
    return random.randint(min_val, max_val)

def generate_random_operator():
    """Generate a random arithmetic operator: +, -, or *."""
    return random.choice(['+', '-', '*'])

def perform_operation(n1, n2, operator):
    """Perform the arithmetic operation."""
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    else:
        result = n1 * n2
    return result

def math_quiz(total_questions):
    """Run the math quiz game."""
    score = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_operation(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz(total_questions=3)

