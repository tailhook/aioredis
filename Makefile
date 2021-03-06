
PYTHON ?= python3
FLAKE ?= pyflakes
PEP ?= pep8
REDIS_VERSION ?= "$(shell redis-server --version)"

.PHONY: all flake doc test cov
all: flake doc cov

doc:
	make -C docs html

flake:
	$(FLAKE) aioredis tests examples
	$(PEP) aioredis tests examples

test:
	REDIS_VERSION=$(REDIS_VERSION) $(PYTHON) runtests.py -v

cov coverage:
	REDIS_VERSION=$(REDIS_VERSION) $(PYTHON) runtests.py --coverage
