FROM node:11.8.0

RUN apt-get update
RUN apt-get -y install xvfb libgtk2.0-0 libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2
RUN npm install -g npm

WORKDIR /e2e

COPY package.json package-lock.json /e2e/
RUN npm install

COPY . /e2e
