# mini-rag

This is minimal implementation of the RAG model for question answering.

## Requirements

- python 3.14 or later 

### Install Python using miniconda

1) Download and install miniconda from [here]{https://anaconda.com/api/installers/Miniconda3-latest-Windows-x86_64.exe }

2) Create Environment using the following command :
```bash 
    $ conda create -n mini-rag python=14
```

3) Activate the environment       
```bash 
    $ conda activate mini-rag
```

## Installation

## Install the require packages 
```bash
    $ pip inatall -r requireents.txt 
```

### Setup environment variables

```bash 
    cp .env.example .env
```

setup your environment variables in the `.env` file like `OPENAI_API_KEY` value.


## Run the FastAPI servier 

```bash
$   uvicorn main:app --reload --host 0.0.0.0
```