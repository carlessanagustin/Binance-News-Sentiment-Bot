IMAGE ?= binance-news-sentiment-bot:1.0.0

start: remove build run

build:
	docker build -t ${IMAGE} .

run:
	docker run --rm ${IMAGE}

remove:
	-docker rmi -f ${IMAGE}

in:
	docker run --entrypoint bash -it ${IMAGE}
