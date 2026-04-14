const express = require("express");
const mongoose = require("mongoose");

const app = express();
const PORT = 3000;

// MongoDB connection URI
const MONGO_URI = "mongodb://mongodb:27017/companydb";

// Connect to MongoDB
mongoose.connect(MONGO_URI)
  .then(() => console.log("Connected to MongoDB successfully"))
  .catch((err) => console.log("MongoDB connection error:", err.message));

app.get("/", (req, res) => {
  res.send("Node.js API is running with MongoDB backend");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

