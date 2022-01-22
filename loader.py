from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
# Trae el engine de conexión a la base de datos 
from database import engine
from csv import reader
from database import SessionLocal
import models

# ----------------------------- CARGADOR TABLA HERRAMIENTAS (tools) ---------------------------------------------
# # Leer el archivo csv y convertirlo en una lista de listas
# with open('./CSV_files/Tools.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_tools = list(csv_reader)

# # Ordena la lista de listas de la z-a
# list_of_tools.sort(reverse=True)

# # Motor de encuadre
# metadata = MetaData(engine)

# # Conecta con las tablas de la DB
# tool_table = Table('tools', metadata, autoload=True)

# # Crea un objeto INSERT
# ins = tool_table.insert()

# # Recorre la lista de listas o lista de herramientas e inserta cada una a la DB
# for i in range(len(list_of_tools)):
#     tool=list_of_tools.pop()

#     # Debe tener 4 registros, 1 por cada columna sin contar el id
#     if(len(tool)==4):

#         # Vincula los datos a insertar
#         ins = ins.values(title=tool[0],description=tool[1],image=tool[2],link=tool[3])
        
#         # Hace la conexión
#         conn = engine.connect()

#         # Ejecuta la sentencia Insert
#         conn.execute(ins)
#     else:
#         print("El registro de Herramienta no tiene los campos necesarios, verifique el registro en el archivo .csv")
    
# ----------------------------- CARGADOR TABLA CURSOS (courses) ---------------------------------------------
# with open('./CSV_files/Courses.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_courses = list(csv_reader)

# list_of_courses.sort(reverse=True)

# metadata = MetaData(engine)
# course_table = Table('course', metadata, autoload=True)
# ins = course_table.insert()

# for i in range(len(list_of_courses)):
#     course=list_of_courses.pop()
#     if(len(course)==4):
#         ins = ins.values(title=course[0],description=course[1],date=course[2],link=course[3])
#         conn = engine.connect()
#         conn.execute(ins)
#     else:
#         print("El registro de Curso no tiene los campos necesarios, verifique el registro en el archivo .csv")
# ----------------------------- CARGADOR TABLA TALLERES (workshops) ---------------------------------------------
# with open('./CSV_files/Workshops.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_workshops = list(csv_reader)

# list_of_workshops.sort(reverse=True)

# metadata = MetaData(engine)
# workshop_table = Table('taller', metadata, autoload=True)
# ins = workshop_table.insert()

# for i in range(len(list_of_workshops)):
#     workshop=list_of_workshops.pop()

#     if(len(workshop)==4):
#         ins = ins.values(title=workshop[0],description=workshop[1],date=workshop[2],liga=workshop[3])
#         conn = engine.connect()
#         conn.execute(ins)
#     else:
#         print("El registro de Taller no tiene los campos necesarios, verifique el registro en el archivo .csv")

# ----------------------------- CARGADOR TABLA MATERIALES (materials) ---------------------------------------------
# with open('./CSV_files/Material.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_material = list(csv_reader)

# list_of_material.sort(reverse=True)

# metadata = MetaData(engine)
# material_table = Table('materials', metadata, autoload=True)
# ins = material_table.insert()

# for i in range(len(list_of_material)):
#     material=list_of_material.pop()

#     if(len(material)==2):        
#         ins = ins.values(title=material[0],url =material[1])
#         conn = engine.connect()
#         conn.execute(ins)
#     else:
#         print("El registro de Material no tiene los campos necesarios, verifique el registro en el archivo .csv")

# ----------------------------- CARGADOR TABLA Videos (videos) ---------------------------------------------
# with open('./CSV_files/Videos.csv', 'r') as csv_file:
#     csv_reader = reader(csv_file)
#     list_of_videos = list(csv_reader)

# metadata = MetaData(engine)
# videos_table = Table('videos', metadata, autoload=True)
# ins = videos_table.insert()
# db = SessionLocal()

# id_material = 0
# for i in range(len(list_of_videos)):    
#     video=list_of_videos.pop()

#     if(len(video)==2):   
#         print(id_material,video)
#         ins = ins.values(id_material=id_material,title=video[0],code=video[1])
#         conn = engine.connect()
#         conn.execute(ins)
#     else:
#         if(len(video)==1):            
#             search = "%{}%".format(video[0])
#             material = db.query(models.Material).filter(models.Material.title.like(search)).first()
#             id_material=material.id
#         else:
#             print("El registro de Video no tiene los campos necesarios, verifique el registro en el archivo .csv")

# ----------------------------- CARGADOR TABLA TEMAS (topics) ---------------------------------------------
with open('./CSV_files/Topic.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    list_of_topics = list(csv_reader)

metadata = MetaData(engine)
topics_table = Table('topics', metadata, autoload=True)
ins = topics_table.insert()
db = SessionLocal()

id_material = 0
for i in range(len(list_of_topics)):    
    topic=list_of_topics.pop()

    if(len(topic)==2):   
        print(id_material,topic)
        ins = ins.values(id_material=id_material,title=topic[0],url_notes=topic[1])
        conn = engine.connect()
        conn.execute(ins)
    else:
        if(len(topic)==1):            
            search = "%{}%".format(topic[0])
            material = db.query(models.Material).filter(models.Material.title.like(search)).first()
            id_material=material.id
        else:
            print("El registro de Video no tiene los campos necesarios, verifique el registro en el archivo .csv")