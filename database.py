from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://zrngbhdjaoychd:5c219d78c07e01b2730c15f72c795b2a44a410be768db23592bb38eca8af10ab@ec2-52-200-28-255.compute-1.amazonaws.com:5432/declggmofabiin",
        echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
