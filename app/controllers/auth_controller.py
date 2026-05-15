# Rotas de autenticação vai ficar aqui
from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session



from app.database import get_db

from app.models.usuarios import Usuario
from app.auth import hash_senha, verificar_senha, criar_token


#APIRouter agrupa as rotas dentro desse modulo com o prefixo /auth
router = APIRouter(prefix="/auth", tags=["auth"])

templates = Jinja2Templates(directory="app/templates")





#Tela de cadastro
@router.get("/cadastro")
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "auth/cadastro.html",
        {"request": request}
    )

#Tela de login
@router.get("/login")
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
        "auth/login.html",
        {"request": request}
    )

#Rota para processar o cadastro
@router.post("/cadastro")
def fazer_cadastro(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    #Verificar se o email já existe
    usuario_existente = db.query(Usuario).filter_by(email == email).firtst()

    # Mensagem de erro se o email já existir
    if usuario_existente:
        return templates.TemplateResponse(
            request,
            "auth/cadastro.html",
            {request: request, "erro": "Email já cadastrado"}
        )
    

    #criar o objeto do usuário
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=senha
    )
    db.add(novo_usuario)
    db.commit()
    
