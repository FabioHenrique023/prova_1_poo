
from fastapi import FastAPI
from rota import router

app = FastAPI(
    title="API: Cursos",
    version='0.0.1',
    description="Prova POO II"
)

app.include_router(router, prefix="/Curso", tags=["Cursos"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
