# GPTSH - OpenAI GPT Chat Interface

GPTSH is a command-line interface (CLI) for interacting with OpenAI's GPT-3.5 Turbo model through the OpenAI API. It allows users to have a conversation with GPT, call custom functions, and perform calculations through Python's `eval` function. This tool provides a text-only client and supports loading custom functions from a configuration file.

## Features

- Text-only interface for chatting with GPT
- Integration of custom functions through a configuration file
- Python code execution
- Support for keeping context in conversation
- Utilizes the OpenAI Chat Completions API

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/yourusername/gptsh.git
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

4. Make sure the `.env` file is listed in `.gitignore` to keep your API key secure:
    ```
    echo ".env" >> .gitignore
    ```

## Usage

1. Run the GPTSH interface:
    ```
    python gptsh.py
    ```

2. Optional: You can pass command-line arguments to specify a custom model and prompt:
    ```
    python gptsh.py --model gpt-3.5-turbo-0613 --prompt "Hello, how can I assist you today?"
    ```

3. Chat with the model by typing your messages. To end the session, type `exit` or `quit`.

## Custom Functions

You can define custom functions in a Python file (e.g., `custom_functions.py`) and specify them in a JSON configuration file (e.g., `functions_config.json`). 

### Example functions_config.json:

```json
[
    {
        "name": "execute_python_code",
        "description": "Executes Python code.",
        "module": "custom_functions",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to execute."
                }
            },
            "required": ["code"]
        }
    }
]
```
## Example custom_functions.py:
```python
def execute_python_code(code):
    try:
        return str(eval(code))
    except Exception as e:
        return str(e)
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or create an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This tool communicates with OpenAI's API and may incur costs. Please be mindful of the number of API requests made and be aware of OpenAI's pricing. Additionally, please adhere to OpenAI's terms of service and use responsibly.