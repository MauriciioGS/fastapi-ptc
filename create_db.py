from database import Base,engine
from models import #Announcement  # Nombre de la tabla a crear

print("Creating database ....")

Base.metadata.create_all(engine)
