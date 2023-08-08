import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def main():
    print("Welcome to the 1st Grade Math Game!")
    print("You will be given addition questions to solve.")
    
    score = 0
    num_questions = 5
    
    for _ in range(num_questions):
        num1, num2 = generate_question()
        correct_answer = num1 + num2
        
        print(f"What is {num1} + {num2}?")
        player_answer = int(input("Your answer: "))
        
        if player_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")
    
    print(f"Your final score: {score}/{num_questions}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
