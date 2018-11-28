                                독커를 설치하는 방법
=======================================================================================

1. # Run Docker Quick Starter
$ docker version       # cf. docker --version
$ docker info          # docker system info
$ docker --help
$ docker run hello-world
$ docker images
$ docker ps                   # cf. docker ps -a
$ docker-machine ls 

--------------------------------------------------------------------------------------

2. # run docker container for ubuntu image
docker container run <docker-image-name> <command>
$> docker container run ubuntu:latest /bin/echo 'Hello world'
$> docker ps -a
$> docker container ps -a
$> docker system df
$> docker image ls

______________________________________________________________________________________
