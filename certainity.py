class CertaintyFactorRule:
    def __init__(self, condition, conclusion, cf):
        self.condition = condition  # A list of conditions (e.g., ['outdoor', 'team_sport'])
        self.conclusion = conclusion  # The conclusion (e.g., 'Football' or 'Basketball')
        self.cf = cf  # Certainty factor for the conclusion

# Function to calculate the winner based on certainty factors
def calculate_winner(rules, conditions):
    cf_values = {}  # Dictionary to store certainty factors for sports
    for rule in rules:
        condition_met = all(cond in conditions for cond in rule.condition)
        if condition_met:
            cf_values[rule.conclusion] = rule.cf
    
    # Determine the winner based on the highest certainty factor
    if cf_values:
        winner = max(cf_values, key=cf_values.get)
        certainty_factor = cf_values[winner]
        return winner, certainty_factor
    else:
        return None, 0

# Collect inputs for each sport
sports_rules = []
for _ in range(4):
    sport_name = input("Enter sport name: ").strip()
    indoor_outdoor = input("Indoor or outdoor? ").strip().lower()
    team_individual = input("Team sport or individual sport? ").strip().lower()
    
    cf = float(input("Enter certainty factor (between 0 and 1): "))
    
    # Validate certainty factor
    while cf < 0 or cf > 1:
        print("Certainty factor must be between 0 and 1.")
        cf = float(input("Enter certainty factor (between 0 and 1): "))
    
    sports_rules.append(CertaintyFactorRule([indoor_outdoor, team_individual], sport_name, cf))

# Ask for the desired sport and playing conditions
desired_indoor_outdoor = input("Indoor or outdoor? ").strip().lower()
desired_team_individual = input("Team sport or individual sport? ").strip().lower()

# Calculate the winner based on the given input
winner, certainty_factor = calculate_winner(sports_rules, [desired_indoor_outdoor, desired_team_individual])

# Print the winner and the certainty factor for the winner
if winner:
    print(f"The best sport for you is: {winner} with a certainty factor of {certainty_factor}")
else:
    print("No suitable sport found based on the given conditions.")
