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

class Course(Base):
  __tablename__='course'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  date = Column(Text, nullable=False)
  link = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Course title={self.title} description={self.description} date={self.date} link={self.link}>"

class Taller(Base):
  __tablename__='taller'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  description = Column(Text, nullable=False)
  date = Column(Text, nullable=False)
  liga = Column(Text, nullable=False)
  
  def __repr__(self):
    return f"<Taller title={self.title} description={self.description} date={self.date} link={self.link}>"

class Material(Base):
  __tablename__='materials'
  id = Column(Integer, primary_key=True)
  title = Column(Text, nullable=False)
  url = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Material title={self.title} url={self.url} >"

class Video(Base):
  __tablename__='videos'
  id = Column(Integer, primary_key=True)
  id_material = Column(Integer, nullable=False)
  title = Column(Text, nullable=False)
  code = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Video id_material={self.id_material} title={self.title} code={self.code} >"

class Handbook(Base):
  __tablename__='handbooks'
  id = Column(Integer, primary_key=True)
  id_material = Column(Integer, nullable=False)
  title = Column(Text, nullable=False)
  url_handbook = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Handbook id_material={self.id_material} title={self.title} url_handbook={self.url_handbook}>"

class Topic(Base):
  __tablename__='topics'
  id = Column(Integer, primary_key=True)
  id_material = Column(Integer, nullable=False)
  title = Column(Text, nullable=False)
  url_notes = Column(Text, nullable=False)

  def __repr__(self):
    return f"<Topic id_material={self.id_material} title={self.title} url_notes={self.url_notes}>"

# Feedback
class Feedback(Base):
  __tablename__='feedback'
  id = Column(Integer, primary_key=True)
  score = Column(Text, nullable=False)
  comments = Column(Text, nullable=False)

  def __repr__(self) -> str:
      return f"Feedback score={self.score} comments={self.comments}>"

# Consultancies
class Consultancies(Base):
  __tablename__='consultancies'
  id = Column(Integer, primary_key=True)
  score = Column(Text, nullable=False)
  comments = Column(Text, nullable=False)

  def __repr__(self) -> str:
      return f"Consultancies score={self.score} comments={self.comments}>"