import requests

def fetch_github_repositories(username):
    url_old = "https://api.github.com/search/repositories?q=topic:portfolio-website"
    # Topis for filtation: "portfolio-website", "finished", ""
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()  # chcek if request was succesfull
        data = response.json()  # Loading JSON file data
        print("Data was load:")
        for repo in data:
            print(f"Repo: {repo['name']} - {repo['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetch data: {e}")

if __name__ == "__main__":
    print("Runing script...")
    username = "Yushikuni"
    fetch_github_repositories(username)

