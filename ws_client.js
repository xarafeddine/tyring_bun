import WebSocket from "ws";

const ws = new WebSocket("ws://localhost:3000");

ws.on("error", console.error);

ws.on("open", function open() {
  console.log("connection established");
  ws.send("hi server");
});

ws.on("message", function message(data) {
  console.log("received: %s", data);
});
