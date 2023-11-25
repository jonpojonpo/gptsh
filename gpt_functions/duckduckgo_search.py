from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

def search_web_ddg(query):
    """Searches the web using DuckDuckGo search engine and retrieves the top result."""
    # Your code to search the web using DuckDuckGo API
    results=""
    word_limit=2000
    with DDGS() as ddgs:
      for r in  ddgs.text(query, region='uk-en', safesearch='Off', timelimit='y', backend="lite"):
          response = requests.get(r['href'])
          soup = BeautifulSoup(response.content, 'html.parser')
          def tag_visible(element):
              if element.parent.name in ['style','script','head','title','meta','[document]']:
                  return False
              if isinstance(element, Comment):
                  return False
              return True
          visible_text= soup.findAll(text=True)
          visible_text=filter(tag_visible, visible_text)
          result = u" ".join(t.strip() for t in visible_text)
          words = result.split()
          if len(words) > word_limit:
              result = ' '.join(words[:word_limit])
          return result


def search_web_ddg_schema():
    return {
    "name": "search_web_ddg",
    "description": "Searches the web using DuckDuckGo search engine",
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



