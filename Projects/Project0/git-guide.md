# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Used to target and create a copy of a repository.
  - `git clone *repo*`
- add
  - Used to add file that will be pushed to repo.
  - `git add *filename*` 
- rm
  - Used to remove tracked files from the Git index  .
  - `git rm`
- commit
  - Captures a snapshot of currently staged changes.
  -  `git commit -m "message"` 
- push
  - Uploads local content to remote repository.
  - `git push`  
- fetch
  - Downloads commits, files, and refs from a remote repository into your local repository.
  -  `git fetch` 
- merge
  - Used to join multiple development histories together.
  - `git merge *branch name*`
- pull
  - Used to copy a remote repository to your local repository
  - `git pull *repository*`
- branch
  - Used to manage branches
  - `git branch`
- checkout
  - Used to switch branches and restore working tree files
  - `git checkout *branch*`
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
  - Contains information that is necessary for the project and all information relating commits, remote repository address, etc. 
- .gitignore file
  - Lists intentionally untracked files to ignore 
- ~~.git/hooks~~

## GitHub

- Pull requests
  - An event in Git where a contributor asks a maintainer of a Git repository to review code they want to merge into a project.
- SSH authentication to repositories
  - Used to maintain the security of repositories
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
