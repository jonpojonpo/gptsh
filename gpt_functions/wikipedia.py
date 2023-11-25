def search_wikipedia(query):
    """Search for a given query in Wikipedia and return the summary."""
    import wikipedia

    try:
        # Search Wikipedia for the query
        results = wikipedia.search(query)
        
        if not results:
            return "No results found."
        
        # Get the summary of the first result
        summary = wikipedia.summary(results[0])
        
        return summary
    
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, return the options
        options = e.options
        return f"Ambiguous query. Options: {', '.join(options)}"
    
    except Exception as e:
        # Return error message if an exception occurs
        return str(e)


def search_wikipedia_schema():
    return {
        "name": "search_wikipedia",
        "description": "Search for a given query in Wikipedia and return the summary",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }
