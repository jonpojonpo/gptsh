import gpt_functions as gptf

# Get the list of available functions
available_functions = gptf.get_available_functions()
print("Available functions:", available_functions)

# Get the schema for a specific function
weather_schema = gptf.get_function_schema('get_current_weather')
print("Schema for 'get_current_weather':", weather_schema)

# Call a function
weather_func = gptf.functions['get_current_weather']
weather = weather_func('San Francisco, CA')
print("Weather in San Francisco:", weather)
