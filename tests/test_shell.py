"""Tests for interactive shell"""

import pytest

from fixit.cli import main


def test_shell_exit(monkeypatch):
    """The exit command should close the shell"""
    commands = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    assert main(["shell"]) == 0


def test_multiple_shell_commands(monkeypatch, capsys):
    """Multiple commands should execute in one session"""
    commands = iter(["palindrome radar", "reverse 'hello world'", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    assert main(["shell"]) == 0

    output = capsys.readouterr().out
    assert "True" in output
    assert "world hello" in output

def test_shell_errors(monkeypatch, capsys):
    """Invalid commands should not close the shell"""
    commands = iter(["invalid", "palindrome racecar", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    assert main(["shell"]) == 0
    assert "True" in capsys.readouterr().out

def test_shell_empty_input(monkeypatch, capsys):
    """Empty input should be ignored."""
    commands = iter(["", "palindrome level", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    assert main(["shell"]) == 0
    assert "True" in capsys.readouterr().out