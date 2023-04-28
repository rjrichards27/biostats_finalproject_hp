install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black src/*.py tests/*.py

mypy:
	mypy --ignore-missing-imports src/*.py tests/*.py

lint:
	pylint --disable=R,C --ignore-patterns=__*__.py --disable=W0511,E1101,E0401,W1514 src/*.py tests/*.py 

test:
	# python -m pytest -vv --cov=Code_10 --cov=main test_*.py
	python -m pytest -vv --cov=src tests/test_*.py

build:
 	#build container
	docker build -t deploy_potterduels .

run:
	#run docker
	# docker run -p 127.0.0.1:8080:8080 2d1505f9302f

deploy:
 	#deploy
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 450825970415.dkr.ecr.us-east-1.amazonaws.com
	# docker build -t deploy_potterduels .
	# docker tag deploy_potterduels:latest 450825970415.dkr.ecr.us-east-1.amazonaws.com/globaltemperatures706:latest
	# docker push 450825970415.dkr.ecr.us-east-1.amazonaws.com/globaltemperatures706:latest
	
all: install format lint test deploy