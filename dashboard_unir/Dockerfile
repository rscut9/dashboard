# Usar la imagen oficial de Python como imagen base
FROM python:3.8

# Establecer el directorio de trabajo en el contenedor
WORKDIR /code

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto del código fuente de la aplicación al contenedor
COPY . .

# Ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
