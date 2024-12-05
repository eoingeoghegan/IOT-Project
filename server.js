const express = require("express");
const multer = require("multer");
const app = express();
const fs = require("fs");

const upload = multer({ dest: "public/uploads/" });

app.use(express.static("public"));

app.post("/upload", upload.single("file"), (req, res) => {
  if (req.file) {
    const fileUrl = `${req.protocol}://${req.get("host")}/uploads/${
      req.file.filename
    }`;
    res
      .status(200)
      .json({ message: "Image uploaded successfully.", url: fileUrl });
  } else {
    res.status(400).send("Failed to upload image.");
  }
});

app.get("/uploads", (req, res) => {
  fs.readdir("public/uploads", (err, files) => {
    if (err) {
      res.status(500).send("Error reading files");
    } else {
      res.json(files);
    }
  });
});

const listener = app.listen(process.env.PORT || 3000, () => {
  console.log(`Your app is listening on port ${listener.address().port}`);
});
