FROM debian:stable

RUN apt-get update && apt-get install curl -y

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -

RUN apt-get install nodejs -y

COPY app /app

WORKDIR /app

RUN npm install

EXPOSE 3000

CMD ["node", "index.js"]
