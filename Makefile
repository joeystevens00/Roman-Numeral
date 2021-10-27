default:
	poetry install

.PHONY:
test:
	poetry run pytest
