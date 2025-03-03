# Groq Chatbot

Welcome to the **Groq Chatbot**, an interactive chatbot built using **Streamlit** and powered by the **Groq API**. This chatbot allows users to have real-time conversations and receive responses using the **llama-3.3-70b-versatile** model.

## Features

- Real-time interactive chatbot with Streamlit UI
- Streaming responses for a seamless chat experience
- Maintains conversation history during the session
- Custom styling for a clean chat interface

## Installation

### Prerequisites
- Python 3.7 or later
- Pip (Python package manager)
- Groq API Key

### Steps to Set Up Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/chatbot.git
   cd chatbot
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root directory.
   - Add the following line:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

5. **Run the chatbot**
   ```bash
   streamlit run app.py
   ```

## Usage

- Open the chatbot in your browser (default: `http://localhost:8501`).
- Enter a message in the input box.
- The chatbot will process your request and respond in real time.
- The conversation history will be maintained during the session.

## Project Structure
```
chatbot/
│── app.py             # Main application file
│── requirements.txt   # Dependencies
│── .env.example       # Example environment file
│── README.md          # Documentation
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push the changes to your fork.
5. Create a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to reach out to:
- **GitHub**: palleyaksha(https://github.com/palleyaksha)
- **Email**: palleyaksha28@gmail.com

Happy coding! 🚀
