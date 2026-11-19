FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir pytest selenium

COPY tests/ /app/tests/

CMD ["pytest", "-v", "tests/"]