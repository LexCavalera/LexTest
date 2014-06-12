Requires:
	- python
	- mongodb
	- pyramid

To run:
	- set environment variables:
		- PRODROOT: path to this directory (library)
		- PYTHONPATH: $PRODROOT\src\python
	- run mongodb server with dbpath $PRODROOT\db
	- run python $PRODROOT/site/app.py
	- go to localhost:8080