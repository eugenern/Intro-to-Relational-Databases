-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- drop the current tournament database to start fresh
drop database if exists tournament;

-- the tournament database
create database tournament;
\c tournament;

-- table of players (id and name)
create table players (
	id serial primary key,
	name text
);

-- table of match results between players
create table matches (
	id serial primary key,
	winner integer references players (id),
	loser integer references players (id)
);