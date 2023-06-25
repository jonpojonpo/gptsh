import json

def interactive_function_creation():
    # Get function name
    function_name = input("Enter the function name: ")

    # Get module name
    module_name = input("Enter the module name [default=custom_functions]: ")
    if not module_name:
        module_name = 'custom_functions'

    # Get parameters
    parameters = {}
    while True:
        param_name = input("Enter parameter name (or 'done' if finished): ")
        if param_name == 'done':
            break
        param_type = input("Enter parameter type [string, number, etc.]: ")
        parameters[param_name] = param_type

    # Get code block
    print("Enter the code block (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    code_block = '\n'.join(lines)

    # Update the function config file (assuming JSON format)
    function_config = {
        'name': function_name,
        'module': module_name,
        'parameters': parameters,
        'code': code_block
    }
    
    # Load existing config
    with open('functions_config.json', 'r') as file:
        config = json.load(file)
    
    # Append new function config
    config.append(function_config)
    
    # Write updated config back to file
    with open('functions_config.json', 'w') as file:
        json.dump(config, file, indent=4)

    print(f"Function {function_name} has been successfully created.")

# Example usage
interactive_function_creation()
