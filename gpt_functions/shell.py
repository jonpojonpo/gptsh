
import subprocess

def execute_shell_command(command):
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return e.output.decode("utf-8")


def execute_shell_command_schema():
    return {
    "module": "custom_functions",
    "name": "execute_shell_command",
    "description": "Execute a shell command in Linux",
    "parameters": {
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "The shell command to be executed"
            }
        },
        "required": ["command"]
    },
    "return": {
        "type": "string",
        "description": "The output of the shell command"
    }
}
