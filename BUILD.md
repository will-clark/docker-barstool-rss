docker login https://docker.willclark.org
docker build . --tag "docker.willclark.org/barstool-rss:1.0"
docker push docker.willclark.org/barstool-rss:1.0
docker logout https://docker.willclark.org