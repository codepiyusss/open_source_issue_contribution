# Git Cheat Sheet for Beginners

A quick reference for common Git commands used when contributing to open source.

## Starting a Project
- `git clone <repository-url>` — Downloads a project from GitHub to your computer.

## Checking & Saving Changes
- `git status` — Shows which files you have changed, added, or not tracked yet.
- `git add <file>` — Prepares specific files to be saved (use `git add .` to add all changed files).
- `git commit -m "message"` — Saves your prepared changes with a short note describing what you did.

## Working with Branches
- `git branch` — Lists all branches on your computer (use `git branch <name>` to create a new branch).

## Syncing with GitHub
- `git pull` — Downloads and updates your local files with the latest changes from GitHub.
- `git push` — Uploads your saved commits to your GitHub repository.

## History & Undoing Mistakes
- `git log` — Shows a list of past commits on your current branch.
- `git stash` — Puts your unfinished changes aside temporarily so you can work on a clean slate.
- `git reset --soft HEAD~1` — Undoes your last commit while keeping all your file changes.
- `git restore --staged <file>` — Removes a file from the prepared list (un-adds it) without losing your edits.
