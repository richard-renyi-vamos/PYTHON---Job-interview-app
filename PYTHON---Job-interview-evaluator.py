def evaluate_answer(answer, keywords):
    score = 0
    for keyword in keywords:
        if keyword.lower() in answer.lower():
            score += 1
    return score

def main():
    questions = [
        {"text": "Tell me about yourself.", "keywords": ["experience", "education", "skills"]},
        {"text": "Why do you want to work here?", "keywords": ["company", "role", "growth"]},
        {"text": "Describe a challenge you've faced at work and how you dealt with it.", "keywords": ["challenge", "solution", "outcome"]},
    ]

    print("Welcome to the Job Interview Chat App! ☺")
    total_score = 0
    for question in questions:
        print("\nQuestion:", question["text"])
        answer = input("Your answer: ")
        score = evaluate_answer(answer, question["keywords"])
        total_score += score
        print(f"Score for this answer: {score}/{len(question['keywords'])}")

    print(f"\nTotal score: {total_score}/{sum(len(q['keywords']) for q in questions)}")
    print("Thank you for participating in this mock interview!")

if __name__ == "__main__":
    main()
