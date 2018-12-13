
deps:
	pip install -r requirements.txt

init:
	./manage.py migrate
	./manage.py loaddata --app creatorz sample.json

shell:
	./manage.py shell_plus

test:
	./manage.py test

rs:
	./manage.py runserver
