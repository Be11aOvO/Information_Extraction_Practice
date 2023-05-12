import spacy
import re
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

user_profile = {}


# def ask_question(question):
#     answer = input(question + "\n")
#     return answer


# TODO: need improve
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


def extract_gender(text):
    gender_pattern = r"\b(male|boy|man|female|girl|woman)\b"
    match = re.search(gender_pattern, text, re.IGNORECASE)
    if match:
        gender = match.group(1).lower()
        if gender == "male":
            return "male"
        elif gender == "female":
            return "female"
        else:
            return None


def extract_weight(text):
    weight_pattern = r"\b(\d+(?:\.\d+)?)\s*(?:kgs?|kilograms?)?\b"
    match = re.search(weight_pattern, text, re.IGNORECASE)
    if match:
        weight = float(match.group(1))
        return weight
    else:
        return None


def extract_height(text):
    height_pattern = r"\b(\d+(?:\.\d+)?)\s*(cm|centimeters?|m|meters?|in|inches?|ft|feet?)\b"
    match = re.search(height_pattern, text, re.IGNORECASE)
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


# TODO: need improvement
def extract_diseases(text):
    disease_name = []

    if "disease" in text.lower():
        # extract the disease name from the user's response
        # and return it as a string
        return disease_name
    else:
        return None


# TODO: need improvement
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
        if extract_name(name):
            print(f"\nHello {extract_name(name)}, nice to meet you! \nI need some basic information to start "
                  f"customizing your plan.")
            break
        else:
            print("I'm sorry, I didn't catch your name. Can you please try again? ")

    # Ask for the user's gender
    while True:
        gender = input("\nWhat's your gender? Female or male? ")
        if extract_gender(gender):
            print(f"gender = {extract_gender(gender)}")
            break
        else:
            print("I'm sorry, I didn't catch your gender. Can you please try again? ")

    # Ask for the user's weight
    while True:
        weight = input("\nHow much do you weigh? (e.g. 70 kg, 150 lbs) ")
        if extract_weight(weight):
            print(extract_weight(weight))
            break
        else:
            print("I'm sorry, I didn't catch your weight. Can you please try again? ")

    # Ask for the user's height
    while True:
        height = input("\nHow tall are you? (e.g. 170 cm, 1.7 m) ")
        if extract_height(height):
            print(extract_height(height))
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
        response = input("\nDo you have any allergies? (yes or no) ")
        if "yes" in response.lower():
            restriction = input("\nWhat allergy you have? (e.g. seafood, nut) ")
            restrictions.append(restriction)
        elif "no" in response.lower():
            break
        else:
            print("I'm sorry, I didn't catch your response. Can you please try again? ")

    # Ask for the user's preference
    preferences = []
    while True:
        response = input("\nWhich type of following cuisine you prefer:\n "
                         "1. Chinese cuisine\n "
                         "2. Indian cuisine\n "
                         "3. Thai cuisine\n "
                         "4. Italian cuisine\n "
                         "5. American cuisine\n "
                         "6. Japanese cuisine\n")
        # TODO: catch the preference
    # TODO: Make food recommendations based on the user's profile



food_recommendation_chatbot()
