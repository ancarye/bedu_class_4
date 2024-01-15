import requests

BASE_URL = 'https://api.github.com/'

def get_github_user(username):
    url = f'{BASE_URL}users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None

def get_user_followers(username):
    url = f'{BASE_URL}users/{username}/followers'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def print_total_followers(username):
    followers = get_user_followers(username)
    if followers is not None:
        total_followers = len(followers)
        print(f'Total followers for {username}: {total_followers}')
    else:
        print(f'Unable to fetch followers for {username}')

username = input('Give me a username you want to extract the information:\n')
selected_user = get_github_user(username)

user_followers = get_user_followers(username)

if user_followers is not None:
    for follower in user_followers:
        print(f'Follower: {follower["login"]}')
else:
    print(f'Unable to fetch followers for {username}')

print_total_followers(username)