from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"ФИО": "Шевченко Никита Олегович"}

@app.get("/users")
def get_users():
    contact = {"телефон": "89132513442", "почта": "nikit15110295@gmail.com"}
    return contact

@app.get("/tools")
def get_tools():
    skills = {"навыки": "Владею языками программирования такими, как Python, R, javascript, typescript"}
    return skills
