from flask import Flask, request, jsonify 
import pandas as pd


app = Flask(__name__)

# Load the saved SVC model
import joblib

# Load the SVC model from the PKL file
svc_model = joblib.load('svc_model.pkl')


@app.route('/')
def home():
    return render_template('index.html')

# Define a route for handling POST requests to "/predict"
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request body
    data = request.get_json()
    
    # Define the function to predict disease based on symptoms
    description = pd.read_csv('C:\\Users\\amitn\\Downloads\\Dataset for project\\Medicine Recomendation\\description.csv')
    symtoms = pd.read_csv('C:\\Users\\amitn\\Downloads\\Dataset for project\\Medicine Recomendation\\symtoms_df.csv')
    medications = pd.read_csv('C:\\Users\\amitn\\Downloads\\Dataset for project\\Medicine Recomendation\\medications.csv')
    diets = pd.read_csv('C:\\Users\\amitn\\Downloads\\Dataset for project\\Medicine Recomendation\\diets.csv')
    precautions = pd.read_csv('C:\\Users\\amitn\\Downloads\\Dataset for project\\Medicine Recomendation\\precautions_df.csv')
    workout = pd.read_csv('C:\\Users\\amitn\\Downloads\\Dataset for project\\Medicine Recomendation\\workout_df.csv')
 


    # Extract symptoms from the JSON data
    symptoms = data.get('symptoms')

    # Perform prediction based on the symptoms (you may call your predict function here)
    predicted_disease, disease_code = predict_disease(symptoms)

    # Prepare the response JSON
    response = {
        'predicted_disease': predicted_disease,
        'disease_code': disease_code
    }

    # Return the response as JSON
    return jsonify(response)



# Define the function to predict disease based on symptoms
def predict_disease(symptoms):
    # Define the symptoms dictionary
    symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}

    # Define the diseases dictionary
    diseases_list = {
        15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction',
        33: 'Peptic ulcer disease', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma',
        23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)',
        28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A',
        19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis',
        36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack'
    }

    # Initialize feature vector with zeros
    num_features = 132  # Adjust this based on the actual number of features expected by svc_model
    feature_vector = [0] * num_features

    # Encode symptoms in the feature vector
    for symptom in symptoms:
        if symptom in symptoms_dict:
            feature_vector[symptoms_dict[symptom]] = 1  # Set the corresponding feature to 1 if the symptom is present
    

    # Predict the disease
    x = svc_model.predict([feature_vector])

    # Map the predicted value to the corresponding disease
    x_disease = diseases_list[x[0]]

    return x_disease, x[0]

# Function to collect symptoms from the user
def collect_symptoms():
    symptoms = []
    while True:
        symptom = input("Enter a symptom (or type 'done' to finish): ").strip().lower()
        if symptom == 'done':
            break
        symptoms.append(symptom)
    return symptoms

# Function to print information based on the predicted disease
def print_information(predicted_disease):

    # Extract information for the predicted disease
    predicted_description_info = description[description['Disease'] == predicted_disease]['Description'].values
    
   # Extract the symptoms information for the predicted disease and remove duplicates
    predicted_symptoms_info = symtoms[symtoms['Disease'] == predicted_disease][['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4']].values
    predicted_symptoms_info = pd.unique(predicted_symptoms_info.ravel())
    predicted_symptoms_info = pd.Series(predicted_symptoms_info).dropna().tolist()  # Drop NaN values and convert to list

    predicted_medications_info = medications[medications['Disease'] == predicted_disease]['Medication'].values
    
    predicted_precautions_info = precautions[precautions['Disease'] == predicted_disease][['Precaution_1', 'Precaution_2', 'Precaution_3','Precaution_4']].values
    predicted_precautions_info = pd.unique(predicted_precautions_info.ravel())
    predicted_precautions_info = pd.Series(predicted_precautions_info).dropna().tolist()  # Drop NaN values and convert to list
    
    # Extract the diet information for the predicted disease
    predicted_diet_info = diets[diets['Disease'] == predicted_disease]['Diet'].values
    
    # Extract the workout information for the predicted disease
    predicted_workout_info = workout[workout['disease'] == predicted_disease]['workout'].values
    
    return predicted_disease, disease_code

if __name__ == '__main__':
    app.run(debug=True)
