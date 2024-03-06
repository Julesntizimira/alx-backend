import { createClient } from "redis";

const subscriber = createClient()
  .on("error", (err) =>
    console.log("Redis client not connected to the server:", err.message)
  )
  .on("connect", () => console.log("Redis client connected to the server"));

subscriber.subscribe("holberton school channel");
subscriber.on("message", (ch, message) => {
  console.log(message);
  if (message == "KILL_SERVER") {
    subscriber.unsubscribe(ch);
    subscriber.quit();
  }
});
