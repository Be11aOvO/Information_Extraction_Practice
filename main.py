import re

def ask_question(question):
    answer = input(question + "\n")
    return answer

def extract_info(answer):
    weight = None
    height = None
    gender = None
    diseases = []
    restrictions = []

    # Extract weight and height using regular expressions
    weight_match = re.search(r"\b\d+\s*(kg|kilograms|lbs|pounds)\b", answer, re.IGNORECASE)
    if weight_match:
        weight_str = re.findall(r"\d+", weight_match.group())[0]
        weight = int(weight_str)
        if "lbs" in weight_match.group().lower() or "pounds" in weight_match.group().lower():
            weight = round(weight * 0.453592, 2)

    height_match = re.search(r"\b\d+\s*(cm|inches|feet)\b", answer, re.IGNORECASE)
    if height_match:
        height_str = re.findall(r"\d+", height_match.group())[0]
        height = int(height_str)
        if "inches" in height_match.group().lower():
            height = round(height * 2.54, 2)
        elif "feet" in height_match.group().lower():
            height = round(height * 30.48, 2)

    # Extract gender using regular expressions
    gender_match = re.search(r"\b(male|female|man|woman)\b", answer, re.IGNORECASE)
    if gender_match:
        gender = gender_match.group().lower()

    # Extract history of diseases
    disease_matches = re.findall(r"\b(cancer|diabetes|heart disease|high blood pressure)\b", answer, re.IGNORECASE)
    if disease_matches:
        diseases = [disease.lower() for disease in disease_matches]

    # Extract dietary restrictions
    restriction_matches = re.findall(r"\b(vegan|vegetarian|gluten-free|dairy-free|nut-free)\b", answer, re.IGNORECASE)
    if restriction_matches:
        restrictions = [restriction.lower() for restriction in restriction_matches]

    return weight, height, gender, diseases, restrictions


# Main program loop
while True:
    print("Welcome to the food recommendation chatbot!")
    answer = ask_question("What is your weight and height? (e.g. 70 kg, 170 cm)")
    weight, height, gender, diseases, restrictions = extract_info(answer)
    print("Weight:", weight)
    print("Height:", height)
    print("Gender:", gender)
    print("Diseases:", diseases)
    print("Restrictions:", restrictions)

    # Ask for food recommendations based on extracted information
    # TODO: Add your own recommendation logic here

    # Ask if the user wants to continue
    answer = ask_question("Do you want to continue? (y/n)")
    if answer.lower() != "y":
        break
