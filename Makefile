SERVICE := cornershop-test

ifdef NO_CACHE
	BUILD_CACHE_FLAG := --no-cache
endif

images:
	docker build ${BUILD_CACHE_FLAG} -t ${SERVICE}-api:dev -f docker/django/Dockerfile .
	docker build ${BUILD_CACHE_FLAG} -t ${SERVICE}-gateway:dev -f docker/nginx/Dockerfile .

###########################
####### DEVELOPMENT #######
###########################
up:
	docker-compose up

load-data:
	docker-compose run --rm ${SERVICE}-api sh -c './wait-for.sh python manage.py loaddata gps/fixtures/countries.json'
	docker-compose run --rm ${SERVICE}-api sh -c './wait-for.sh python manage.py loaddata sends/fixtures/clusters.json'

migrate:
	docker-compose run --rm ${SERVICE}-api sh -c './wait-for.sh python manage.py migrate'

makemigrations:
	docker-compose run --rm ${SERVICE}-api sh -c './wait-for.sh python manage.py makemigrations'

shell:
	docker-compose run --rm ${SERVICE}-api python manage.py shell

test:
	docker-compose run ${SERVICE}-api sh -c './wait-for.sh python manage.py test'

bash:
	docker-compose run --rm ${SERVICE}-api sh

add-app:
	docker-compose run --rm ${SERVICE}-api python manage.py startapp ${APP}

isort:
	docker-compose run --rm ${SERVICE}-api isort -rc --skip migrations .

coverage:
	docker-compose run --rm ${SERVICE}-api coverage run manage.py test

coverage_report:
	docker-compose run --rm ${SERVICE}-api coverage report

coverage_html_report:
	docker-compose run --rm ${SERVICE}-api coverage html
