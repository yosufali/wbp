var Fetch = require('whatwg-fetch');
var baseUrl = "http://localhost";

var service = {
	get: function(url) {
		return fetch(baseUrl + url)
		// Called when fetch succesfully returns
		.then(function(response) {
			return response.json();
		});
	},

	post: function(url, body) {
		return fetch(baseUrl + url, {
			method: 'POST',
			header: {
				'Accept': 'text/plain',
				'Content-Type': 'application/json'
			},
			crossOrigin: true,
			body: JSON.stringify(body)
		}).then(function(response) {
			console.log(response);
			return response;
		});
	}
};

module.exports = service;