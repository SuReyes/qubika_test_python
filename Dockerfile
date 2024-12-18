FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN python -m playwright install

ENV PYPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v"]
