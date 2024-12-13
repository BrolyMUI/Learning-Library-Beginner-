
questions = [
    {
    "prompt": "What is the capital of India?",
    "options": ["A.Wellington", "B. London", "C. Bangeluru", "D. Delhi"],
    "answer": "D"
    },
    {
    "prompt": "Which language is primarily spoken in Pakistan?",
    "options":["A. Urdu", "B. Arabic", "C. Hindi", "D. English"],
    "answer": "A"

     },
    {
    "prompt": "What is 20+30?",
    "options":["A. 70", "B. 12", "C. 50", "D. 40"],
    "answer": "C"
    },
    {
    "prompt": "What is the tallest mountain in the world?",
    "options":["A. Mountain Kilimanjaro", "B. Mountain Everest", "C. Mountain Cook", "D. Mountain Kamet "],
    "answer": "B"
    }
 ]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ")
        if answer == question["answer"]:
            print("Correct, well done!!!")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"])

    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)
