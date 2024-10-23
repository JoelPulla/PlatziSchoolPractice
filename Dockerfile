FROM python:3.13

# Directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias
#      Local               Docker
COPY requirements.txt /app/requirements.txt

# Ejecuta el comando para instalar dependencias del archivo de requerimientos
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia todo el proyecto desde el archivo raíz
# Pegar en el directorio de trabajo en Docker
COPY . /app/

# Comando para mantener el contenedor en ejecución
CMD bash -c "while true; do sleep 1; done"


#PARA SERVER CON FASTAPI

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8080"]