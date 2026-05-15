# ponte de entrada do meu sistema 
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.controllers import auth_controller

app= FastAPI(title="Sistema de Gerenciamento de Usuários")


#configurar a pasta para servir arquivos estáticos (css, js, imagens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


#configurar o Jinja2 para renderizar os templates HTML
templates = Jinja2Templates(directory="app/templates")


app.include_router(auth_controller.router)