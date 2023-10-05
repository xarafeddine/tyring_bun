FROM node:19-alpine3.16
WORKDIR /app
COPY package*.json /.
RUN npm install
COPY . .
ENV PORT=3000
EXPOSE 3000
CMD [ "node", "ws_server.js" ]