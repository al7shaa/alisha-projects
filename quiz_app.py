questions = {
    "What is the capital of Pakistan?": "Islamabad",
    "What does CPU stand for?": "Central Processing Unit",
    "Who created Python?": "Guido van Rossum"
}

score = 0

for q in questions:
    answer = input(q + "\n")
    if answer.lower() == questions[q].lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer was {questions[q]}\n")

print(f"Your final score is {score}/{len(questions)}")
