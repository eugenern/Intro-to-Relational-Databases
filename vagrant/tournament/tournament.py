#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cur = db.cursor()
        return db, cur
    except:
        print("Nope")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cur = connect()

    query = "TRUNCATE matches;"
    cur.execute(query)

    db.commit()
    cur.close()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cur = connect()

    query = "TRUNCATE players CASCADE;"
    cur.execute(query)

    db.commit()
    cur.close()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cur = connect()

    query = "SELECT COUNT(*) FROM players;"
    cur.execute(query)
    count = cur.fetchone()[0]

    cur.close()
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, cur = connect()

    query = "INSERT INTO players (name) VALUES (%s);"
    param = (name,)
    cur.execute(query, param)

    db.commit()
    cur.close()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or
    a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cur = connect()

    # left join players table with matches table twice so that
    # both won and lost matches for a player can be grouped
    query = ("SELECT players.id, players.name, COUNT(w.winner) AS wins, "
             "COUNT(w.winner) + COUNT(l.loser) AS games "
             "FROM players LEFT JOIN matches AS w ON players.id = w.winner "
             "LEFT JOIN matches AS l ON players.id = l.loser "
             "GROUP BY players.id "
             "ORDER BY wins DESC, games;")
    cur.execute(query)
    standings = cur.fetchall()

    cur.close()
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cur = connect()

    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    param = (winner, loser)
    cur.execute(query, param)

    db.commit()
    cur.close()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, cur = connect()

    standings = playerStandings()

    # try to account for some situations that this function doesn't cover
    if not standings:
        raise Exception("Must have players!")
    if len(standings) % 2 != 0:
        raise Exception("Must have an even number of players!")
    if any(player[3] != standings[-1][3] for player in standings):
        raise Exception("Everyone must have played the same number of games!")

    # convert standings to pairings by taking two players at a time and
    # concatenating their ids and names into single tuples
    pairings = [(standings[i][0:2] + standings[i+1][0:2])
                for i in range(0, len(standings), 2)]

    cur.close()
    db.close()
    return pairings
