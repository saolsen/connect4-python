install:
	python -m pip install --upgrade pip
	python -m pip install -e .

install-dev: install
	python -m pip install -e ".[dev]"
