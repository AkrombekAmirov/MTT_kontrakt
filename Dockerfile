FROM python:3.7

WORKDIR /code

COPY ./ /code/

RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python setup.py install



CMD ["python", "app.py"]
