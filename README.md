# Dev Productivity Tracker

A fast command-line tool for tracking your work. Tasks, time, goals, streaks and a
daily journal all live in one SQLite file on your own machine. There is no account,
no server and no internet connection needed.

```text
$ python -m src.main list
[3] Read Python book | low | learning | Pending
[2] Fix login bug | medium | work | Pending | #bugfix
[1] Write project docs | high | work | Pending | due 2026-12-01 | #docs #work

$ python -m src.main complete 2
Task completed.
Daily goal: [###-------] 1/3 (33.3%) - 2 to go
Streak: 1 day. Keep it going tomorrow!
```

## What it does

| Area | What you can do |
|---|---|
| **Review** | Look back over the last week: what you finished, time tracked, goals hit |
| **Today** | One command that shows overdue and due tasks, your timer, goals and streak |
| **Tasks** | Add, edit, show, complete, reopen and delete tasks with priority, category, description and due date |
| **Recurring tasks** | Repeat a task daily, weekly or monthly; completing it creates the next one |
| **Dependencies** | Make a task wait for others, and see what is ready to start |
| **Notes** | Attach short timestamped notes to any task |
| **Tags and search** | Give tasks several tags, then search, filter and sort your list |
| **Reminders** | See overdue tasks and tasks due soon |
| **Time tracking** | Start and stop a timer, log time by hand, and see totals by day, category and task |
| **Goals** | Set a daily and a weekly target and watch your progress |
| **Streaks** | Track how many days in a row you complete something |
| **Analytics** | Completion rates by priority, category and tag, how long tasks have waited, and short insights |
| **Journal** | Write a daily entry (achievements, challenges, next steps), then search it by text or date range |
| **Search** | Find tasks and journal entries by any words, best matches first |
| **Health check** | `doctor` checks your database and setup for problems |
| **Backups** | Save, verify and restore snapshots of your whole database |
| **Import and export** | Export tasks to CSV or JSON, and import tasks from CSV |

Your data stays local. Existing databases are upgraded automatically when you update
the tool, and no data is lost.

## Getting started

You need Python 3. The project is developed and tested on Python 3.12.

```bash
git clone https://github.com/codepiyusss/dev-productivity-tracker.git
cd dev-productivity-tracker

python -m venv .venv
# Windows:        .venv\Scripts\activate
# macOS / Linux:  source .venv/bin/activate

pip install -r requirements.txt
```

Run every command from the project folder:

```bash
python -m src.main add "Write project docs" --priority high --due-date 2026-12-01 --tags docs,work
python -m src.main list
python -m src.main --help
```

Add `--help` after any command to see its options, for example
`python -m src.main timer --help`.

## Using it

Every example starts with `python -m src.main`. It is shortened to `tracker` below
for readability.

### Your day at a glance

```bash
tracker today
```

```text
Today: 2026-11-10 (Tuesday)

Overdue (1):
  [3] Pay rent - due 2026-11-01

Due today (1):
  [5] Weekly report (high priority)

Pending: 6 (5 ready to start, 1 blocked)

Daily goal: [###-------] 1/3 (33.3%) - 2 to go

Completed today: 1
Streak: 2 days
```

### Looking back

```bash
tracker review                # the last 7 days
tracker review --days 30
```

```text
Review: 2026-11-04 to 2026-11-10 (7 days)

Completed: 9 tasks (created: 12)
Active days: 5 of 7
Busiest day: 2026-11-10 (4 tasks)
Activity: [-#-#####] (oldest to today)
Time tracked: 11h 30m (work 8h, learning 3h 30m)
Daily goal met on 4 of 7 days (target: 2 per day)
Journal: written on 5 days
Streak: 3 days
```

### Tasks

```bash
tracker add "Fix login bug" --priority medium --category work --tags bugfix
tracker list                                  # newest first
tracker list --status pending --sort due_date --ascending
tracker list --search login --tag work        # --tag can be repeated
tracker list --overdue                        # pending tasks past their due date
tracker list --due-today
tracker list --due-within 7                   # due in the next 7 days
tracker list --no-due-date
tracker list --json                           # machine-readable output (also: show 3 --json, today --json)
tracker show 2                                # full details of one task
tracker edit 2 --priority high --due-date 2026-12-05
tracker edit 2 --clear-due-date
tracker complete 2
tracker reopen 2
tracker delete 2                              # asks first; add --yes to skip
```

- Priorities are `low`, `medium` or `high`.
- Due dates must be real `YYYY-MM-DD` dates. Tasks past their date show `(OVERDUE)`.

### Recurring tasks

```bash
tracker add "Weekly report" --due-date 2026-11-20 --repeat weekly
tracker complete 1                            # creates the next one, due 2026-11-27
tracker edit 1 --repeat monthly
tracker edit 1 --no-repeat
```

- Repeat rules are `daily`, `weekly` and `monthly`, and a repeating task needs a due date.
- Completing a repeating task creates a new pending copy (same title, priority, category and tags)
  with the next due date. If you finish late, the new due date is the next regular date after today,
  so you do not get a pile of overdue copies.
- Monthly repeats move to the end of short months (Jan 31 becomes Feb 28) and keep that day afterwards.

### Dependencies

```bash
tracker depend add 3 2                        # task 3 cannot be finished before task 2
tracker depend remove 3 2
tracker depend list 3                         # what it waits for, and what waits for it
tracker list --ready                          # pending tasks nothing is blocking
tracker list --blocked                        # pending tasks waiting on unfinished tasks
tracker complete 3 --force                    # finish a blocked task anyway
```

- A task can wait for several others. Circular chains (A waits for B, B waits for A) are rejected.
- Only unfinished blockers hold a task up. Once they are completed the task is ready.
- Blocked tasks are marked `BLOCKED by 2` in `list`, and completing a blocker tells you which tasks were freed up.

### Notes

```bash
tracker note add 3 Remember to check the CLI examples
tracker note list 3
tracker note delete 7                         # asks first; add --yes to skip
tracker show 3                                # notes appear at the bottom
```

Notes are timestamped, kept with the task, deleted with it, and included in backups.

### Tags

```bash
tracker add "Write docs" --tags docs,work
tracker tag add 1 urgent
tracker tag remove 1 urgent
tracker tag list                              # every tag with its task count
tracker tag rename bug defect                 # rename on every task
tracker tag merge fix bugfix                  # move all tasks from one tag to another
tracker tag delete old-tag                    # asks first; add --yes to skip
tracker list --tag docs
```

Tags are lowercase, so `Work` and `work` are the same tag.

### Reminders

```bash
tracker reminders                             # overdue and due within 7 days
tracker reminders --days 14
```

### Time tracking

```bash
tracker timer start 1                         # only one timer runs at a time
tracker timer status
tracker timer stop
tracker timer log 2 1h30m --date 2026-11-08   # add time you did not track live
tracker timer list --days 7
tracker timer summary                         # by day, category and task
tracker timer delete 4                        # remove a mistaken entry
```

- Durations can be written as `45`, `45m`, `1h30m`, `1.5h` or `1:30`. A bare number means minutes.
- A timer that has been running for more than 12 hours is flagged, in case you forgot it.
- Completing a task stops its timer automatically.

### Goals and streaks

```bash
tracker goal set daily 3                      # complete 3 tasks per day
tracker goal set weekly 15                    # weeks run Monday to Sunday
tracker goal show
tracker goal clear weekly
tracker streak
```

```text
Current streak: 5 days (completed a task today)
Longest streak: 9 days (2026-10-01 to 2026-10-09)
Active days: 21
Last 14 days: [--##-#####--####] (oldest to today)
```

A streak counts days with at least one completed task. It stays alive until the end of
the next day, so it does not reset just because you have not finished anything yet today.
In the activity strip, `#` is a day with a completed task and `-` is a day without.

### Analytics and reports

```bash
tracker stats                                 # quick overview
tracker stats --detailed                      # full breakdown with insights
tracker stats --json                          # machine-readable
tracker report --output my_report.txt         # save the detailed report to a file
```

The detailed view includes completion rates by priority and tag, overdue and upcoming
tasks, goal progress, streaks, time tracked in the last 7 days, and a few plain-language
insights.

### Journal

```bash
tracker journal add --achievements "Shipped time tracking" --challenges "Edge cases" --next-steps "Write docs"
tracker journal list --limit 5
tracker journal list --search tracking --from-date 2026-11-01 --to-date 2026-11-30
tracker journal show 2026-11-08
tracker journal export --format md --output my_journal.md   # also json or csv
tracker journal update 2026-11-08 --achievements "Shipped and tested time tracking"
tracker journal delete 2026-11-08
```

### Import and export

```bash
tracker export --format csv --output exports/tasks.csv
tracker export --format json --status pending --tag work
tracker export --include-time                 # adds a time_spent_seconds column

tracker import tasks.csv --dry-run            # check the file without saving
tracker import tasks.csv
tracker import tasks.json                     # JSON files work too (round-trips with export)
```

- Only a `title` column (or key, in JSON) is required to import. Optional columns are `description`,
  `priority`, `category`, `due_date`, `completed` (yes/no), `recurrence` and `tags` (separated by `;` or `,`).
- Files made by `export` can be imported again.
- Invalid rows are skipped and reported by line number. Tasks that already exist
  (same title, category and due date) are skipped unless you pass `--allow-duplicates`.

### Search

```bash
tracker search python docs            # all words must match
tracker search login --tasks --limit 5
tracker search "deploy" --journal
```

Searches task titles, tags, categories and descriptions, and journal entries. Title matches rank first,
and journal results show a short snippet around the match.

### Health check

```bash
tracker doctor
```

Checks that the database opens and passes integrity checks, that all tables exist, and looks for odd
data (invalid due dates, repeating tasks without due dates, a forgotten timer), plus how old your
newest backup is. It works even on a damaged database and exits with code 1 if it finds a real problem.

### Cleaning up old tasks

```bash
tracker purge --older-than 90 --dry-run       # preview only
tracker purge --older-than 90                 # backs up first, then asks before deleting
```

`purge` deletes completed tasks that were finished at least that many days ago, together with their time
entries and links. A `before-purge` backup is saved first, so you can undo it with `backup restore`.

### Backups

```bash
tracker backup create                         # saves to data/backups/
tracker backup create --label before-upgrade --keep 10
tracker backup list
tracker backup verify data/backups/productivity-20261110-153005.db
tracker backup restore data/backups/productivity-20261110-153005.db
tracker backup prune --keep 5
tracker import tasks.csv --backup             # saves a copy first, so you can undo an import
```

- Backups are consistent snapshots and are checked for problems before they are kept.
- `restore` always saves your current data as a `pre-restore` backup first, then asks for confirmation
  (use `--yes` to skip). Safety copies are never deleted by `prune`.
- Backups contain all of your data, so keep them somewhere private.

## Where your data is stored

Everything is saved in `data/productivity.db`, created the first time you run a command.
The path is relative to the folder you run the tool from, so run it from the project
folder. To use a different file, put `--db` before the command:

```bash
tracker --db work.db list
```

Commands exit with code 0 on success and 1 on failure (for example, a task that does not
exist), so they can be used in scripts.

## Running the tests

```bash
python -m pytest
```

## Project layout

```text
src/
  main.py          command-line interface
  models/task.py   the Task data model
  database.py      SQLite storage and automatic upgrades
  tasks.py         task management
  task_filters.py  search, filter and sort
  analytics.py     statistics and insights
  reports.py       text reports
  goals.py         daily and weekly goals
  streaks.py       completion streaks
  timetracking.py  timers and time summaries
  journal.py       daily journal
  exporter.py      CSV and JSON export
  importer.py      CSV import
  utils.py         validation and formatting helpers
tests/             pytest test suite
docs/              architecture, database, features, installation, testing
```

More detail is in the [`docs/`](docs/) folder, and the history of changes is in
[`CHANGELOG.md`](CHANGELOG.md).

## Contributing

Issues and pull requests are welcome. Please run `python -m pytest` before opening a pull
request, and add tests for new behaviour.
