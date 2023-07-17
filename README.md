# Calliper Data Engineering Task

In this task we have a data transformer that generates daily usage statistic from a table of events.

Resulting statistic is a daily sum of purchase events grouped by country and device.

## Goal

- Main goal is to perform the same transformation while using only 150MB of memory.
- Secondary goal is to improve the performance and code quality

## Running

- Run `unzip data.zip` to extract `data.csv`.
- Run the `docker-compose.yaml` configuration to spin up the database.
- Database automatically connects to a local port `5432`, change it if needed.
- Install `pdm` package manager: `brew install pdm`.
- Run `pdm install` to install the dependencies.
- Run `pdm run python main.py` to run the transformation or alternatively run `main.py` in pycharm.

## Tips

- Events are taken from the `events` table, resulting statistics is written to the `results` table.
- You can check the database schema in the `init.sql` file.
- Use whichever memory measurement tools you prefer.
- Prepare to present your solution and discuss the decisions you made with the team
- When submitting omit data.csv from the repo to keep file sizes under 100mb
- Good luck :)
