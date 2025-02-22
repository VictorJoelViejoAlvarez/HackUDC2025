from fastapi import FastAPI, Request, Response
import uvicorn
from routes import router

app = FastAPI(title='Hack UDC 2025 CompetenciApp')

# Incluir las rutas
app.include_router(router)

@app.get(path='/')
async def home(req: Request) -> Response:
    return Response(content='API conectada a PostgreSQL 🚀', status_code=200)

if __name__=='__main__':
    uvicorn.run(app=app, host='localhost', port=8000)