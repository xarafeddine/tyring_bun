const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let query = "What is your name?\n";
rl.question(query, (answer: string) => {
  console.log(`Hello ${answer}!`);

  rl.close();
});
console.log("asdf");
