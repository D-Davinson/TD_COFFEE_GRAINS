
FROM python:alpine
WORKDIR /app
COPY seeder.py .
COPY Grain.py .
RUN pip install pymongo
CMD ["python", "seeder.py"]