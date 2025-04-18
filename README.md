# 🧠 MCQ Generator with Streamlit + LangChain + OpenAI

## 🚀 Overview

This project is a **Streamlit application** that allows users to upload a document and automatically generate **Multiple Choice Questions (MCQs)** using **LangChain** and **OpenAI**'s language models. It's perfect for educators, trainers, and learners who want to quickly turn reading material into quizzes. 📄➡️❓

## 🎯 Features

- 📁 Upload a document (e.g., PDF, TXT)
- 🤖 Generate MCQs using OpenAI's LLM via LangChain
- ✅ Interactive UI with Streamlit
- 📊 View and answer generated quiz questions
- ☁️ Deployed on AWS EC2 (t3.micro)

## 🗂️ Project Structure

```
src/                # Source code directory
├── data/
|   ├── response.json  # Sample response file
├── mcq/
|   ├── streamlit_app.py    # Streamlit application entry point
|   ├── mcqgenerator/       # LangChain prompt templates and chain logic
|   ├── utils/              # Utility functions for file handling, parsing, etc.
├── .venv/              # Python virtual environment (not pushed to repo)
├── requirements.txt    # Required Python packages
└── README.md           # This file
```

## ⚙️ Requirements

- Python 3.8+
- Streamlit
- LangChain
- OpenAI
- Other dependencies in `requirements.txt`

## 🛠️ Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate into the project directory**:

   ```bash
   cd ai-mcq
   ```

3. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set your OpenAI API key**:

   ```bash
   export OPENAI_API_KEY=your-api-key  # On Windows: set OPENAI_API_KEY=your-api-key
   ```

   or set it in the .env file in the root directory of the project.

   ```bash
   echo "OPENAI_API_KEY=your-api-key" > .env
   ```

6. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```
   Hot-reload
   ```bash
   streamlit run main.py --server.runOnSave=true
   ```
7. **Open your browser** and navigate to `http://localhost:8501` to view the app.

## 🖥️ Deployment

The app is deployed on an **AWS EC2 instance**:

- **Instance type**: `t3.micro`
- **OS**: Ubuntu 22.04 LTS
- **Deployment stack**: Streamlit + Python + OpenAI API
- **Status**: Live (optional: secured with Nginx + HTTPS)

> Since ML processing is handled by OpenAI's API, the app remains lightweight and runs smoothly on a micro instance.

# Commands to execute on the EC2 instance

```bash
# Update and install required packages
sudo apt update && sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget
sudo apt install python3-venv python3-pip -y

```

Clone the repo and install the requirements

```bash
git clone https://github.com/fury-r/ai-mcq-generator.git
cd ai-mcq-generator
```

Install the requirements

```bash
pip install -r requirements.txt
```

Start the streamlit app

```bash
python3 -m streamlit run main.py
```

## 📌 Usage

1. Launch the app in your browser (it will open automatically).
2. Upload a file you want to generate a quiz from.
3. The app will analyze the text and generate MCQs using the OpenAI model.
4. You can view and attempt the generated quiz interactively.

## 🤝 Contributing

We welcome contributions! To contribute:

1. 🍴 Fork the repository
2. 🌿 Create a new branch: `git checkout -b feature/your-feature`
3. 💾 Commit your changes
4. 🚀 Push to the branch: `git push origin feature/your-feature`
5. 📥 Create a pull request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

🧠 Made with LangChain + OpenAI + Streamlit.
