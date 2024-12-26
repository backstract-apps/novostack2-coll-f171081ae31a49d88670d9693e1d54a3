from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostack2-coll-f171081ae31a49d88670d9693e1d54a3',debug=False,docs_url='/intelligent-hugle-dd57dfeac37311ef85b10242ac12000362/docs',openapi_url='/intelligent-hugle-dd57dfeac37311ef85b10242ac12000362/openapi.json')

app.include_router(router, prefix='/intelligent-hugle-dd57dfeac37311ef85b10242ac12000362/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()