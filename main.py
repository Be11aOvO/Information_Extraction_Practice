import spacy
import re

nlp = spacy.load("en_core_web_sm")

def ask_question(question):
    answer = input(question + "\n")
    return answer

def extract_weight(doc):
    weight = None

    # Extract weight using spaCy named entity recognition
    for ent in doc.ents:
        if ent.label_ == "WEIGHT":
            weight = int(ent.text)

    return weight

def extract_height(doc):
    height = None

    # Extract height using spaCy named entity recognition
    for ent in doc.ents:
        if ent.label_ == "HEIGHT":
            height = int(ent.text)

    return height

def extract_gender(doc):
    gender = None

    # Extract gender using spaCy named entity recognition
    for ent in doc.ents:
        if ent.label_ == "GENDER":
            gender = ent.text.lower()

    return gender

def extract_diseases(doc):
    diseases = []

    # Extract history of diseases using regular expressions
    disease_matches = re.findall(r"\b(cancer|diabetes|heart disease|high blood pressure)\b", doc.text, re.IGNORECASE)
    if disease_matches:
        diseases = [disease.lower() for disease in disease_matches]

    return diseases

def extract_restrictions(doc):
    restrictions = []

    # Extract dietary restrictions using regular expressions
    restriction_matches = re.findall(r"\b(vegan|vegetarian|gluten-free|dairy-free|nut-free)\b", doc.text, re.IGNORECASE)
    if restriction_matches:
        restrictions = [restriction.lower() for restriction in restriction_matches]

    return restrictions


# Main program loop
while True:
    print("Welcome to the food recommendation chatbot!")

    # Ask for user input and perform natural language understanding with spaCy
    answer = input()
    doc = nlp(answer)

    # Extract weight, height, and gender using spaCy named entity recognition
    weight = extract_weight(doc)
    print("Weight:", weight)
    height = extract_height(doc)
    print("Height:", height)
    gender = extract_gender(doc)
    print("Gender:", gender)

    # Extract history of diseases and dietary restrictions using regular expressions
    diseases = extract_diseases(doc)
    print("Diseases:", diseases)
    restrictions = extract_restrictions(doc)
    print("Restrictions:", restrictions)

    # Ask for food recommendations based on extracted information
    # ...

