var app = app || {};

app.Book = Backbone.Model.extend({
    defaults: {
        name: 'No title',
        author: 'Unknown',
        release_date: 'Unknown',
        keywords: 'None'
    },
	
	parse: function( response ) {
		response.id = response._id;
		return response;
	}
});