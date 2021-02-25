# build environment
FROM java:8-jdk-alpine as build
WORKDIR /app
COPY gradle gradle
COPY .gradle .gradle
COPY build.gradle settings.gradle gradlew ./
COPY src src
RUN ./gradlew build -x test

# production environment
FROM java:8-jdk-alpine
WORKDIR /usr/src/app
COPY  --from=build /app/build/libs/api-gateway-0.0.1-SNAPSHOT.jar .

ENTRYPOINT ["java","-jar","/usr/src/app/api-gateway-0.0.1-SNAPSHOT.jar"]