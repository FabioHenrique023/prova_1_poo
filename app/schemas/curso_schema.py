from typing import Generic, Optional, List, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class CursoSchema(BaseModel):
    id: Optional[int] = None 
    titulo: Optional[str] = None
    aulas: Optional[int] = None 
    horas: Optional[int] = None 
    dia: Optional[int] = None 
    
    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestCurso(BaseModel):
    parameter: CursoSchema = Field(...)
    
class Response(GenericModel, Generic[T]):
    code: str 
    status: str 
    mensagem: str 
    resultado: Optional[T]