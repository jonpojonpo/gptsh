# GPTsh - Your Interactive Programming Assistant

GPTsh is a powerful tool that lets you interact with OpenAI's GPT-4 in a shell-like environment. You can write code, execute shell commands, run database queries, and much more, all with the power of AI.


## Features

- Text-only interface for chatting with GPT
- Dynamic integration of custom functions through a functionGPT assistant 
- Python code execution
- Command line shell code execution
- Support for keeping context in conversation and chat history that can be scrolled through
- Utilizes the OpenAI Chat Completions API

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/jonpojonpo/gptsh.git
    cd gptsh
    ```

2. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the repository and set your OpenAI API key:
    ```
    OPENAI_API_KEY=your_api_key_here
    ```


## Key Features

* Execute GPT Functions: GPTsh can execute predefined functions. These functions can run shell commands, SQL queries, write files, and more. The possibilities are virtually endless.

* Dynamic Function Addition: Adding new functions is easy. Just use the provided script `add-function.sh`, or have the assistant write the function and its schema for you in the shell.

* System Prompts: The system prompts are customizable and can be set at runtime via command line flags. You can also add your own prompts!

* Token-efficient Design: The GPTsh tool is designed to be token-efficient. It manages tokens for you, so you don't have to worry about exceeding the maximum limit.

## How to Use GPTsh

1. **Start the Shell**

```bash
./gptsh

    Select a System Prompt

You can select a specific system prompt using the --prompt-file flag:

bash

./gptsh --prompt-file functionGPT

    Add a Function

You can add a new function using the add-function.sh script:

bash

./add-function.sh

This will open the GPTsh shell with a specific prompt that guides the assistant in writing a new function and its schema.

How to Contribute

You're welcome to contribute to the development of GPTsh! Feel free to submit a pull request if you've made any improvements or fixed any bugs.
