import importlib
import os

# Initialize dictionaries to hold functions and their schemas
functions = {}
function_schemas = {}

# Get the current directory of this file.
current_dir = os.path.dirname(__file__)

# Get all the .py files in this directory.
files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f)) and f.endswith('.py')]

# Import each file.
for file in files:
    if file != "__init__.py":  # Avoid importing self
        module_name, _ = os.path.splitext(file)  # Remove the .py
        #print("importing: ", module_name)
        module = importlib.import_module('.' + module_name, 'gpt_functions')
        
        for attr in dir(module):
            if attr.endswith('_schema'):
                function_schemas[attr[:-7]] = getattr(module, attr)
            elif not attr.startswith('_'):
                functions[attr] = getattr(module, attr)

def get_available_functions():
    # Only include functions for which a schema is defined
    return [f for f in functions.keys() if f in function_schemas]

def get_function_schema(function_name):
    if function_name not in function_schemas:
        return ''
        raise ValueError(f"No such function: {function_name}")
    return function_schemas[function_name]()

def get_function(function_name):
    if function_name not in functions:
        raise ValueError(f"No such function: {function_name}")
    return functions[function_name]
