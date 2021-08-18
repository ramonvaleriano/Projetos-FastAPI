from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from infra.sqlalchemy.config.database import criar_db, get_db
from schemas import schemas
from infra.sqlalchemy.repositorio.series import RepositorioSerie

# Criar a base de dados
criar_db()

app =  FastAPI()


@app.post('/series')
def criar_serie(serie : schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    
    return serie_criada

@app.get('/series')
def listar_series(db : Session=Depends(get_db)):
    lista_de_series = RepositorioSerie(db).listar()

    return lista_de_series


@app.get('/series/{serie_id}')
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).obter(serie_id)

    return serie

@app.delete('/series/{serie_id}')
def remover_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).remover(serie_id)

    return {'mensage':'Serie Deletada!'}