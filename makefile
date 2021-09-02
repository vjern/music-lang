.ONESHELL:

test:
	python -m pytest tests -vvv

%:
	python -m midi example/$*.m
