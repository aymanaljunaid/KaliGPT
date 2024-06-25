# KaliGPT

KaliGPT is a simple Python-based chatbot application that interacts with the OpenAI API to provide responses to your inputs.


## Installation

To ensure compatibility with the current code, install a specific older version of the OpenAI library:

```bash
pip install openai==0.28
```

### Setup

To run KaliGPT, you need to set up your OpenAI API key as an environment variable. This ensures secure handling of sensitive information and avoids hardcoding it directly into the source code.

#### Setting up your OpenAI API Key

##### For Windows:

1. **Using Command Prompt:**
   - Open Command Prompt and use the following command to set the `OPENAI_API_KEY` environment variable for the current session:
     ```cmd
     set OPENAI_API_KEY=your_actual_openai_api_key_here
     ```
   - To set it permanently, use the `setx` command:
     ```cmd
     setx OPENAI_API_KEY "your_actual_openai_api_key_here"
     ```

2. **Using Windows PowerShell:**
   - For the current session only:
     ```powershell
     $env:OPENAI_API_KEY="your_actual_openai_api_key_here"
     ```
   - To set it permanently in PowerShell:
     ```powershell
     [System.Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your_actual_openai_api_key_here", [System.EnvironmentVariableTarget]::User)
     ```

3. **Through Windows System Properties:**
   - Open the Start Search, type in `env`, and select **Edit the system environment variables** or **Edit environment variables for your account**.
   - In the System Properties window, click on the **Environment Variables** button.
   - In the Environment Variables window, click **New** under the "User variables" or "System variables" section depending on whether you want the variable to be available system-wide or just for your user account.
   - Enter `OPENAI_API_KEY` as the Variable name and paste your API Key in the Variable value field.
   - Click OK to close all dialogs.

#### For macOS and Linux:

1. **Using the Terminal:**
   - For a temporary setting that lasts until the terminal is closed, type the following:
     ```bash
     export OPENAI_API_KEY=your_actual_openai_api_key_here
     ```
   - To set it permanently, add the export command to your shell’s startup file, like `.bashrc` or `.zshrc`:
     ```bash
     echo 'export OPENAI_API_KEY="your_actual_openai_api_key_here"' >> ~/.bashrc
     ```
   - After editing `.bashrc` or `.zshrc`, reload it or restart your terminal:
     ```bash
     source ~/.bashrc
     ```

### Verify the Environment Variable

To confirm that your environment variable is set correctly:

- On Windows Command Prompt or PowerShell:
  ```cmd
  echo %OPENAI_API_KEY%

- On macOS or Linux:
  ```bash
  echo $OPENAI_API_KEY
  ```
Setting this environment variable allows your scripts and applications to securely access it, reducing the risk of exposing your key in your code.

# Usage
Once your environment variable is set up:

1. Clone the repository and navigate to the directory containing KaliGPT.py.
   ```bash
   git clone https://github.com/aymanaljunaid/KaliGPT.git
   cd KaliGPT
   ```
3. Run the script using Python:
   ```bash
   python KaliGPT.py
   ```
4. Enter your messages in the terminal where prompted.
5. Type exit to end the chat session.
