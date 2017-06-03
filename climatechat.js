const irc = require('irc') 
var http = require('http');

const client = new irc.Client('irc.smurfnet.ch', 'pbclimate',{
    channels : ['#pixelbar']
})

client.addListener('message', (from, to, message) => {
   //console.log(from, to, message)

    if(message.indexOf('!temp') != -1) {
      var request = http.get("http://172.30.101.3:8080/temp.json", function(response) {
        var str = ''

        response.on('data', function (chunk) {
          str += chunk;
        });

        response.on('end', function() {
          //console.log(str);
          try{
            const tempdata = JSON.parse(str)
            client.say('#pixelbar','Temperature is '+tempdata.BarometerTemperature+'C, Pressure is '+tempdata.BarometerPressure + 'Pa and Humidity is '+tempdata.Humidity+'%')
          } catch (e) {
            console.log('error',e)
          }
        });
      });
    }
    
    if(message.indexOf('!prod') != -1) {
      client.say('#pixelbar','Au')
    }
})

client.addListener('error', function(message) {
    console.log('IRC error: ', message);
});
