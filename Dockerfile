FROM python:3.12-slim

WORKDIR /work

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /work

CMD ["python3", "benchmarks/benchmark_runner.py"]
