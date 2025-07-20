FROM python:3.12.6

WORKDIR /app

COPY . /app

RUN pip install -r backend/requirements.txt

CMD cd backend && uvicorn server:app --host 0.0.0.0

# just a comment
