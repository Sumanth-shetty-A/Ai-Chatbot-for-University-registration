import os
import requests
from dotenv import load_dotenv
from db import save_student_details, get_all_courses
from flask import session

load_dotenv()

# Watsonx API Credentials
api_key = os.getenv("WATSONX_API_KEY")
url = os.getenv("WATSONX_URL")
model_id = os.getenv("WATSONX_MODEL")

# Watsonx Headers
HEADERS = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Dictionary to store ongoing user sessions
user_sessions = {}

def send_message(user_id, user_input):
    if user_id not in user_sessions:
        user_sessions[user_id] = {"state": None, "step": None, "data": {}}

    user_session = user_sessions[user_id]

    if user_session["state"] == "registering":
        return handle_registration(user_id, user_input)

    if user_input.lower() in ["help me register", "start registration", "please register", "register me", "apply now"]:
        user_sessions[user_id] = {"state": "registering", "step": "first_name", "data": {}}
        return "Sure! Let's start your registration. What is your first name?"

    return get_ai_response(user_input)

def handle_registration(user_id, user_input):
    user_session = user_sessions[user_id]

    if user_session["step"] == "first_name":
        user_session["data"]["first_name"] = user_input
        user_session["step"] = "last_name"
        return "Great! What's your last name?"

    elif user_session["step"] == "last_name":
        user_session["data"]["last_name"] = user_input
        user_session["step"] = "city"
        return "Thanks! Which city are you from?"

    elif user_session["step"] == "city":
        user_session["data"]["city"] = user_input
        user_session["step"] = "email"
        return "Got it! What's your email address?"

    elif user_session["step"] == "email":
        user_session["data"]["email"] = user_input
        user_session["step"] = "program_id"
        return list_available_courses() + "\nPlease enter the Program ID of your chosen course."

    elif user_session["step"] == "program_id":
        try:
            program_id = int(user_input)
            user_session["data"]["program_id"] = program_id

            student_details = user_session["data"]
            student_details["language"] = "English"  

            save_student_details(student_details)  # Save to database

            del user_sessions[user_id]  # Clear user session after registration
            return "Registration complete! You are now enrolled in the selected program. Thank you!"
        
        except ValueError:
            return "Invalid Program ID. Please enter a valid numeric Program ID."

def list_available_courses():
    courses = get_all_courses()
    if courses:
        return "Here are the available programs:\n" + "\n".join(f"{course[0]}: {course[1]} ({course[2]}, {course[3]} years, {course[4]}) - {course[5]}" for course in courses)
    return "No programs found at the moment."

def get_ai_response(user_input):
   try:
    payload = {
        "model_id": model_id,
        "input": user_input,
        "parameters": {"temperature": 0.7, "max_tokens": 200}
    }
    
    print("Sending Request to Watsonx API:", payload)  # Debugging

    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    print("Watsonx API Response:", data)  # Debugging

    if "results" in data and len(data["results"]) > 0:
        return data["results"][0]["generated_text"]
    
    return "I'm sorry, I didn't understand that."
   except requests.exceptions.RequestException as e:
    print(f"Watsonx API Request Failed: {e}")  
    return "An error occurred. Please try again later."
 