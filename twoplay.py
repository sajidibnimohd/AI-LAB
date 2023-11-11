import random
def generate_question():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, round(answer, 2)  # Round the answer to two decimal places
def main():
    print("Welcome to the Math Quiz Game!")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    player1_score = 0
    player2_score = 0
    num_questions = 5
    for i in range(num_questions):
        print(f"\nQuestion {i + 1}:")
        question, answer = generate_question()
        print(f"{question} = ?")
        # Player 1's turn
        player1_response = float(input(f"{player1_name}, your answer: "))
        # Player 2's turn
        player2_response = float(input(f"{player2_name}, your answer: "))
        print(f"The correct answer is {answer}.")
        if round(player1_response, 2) == answer:
            print(f"{player1_name} answered correctly!")
            player1_score += 1
        else:
            print(f"{player1_name} answered incorrectly.")
        if round(player2_response, 2) == answer:
            print(f"{player2_name} answered correctly!")
            player2_score += 1
        else:
            print(f"{player2_name} answered incorrectly.")
    print("\nGame Over!")
    print(f"Final Scores:")
    print(f"{player1_name}: {player1_score} points")
    print(f"{player2_name}: {player2_score} points")
    if player1_score > player2_score:
        print(f"{player1_name} wins!")
    elif player2_score > player1_score:
        print(f"{player2_name} wins!")
    else:
        print("It's a tie!")
if __name__ == "__main__":
    main()
