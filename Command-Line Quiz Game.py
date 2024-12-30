import random
import time

# List of questions and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "Which programming language is known for its snake logo?",
        "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
        "answer": "B"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Nikola Tesla", "C. Albert Einstein", "D. Galileo Galilei"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A. Tomato", "B. Onion", "C. Avocado", "D. Lime"],
        "answer": "C"
    },
]

def run_quiz():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Type the letter of your answer.\n")
    
    # Shuffle the questions for randomization
    random.shuffle(questions)
    
    score = 0
    total_questions = len(questions)
    start_time = time.time()
    
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
        time.sleep(1)  # Optional pause for better user experience
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print("\nQuiz Completed!")
    print(f"Your score: {score}/{total_questions}")
    print(f"Time taken: {total_time:.2f} seconds")

# Run the quiz game
if __name__ == "__main__":
    run_quiz()
