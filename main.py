import spacy

nlp = spacy.load('en_core_web_sm')

# define the prompts for each user input
prompts = {
    'name': 'What\'s your name?',
    'weight': 'Can you tell me your weight?',
    'height': 'And how tall are you?',
    'gender': 'Are you male or female?',
    'diseases': 'Do you have any diseases or health conditions?',
    'restrictions': 'Do you have any food restrictions, like allergies or dietary preferences?',
    'preferences': 'What types of food do you like or dislike?'
}

# define the meal suggestions based on user preferences
meal_suggestions = {
    'spicy': 'Spicy tofu stir-fry with brown rice and steamed vegetables',
    'vegetarian': 'Lentil soup with a side salad and whole grain bread',
    'lactose intolerant': 'Veggie burger with sweet potato fries and a side of roasted Brussels sprouts'
}

# define the function to extract user information from input text
def extract_user_info(text):
    doc = nlp(text)
    name = ''
    weight = ''
    height = ''
    gender = ''
    diseases = ''
    restrictions = ''
    preferences = ''
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
        elif ent.label_ == 'QUANTITY' and 'weight' in ent.text.lower():
            weight = ent.text.split()[0]
        elif ent.label_ == 'QUANTITY' and 'height' in ent.text.lower():
            height = ent.text.split()[0]
        elif ent.label_ == 'GENDER':
            gender = ent.text
        elif ent.label_ == 'DISEASE':
            diseases = ent.text
        elif ent.label_ == 'FOOD_RESTRICTION':
            restrictions = ent.text
        elif ent.label_ == 'FOOD_PREFERENCE':
            preferences = ent.text
    return {
        'name': name,
        'weight': weight,
        'height': height,
        'gender': gender,
        'diseases': diseases,
        'restrictions': restrictions,
        'preferences': preferences
    }

# define the main function for the chatbot
def food_recommendation_chatbot():
    print('Hi there! I\'m your food recommendation chatbot.')
    user_info = {}
    for key in prompts.keys():
        while not user_info.get(key):
            input_text = input(prompts[key])
            user_info.update(extract_user_info(input_text))
    print('Based on your profile, I recommend a balanced diet with a focus on low glycemic index foods and plenty of '
          'fiber. Here are some meal suggestions based on your preferences:')
    meal_options = []
    for pref in user_info['preferences'].split():
        if pref in meal_suggestions.keys():
            meal_options.append(meal_suggestions[pref])
    if meal_options:
        for meal in meal_options:
            print('- ' + meal)
    else:
        print('Sorry, I don\'t have any meal suggestions that match your preferences.')
    print('Enjoy your meal!')

# run the chatbot
food_recommendation_chatbot()
