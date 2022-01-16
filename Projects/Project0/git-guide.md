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
  - Used to target and create a copy of a repository
  - `git clone *repo*`
- add
  - Used to add file that will be pushed to repo
  - `git add *filename*` 
- rm
  - Used to remove tracked files from the Git index  
  - `git rm`
- commit
  - Captures a snapshot of currently staged changes
  -  `git commit -m "message"` 
- push
  - Uploads local content to remote repository
  - `git push`  
- fetch
  - Downloads commits, files, and refs from a remote repository into your local repository.
  -  `git fetch` 
- merge
- pull
- branch
- checkout
- ~~init~~
- ~~remote~~

## git files & folders

- .git folder
- .gitignore file
- ~~.git/hooks~~

## GitHub

- Pull requests
- SSH authentication to repositories
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)
