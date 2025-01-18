from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres@pg:5432/week3')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Veggie(Base):
  __tablename__ = "veggies"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  color = Column(String, nullable=False)

  def formatted_name(self):
    return self.color.capitalize() + " " + self.name.capitalize()


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
  {'name': 'carrot', 'color': 'orange'},
  {'name': 'onion', 'color': 'yellow'},
  {'name': 'zucchini', 'color': 'green'},
  {'name': 'squash', 'color': 'yellow'},
  {'name': 'pepper', 'color': 'red'},
  {'name': 'onion', 'color': 'red'}
]

veggie_objects = []

for item in seed_data:
  veggie = Veggie(name=item["name"], color=item["color"])
  veggie_objects.append(veggie)


session = Session()
session.bulk_save_objects(veggie_objects)
session.commit()


session = Session()
veggies = session.query(Veggie).all()

for veggie in veggies:
  print(veggie.name, veggie.color)


veggies = session.query(Veggie).order_by(
  Veggie.name, Veggie.color).all()


for i, v in enumerate(veggies):
  print(str(i+1) + ". " + v.formatted_name())