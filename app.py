from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dictionary containing detailed illness information
illness_data = {
    "Acid Reflux": {
        "causes": "Overeating, spicy food, obesity, or smoking.",
        "precautions": "Avoid acidic foods, eat smaller meals, and don't lie down after eating.",
        "advice": "If symptoms persist, consult a gastroenterologist."
    },
    "Allergies": {
        "causes": "Pollen, dust, food, insect bites, or pet dander.",
        "precautions": "Avoid allergens, take antihistamines, and use air purifiers.",
        "advice": "If severe, seek medical attention for allergy shots."
    },
    "Anemia": {
        "causes": "Iron deficiency, blood loss, or chronic disease.",
        "precautions": "Eat iron-rich foods like spinach, red meat, and beans.",
        "advice": "Take iron supplements if prescribed."
    },
    "Anxiety": {
        "causes": "Stress, trauma, genetics, or chemical imbalances.",
        "precautions": "Practice relaxation techniques, exercise, and get enough sleep.",
        "advice": "Seek therapy if anxiety affects daily life."
    },
    "Arthritis": {
        "causes": "Joint inflammation due to age, genetics, or autoimmune disorders.",
        "precautions": "Stay active, maintain a healthy weight, and avoid overuse of joints.",
        "advice": "Consult a rheumatologist for treatment options."
    },
    "Asthma": {
        "causes": "Allergies, pollution, respiratory infections.",
        "precautions": "Use inhalers, avoid allergens, and practice breathing exercises.",
        "advice": "Seek medical help for severe attacks."
    },
    "Back Pain": {
        "causes": "Poor posture, heavy lifting, or muscle strain.",
        "precautions": "Maintain good posture, exercise, and use ergonomic furniture.",
        "advice": "Seek physical therapy if pain persists."
    },
    "Body Pain": {
        "causes": "Fatigue, flu, stress, or infections.",
        "precautions": "Rest, stay hydrated, and take pain relievers if necessary.",
        "advice": "Consult a doctor if pain persists for more than a few days."
    },
    "Bronchitis": {
        "causes": "Viral or bacterial infection, smoking, pollution.",
        "precautions": "Avoid smoking, drink warm fluids, and rest.",
        "advice": "Use inhalers or medication if prescribed."
    },
    "Chickenpox": {
        "causes": "Varicella-zoster virus infection.",
        "precautions": "Avoid scratching, stay hydrated, and use calamine lotion.",
        "advice": "Get vaccinated to prevent future infections."
    },
    "Cold": {
        "causes": "Viral infection, weak immunity, cold exposure.",
        "precautions": "Wash hands frequently, stay warm, and drink fluids.",
        "advice": "Rest and take over-the-counter medications."
    },
    "Cough": {
        "causes": "Allergies, flu, respiratory infections.",
        "precautions": "Avoid smoke, drink warm fluids, and use cough syrup.",
        "advice": "Consult a doctor if it lasts more than 2 weeks."
    },
    "Dengue": {
        "causes": "Mosquito-borne viral infection.",
        "precautions": "Use mosquito repellents, wear full-sleeved clothing.",
        "advice": "Seek medical attention if high fever and rashes occur."
    },
    "Depression": {
        "causes": "Genetics, stress, chemical imbalance in the brain.",
        "precautions": "Stay active, talk to loved ones, and practice meditation.",
        "advice": "Seek professional help if symptoms persist."
    },
    "Diabetes": {
        "causes": "High blood sugar due to insulin resistance or deficiency.",
        "precautions": "Monitor diet, exercise, and take prescribed medication.",
        "advice": "Consult a doctor for regular check-ups."
    },
    "Diarrhea": {
        "causes": "Food poisoning, viral infections, or contaminated water.",
        "precautions": "Stay hydrated, eat light meals, and avoid dairy.",
        "advice": "See a doctor if dehydration occurs."
    },
    "Dizziness": {
        "causes": "Low blood pressure, dehydration, or inner ear issues.",
        "precautions": "Sit down immediately, drink fluids, and avoid sudden movements.",
        "advice": "Consult a doctor if dizziness persists."
    },
    "Ear Infection": {
        "causes": "Bacterial or viral infection in the ear.",
        "precautions": "Keep ears dry, avoid loud noises, and practice ear hygiene.",
        "advice": "Use prescribed ear drops if necessary."
    },
    "Epilepsy": {
        "causes": "Brain disorder causing seizures.",
        "precautions": "Take medications as prescribed, avoid triggers, and maintain a routine.",
        "advice": "Consult a neurologist for proper diagnosis."
    },
    "Fatigue": {
        "causes": "Lack of sleep, poor nutrition, stress.",
        "precautions": "Get enough rest, eat a balanced diet, and exercise regularly.",
        "advice": "See a doctor if chronic fatigue occurs."
    },
    "Flu": {
        "causes": "Influenza virus infection.",
        "precautions": "Wash hands frequently, get vaccinated, and stay hydrated.",
        "advice": "Rest and take antiviral medications if prescribed."
    },
    "Headache": {
        "causes": "Stress, dehydration, sinus issues, or migraines.",
        "precautions": "Stay hydrated, avoid bright lights, and manage stress.",
        "advice": "Seek medical attention if headaches are persistent."
    },
    "Insomnia": {
        "causes": "Stress, anxiety, irregular sleep schedule.",
        "precautions": "Follow a sleep routine, avoid caffeine before bed.",
        "advice": "Consult a doctor if sleep issues persist."
    },
    "Malaria": {
        "causes": "Mosquito-borne parasitic infection.",
        "precautions": "Use mosquito repellents, sleep under nets.",
        "advice": "Seek medical treatment for fever and chills."
    },
    "Migraine": {
        "causes": "Stress, hormonal changes, sensory stimuli.",
        "precautions": "Avoid triggers, maintain a sleep schedule.",
        "advice": "Use prescribed migraine medication."
    },
    "Pneumonia": {
        "causes": "Bacterial, viral, or fungal lung infection.",
        "precautions": "Avoid smoking, get vaccinated, maintain hygiene.",
        "advice": "Seek immediate medical attention if breathing is difficult."
    },
    "Typhoid": {
        "causes": "Salmonella bacterial infection from contaminated food/water.",
        "precautions": "Drink clean water, maintain hygiene.",
        "advice": "Take antibiotics as prescribed by a doctor."
    }
}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    symptom = data.get("symptoms")

    if symptom in illness_data:
        response = {"illness": symptom, **illness_data[symptom]}
    else:
        response = {
            "illness": "Unknown Illness",
            "causes": "No data available.",
            "precautions": "Consult a doctor for further diagnosis.",
            "advice": "Seek medical help if symptoms persist."
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
