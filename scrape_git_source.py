import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Function to scrape source code from GitHub repositories
def scrape_github_source_code(username, repository_name, target_languages=None):
    base_url = f"https://github.com/{username}/{repository_name}/"
    url = f"{base_url}/tree/master"
    headers = {
        'User-Agent': 'Your User Agent Here'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find links to files in target languages
            file_links = []
            for link in soup.find_all('a', {'class': 'js-navigation-open Link--primary'}):
                file_url = urljoin(base_url, link.get('href'))
                if target_languages:
                    for lang in target_languages:
                        if f'.{lang}' in file_url:
                            file_links.append(file_url)
                            break
                else:
                    file_links.append(file_url)
            
            # Download source code files
            for file_url in file_links:
                filename = file_url.split('/')[-1]
                file_path = os.path.join('downloaded_code', filename)  # Adjust path as needed
                with open(file_path, 'wb') as file:
                    file_response = requests.get(file_url, headers=headers)
                    if file_response.status_code == 200:
                        file.write(file_response.content)
                        print(f"Downloaded: {filename}")
                    else:
                        print(f"Failed to download {filename}. Status code: {file_response.status_code}")
        else:
            print(f"Failed to retrieve page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    username = "tomnomnom"  # Replace with the GitHub username
    repository_name = "waybackurls"  # Replace with the repository name
    target_languages = ["py", "java", "cpp"]  # Specify target languages or None for all
    
    scrape_github_source_code(username, repository_name, target_languages)


