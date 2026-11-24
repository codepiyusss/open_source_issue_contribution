from fixit.cli import main


def test_dice_command_prints_each_roll_and_total(capsys):
    assert main(["dice", "1d6"]) == 0

    output = capsys.readouterr().out.strip()
    assert output.startswith("rolls: ")
    assert "  total: " in output
