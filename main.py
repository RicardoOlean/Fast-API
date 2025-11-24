from fastapi import FastAPI
from typing import Annotated
from fastapi import Path
from pydantic import BaseModel

app = FastAPI()

cursos =[
    "Digital solutions",
    "mecatronica",
    "Manufatura Digital",
    "Manufatura Eletronica",
    "Manufatura Automobilistica",
    "Administracao "
]




@app.get('/cursos')
async def get_cursos():
    return {"cursos" : cursos}

# @app.get('/cursos/{curso_id}')
# async def get_curso(curso_id :int):
#     return {"curso" : cursos[curso_id]}



@app.get('/cursos/{curso_id}')
async def get_curso(curso_id : Annotated[int, Path(ge=0, le=5)]):
    return {"curso" : cursos[curso_id]}

disciplinas = {
    "python" :{
        "carga horaria" : 60,
        "instrutor" : "cleber augusto"
    },
    "iot" : {
        "carga horaria" : 40,
        "instrutor" : "luca dias"
    },
    "java":{
        "carga horaria": 20,
        "instrutor":"Agatha"
    }
}

# @app.get('/disciplina')
# async def get_disciplina (nome: str):
#     print (nome)
#     return disciplinas[nome]

from pydantic import BaseModel

@app.get('/disciplinas')
async def get_disciplina(nome : str | None = None):
    if nome:
        return disciplinas[nome]
    else:
        return disciplinas

from pydantic import BaseModel

class Disciplinas(BaseModel):
    nome : str
    carga_horaria : int
    instrutor : str

@app.post('/disciplinas')
async def post_disciplina(disciplina : Disciplinas):

    temp = disciplina.model_dump()
    nome = temp["nome"]
    carga_horaria = temp["carga_horaria"]
    instrutor = temp["instrutor"]
    disciplinas[nome] = {
        "carga horaria" : carga_horaria,
        "instrutor" : instrutor
    }
@app.put("/disciplinas/{nome}")
async def put_disciplinas(
    nome: str,
    carga_horaria: int | None = None,
    instrutor: str | None = None
):
    if nome in disciplinas.keys():
        if carga_horaria:
            disciplinas[nome].update({"carga horaria" : carga_horaria})
        if instrutor:
            disciplinas[nome].update({"instrutor" : instrutor})
        return disciplinas[nome]
    
@app.delete("/disciplinas/{nome}")
async def delete_disciplinas(
    nome: str,
    carga_horaria: int | None = None,
    instrutor: str | None = None
):
    if nome in disciplinas:
        if carga_horaria is not None:
            disciplinas[nome].pop("carga horaria", None)
        if instrutor:
            disciplinas[nome].pop("instrutor", None)
        return disciplinas[nome]
    