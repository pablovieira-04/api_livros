from fastapi import FastAPI, APIRouter
from app.controllers.livro_controller import router as livro_router
from app.controllers.usuario_controller import router as usuario_router

router = APIRouter()
router.include_router(livro_router, prefix="/livros", tags=["Livros"])
router.include_router(usuario_router, prefix="/usuarios", tags=["Usuários"])


app = FastAPI(title="API de Livros", version="1.0.0")
app.include_router(router)



@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Livros!"}
