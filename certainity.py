class Rule:
    def __init__(self, antecedent, consequent, cf):
        self.antecedent = antecedent  # Antecedent condition (e.g., a list of facts)
        self.consequent = consequent  # Consequent action (e.g., a fact to assert)
        self.cf = cf  # Certainty factor

class ExpertSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, facts):
        result = {}
        for rule in self.rules:
            if all(fact in facts for fact in rule.antecedent):
                # All antecedent conditions are satisfied
                result[rule.consequent] = rule.cf

        return result

if __name__ == "__main__":
    # Create an expert system
    expert_system = ExpertSystem()

    # Define rules with certainty factors
    rule1 = Rule(["Sunny"], "PlayTennis", 0.8)
    rule2 = Rule(["Rainy"], "PlayTennis", -0.6)

    # Add rules to the expert system
    expert_system.add_rule(rule1)
    expert_system.add_rule(rule2)

    # Prompt the user to input facts
    user_input = input("Enter facts (comma-separated, e.g., Sunny,Rainy): ")
    user_facts = user_input.split(",")

    # Evaluate the expert system based on user input
    result = expert_system.evaluate(user_facts)

    # Determine the decision based on certainty factors
    if "PlayTennis" in result:
        cf_play_tennis = result["PlayTennis"]
        if cf_play_tennis > 0:
            print("Let's play tennis!")
        else:
            print("It's better not to play tennis.")
    else:
        print("No matching rules found.")
