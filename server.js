const express = require("express");
const connectDB = require("./config/db");
const path = require("path");

const app = express();

// Connect to database
connectDB();
// Init middleware
app.use(express.json({ extended: true }));

// Define Routes
app.use("/api/users", require("./routes/users"));
app.use("/api/auth", require("./routes/auth"));
app.use("/api/contacts", require("./routes/contacts"));

const PORT = 5000;

app.listen(PORT, () => console.log("server started on port: ", PORT));
