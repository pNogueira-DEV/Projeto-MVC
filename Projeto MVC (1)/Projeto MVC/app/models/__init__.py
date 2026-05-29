from app.models import categoria
from app.models import produto
from app.models import usuarios 


#gerar a migrations

#python -m alembic revision --autogenerate -m "Criando tabelas de categorias, produtos"

#aplicar a migration

# python -m alembic upgrade head