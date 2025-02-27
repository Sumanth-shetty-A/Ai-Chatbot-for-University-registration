import sqlite3

def create_student_details_tables():
    conn = sqlite3.connect('university_admissions.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS university_programs (
        program_id INTEGER PRIMARY KEY,
        program_name TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        language TEXT,
        first_name TEXT,
        last_name TEXT,
        city TEXT,
        email TEXT,
        program_id INTEGER,
        FOREIGN KEY (program_id) REFERENCES university_programs(program_id)
    )''')

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_program_id ON student_details (program_id)")

    conn.commit()
    conn.close()

def save_student_details(student_details):
    """Saves a new student record into the database."""
    try:
        with sqlite3.connect('university_admissions.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
            INSERT INTO student_details (language, first_name, last_name, city, email, program_id)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (student_details.language, student_details.first_name, student_details.last_name, 
                  student_details.city, student_details.email, student_details.program_id))
            conn.commit()
    except Exception as e:
        print(f"Error saving student details: {e}")

def get_latest_student():
    """Fetches the most recent student record."""
    try:
        with sqlite3.connect('university_admissions.db') as conn:
            cursor = conn.cursor()
            query = '''
            SELECT sd.id, sd.language, sd.first_name, sd.last_name, sd.city, sd.email, p.program_name
            FROM student_details sd
            JOIN university_programs p ON sd.program_id = p.program_id
            ORDER BY sd.id DESC LIMIT 1
            '''
            cursor.execute(query)
            return cursor.fetchone()
    except Exception as e:
        print(f"Error fetching latest student: {e}")
        return None

def get_all_students():
    """Fetches all students along with their programs."""
    try:
        with sqlite3.connect('university_admissions.db') as conn:
            cursor = conn.cursor()
            query = '''
            SELECT sd.id, sd.language, sd.first_name, sd.last_name, sd.city, sd.email, p.program_name
            FROM student_details sd
            JOIN university_programs p ON sd.program_id = p.program_id
            '''
            cursor.execute(query)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching all students: {e}")
        return []

def get_students_by_course(program_id):
    """Fetches students enrolled in a specific course."""
    try:
        with sqlite3.connect('university_admissions.db') as conn:
            cursor = conn.cursor()
            query = '''
            SELECT sd.id, sd.language, sd.first_name, sd.last_name, sd.city, sd.email, p.program_name
            FROM student_details sd
            JOIN university_programs p ON sd.program_id = p.program_id
            WHERE sd.program_id = ?
            '''
            cursor.execute(query, (program_id,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching students by course: {e}")
        return []

def delete_student(student_id):
    """Deletes a student from the database."""
    try:
        with sqlite3.connect('university_admissions.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student_details WHERE id = ?", (student_id,))
            conn.commit()
    except Exception as e:
        print(f"Error deleting student: {e}")

def get_all_courses():
    """Fetches all available university programs with full details."""
    try:
        with sqlite3.connect('university_admissions.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT program_id, program_name, department, duration, degree_type, description FROM university_programs")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []


def get_students_by_program(program_id):
    conn = sqlite3.connect('university_admissions.db')
    cursor = conn.cursor()

    query = '''
    SELECT sd.id, sd.language, sd.first_name, sd.last_name, sd.city, sd.email, p.program_name
    FROM student_details sd
    JOIN university_programs p ON sd.program_id = p.program_id
    WHERE sd.program_id = ?
    '''
    cursor.execute(query, (program_id,))
    students = cursor.fetchall()

    conn.close()
    return students
