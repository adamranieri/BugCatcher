
FROM python

WORKDIR /code

COPY . /workspace
WORKDIR /workspace
RUN pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000" ]