FROM python:latest

# ARG ping_pong_application_port=8000

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "-m", "uvicorn", "pingpong:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000" ]