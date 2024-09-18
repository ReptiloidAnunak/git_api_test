import json
import time
import datetime
from github import Github
from github import Auth
import os
from dotenv import load_dotenv

load_dotenv()
git_login = os.environ.get('GIT_LOGIN')
git_password = os.environ.get('GIT_TOCKEN')
test_repo_name = os.environ.get('REPO_NAME')


def get_git_user(git_login: str, git_password: str):
    auth = Auth.Login(git_login,git_password)
    git = Github(auth=auth)
    git_user = git.get_user()
    print(f'\n\n✅ GitHub user has logged in: {git_user.login}')
    return git_user

def get_repositories_lst(git_user):
    repos = git_user.get_repos()
    git_users_repos_lst = [r.name for r in repos]
    return git_users_repos_lst


def create_new_repository(git_user, new_repo_name: str):
    new_repo = git_user.create_repo(name=new_repo_name, private=False)
    print(f"\n\n✅ Repository successfully crated: {new_repo.url}")
    return new_repo

def check_new_repo_in_repos_lst(git_user, repo_name):
    user_repos_lst = get_repositories_lst(git_user)
    if repo_name in user_repos_lst:
        print(f'\nRepositories list updated: {user_repos_lst}')
        print(f'{repo_name} has been created  & presents in the repositories list')
        print(f'New repositories` amount: {len(user_repos_lst)}')
    else:
        print('ERROR')


def delete_test_repository(git_user, repo):
    repo.delete()
    print(f'\n\n✅ Repository successfully deleted: {repo.name}')


def run_git_repositories_test():
    git_user = get_git_user(git_login, git_password)
    user_repositories_link = git_user.html_url + '?tab=repositories'

    user_repos_lst = get_repositories_lst(git_user)
    print(f'\nCurrent repositories list:\n{user_repos_lst}')
    print(f'Current repositories amount: {len(user_repos_lst)}')
    print(user_repositories_link)

    new_repo = create_new_repository(git_user, test_repo_name)
    time.sleep(10)
    check_new_repo_in_repos_lst(git_user, new_repo.name)
    print(user_repositories_link)
    time.sleep(5)

    delete_test_repository(git_user, new_repo)
    user_repos_lst = get_repositories_lst(git_user)
    print(f'Current repositories list:\n{user_repos_lst}')
    print(f'Current repositories amount: {len(user_repos_lst)}')
    print(user_repositories_link)

def save_error_log(error_text):
    errors_logs_json = os.path.join('errors_logs', 'errors_logs.json')
    cur_time_str = str(datetime.datetime.now())

    if not os.path.exists(errors_logs_json):
        with open(errors_logs_json, 'w') as file:
            file.write(json.dumps({}))

    with open(errors_logs_json, 'r') as file:
        errors_dict = json.load(file)

    errors_dict[cur_time_str] = error_text

    with open(errors_logs_json, 'w') as file:
        new_content = json.dumps(errors_dict, indent=4)
        file.write(new_content)

if __name__ == '__main__':
    try:
        run_git_repositories_test()
    except Exception as e:
        print(str(e))
        # error = str(e)
        save_error_log(str(e))




