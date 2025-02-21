<code>
def ask_question(question, options, correct_answer):
    """
    Asks a multiple-choice question and returns True if the answer is correct, False otherwise.
    """
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True:
        try:
            answer = int(input("Enter your choice (1-" + str(len(options)) + "): "))
            if 1 <= answer <= len(options):
                break
            else:
                print("Invalid input. Please enter a number between 1 and " + str(len(options)))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if options[answer-1] == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is: " + correct_answer)
        return False

def run_quiz():
    """
    Runs a simple programming quiz.
    """
    print("Welcome to the Programming Quiz!")
    score = 0

    questions = [
        {
            "question": "What is the purpose of a function in programming?",
            "options": ["To perform a specific task", "To declare variables", "To define data types", "To create loops"],
            "correct_answer": "To perform a specific task"
        },
        {
            "question": "What does the acronym DRY stand for?",
            "options": ["Don't Repeat Yourself", "Do Repeat Yourself", "Data Recovery Yield", "Disk Read Yield"],
            "correct_answer": "Don't Repeat Yourself"
        },
        {
            "question": "What is the difference between '==' and '=' in Python?",
            "options": ["'==' is assignment, '=' is comparison", "'==' is comparison, '=' is assignment", "They are the same", "None of the above"],
            "correct_answer": "'==' is comparison, '=' is assignment"
        }
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            score += 1

    print("\nQuiz complete!")
    print("Your score: " + str(score) + "/" + str(len(questions)))

if __name__ == "__main__":
    run_quiz()
</code>
