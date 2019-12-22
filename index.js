var express = require('express');
var app = express();
var expressWs = require('express-ws')(app);

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.ws('/echo', function(ws, req) {
  ws.on('message', function(msg) {
    ws.send(msg);
  });
});

app.listen(3000, function () {
  console.log('Listening on port 3000!');
});

