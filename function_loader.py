import importlib
import json

def load_functions(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)

    functions = []
    available_functions = {}

    for func_config in config:
        module_name = func_config["module"]
        function_name = func_config["name"]

        module = importlib.import_module(module_name)
        function = getattr(module, function_name)
        
        available_functions[function_name] = function

        func_config.pop("module", None)
        functions.append(func_config)

    return functions, available_functions