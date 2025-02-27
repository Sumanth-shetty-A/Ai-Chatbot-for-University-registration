# AI-Powered Course Registration Chatbot

### Idea of the Project: 

**Project Overview: Creating an AI-Powered University Admission Chatbot**

This project focuses on developing a user-friendly chatbot that assists students in registering for courses. The AI chatbot interacts with students, collects necessary registration details, and dynamically handles missing information. After completing registration, students can review their details and explore information about other registered students and their enrolled courses. This project leverages advanced AI technologies and database management to streamline the course registration process, providing students with a seamless and interactive experience.

**Project Details:**

**Part 1: AI-Powered Admission Chatbot**
- Implemented an AI chatbot to facilitate course registration in a friendly and interactive manner.
- Utilized natural language processing to extract essential registration details such as first name, last name, email, preferred language, and desired course.
- Dynamically prompts users for any missing information during the conversation.
- Once registration details are complete, the chatbot acknowledges the user and securely stores the information in the database.

**Part 2: Information Review Interface**
- Developed a web-based interface using Flask to allow students to review their registered course information.
- Enables students to view details of other registered students and the courses they are enrolled in.

**Features:**

- **Chatbot Registration:**
  - Engages students in a friendly conversation.
  - Collects essential registration details interactively.
  - Dynamically prompts for missing information.

- **Information Review:**
  - Provides students with access to their registered course information.
  - Allows viewing of other students' enrollment details.

**Technologies Used:**

- **Flask Application:**
  - Primary framework for web application development.
  - Manages routing and renders HTML templates for user interface.

- **SQLite3 Database:**
  - Stores and manages student registration data securely.
  - Supports operations such as querying details of specific students and listing all registered students.

- **AI Chatbot:**
  - Powered by the Gemini 1.5 Pro/Flash language model.
  - Integrated with LangChain for efficient form filling via a conversational interface.
## Demo
Test Cases:
- Test 1 - When the user's message has only one field to save in the database.  
https://youtu.be/V9fJgMzlNzs 
- Test 2 - When the user's message has multiple fields to save in the database.  
https://youtu.be/pgGiZA6UGPs 
- Test 3 - When the user's message has all fields to save in the database.   
https://youtu.be/FjvBS84DO3U 
- Test 4 - When the user's message contains misleading information with unrelated details, understanding what information should be saved in the database.  
https://youtu.be/Cz0gebv4_xk 
## Getting Started

### Prerequisites
Ensure you have the following installed:

- Python 3.11+
- Docker (optional)
- Docker Compose (optional)

You will also need a WATSONX_API_KEY token from [Watson AI Studio](https://aistudio.google.com/). 

### Installation

#### Using Docker

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ruqyai/AI-Powered-Course-Registration-Chatbot.git
    cd qanoniiah
    ```

2. **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your your key of WATSONX API KEY here:

    ```env
    WATSONX_API_KEY="Add your WATSONX_API_KEY here "
    WATSONX_URL="Add WatsonX URL here"
    WATSONX_MODEL="Add Languege Model ID here"
    ```

3. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

4. **Access the application:**
   - Open your browser and navigate to http://localhost:8000.

#### Without Docker

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ruqyai/AI-Powered-Course-Registration-Chatbot.git
    cd qanoniiah
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your your key of WATSONX API KEY here:

    ```env
    WATSONX_API_KEY="Add your WATSONX_API_KEY here "
    WATSONX_URL="Add WatsonX URL here"
    WATSONX_MODEL="Add Languege Model ID here"
    ```
 
5. **Run the Flask application:**

    ```bash
    python main.py
    ```

6. **Access the application:**
   - Open your browser and navigate to `http://localhost:8080`.
