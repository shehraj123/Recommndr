run:
	venv/bin/python3 server.py

install: requirements.txt
	( \
		python3 -m venv venv; \
		source ./venv/bin/activate; \
		pip install -r requirements.txt; \
	)