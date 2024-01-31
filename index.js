// index.js (server-side)
import express from "express";
import bodyParser from "body-parser";
import { PythonShell } from "python-shell";
import path from "path";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, "../frontend")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "../frontend/index.html"));
});

app.post("/webcam_scan", (req, res) => {
  // Execute your Python script using PythonShell
  PythonShell.run("application.py", null, (err) => {
    if (err) {
      console.error("Error:", err);
      return res.status(500).json({ error: "Internal Server Error" });
    }

    // Return a response to the frontend
    return res.json({ message: "Webcam scanning initiated" });
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
