from sqlalchemy.sql.sqltypes import Date
from database import Base
from sqlalchemy import Text,Integer,Column

class Tool(Base):
  __tablename__='tools'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  image = Column(Text, nullable=False)
  link = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Tool title={self.title} description={self.description} image={self.image} link={self.link}>"

class Material(Base):
  __tablename__='materials'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  conceptos = Column(Text, nullable=False)
  manuales = Column(Text, nullable=False)
  videos = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Material title={self.title} description={self.description} conceptos={self.conceptos} manuales={self.manuales} videos={self.videos}>"

class Curso(Base):
  __tablename__='materials'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  date = Column(Date, nullable=False)
  link = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Cursos title={self.title} description={self.description} date={self.date} link={self.link}>"

class Taller(Base):
  __tablename__='materials'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  date = Column(Date, nullable=False)
  liga = Column(Text, nullable=False)
  

  def __repr__(self):
    return f"<Talleres title={self.title} description={self.description} date={self.date} li:nk={self.link}>"