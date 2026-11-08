import subprocess
import sys


def test_module_entry_point_palindrome():
    result = subprocess.run(
        [sys.executable, "-m", "fixit", "palindrome", "level"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == "True"
