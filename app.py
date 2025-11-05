from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def olá_mundo():
    return {"teste": "Olá, mundo!"}

@app.get("/teste")
def teste():
    return {"Teste": "testando"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)