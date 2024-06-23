FROM node:22
RUN mkdir /home/node/app
WORKDIR /home/node/app
COPY package*.json ./
COPY src /home/node/app/src
RUN npm install
CMD [ "npm", "run", "start"]