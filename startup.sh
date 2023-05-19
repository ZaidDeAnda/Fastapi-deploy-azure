#!/bin/bash

# Actualiza los paquetes del sistema
apt-get update

# Instala las dependencias necesarias
apt-get install -y libgl1-mesa-glx
apt-get install -y libglib2.0-0

# Inicia la aplicación FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000