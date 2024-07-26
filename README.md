# Finder API.

![logo-teal](https://github.com/Sebastian9751/tramifast-api/assets/85807291/232a0041-1384-4988-8fd9-41903e5e11c2)

#### This is a API has been developed using  FastAPI.

## Configuration

#### Before running the application, ensure that you configure the following environment variables:

```bash
#These variables are necessary to connect to SQL server
DB_USER=
DB_PASSWORD=
DB_SERVER=
DB_NAME=
```

## Installation

#### Clone this repository.

#### Install the dependencies using pip:

```bash
$ pip install -r requirements.txt
```
## Running the Server



```bash
# Launch application

$ uvicorn app:app --host 0.0.0.0 --port 8000
 
```

