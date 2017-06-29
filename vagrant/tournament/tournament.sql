-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- drop the current tournament database to start fresh
DROP DATABASE IF EXISTS tournament;

-- create and connect to the tournament database
CREATE DATABASE tournament;
\c tournament;

-- table of players (id and name)
CREATE TABLE players (
	id serial PRIMARY KEY,
	name text
);

-- table of match results between players
CREATE TABLE matches (
	id serial PRIMARY KEY,
	winner integer REFERENCES players (id),
	loser integer REFERENCES players (id)
);