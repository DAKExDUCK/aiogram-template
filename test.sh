black .
isort .
pylint --recursive=y .
mypy .
python -m pytest tests/
