# goit-python-web
My python repository for second module

The instruction for the running the application:

1. Build of the image:
sudo docker build -f "lesson3/DockerFile" -t teosoph/myproject:tagname "lesson3"

2. Push of the image on the dockerhub:
docker push teosoph/myproject:tagname

3. The running of the application in interactive terminal:
sudo docker run --rm -it teosoph/myproject:tagname
