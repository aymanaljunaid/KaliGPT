# KaliGPT

KaliGPT is a simple Python-based chatbot application that interacts with the OpenAI API to provide responses to your inputs.

## Installation

To set up KaliGPT, follow these steps:

### Clone the repository

```bash
git clone https://github.com/aymanaljunaid/KaliGPT.git
cd KaliGPT
```

### Install dependencies

Ensure you have Python installed, and then run:

```bash
pip install -r requirements.txt
```

## Configuration

To use KaliGPT, you need to set up your OpenAI API key:

1. There is a file `config.py` in the project root directory.
2. Add your OpenAI API key in `config.py`:

```python
# config.py
OPENAI_API_KEY = "your_actual_openai_api_key_here"
```

Replace `your_actual_openai_api_key_here` with your actual OpenAI API key.

## Usage

To start a chat with KaliGPT, run the following command in your terminal:

```bash
python KaliGPT.py
```

Type your messages and see how KaliGPT responds! Type 'exit' to end the chat session.
