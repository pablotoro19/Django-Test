SERVICE := cornershop-test

ifdef NO_CACHE
	BUILD_CACHE_FLAG := --no-cache
endif

images:
	docker build ${BUILD_CACHE_FLAG} -t ${SERVICE}:dev -f docker/django/Dockerfile .
	docker build ${BUILD_CACHE_FLAG} -t ${SERVICE}-gateway:dev -f docker/nginx/Dockerfile .

###########################
####### DEVELOPMENT #######
###########################
up:
	docker-compose up

load-data:
	docker-compose run --rm ${SERVICE} sh -c './wait-for.sh python manage.py loaddata menu/fixtures/menu.json'
	docker-compose run --rm ${SERVICE} sh -c './wait-for.sh python manage.py loaddata menu/fixtures/options.json'
	docker-compose run --rm ${SERVICE} sh -c './wait-for.sh python manage.py loaddata user/fixtures/users.json'
	docker-compose run --rm ${SERVICE} sh -c './wait-for.sh python manage.py loaddata user_menu/fixtures/orders.json'

migrate:
	docker-compose run --rm ${SERVICE} sh -c './wait-for.sh python manage.py migrate'

makemigrations:
	docker-compose run --rm ${SERVICE} sh -c './wait-for.sh python manage.py makemigrations'

shell:
	docker-compose run --rm ${SERVICE} python manage.py shell

test:
	docker-compose run ${SERVICE} sh -c './wait-for.sh python manage.py test'

bash:
	docker-compose run --rm ${SERVICE} sh

add-app:
	docker-compose run --rm ${SERVICE} python manage.py startapp ${APP}

isort:
	docker-compose run --rm ${SERVICE} isort -rc --skip migrations .

coverage:
	docker-compose run --rm ${SERVICE} coverage run manage.py test

coverage_report:
	docker-compose run --rm ${SERVICE} coverage report

coverage_html_report:
	docker-compose run --rm ${SERVICE} coverage html
