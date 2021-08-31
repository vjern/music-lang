.ONESHELL:

test:
	python -m pytest tests -vvv

%:
	python -m midi mm/$*.m
