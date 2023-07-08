def eval(expression):
    """Evaluate a Python expression and return the result"""
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


def eval_schema():
    return {
        "name": "eval",
        "description": "Evaluate a Python expression",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The Python expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    }

