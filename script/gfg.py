import requests

# URL for fetching data
url = "https://authapi.geeksforgeeks.org/api-get/user-profile-info/?handle=govinddwivedi&article_count=false"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    total_problems_solved = data['data']['total_problems_solved']
    total_problems_count = data['data']['pod_solved_global_longest_streak']

    print(f"Total problems solved: {total_problems_solved}")

    # Read README.md file
    with open('README.md', 'r', encoding="utf8") as file:
        readme_content = file.read()

    # Define start and end markers
    start_marker = '<!-- GFG_DATA_START -->'
    end_marker = '<!-- GFG_DATA_END -->'

    # Find the position of start and end markers
    start_pos = readme_content.find(start_marker)
    end_pos = readme_content.find(end_marker)

    if start_pos != -1 and end_pos != -1:
        # Calculate the content between markers
        content_before = readme_content[:start_pos + len(start_marker)]
        content_after = readme_content[end_pos:]

        # Generate updated content
        updated_content = f"{content_before}\n <img src=\"https://img.shields.io/badge/GeeksforGeeks-{total_problems_solved}-298D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white\" /> \n{content_after}"

        # Write updated content back to README.md
        with open('README.md', 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print("README.md updated successfully.")
    else:
        print("Start or end marker not found in README.md.")

else:
    print(f"Failed to retrieve data: {response.status_code}")
