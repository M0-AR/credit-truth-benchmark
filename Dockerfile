FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY experiments/ ./experiments/
COPY tests/ ./tests/
COPY data/ ./data/
COPY benchmarks/ ./benchmarks/
COPY notebooks/ ./notebooks/
ENV PYTHONPATH=/app/src
CMD ["python", "-m", "credit_truth.evaluate", "--out", "/app/benchmarks/results.json"]
