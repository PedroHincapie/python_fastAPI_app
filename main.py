from fastapi import FastAPI

app = FastAPI()

"""
Se deseamos cambiar el título de la aplicación, podemos hacerlo con la propiedad title de la instancia de FastAPI.
app.title = "My API with FastAPI"
"""
app.title = "My API with FastAPI"


"""
Si deseamos adicionar alguna descripcion de proyecto tenemos
la propiedad description de la instancia de FastAPI.
app.description = "xXxxxxx"
"""
app.description = """
Este es mi primer proyecto con FastAPI, dentro de este podemos hacer las
prubeas de uso de la misma y aprender a componer API con FastAPI
"""

"""
Si deseamos adicionar una versión a nuestra API, podemos hacerlo con la propiedad version de la instancia de FastAPI.
app.version = "1.0.0"
"""
app.version = "1.0.0"


@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}
