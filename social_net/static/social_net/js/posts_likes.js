$(document).ready(function () {
    $(".like-btn, .unlike-btn").on("click", function () {
        var postId = $(this).data("post-id");
        var likesCountElement = $(this).closest('.media').find('.likes-count');
        var isLiked = $(this).data("is-liked");

        // Get the CSRF token from the cookie
        var csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];

        // Send an AJAX request to handle the like/unlike action
        $.ajax({
            url: "/like_post/" + postId + "/",
            type: "POST",
            dataType: "json",
            headers: { "X-CSRFToken": csrftoken },
            success: function (data) {
                // Update the likes count on the page
                likesCountElement.text(data.likes_count);

                // Toggle the "is-liked" data attribute
                $(".like-btn, .unlike-btn").data("is-liked", data.is_liked);

                // Show/hide buttons based on like status
                if (data.is_liked) {
                    $(".like-btn").hide();
                    $(".unlike-btn").show();
                } else {
                    $(".like-btn").show();
                    $(".unlike-btn").hide();
                }
            },
            error: function (error) {
                console.log("Error liking/unliking post:", error);
            }
        });
    });
});