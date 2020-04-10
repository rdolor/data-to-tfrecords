IMAGE_NAME=data-to-tfrecords:master

build ::
	echo ${IMAGE_NAME}
	docker build -f ./docker/Dockerfile -t ${IMAGE_NAME} .
	#docker push ${IMAGE_NAME}

