FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./ /app


COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]