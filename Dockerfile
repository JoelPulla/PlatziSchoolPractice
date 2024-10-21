FROM python:3.13

#directorio de trabajo 
WORKDIR /app

#copia el archivo de las deprendicas 
    #local              #docker 
COPY requirements.txt /app/requirements.txt

#ejecuta el comando 
    #instala las dependicas de los requerimentos de docker
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#copiamos todo el proyecto desde el archivo raiz
COPY ./ app/
        #pegar en directorio de trabajo de docker

#comando para mantener encendico el contenedor
CMD bash -c "while true; do sleep 1; done "

