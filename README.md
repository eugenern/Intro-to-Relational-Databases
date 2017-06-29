Tournament Tracker
==================

This project makes use of a PostgreSQL-managed database to plan and track matches played in a Swiss-style tournament. The Python functions provided allow users to fill the database with information about players and their matches, as well as form matchups that would be appropriate for the next round according to a Swiss-style format.

----
## Setup
1. Running this project requires that [PostgreSQL](https://www.postgresql.org/download/), [psycopg2](http://initd.org/psycopg/download/), and [Python](https://www.python.org/downloads/) be installed. The code is compatible with both Python 2 and 3.
2. To set up the tournament database, use a command line or shell to go into the `Intro-to-Relational-Databases/vagrant/tournament` directory.
3. Use the command `psql` to start the PostgreSQL interactive terminal.
4. Use the command `\i tournament.sql` to create project's the database and tables. Exit the psql terminal with the command `\q` or by pressing `Ctrl-D`.
5. If you want to run the unit tests that help verify that the Python functions are working correctly, run `tournament_tests.py`.

----
## Usage
Once the database is set up,  you can use the functions in `tournament.py` with a Python script or a Python interpreter.

* To enter information about the players and the matches played into the database, use the functions `registerPlayer(name)` and `reportMatch(winner, loser)`, respectively.
* The database can be cleared of all matches with `deleteMatches()`, or of all players with `deletePlayers()` (note that deleting the players will cause the matches to be deleted as well).
* Before each round, `swissPairings()` can be run to produce a list of possible matchups that would maintain the tournament's Swiss-style format.
* The functions `countPlayers()` and `playerStandings()` provide miscellaneous information about the current state of the database.
