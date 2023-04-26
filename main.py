import spacy
import re

nlp = spacy.load('en_core_web_sm')

user_profile = {}

def ask_question(question):
    answer = input(question + "\n")
    return answer

def extract_name(doc):
    name = None

    # Extract name using spaCy NER
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text

    return name

def extract_weight(doc):
    weight = None

    # Extract weight using regular expressions
    weight_regex = r"(\d+(\.\d+)?)\s*(kg|lbs)"
    matches = re.findall(weight_regex, doc.text)
    if matches:
        weight, _ = matches[0]
        weight = float(weight)

    return weight

def extract_height(doc):
    height = None

    # Extract height using spaCy NER
    for ent in doc.ents:
        if ent.label_ == "HEIGHT":
            height = int(ent.text)

    return height

def extract_gender(doc):
    gender = None

    # Extract gender using spaCy NER
    for ent in doc.ents:
        if ent.label_ == "GENDER":
            gender = ent.text.lower()

    return gender

# TODO: Extract disease

# TODO: Extract restrictions

# TODO: Extract preference

# Main program loop
questions = [("What's your name?", extract_name),
             # ("What's your weight?", extract_weight),
             ("What's your height?", extract_height),
             ("What's your gender?", extract_gender)]

for question, extraction_func in questions:
    answer = ask_question(question)
    doc = nlp(answer)
    extracted_value = extraction_func(doc)

    while extracted_value is None:
        print("Sorry, I didn't understand your answer. Please try again.")
        answer = ask_question(question)
        doc = nlp(answer)
        extracted_value = extraction_func(doc)

    user_profile[extraction_func.__name__.replace("extract_", "")] = extracted_value

print("Thank you for providing your information!")
print(user_profile)
#
# while True:
#     print("Welcome to the food recommendation chatbot!")
#     print("I am your Foodvisor.")
#     print("What’s your name?")
#
#     # Ask for user input and perform natural language understanding with spaCy
#     answer = input()
#     doc = nlp(answer)
#
#     # Extract name, weight, height, and gender
#     name = extract_name(doc)
#     print("Name:", name)
#     weight = extract_weight(doc)
#     print("Weight:", weight)
#     height = extract_height(doc)
#     print("Height:", height)
#     gender = extract_gender(doc)
#     print("Gender:", gender)

    # Extract history of diseases and dietary restrictions using regular expressions??
    # diseases = extract_diseases(doc)
    # print("Diseases:", diseases)
    # restrictions = extract_restrictions(doc)
    # print("Restrictions:", restrictions)

    # TODO: food recommendations based on extracted information
    # ...
