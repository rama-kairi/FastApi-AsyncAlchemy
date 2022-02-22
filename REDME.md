# Async SQLAlchemy usage with FastAPI

This project demonstrates async usage of SQLAlchemy 1.4 with FastAPI.

## Installation

To run the example, change the `DATABASE_URL` in `fastapi_asyncalchemy/db/base.py`.

To install the project:

```
poetry install
```

To run the examples, we need to enter the virtual environment:

```
poetry shell
```

Create the database tables:

```
python main.py
```

Run FastAPI with Uvicorn:

```
uvicorn main:app --reload
```

You can send HTTP requests from [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Licence

License: The MIT License (MIT)
