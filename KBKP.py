# lets make a copy of kaun banega karodpathi show simulation
# Step 1: Define the lists
questions = [
    "What is the capital of France?",
    "Which language is used for web development?",
    "What is 2 + 2?"
]

options = [
    ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
    ["A. Python", "B. Java", "C. HTML", "D. C++"],
    ["A. 3", "B. 4", "C. 5", "D. 6"]
]

correct_answers = ["C", "C", "B"]  # Correct answer keys
user_answers = []  # List to store user responses

# Step 2: Loop through the questions
for i in range(len(questions)):
    print(f"\nQ{i+1}: {questions[i]}")
    
    # Step 3: Display options
    for option in options[i]:
        print(option)
    
    # Step 4: Get user input
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    user_answers.append(answer)  # Store the user's answer

# Step 5: Compare user answers and calculate score
score = 0  # Variable to track the score

for i in range(len(questions)):
    if user_answers[i] == correct_answers[i]:
        score += 1  # Increase score if answer is correct

# Step 6: Display the final result
print("\nQuiz Completed!")
print(f"Your final score: {score}/{len(questions)}")

# Show correct and incorrect answers
for i in range(len(questions)):
    print(f"\nQ{i+1}: {questions[i]}")
    print(f"Your answer: {user_answers[i]}")
    print(f"Correct answer: {correct_answers[i]}")

















# Qlist = ["who is the PM of india?","Who invented python?","who owns chatGPT?"]
# AList = [["me","you","harry bahi","modiji"],["van rossum","charlesh","idk","call a friend"]]
# for i in Qlist:
#     print(i)
    
#     for i in AList:
#         print(i)
#         q1 = list(input("choose correct answer:"))

# print("your answers:",q1)
# print("correct answers:",a1)