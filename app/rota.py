from fastapi import APIRouter, HTTPException, status, Depends
from schemas.curso_schema import CursoSchema, Request, RequestCurso, Response

router = APIRouter()

curso_data = {}  
proximo_id = 1  

@router.post('/Criarcurso')
async def create(request: RequestCurso):
    global proximo_id
    curso = request.parameter

    #Tramento para se o usuário deixar sempre zero o id soma + 1 ou se o usuário informar o mesmo id duas vezes
    curso.id = proximo_id
    curso_data[proximo_id] = curso
    proximo_id += 1

    return Response(code=200, status="Ok", mensagem="Curso cadastrado com sucesso!").dict(exclude_none=True)

@router.get("/listartodos")
async def get_curso(skip: int = 0, limit: int = 100):
    _curso = list(curso_data.values())[skip:skip + limit]

    if _curso:
        return Response(code=200, status="Ok", mensagem="Busca completa", resultado=_curso).dict(exclude_none=True)
    elif len(_curso) == 0:
        return Response(code=200, status="Ok", mensagem="Não possui curso cadastrado")
    else:
        raise HTTPException(detail="Página não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.get("/id/{id}")
async def get_by_id(id: int):
    curso = curso_data.get(id)

    if curso:
        return Response(code=200, status="Ok", mensagem=f"Busca concluída com sucesso: {id}", resultado=curso)
    else:
        raise HTTPException(detail="Não possui um curso com esse id", status_code=status.HTTP_404_NOT_FOUND)

@router.patch("/update")
async def update_curso(request: RequestCurso):
    curso = request.parameter

    if curso.id in curso_data:
        curso_data[curso.id] = curso
        return Response(code=200, status="Ok", mensagem="Alterado com sucesso!", resultado=curso)
    else:
        raise HTTPException(detail="Não possui um curso com esse id", status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/delete/{id}")
async def delete_tipo(id: int):
    if id in curso_data:
        del curso_data[id]
        return Response(code=200, status="Ok", mensagem="Deletado com sucesso!")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não possui um curso com esse id")