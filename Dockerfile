FROM python:3.10
WORKDIR /django-app-login

RUN mkdir /django-app-login/core
RUN mkdir /django-app-login/templates
RUN mkdir /django-app-login/usuarios

COPY core/* /django-app-login/core/
COPY templates/* /django-app-login/templates/
COPY usuarios/* /django-app-login/usuarios/
COPY manage.py /django-app-login/manage.py
COPY var_ignore.py /django-app-login/var_ignore.py

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod -R a+rwx /django-app-login/core
RUN chmod -R a+rwx /django-app-login/templates
RUN chmod -R a+rwx /django-app-login/usuarios
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]