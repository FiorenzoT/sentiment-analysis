FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY ./backend /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["backend/manage.py", "runserver", "0.0.0.0:8080"]