from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_name():
    return {
        "first_name": "Зубенко",
        "last_name": "Михаил",
        "sur_name": "Петрович",
    }


@app.get("/users")
def get_contact_info():
    return {
        "phone": "88002000122",
    }


@app.get("/tools")
def get_info():
    return {
        "my_skills": {
            "python": [
                "Flask",
                "FastAPI",
            ],
            "javascript": [
                "Vue"
            ]
        },
    }