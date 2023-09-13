from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates


note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    docs = conn.notesDB.myNotes.find()
    newDoc = []
    for i, doc in enumerate(docs):
        newDoc.append({
            "id": i,
            "title": doc["title"],
            "desc": doc["desc"],
            # "important": doc["important"]
        })
    
    return templates.TemplateResponse("index.html", {"request": request, "newDoc": newDoc})
       

@note.post("/")
async def add_note(note: Note):
    form = await note.form()
    form_dict = dict(form)
    form_dict["important"] = True if form_dict.get("important") == "on" else False
    inserted_note = conn.notesDB.myNotes.insert_one(dict(note))
    return {"Success": True}