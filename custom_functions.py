def get_current_weather(location, unit="fahrenheit"):
    # Dummy function for example, in practice, you can implement actual functionality.
    return f"The weather in {location} is sunny with temperature 25 degrees {unit}."


def evaluate_expression(expression):
    try:
        # Using eval to evaluate the mathematical expression
        return eval(expression)
    except Exception as e:
        # Returning error message in case of an exception (e.g. invalid expression)
        return str(e)
    
def write_to_file(file_name, text, mode='write'):
    """
    Write text to a file on the local system.
    
    :param file_name: The name of the file to write to.
    :param text: The text content to write to the file.
    :param mode: Whether to write to a new file or append to an existing file.
                 'write' for writing to a new file,
                 'append' for appending to an existing file.
    """
    # Determine the mode
    if mode == 'write':
        write_mode = 'w'
    elif mode == 'append':
        write_mode = 'a'
    else:
        raise ValueError("Mode must be either 'write' or 'append'")
    
    # Write to the file
    with open(file_name, write_mode) as file:
        file.write(text)

def read_from_file(file_name):
    """
    Read text from a file on the local system.
    
    :param file_name: The name of the file to read from.
    :return: The text content of the file.
    """
    # Read from the file
    with open(file_name, 'r') as file:
        content = file.read()
    
    return content       

import subprocess

def execute_shell_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")

