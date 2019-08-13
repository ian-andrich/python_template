SHELL=/bin/bash
CONDAROOT = ~/*conda*/
ENVNAME = python_template

env: .env

.env: env.yml
	conda env create -f env.yml
	touch .env

refresh_env:
	rm .env; conda env remove -y --name $(ENVNAME);
	make env

docs: docs/

docs/:
	echo "Make it"
