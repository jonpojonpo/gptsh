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