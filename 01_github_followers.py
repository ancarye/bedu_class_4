import requests

BASE_URL = 'https://api.github.com/'

def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None


def download_avatar_user(avatar_url, username):
    response = requests.get(avatar_url)
    if response.status_code == 200:
        # Download image
        response_content = response.content
        filename = f'tmp/{username}.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None

def get_user_folowers(username):
    url = f'{BASE_URL}users/{username}/followers'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

username = input('Give me an username you want to extract the information:\n')
selected_user = get_github_user(username)

user_folowers = get_user_folowers(username)

for follower in user_folowers:
    folower_avatar_url = follower.get('avatar_url')
    folower_username = follower.get('login')
    download_avatar_user(folower_avatar_url, folower_username)











