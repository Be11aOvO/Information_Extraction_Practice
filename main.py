import spacy
import re
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

user_profile = {}


def ask_question(question):
    answer = input(question + "\n")
    return answer


def extract_name(doc):
    name = None

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text

    return name


def extract_gender(doc):
    gender_pattern = r"\b(male|female|non-binary|transgender|other)\b"
    match = re.search(gender_pattern, doc, re.IGNORECASE)
    if match:
        gender = match.group(1).lower()
        if gender == "male":
            return "male"
        elif gender == "female":
            return "female"
        else:
            return gender
    else:
        return None


def extract_weight(doc):
    weight_pattern = r"\b(\d+(?:\.\d+)?)\s*(?:kgs?|kilograms?)?\b"
    match = re.search(weight_pattern, doc, re.IGNORECASE)
    if match:
        weight = float(match.group(1))
        return weight
    else:
        return None


def extract_height(doc):
    height_pattern = r"\b(\d+(?:\.\d+)?)\s*(cm|centimeters?|m|meters?|in|inches?|ft|feet?)\b"
    match = re.search(height_pattern, doc, re.IGNORECASE)
    if match:
        height = float(match.group(1))
        unit = match.group(2).lower()
        if unit in ["cm", "centimeter", "centimeters"]:
            return height
        elif unit in ["m", "meter", "meters"]:
            return height * 100
        elif unit in ["in", "inch", "inches"]:
            return height * 2.54
        elif unit in ["ft", "foot", "feet"]:
            return height * 30.48
    else:
        return None


def extract_diseases(text):
    disease_name = []

    if "disease" in text.lower():
        # extract the disease name from the user's response
        # and return it as a string
        return disease_name
    else:
        return None


def extract_restrictions(text):
    restrictions = []
    if "vegan" in text.lower():
        restrictions.append("vegan")
    if "vegetarian" in text.lower():
        restrictions.append("vegetarian")
    # extract other dietary restrictions from the user's response
    # and append them to the restrictions list
    return restrictions


# TODO: Extract preference


def food_recommendation_chatbot():
    # Ask for the user's name
    while True:
        name = input("What's your name? ")
        if extract_name(nlp(name)):
            print(f"\nHello {name}, nice to meet you! I need some basic information to start customizing your plan.")
            break
        else:
            print("I'm sorry, I didn't catch your name. Can you please try again? ")

    # Ask for the user's gender
    while True:
        gender = input("\nWhat's your gender? Female or male? ")
        if extract_gender(gender):
            break
        else:
            print("I'm sorry, I didn't catch your gender. Can you please try again? ")

    # Ask for the user's weight
    while True:
        weight = input("\nHow much do you weigh? (e.g. 70 kg, 150 lbs) ")
        if extract_weight(weight):
            print(weight)
            break
        else:
            print("I'm sorry, I didn't catch your weight. Can you please try again? ")

    # Ask for the user's height
    while True:
        height = input("\nHow tall are you? (e.g. 170 cm, 1.7 m) ")
        if extract_height(height):
            print(height)
            break
        else:
            print("I'm sorry, I didn't catch your height. Can you please try again? ")

    # Ask for the user's diseases
    diseases = []
    while True:
        response = input("\nDo you have any diseases or health conditions? (yes or no) ")
        if "yes" in response.lower():
            disease = input("\nWhat disease or health condition do you have? ")
            diseases.append(disease)
            more_diseases = input("\nDo you have any more diseases or health conditions? (yes or no) ")
            if "no" in more_diseases.lower():
                break
        elif "no" in response.lower():
            break
        else:
            print("I'm sorry, I didn't catch your response. Can you please try again? ")

    # Ask for the user's dietary restrictions
    restrictions = []
    while True:
        response = input("\nDo you have any dietary restrictions? (yes or no)")
        if "yes" in response.lower():
            restriction = input("\nWhat dietary restriction do you have?")
            restrictions.append(restriction)
            more_restrictions = input("\nDo you have any more dietary restrictions? (yes or no)")
            if "no" in more_restrictions.lower():
                break
        elif "no" in response.lower():
            break
        else:
            print("I'm sorry, I didn't catch your response. Can you please try again? ")

    # Make food recommendations based on the user's profile
    if "vegan" in restrictions:
        print("Here are some vegan food recommendations for you.")
        # make vegan food recommendations based on the user's profile
    elif "vegetarian" in restrictions:
        print("Here are some vegetarian food recommendations for you.")
        # make vegetarian food recommendations based on the user's profile
    else:
        print("Here are some food recommendations for you.")
        # make food recommendations based on the user's profile


food_recommendation_chatbot()
