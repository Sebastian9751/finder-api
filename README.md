# Finder API.

![gg](https://github.com/user-attachments/assets/b04de048-a4d8-4424-8e1e-a488401102df)


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

