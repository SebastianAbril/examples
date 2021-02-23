# pull official base image
FROM java:8-jdk-alpine

# set work directory
WORKDIR /usr/src/app

# copy jar
COPY ./build/libs/api-gateway-0.0.1-SNAPSHOT.jar .

WORKDIR /usr/app

ENTRYPOINT ["java","-jar","/usr/src/app/api-gateway-0.0.1-SNAPSHOT.jar"]