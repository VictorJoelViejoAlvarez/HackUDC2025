from fastapi import FastAPI, Request, Response
import uvicorn
from routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Hack UDC 2025 CompetenciApp')

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (puedes restringirlo a "http://localhost:3000" por seguridad)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir las rutas
app.include_router(router)

@app.get(path='/')
async def home(req: Request) -> Response:
    return Response(content='API conectada a PostgreSQL 🚀', status_code=200)

if __name__=='__main__':
    uvicorn.run(app=app, host='localhost', port=8000)