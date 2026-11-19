# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `uuid` command to generate UUIDs (`--count`).
- `slugify` command to turn text into a URL-friendly slug.
- `case` command to convert text between `snake`, `kebab`, `camel` and `pascal` naming.
- `top-words` command to show the most frequent words (`--n`).
- `roman` command to convert numbers to Roman numerals and back.
- `leap-year`, `prime`, `lorem`, `coin` and `bmi` commands.
- `wc --file` to read the text from a file and `wc --json` to print the counts as JSON.
- Global `-v` / `--verbose` option to enable verbose logging.

### Changed

- Running `fixit` without a command now prints the help menu.

### Fixed

- `wc` handles whitespace and other word-count edge cases.
- `password` guarantees the requested character types and validates the length.
- `convert` rejects non-finite values such as `nan` and `inf`.

## [0.1.0] - 2026-10-08

### Added

- Initial release of the `fixit` command line toolbox.
- `wc` command to count words, lines and characters.
- `convert` command for unit conversions (`c2f`, `f2c`, `c2k`, `k2c`, `km2mi`, `mi2km`).
- `password` command to generate a password (`--length`, `--symbols`).
- `json` command to pretty-print JSON.
- `palindrome` command to check if text is a palindrome.
- `reverse` command to reverse the words in a sentence.
- `--version` option.
