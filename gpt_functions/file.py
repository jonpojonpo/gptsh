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


def write_to_file_schema():
   return {
        "module": "custom_functions",
        "name": "write_to_file",
        "description": "Write text to a file on the local system",
        "parameters": {
          "type": "object",
          "properties": {
            "file_name": {
              "type": "string",
              "description": "The name of the file to write to"
            },
            "text": {
              "type": "string",
              "description": "The text content to write to the file"
            },
            "mode": {
              "type": "string",
              "enum": ["write", "append"],
              "description": "Whether to write to a new file or append to an existing file"
            }
          },
          "required": ["file_name", "text"]
        }
      }

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


def read_from_file_schema():
    return {
        "module": "custom_functions",
        "name": "read_from_file",
        "description": "Read text from a file on the local system",
        "parameters": {
          "type": "object",
          "properties": {
            "file_name": {
              "type": "string",
              "description": "The name of the file to read from"
            }
          },
          "required": ["file_name"]
        },
        "return": {
          "type": "string",
          "description": "The text content of the file"
        }
      }
