from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# comment CORS as not needed when the react app is statically mounted. 
# CORS only needed when working in local hosting and hosting frontend and backend seperatelly 
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/form_display")
def form_display(first_name: Annotated[str, Form()], last_name: Annotated[str, Form()]):
    print("recieved we have: ", first_name, last_name)
    if first_name == "scott":
        print(f"correct input as {input} detected")
        return {"message": f"Hello pathfinder {first_name} {last_name}"}
    else:
        return {"message": "Not found"}

app.mount("/", StaticFiles(directory="../frontend/build", html=True), name="ui")