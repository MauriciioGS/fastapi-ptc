from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://admin:9xQKGUXlZjwPXh3jMKlWWfV0pfJEiyhY@dpg-cevi2j94reb4eatsep20-a.oregon-postgres.render.com/testdb_yr6w",
        echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
