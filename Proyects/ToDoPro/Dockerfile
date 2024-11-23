FROM python:3.13.o 

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app/

#manter el server corriendo 
# CMD bash -c "whilw True; do sleep 1; done" 

#run django 
CMD [ "python manage.py runserver" ]