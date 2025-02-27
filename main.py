from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from dotenv import load_dotenv
from db import create_student_details_tables, get_latest_student, get_all_students, delete_student, get_students_by_program, get_all_courses
from chatbot import send_message

load_dotenv()

# Flask app setup
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")  # Change this to a secure key
create_student_details_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admission-chat', methods=['POST'])
def admission_chat():
    user_input = request.json.get('message', '')
    user_id = request.json.get('user_id', request.remote_addr)  # Use user's IP if user_id is missing

    if not user_input:
        return jsonify({'response': "Please provide a message."}), 400

    response = send_message(user_id, user_input)
    print(f"Chatbot Response: {response}")  # Debugging Log
    return jsonify({'response': response})
  # Ensure response is returned correctly

@app.route('/student-details')
def student_details():
    try:
        student = get_latest_student()
        if student:
            return render_template('student_details.html', student=student)
        else:
            return render_template('error.html', message="No student details found."), 404
    except Exception as e:
        print(f"Error fetching student details: {e}")
        return render_template('error.html', message="An error occurred while fetching student details."), 500

@app.route('/students', methods=['GET', 'POST'])
def all_students():
    selected_program = '0'
    programs = get_all_courses()
    try:
        if request.method == 'POST':
            program_id = request.form.get('program_id')
            students = get_students_by_program(program_id if program_id != '0' else None)
            selected_program = program_id
        else:
            students = get_all_students()
        return render_template('all_students.html', students=students, selected_program=selected_program, programs=programs)
    except Exception as e:
        print(f"Error fetching students: {e}")
        return render_template('error.html', message="An error occurred while fetching students."), 500

@app.route('/delete/<int:student_id>')
def delete(student_id):
    try:
        delete_student(student_id)
        return redirect(url_for('all_students'))
    except Exception as e:
        print(f"Error deleting student: {e}")
        return render_template('error.html', message="An error occurred while deleting the student."), 500

@app.route('/courses')
def courses():
    try:
        courses = get_all_courses()
        return render_template('courses.html', courses=courses)
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return render_template('error.html', message="An error occurred while fetching courses."), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
