<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">My First API in Python</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

Estas es mi primera API con Pyhton.

## 🏁 Getting Started <a name = "getting_started"></a>

Por medio de la presente, deseo poner a disponision toda la informacion que recopile del presente.

### Prerequisitos

Estos fuero mis pasos para la construcion

```
cd my_first_api
python3 -m venv env
source env/bin/activate
```

En caso de salir del entorno virtual

```
deactivate
```

Para validar que los pasos anteriores sean correacto tenemos

```
which python3
```

Librerias que uso
```
pip install fastapi
```
```
pip install uvicorn
```

Luego, guardo todo lo instalado en mi archivo requirements.txt
```
pip3 install -r requirements.txt
```

### Installing

Para obtener el proyecto

```
git clone
cd my_first_api
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## 🔧 Running the tests <a name = "tests"></a>

Pasos para poner a correr esta APP
### Ejucutar modo local
```
uvicorn main:app
```

## En caso que deses realizar cambios sin tener que estar deteniendo la APP
```
uvicorn main:app --reload
```

## En caso de necesitar cambiar el puerto de la appla APP
```
uvicorn main:app --reload --port 8080
```

## 🎈 Y la Documentación <a name="usage"></a>

Para hacer uso de la documentacion tenemos
Dependera de donde tiene corriendo la app pero siempre sera el /docs
```
http://127.0.0.1:8080/docs
```

En el archivo main.py tenemos la siguiente informacion:

```
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


@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Si deseasmos adicionar un seccion con el tag, solo lo que necesiamos es:

```
@app.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World"}
```


##### Para editar informacion de la documentacion tenemos
```
Por favor, ir al repositorio y buscar "Adicionar informacion para la doc de la APP"
```

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
