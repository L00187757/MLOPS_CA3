FROM python:3.9-slim

WORKDIR /app

# Install system dependencies

COPY app/requirements.txt .  
RUN pip install -r requirements.txt

COPY . .

RUN python app/models/train.py

EXPOSE 5000
CMD ["python", "app/app.py"]
