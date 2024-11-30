import requests

def fetch_github_repositories(username):
    url_old = "https://api.github.com/search/repositories?q=topic:portfolio-website"
    url = f"https://api.github.com/users/{username}/repos"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Zkontroluje, zda byl požadavek úspìšný
        data = response.json()  # Naètení JSON dat
        print("Data was load:")
        #for repo in data.get("items", []):
        for repo in data:
            print(f"Repo: {repo['name']} - {repo['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetch data: {e}")

#if __name__ == "__main__":
 #   print("Aplication is running!")
  #  username = "Yushikuni"
   # fetch_github_repositories(username)

if __name__ == "__main__":
    print("Runing script...")
    fetch_github_repositories("Yushikuni")

