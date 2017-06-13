# "Database code" for the DB Forum.

import datetime, psycopg2

conn = psycopg2.connect("dbname=forum")
cur = conn.cursor()

def get_posts():
  """Return all posts from the 'database', most recent first."""
  cur.execute("select * from posts order by time desc;")
  return ((content, time) for (content, time, post_id) in cur.fetchall())

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  cur.execute("insert into posts (content) values (%s);", (content,))
  conn.commit()

# cur.close()
# conn.close()