import wsgiref
import requests
import os
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

def fetch_github_repositories(topics, username):
    # Get the token from environment
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not set.")
        return

    # Topics for filtration: "portfolio-website", "finished", etc.
    topics_query = "+".join([f"topic:{topic}" for topic in topics])
    url = f"https://api.github.com/search/repositories?q={topics_query}+user:{username}"
    headers = {
        "Authorization": f"token {token}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if request was successful
        data = response.json()  # Load JSON data
        if not isinstance(data, dict):  # Ensure data is a dictionary (JSON)
            print(f"Unexpected data format: {data}")
            return
        
        print("Data was loaded:")
        for repo in data.get("items", []):
            print(f"Repo: {repo['name']} - {repo['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    print("Running script...")
    username = "Yushikuni"
    topics = ["portfolio-website", "unfinished-project"]
    topics2 = ["portfolio-website", "finished-project"]
    print("Unfinished projects:")
    fetch_github_repositories(topics, username)
    print("Finished projects:")
    fetch_github_repositories(topics2, username)
