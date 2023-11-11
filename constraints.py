from itertools import permutations
def cryptarithmetic_solver():
    puzzle = input("Enter the cryptarithmetic puzzle (e.g., 'SEND + MORE = MONEY'): ").upper()
    words = puzzle.split()
    unique_letters = set(''.join(words))
    unique_letters -= {'+', '='}
    if len(unique_letters) > 10:
        print("Error: Too many unique letters.")
        return
    digits = list(range(10))
    solution_found = False
    for perm in permutations(digits, len(unique_letters)):
        digit_map = dict(zip(unique_letters, perm))
        if all(digit_map[word[0]] != 0 for word in words if word[0] in digit_map):
            num1 = int(''.join(str(digit_map[c]) for c in words[0]))
            num2 = int(''.join(str(digit_map[c]) for c in words[2]))
            result = int(''.join(str(digit_map[c]) for c in words[4]))
            if num1 + num2 == result:
                solution_found = True
                print("Solution found:")
                print(puzzle)
                print(f"{' ' * (len(words[4]) - len(words[0]))}{num1}")
                print(f"+{' ' * (len(words[4]) - len(words[2]))}{num2}")
                print("-" * (len(words[4]) + 2))
                print(f"={' ' * (len(words[4]) - len(str(result)))}{result}")
                print("-" * (len(words[4]) + 2))
                for letter, digit in digit_map.items():
                    if letter not in {'+', '='}:
                        print(f"{letter} = {digit}")
                break
    if not solution_found:
        print("No solution found.")
if __name__ == "__main__":
    cryptarithmetic_solver()
