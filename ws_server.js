import express from "express";
const app = express();

app.get("/", (req, res) => {
  res.send("assalamo alykom");
});
app.listen(3000, () => console.log("server on 3000"));

// working socket
// import { WebSocketServer } from 'ws';

// const wss = new WebSocketServer({ port: 3000 });

// wss.on('connection', function connection(ws) {
//   console.log('A new visitor connected');

//   ws.on('error', function (error) {
//     console.error('WebSocket error:', error);
//   });

//   ws.on('message', function (message) {
//     console.log('Received message: %s', message);

//     // You can process the Telnet message here and send a response
//     // For example, you can convert the Telnet message to uppercase and send it back
//     const response = message.toString().toUpperCase();

//     // Send the response back to the Telnet client
//     ws.send(response);
//   });

//   // Send a welcome message to the Telnet client
//   ws.send('Welcome to the Telnet-to-WebSocket server');
// });

// console.log('WebSocket server is running on port 3000');
