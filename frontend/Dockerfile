FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rio new 

COPY . .
CMD ["rio", "run"]
