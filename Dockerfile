FROM python:3.12-slim

#Set workdir
WORKDIR /app

#Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

#Copy backend files
COPY backend /app/backend

#Install Python deps
COPY pip_requirements.txt .
RUN pip install --no-cache-dir -r pip_requirements.txt

#Expose FastAPI port
EXPOSE 8000

#add backend to python path
ENV PYTHONPATH=/app/backend

#ssStart the app
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
