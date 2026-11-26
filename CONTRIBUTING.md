# Contributing to issue

Thanks for helping! This guide walks you through your first pull request.

## 1. Find an issue
- Browse [open issues](../../issues) and filter by `good first issue`.
- Comment on the issue to claim it. Wait for a maintainer to assign it to you.
- One person per issue. If there is no activity for 5 days, it may be reassigned.

## 2. Set up locally
```bash
git clone https://github.com/<your-username>/issue.git
cd issue
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -e ".[dev]"
pytest
```
All tests should pass (known bugs show as `xfail`).

New to Git? Check out the [Git Cheat Sheet](docs/GIT_CHEATSHEET.md) for a quick command reference.

## Pre-commit hooks

Install pre-commit:

```bash
pip install pre-commit
```

Install the git hooks:

```bash
pre-commit install
```

Run the hooks on all files:

```bash
pre-commit run --all-files
```

## 3. Make your change
```bash
git checkout -b fix-short-description
```
- Fix the bug or build the feature.
- **Remove the `@pytest.mark.xfail` marker** from the test that covers your issue.
- Add tests for new features.
- Keep changes small and focused on one issue.

## 4. Check your work
```bash
pytest
```

## 5. Commit and push
Use a clear message:
```bash
git commit -m "Fix: ignore extra spaces in count_words (closes #3)"
git push origin fix-short-description
```

## 6. Open a Pull Request
Fill in the PR template and write `Closes #<issue-number>`. A maintainer will review it, usually within a few days.

## Style
- Python 3.8+, follow PEP 8.
- Add docstrings to new functions.
- Don't reformat code unrelated to your issue.

## Not allowed
- Whitespace-only or empty PRs.
- Changing many unrelated files.
- AI-generated bulk PRs with no understanding of the change.

Questions? Ask in the issue thread. No question is too basic. 💚
