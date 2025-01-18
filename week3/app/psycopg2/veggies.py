import psycopg2

conn = psycopg2.connect(
  """
  dbname=week3 user=postgres host=pg port=5432
  """
)

conn.set_session(autocommit=True)

cur = conn.cursor()

cur.execute(
  """
  DROP TABLE IF EXISTS veggies
  """
)

cur.execute(
  """
  CREATE TABLE veggies(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    color TEXT NOT NULL
  )
  """
)

cur.execute(
  """
  INSERT INTO veggies VALUES
  (1, 'carrot', 'orange'),
  (2, 'onion', 'yellow'),
  (3, 'zucchini', 'green'),
  (4, 'squash', 'yellow'),
  (5, 'pepper', 'red'),
  (6, 'onion', 'red')
  """
)

cur.execute(
  """
  SELECT * FROM veggies
  """
)

records = cur.fetchall()

# print(records)

cur.execute(
  """
  SELECT color, name FROM veggies ORDER BY name, color
  """
)

veggie_records = cur.fetchall()

for index, veggie in enumerate(veggie_records):
  print(str(index+1) + ".", veggie[0].capitalize(), veggie[1].capitalize())