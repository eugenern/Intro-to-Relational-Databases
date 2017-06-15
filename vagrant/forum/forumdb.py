# "Database code" for the DB Forum.

import datetime, psycopg2, bleach

def get_posts():
  """Return all posts from the 'database', most recent first."""
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  cur.execute("select * from posts order by time desc;")
  return ((bleach.clean(content), time) for (content, time, post_id) in cur.fetchall())

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  conn = psycopg2.connect("dbname=forum")
  cur = conn.cursor()
  cur.execute("insert into posts (content) values (%s);", (bleach.clean(content),))
  conn.commit()
