from time import sleep

from github import Github
from github import Auth


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
        print(f'Repositories list updated: {user_repos_lst}')
        print(f'{repo_name} has been created  & presents in the repositories list')
        print(f'New repositories` amount: {len(user_repos_lst)}')
    else:
        print('ERROR')


def delete_test_repository(git_user, repo):
    repo.delete()
    print(f'\n\n✅ Repository successfully deleted: {repo.name}')

git_login = 'ReptiloidAnunak'
git_password = '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'
test_repo_name = 'test_repo_1'


def run_git_repositories_test():
    git_user = get_git_user(git_login, git_password)
    user_repositories_link = git_user.html_url + '?tab=repositories'

    user_repos_lst = get_repositories_lst(git_user)
    print(f'\nCurrent repositories list:\n{user_repos_lst}')
    print(f'Current repositories amount: {len(user_repos_lst)}')
    print(user_repositories_link)

    new_repo = create_new_repository(git_user, test_repo_name)
    sleep(10)
    check_new_repo_in_repos_lst(git_user, new_repo.name)
    print(user_repositories_link)
    sleep(5)

    delete_test_repository(git_user, new_repo)
    user_repos_lst = get_repositories_lst(git_user)
    print(f'Current repositories list:\n{user_repos_lst}')
    print(f'Current repositories amount: {len(user_repos_lst)}')
    print(user_repositories_link)

run_git_repositories_test()




