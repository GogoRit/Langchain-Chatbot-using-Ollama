# Langchain-Chatbot-using-Ollama

This project demonstrates how to build a conversational AI chatbot using LangChain, powered by an open-source large language model (LLM) served through [Ollama](https://ollama.ai). The chatbot interface is implemented using **Streamlit** for an intuitive and interactive user experience.

---

## 🚀 Features

- **Open Source LLM Integration**: Uses an LLM through Ollama to provide high-quality conversational capabilities.
- **LangChain Framework**: Utilizes LangChain for managing conversational workflows and enhancing chatbot functionality.
- **Streamlit Interface**: Provides a sleek, user-friendly interface for interacting with the chatbot.
- **Customizable Prompts**: Easily modify and experiment with prompts to fine-tune chatbot responses.
- **Plug-and-Play Architecture**: Scalable and easy-to-deploy chatbot pipeline.

---

## 🛠️ Technologies Used

- **LangChain**: Framework for building LLM-powered applications.
- **Ollama**: Tool for running open-source LLMs locally or in production.
- **Streamlit**: Framework for building interactive web applications.
- **Python**: Core programming language for implementation.

---

### Preview Image

![Preview Image](path/to/your/screenshot.png)

---

## ⚙️ Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
Clone this repository to your local system:
```bash
git clone https://github.com/yourusername/langchain-chatbot-ollama.git
cd langchain-chatbot-ollama
```

### Step 2: Set Up a Python Environment

1. **Create a virtual environment:**

   - For **Linux/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - For **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. **Activate the virtual environment** to isolate the dependencies of this project from your global environment.

3. Once activated, you should see `(venv)` appear in your terminal prompt, indicating the environment is active.

---

### Step 3: Install Project Dependencies

1. Ensure you are in the root directory of the project.

2. Install all required Python libraries listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

   ```
### Step 4: Install Ollama

1. **Download and install Ollama** by visiting the [Ollama website](https://ollama.ai) and following the platform-specific installation instructions.

2. After installing Ollama, pull the required LLM model by running:
   ```bash
   ollama pull <llm-model-name>
   ```
### Step 5: Run the Chatbot

1. Start the Ollama server with the selected LLM model:
   ```bash
   ollama run <llm-model-name>
   ```
2. Launch the Streamlit app by running:
   ```bash
   streamlit run src/app.py
   ```
