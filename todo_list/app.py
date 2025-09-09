from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from todo_list.schemas import Message

app = FastAPI(title='ToDo List')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/home', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_world():
    return """
    <html>
        <head>
            <title>Hello World from FastAPI</title>
        </head>
        <body>
            <h1>
                Hello World!
            </h1>
        </body>
    </html>
    """
