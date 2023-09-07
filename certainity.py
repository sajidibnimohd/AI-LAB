import numpy as np

# Define fuzzy sets for temperature and weather forecast
def fuzzy_temperature(temp):
    cold = max(0, min((50 - temp) / 20, 1))
    warm = max(0, min((temp - 30) / 20, 1))
    return cold, warm

def fuzzy_forecast(forecast):
    sunny = max(0, min((forecast - 70) / 20, 1))
    rainy = max(0, min((forecast - 30) / 20, 1))
    return sunny, rainy

# Define fuzzy rules
def apply_rules(temperature, forecast):
    rules = []

    # Rule 1: If it's cold and sunny, then go for a picnic (certainty factor 0.8)
    cold, warm = fuzzy_temperature(temperature)
    sunny, rainy = fuzzy_forecast(forecast)
    rules.append(("Go for a picnic", min(cold, sunny), 0.8))

    # Rule 2: If it's warm and rainy, then don't go for a picnic (certainty factor 0.6)
    rules.append(("Don't go for a picnic", min(warm, rainy), 0.6))

    return rules

# Combine evidence using certainty factors
def combine_evidence(rules):
    numerator = 0
    denominator = 0

    for rule in rules:
        conclusion, support, certainty_factor = rule
        numerator += support * certainty_factor
        denominator += support

    if denominator == 0:
        return None

    final_certainty_factor = numerator / denominator
    return final_certainty_factor

# Main function to make a decision
def make_decision(temperature, forecast):
    rules = apply_rules(temperature, forecast)
    certainty_factor = combine_evidence(rules)

    if certainty_factor is None:
        return "Cannot make a decision"
    elif certainty_factor >= 0.5:
        return "Go for a picnic"
    else:
        return "Don't go for a picnic"

# Test the decision-making process
temperature = 65  # Example temperature
forecast = 60    # Example weather forecast

decision = make_decision(temperature, forecast)
print(f"Decision: {decision}")
