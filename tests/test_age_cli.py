from datetime import date

from fixit.cli import main


def test_age_command_prints_completed_years(capsys, monkeypatch):
    monkeypatch.setattr("fixit.dates.date", type("FixedDate", (date,), {"today": classmethod(lambda cls: date(2026, 5, 17))}))

    assert main(["age", "2000-05-17"]) == 0
    assert capsys.readouterr().out.strip() == "26"
