from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
import models

app = FastAPI()

class Tool(BaseModel):
    id:int
    title:str
    description:str
    image:str
    link:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/tools',response_model=List[Tool],
        status_code=status.HTTP_200_OK)
def get_all_tools():
    tools = db.query(models.Tool).all()
    return tools

@app.get('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def get_an_tool(tool_id:int):
    tool = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    return tool

@app.post('/tools',response_model=Tool,
        status_code=status.HTTP_201_CREATED)
def create_an_tool(tool:Tool):

    db_item = db.query(models.Tool).filter(models.Tool.title == tool.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Tool already exists")

    new_tool = models.Tool(
            title=tool.title,
            description = tool.description,
            image = tool.image,
            link = tool.link
            )

    db.add(new_tool)
    db.commit()

    return new_tool

@app.put('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def update_an_tool(tool_id:int,tool:Tool):
    tool_to_update = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    tool_to_update.title = tool.title
    tool_to_update.description = tool.description
    tool_to_update.image = tool.image
    tool_to_update.link = tool.link

    db.commit()

    return tool_to_update

@app.delete('/tool/{tool_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def delete_tool(tool_id:int):
    tool_to_delete = db.query(models.Tool).filter(models.Tool.id == tool_id).first()
    db.delete(tool_to_delete)
    db.commit()

    if tool_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return tool_to_delete

# Material CRUD -----------------------------------------------------------------------------------------
class Material(BaseModel):
    id:int
    title:str
    description:str
    conceptos:str
    manuales:str
    videos:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/material',response_model=List[Material],
        status_code=status.HTTP_200_OK)
def get_all_materials():
    materials = db.query(models.Material).all()
    return materials

@app.get('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def get_an_material(material_id:int):
    material = db.query(models.Material).filter(models.Material.id == material_id).first()
    return material

@app.post('/materials',response_model=Material,
        status_code=status.HTTP_201_CREATED)
def create_an_material(material:Material):

    db_item = db.query(models.Material).filter(models.Material.title == material.title).first()
    if db_item is not None:
        raise HTTPException(status_code=400, details="Material already exists")

    new_material = models.Material(
            title=material.title,
            description = material.description,
            conceptos = material.conceptos,
            manuales = material.manuales,
            videos = material.videos
            )

    db.add(new_material)
    db.commit()

    return new_material

@app.put('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def update_an_material(material_id:int,material:Material):
    material_to_update = db.query(models.Material).filter(models.Material.id == material_id).first()
    material_to_update.title = material.title
    material_to_update.description = material.description
    material_to_update.conceptos = material.conceptos
    material_to_update.manuales = material.manuales
    material_to_update.videos = material.videos

    db.commit()

    return material_to_update

@app.delete('/material/{material_id}', response_model=Material,
        status_code=status.HTTP_200_OK)
def delete_material(material_id:int):
    material_to_delete = db.query(models.Material).filter(models.Material.id == material_id).first()
    db.delete(material_to_delete)
    db.commit()

    if material_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return material_to_delete

# Cursos CRUD -----------------------------------------------------------------------------------------
class Curso(BaseModel):
    id:int
    title:str
    description:str
    date:str
    link:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/cursos',response_model=List[Curso],
        status_code=status.HTTP_200_OK)
def get_all_cursos():
    cursos = db.query(models.Curso).all()
    return cursos

@app.get('/curso/{curso_id}', response_model=Curso,
        status_code=status.HTTP_200_OK)
def get_an_curso(curso_id:int):
    curso = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    return curso

@app.post('/curso',response_model=Curso,
        status_code=status.HTTP_201_CREATED)
def create_an_curso(curso:Curso):

    db_item = db.query(models.Curso).filter(models.Curso.title == curso.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Curso already exists")

    new_curso = models.Curso(
            title=curso.title,
            description = curso.description,
            date = curso.date,
            link = curso.link
            )

    db.add(new_curso)
    db.commit()

    return new_curso

@app.put('/curso/{curso_id}', response_model=Curso,
        status_code=status.HTTP_200_OK)
def update_an_curso(curso_id:int,curso:Curso):
    curso_to_update = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    curso_to_update.title = curso.title
    curso_to_update.description = curso.description
    curso_to_update.date = curso.date
    curso_to_update.link = curso.link

    db.commit()

    return curso_to_update

@app.delete('/curso/{curso_id}', response_model=Tool,
        status_code=status.HTTP_200_OK)
def delete_curso(curso_id:int):
    curso_to_delete = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    db.delete(curso_to_delete)
    db.commit()

    if curso_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return curso_to_delete

# Talleres CRUD -----------------------------------------------------------------------------------------
class Taller(BaseModel):
    id:int
    title:str
    description:str
    date:str
    link:str

    class Config:
        orm_mode=True

db = SessionLocal()

@app.get('/talleres',response_model=List[Taller],
        status_code=status.HTTP_200_OK)
def get_all_talleres():
    talleres = db.query(models.Taller).all()
    return talleres

@app.get('/taller/{taller_id}', response_model=Taller,
        status_code=status.HTTP_200_OK)
def get_an_taller(taller_id:int):
    taller = db.query(models.Taller).filter(models.Taller.id == taller_id).first()
    return taller

@app.post('/taller',response_model=Taller,
        status_code=status.HTTP_201_CREATED)
def create_an_taller(taller:Taller):

    db_item = db.query(models.Taller).filter(models.Taller.title == taller.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400, details="Taller already exists")

    new_taller = models.Taller(
            title=taller.title,
            description = taller.description,
            date = taller.date,
            link = taller.liga
            )

    db.add(new_taller)
    db.commit()

    return new_taller

@app.put('/taller/{taller_id}', response_model=Taller,
        status_code=status.HTTP_200_OK)
def update_an_taller(taller_id:int,taller:Taller):
    taller_to_update = db.query(models.Curso).filter(models.Curso.id == curso_id).first()
    taller_to_update.title = taller.title
    taller_to_update.description = taller.description
    taller_to_update.date = taller.date
    taller_to_update.link = taller.liga

    db.commit()

    return taller_to_update

@app.delete('/taller/{taller_id}', response_model=Taller,
        status_code=status.HTTP_200_OK)
def delete_taller(taller_id:int):
    taller_to_delete = db.query(models.Taller).filter(models.Taller.id == taller_id).first()
    db.delete(taller_to_delete)
    db.commit()

    if taller_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = "Resource Not Found")

    return taller_to_delete
