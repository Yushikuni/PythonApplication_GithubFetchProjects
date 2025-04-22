


from wsgiref import headers
import requests
import os
from dotenv import load_dotenv

# Načti proměnné z .env souboru
load_dotenv()

def fetch_github_repositories(topics, username):

    # Získání tokenu z prostředí
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not set.")
        return

    # Topis for filtation: "portfolio-website", "finished", ""
    topics_query = "+".join([f"topic:{topic}" for topic in topics])
    url = f"https://api.github.com/search/repositories?q={topics_query}+user:{username}"
    headers = {
        "Authorization": f"token {token}"
    } 
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # chcek if request was succesfull
        data = response.json()  # Loading JSON file data
        if not isinstance(data, dict):  # Ověření, že data jsou slovník (JSON)
            print(f"Unexped data format: {data}")
            return
        
        print("Data was load:")
        for repo in data.get("items", []):
            print(f"Repo: {repo['name']} - {repo['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetch data: {e}")

if __name__ == "__main__":
    print("Runing script...")
    username = "Yushikuni"
    topics = ["portfolio-website","unfinished-project"]
    topics2 = ["portfolio-website","finished-project"]
    print(f"Unfinished projects:")
    fetch_github_repositories(topics, username)
    print(f"Finished projects:")
    fetch_github_repositories(topics2, username)
