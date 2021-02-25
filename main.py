from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/", response_class=HTMLResponse)
async def login_input(request: Request):
    return templates.TemplateResponse("first.html", {"request": request})


@app.post('/chat/', response_class=HTMLResponse)
async def create_user(request: Request, name: str = Form(...)):
    if len(name) > 15 or len(name) < 2:
        return templates.TemplateResponse("first.html", {"request": request})
    return templates.TemplateResponse("index.html", {"request": request, "user": name})


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id):
    await manager.connect(websocket)
    try:
        await manager.broadcast(f"{client_id}:::--UserAddToChat")
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{client_id}:::{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{client_id}:::--UserLeftToChat")
