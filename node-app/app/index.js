var express = require('express');
var app = express();

app.get('/', function (req, res) {
  var looqers = ["Will", "Gabs", "Math"]
  res.send(looqers);
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
