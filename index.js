#!/usr/bin/env node

var fs = require('fs');

/**
 * Module dependencies.
 */

var express = require('express');
//var app = require('./app');
var app = express();
var debug = require('debug')('server:server');
//var http = require('http');
var https = require('https');


/**
 * Get port from environment and store in Express.
 */

var port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

app.get('/', function (req, res) {
  res.sendFile('/test-website/index.html' ,{ root : __dirname});
})

/**
 * Create HTTP server.
 */

//var server = http.createServer(app);
var server = https.createServer({
  key: fs.readFileSync('server.key'),
  cert: fs.readFileSync('server.cert')
}, app)
.listen(port, function () {
  console.log('Example app listening on port 3000! Go to https://localhost:3000/')
})
var io = require('socket.io').listen(server);

/**
 * Listen on provided port, on all network interfaces.
 */

//server.listen(port);
//server.on('error', onError);
//server.on('listening', onListening);

/**
 * Normalize a port into a number, string, or false.
 */

function normalizePort(val) {
  var port = parseInt(val, 10);

  if (isNaN(port)) {
    // named pipe
    return val;
  }

  if (port >= 0) {
    // port number
    return port;
  }

  return false;
}

/**
 * Event listener for HTTP server "error" event.
 */

function onError(error) {
  if (error.syscall !== 'listen') {
    throw error;
  }

  var bind = typeof port === 'string'
    ? 'Pipe ' + port
    : 'Port ' + port;

  // handle specific listen errors with friendly messages
  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use');
      process.exit(1);
      break;
    default:
      throw error;
  }
}

/**
 * Event listener for HTTP server "listening" event.
 */

function onListening() {
  var addr = server.address();
  var bind = typeof addr === 'string'
    ? 'pipe ' + addr
    : 'port ' + addr.port;
  debug('Listening on ' + bind);
}

io.on('connection', function(socket){
  socket.on('temperature', function(msg){
    console.log(msg);
    console.log("got temperature message");
    var parsedmsg2 = JSON.parse(msg);
    var nmsg2 = parsedmsg2.temp;
    fs.writeFile('/home/pi/MindLabs/temp.txt', nmsg2, function(err){
      if(err) {
        console.log(err);
      } 
    });
  });

});
