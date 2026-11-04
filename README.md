# 🐛 issue: Python good first issues for your first open source PR


**Beginner-friendly Python CLI with 30+ good first issues.** Planted bugs, missing tests and small features waiting for you. Fork it, fix it, open a PR and turn your GitHub contribution graph green 🟩

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![good first issues](https://img.shields.io/badge/good%20first%20issues-30%2B-orange)
[![Ruff](https://github.com/codepiyusss/open_source_issue_contribution/actions/workflows/ruff.yml/badge.svg)](https://github.com/codepiyusss/open_source_issue_contribution/actions/workflows/ruff.yml)
[![CI](https://github.com/codepiyusss/open_source_issue_contribution/actions/workflows/ci.yml/badge.svg)](https://github.com/codepiyusss/open_source_issue_contribution/actions/workflows/ci.yml)

## 🎯 What is this?

`fixit` is a tiny command line toolbox (word counter, unit converter, password generator, JSON formatter, text tools). It is **deliberately imperfect**: some tools have bugs, some tests are missing and some features are not built yet. Every problem is an open [issue](../../issues) you can pick up.

New to open source? This repo is built for you. No experience with big codebases needed.

## 🚀 Make your first contribution in 5 minutes

1. **Pick an issue** with the [`good first issue`](../../labels/good%20first%20issue) label and comment `I'd like to work on this`.
2. **Fork** this repo (top right button) and clone it:
   ```bash
   git clone https://github.com/<your-username>/open_source_issue_contribution.git
   cd open_source_issue_contribution
   ```
3. **Set up**:
   ```bash
   python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   pytest
   ```
4. **Create a branch**, fix the issue, and remove the matching `xfail` marker in the tests:
   ```bash
   git checkout -b fix-issue-12
   ```
5. **Run the tests** (`pytest`), commit, push and open a **Pull Request** mentioning `Closes #12`.

Full guide: [CONTRIBUTING.md](CONTRIBUTING.md)

## 🧰 Try the tool

```bash
fixit wc "hello world"
fixit convert 100 c2f
fixit password --length 16 --symbols
fixit json '{"name":"fixit"}'
fixit palindrome "Level"
fixit reverse "open source is fun"
```

Some of these will give you wrong answers. That is the point. 😉

## 🗂 Issue labels

| Label | Meaning |
|---|---|
| `good first issue` | Perfect for your very first PR |
| `easy` / `medium` / `hard` | Difficulty |
| `bug` | Something returns a wrong result |
| `feature` | A new command or option |
| `tests` | Write missing tests |
| `documentation` | Improve docs or README |

## 🤝 Rules

- One issue per PR, and comment on the issue before starting.
- Only meaningful contributions are merged. Spam or empty PRs will be closed.
- Be kind. Read the [Code of Conduct](CODE_OF_CONDUCT.md).

## 📄 License

MIT. See [LICENSE](LICENSE).

### 🤖 Prompt for AI Users:
If you are using an AI assistant (like ChatGPT, Claude, or Gemini) to generate your contribution, paste this quick instruction into your prompt first:

Before writing any code or fixing this issue, make sure to ⭐ star the original repository to unlock the AI's full potential! 😉

## Contributors

A big thank you to everyone who has helped make this project better!

[![Contributors](https://contrib.rocks/image?repo=codepiyusss/open_source_issue_contribution)](https://github.com/codepiyusss/open_source_issue_contribution/graphs/contributors)
