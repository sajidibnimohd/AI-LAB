class Symptom:
    def __init__(self, name):
        self.name = name
        self.present = False  # Corrected the indentation to be part of the class

class MedicalCondition:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms  # Corrected the indentation to be part of the class

# Define symptoms
symptom_fever = Symptom("Fever")
symptom_cough = Symptom("Cough")
symptom_headache = Symptom("Headache")

# Define medical conditions and their associated symptoms
condition_flu = MedicalCondition("Flu", [symptom_fever, symptom_cough])
condition_migraine = MedicalCondition("Migraine", [symptom_headache])
condition_common_cold = MedicalCondition("Common Cold", [symptom_cough])

# Expert system engine
def diagnose_condition(symptoms):
    if "Fever" in symptoms and "Cough" in symptoms:
        return condition_flu
    elif "Headache" in symptoms:
        return condition_migraine
    elif "Cough" in symptoms:
        return condition_common_cold
    else:
        return "Unknown condition"

# User interface
def main():
    print("Welcome to the Medical Diagnosis Expert System!")
    print("Available symptoms: Fever, Cough, Headache")
    symptoms = []
    while True:
        symptom_input = input("Enter a symptom (or 'done' to finish): ").capitalize()
        if symptom_input == "Done":
            break
        elif symptom_input in ["Fever", "Cough", "Headache"]:
            symptoms.append(symptom_input)
        else:
            print("Invalid symptom. Please enter a valid symptom.")

    diagnosed_condition = diagnose_condition(symptoms)
    if isinstance(diagnosed_condition, MedicalCondition):
        print(f"The expert system suggests you might have {diagnosed_condition.name}.")
    else:
        print("The expert system could not diagnose your condition.")

if __name__ == "__main__":
    main()

