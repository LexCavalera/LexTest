var app = app || {};

app.Book = Backbone.Model.extend({
    defaults: {
<<<<<<< HEAD
=======
        coverImage: 'img/placeholder.png',
>>>>>>> fc9324f29d785d9fb69595fcdecf2f0e01524a6b
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