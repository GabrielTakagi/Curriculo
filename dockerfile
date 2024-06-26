
FROM python:alpine3.20
EXPOSE 5050
WORKDIR /Curriculo

#Criacao de imagem
RUN python -m venv .venv
RUN . .venv/bin/activate
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

#Executar servidor
CMD [ "flask", "--app", "flaskr", "run", "-h", "0.0.0.0", "-p", "5050"]