var sys = require("sys"),
my_http = require("http"),
path = require("path"),
url = require("url"),
filesys = require("fs");
var events = require('events');
var github = require('octonode');

var github_emitter = new events.EventEmitter();	

function get_data() {

	var accesstoken = '3c00f2dc6a4be9a9b1926c65b7451aabb48b06fe';

	var client = github.client(accesstoken);
	
	client.get('orgs/coeus-solutions', function(err, status, body){
		//body is already json, you can start parsing it
		github_emitter.emit("data", JSON.stringify(body));
		
	});
}


my_http.createServer(function(request,response){
	response.writeHeader(200, { "Content-Type" : "text/plain" });
	get_data();
	response.write("Fetching...");
	var listener = github_emitter.once("data", function(data) {
				
	    		response.write(data);
	    		response.end();
			});
}).listen(8080);

sys.puts("Server Running on 8080");
