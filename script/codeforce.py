import requests

def get_total_problem_count():
    url = 'https://codeforces.com/api/problemset.problems'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()

        if data['status'] == 'OK':
            problem_count = data['result']['problems']
            total_count = len(problem_count)
            return total_count
        else:
            print(f"Error: {data['comment']}")
            return -1

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return -1
    
def get_solved_problem_count(handle):
    url = f'https://codeforces.com/api/user.status?handle={handle}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        data = response.json()

        if data['status'] == 'OK':
            solved_count = 0
            for submission in data['result']:
                if submission['verdict'] == 'OK':
                    solved_count += 1

            return solved_count
        else:
            print(f"Error: {data['comment']}")
            return -1  # Return -1 or handle error accordingly

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return -1


def updateReadme(solved_count, total_problem_count):
    # Read README.md file
    with open('README.md', 'r', encoding="utf8") as file:
        readme_content = file.read()

    # Define start and end markers
    start_marker = '<!-- CODEFORCE_DATA_START -->'
    end_marker = '<!-- CODEFORCE_DATA_END -->'

    # Find the position of start and end markers
    start_pos = readme_content.find(start_marker)
    end_pos = readme_content.find(end_marker)

    if start_pos != -1 and end_pos != -1:
        # Calculate the content between markers
        content_before = readme_content[:start_pos + len(start_marker)]
        content_after = readme_content[end_pos:]

        # Generate updated content
        updated_content = f"{content_before}\n<img src=\"https://img.shields.io/badge/Codeforces-{solved_count}-445f9d?style=for-the-badge&logo=Codeforces&logoColor=white\" />\n{content_after}"

        # Write updated content back to README.md
        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print("README.md updated successfully.")
    else:
        print("Start or end marker not found in README.md.")



if __name__ == "__main__":

    username = "govinddwivedi"

    solved_count = get_solved_problem_count(username)

    if solved_count != -1:
        print(f"[Codeforce] Total solved problems for {username}: {solved_count}")

    total_problem_count = get_total_problem_count()

    if total_problem_count != -1:
        print(f"[Codeforce] Total number of problems: {total_problem_count}")
    

    updateReadme(solved_count, total_problem_count)
