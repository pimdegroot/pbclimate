var http = require('http');
var request = http.get("http://172.30.101.3:8080/temp.json", function(response) {
  var str = ''

  response.on('data', function (chunk) {
    str += chunk;
  });

  response.on('end', function() {
    console.log(str);
  });
});
//console.log(request)
