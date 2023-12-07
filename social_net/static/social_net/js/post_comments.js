$(document).ready(function() {
    // Get the post_id from the data attribute of the comments-container
    var post_id = $('#comments-container').data('post-id');

    // API endpoint for comments
    var apiUrl = '/api/v1/posts/' + post_id + '/comments/';

    // Use jQuery AJAX to fetch comments
    $.ajax({
        url: apiUrl,
        method: 'GET',
        success: function(data) {
            // Assuming data is an array of comments
            var comments = data;

            // Iterate through comments and append to the comments-container
            for (var i = 0; i < comments.length; i++) {
                $('#comments-container').append('<p class="ms-2">' + comments[i].username + ': ' + comments[i].content + '</p>');
            }
        },
        error: function(error) {
            console.log('Error fetching comments:', error);
        }
    });
});