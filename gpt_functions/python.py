import sys
from io import StringIO

def execute_python_code(code):
    # Redirect stdout to a string buffer
    stdout = sys.stdout
    sys.stdout = output = StringIO()

    try:
        # Compile the code
        compiled_code = compile(code, "<string>", "exec")
        
        # Execute the compiled code
        exec(compiled_code, {})

        # Get the output from stdout
        output_str = output.getvalue()

        return output_str

    except Exception as e:
        return f"Error: {str(e)}"
    
# Function schema
def execute_python_code_schema():
    return {
        "name": "execute_python_code",
        "description": "Compile and execute arbitrary Python code",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to execute"
                }
            },
            "required": ["code"]
        }
    }


def python(code):
    """Execute a Python code snippet.

    Args:
        code (str): The Python code to execute.

    Returns:
        Any: The result of executing the code.
    """
    try:
        # Execute the Python code
        exec(code)
    except Exception as e:
        return str(e)

def python_schema():
    return {
        "name": "python",
        "description": "Execute a Python code snippet",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The Python code to execute"
                }
            },
            "required": ["code"]
        }
    }

