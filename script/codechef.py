import requests
from bs4 import BeautifulSoup
import re

def updateReadme(solved_count):
    # Read README.md file
    with open('README.md', 'r', encoding="utf8") as file:
        readme_content = file.read()

    # Define start and end markers
    start_marker = '<!-- CODECHEF_DATA_START -->'
    end_marker = '<!-- CODECHEF_DATA_END -->'

    # Find the position of start and end markers
    start_pos = readme_content.find(start_marker)
    end_pos = readme_content.find(end_marker)

    if start_pos != -1 and end_pos != -1:
        # Calculate the content between markers
        content_before = readme_content[:start_pos + len(start_marker)]
        content_after = readme_content[end_pos:]

        # Generate updated content
        updated_content = f"{content_before}\n<img src=\"https://img.shields.io/badge/CodeChef-{solved_count}-5B4638?style=for-the-badge&logo=CodeChef&logoColor=white\" />\n{content_after}"

        # Write updated content back to README.md
        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print("README.md updated successfully.")
    else:
        print("Start or end marker not found in README.md.")


def fetch_codechef_solved_problems(username):
    # URL of the user's profile page
    url = f"https://www.codechef.com/users/{username}"

    # Send a request to fetch the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the profile page. Status code: {response.status_code}")
        return None

    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert the soup object to a string
    page_content = str(soup)

    # Use regex to find the "Total Problems Solved" line and extract the number
    match = re.search(r'Total Problems Solved:\s*(\d+)', page_content)

    if match:
        total_solved = int(match.group(1))
        return total_solved
    else:
        print("Total Problems Solved section not found.")
        return None

# Example usage
username = "govinddwivedi"
total_solved = fetch_codechef_solved_problems(username)
if total_solved is not None:
    print(f"[CodeChef] Total Problems Solved by {username}: {total_solved}")
    updateReadme(total_solved)
else:
    print("Could not retrieve the total number of solved problems.")
