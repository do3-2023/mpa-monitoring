import { renderFileToString } from "./deps.ts";
import { Application, Router } from "./deps.ts";


const PORT = 8000;

const API_URL = Deno.env.get("API_URL");

if (!API_URL) {
  console.log("API URL MISSING!");
  Deno.exit(1)
}

const app = new Application();
const router = new Router();
router.get("/", async (context) => {
  let res = await fetch(`${API_URL}/hello`);
  let msg = await res.json()
  const myTemplate = await renderFileToString("index.ejs", {
    message: msg,
  });
  context.response.body = myTemplate
  context.response.status = 200
});

router.get("/healthz", async (context) => {
  try {
    let res = await fetch(`${API_URL}/healthz`);
    context.response.status = res.status;
  }
  catch (err) {
    context.response.status = 500;
  }
});

console.log(`HTTP webserver running. Access it at: http://localhost:${PORT}/`);
await app.listen({ port: PORT });