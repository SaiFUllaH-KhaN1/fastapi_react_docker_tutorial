FROM python:3.12.6

WORKDIR /app

ADD ./backend/requirements.txt /app/backend/requirements.txt

RUN pip install -r backend/requirements.txt

COPY . /app

CMD cd backend && uvicorn server:app --host 0.0.0.0