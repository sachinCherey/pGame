import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    question = f"What is {num1} {operator} {num2}?"
    return question, answer

def play_quiz():
    print("Welcome to the Math Quiz!")
    score = 0
    num_questions = 10
    for i in range(num_questions):
        question, correct_answer = generate_question()
        print(question)
        user_answer = input("Your answer: ")
        if (user_answer) == str(correct_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")
    print(f"\nQuiz complete! Your score is {score}/{num_questions}.")
    if score == num_questions:
        print("Congratulations! You got a perfect score!")
    elif score >= num_questions // 2:
        print("Not bad! You did fairly well.")
    else:
        print("You need more practice. Keep learning!")

play_quiz()
