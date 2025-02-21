# Linux and Windows Command Generator using OpenAI GPT

## Overview

This **Python script** is an interactive command-line tool that generates **Linux** or **Windows commands** based on user input. It leverages **OpenAI's GPT model (`gpt-4o-mini`)** to generate shell commands and provides an option to execute them directly from the terminal.

## Features

- 🖥️ **Detects the user’s operating system** (Linux/macOS or Windows).
- 🤖 **Uses OpenAI's API** to generate a command based on a natural language description.
- 🔍 **Displays the generated command** for user approval.
- ⚡ **Allows users to execute the command** directly from the terminal.

### Requirements

### 📌 1. Install Python (if not installed)
### 📌 2. API KEY for OPENAPI (as as ENV_VARIABLE)
### 📌 3. Import openapi (if not installed) 

### Usage

## 🚀 Run The script
```
python CommandGenerator
```

## ⚙️ Choose your os 
```
1  # For Linux/macOS
2  # For Windows
```
## 📝 3. Describe the Command
```
Please describe the command you want: list all files in the current directory
```
# example output :
```
ls -l
```
# 🏗️ 5. Execute the Command (Optional)
```
Do you want to run the command? (yes/no):
```

## Security Considerations
	•	🔎 Always review the generated command before executing it, as AI-generated commands might be incorrect or harmful.
	•	❗ This script does not validate the command’s safety before execution. Use with caution.
	•	🛑 Running AI-generated commands as root/admin can be dangerous.



