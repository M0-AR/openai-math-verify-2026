.PHONY: setup run test docker-up docker-run clean

setup:
	pip install -r requirements.txt

run:
	python3 benchmarks/benchmark_runner.py --out benchmarks/results/summary.json

test:
	pytest -q experiments benchmarks

docker-up:
	docker compose build
	docker compose up --abort-on-container-exit

docker-run:
	docker compose run --rm verify

clean:
	rm -rf benchmarks/results/*.json benchmarks/results/*.md __pycache__ data/*.csv
