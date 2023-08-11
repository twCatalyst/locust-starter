FROM python:3.9-slim

WORKDIR /locust

COPY requirements.txt .
COPY org/thoughtworks .
COPY entrypoint.sh .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# CMD ["sh", "-c", "locust -f generic.py --host=$TARGET_HOST"]

