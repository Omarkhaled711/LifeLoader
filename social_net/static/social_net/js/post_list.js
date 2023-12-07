        // Function to fetch and display posts
        function fetchPosts(page) {
            $.ajax({
                url: `/api/v1/posts/?page=${page}`,
                method: 'GET',
                success: function(data) {
                    displayPosts(data.results);
                    displayPagination(data);
                },
                error: function(error) {
                    console.error('Error fetching posts:', error);
                }
            });
        }
        function displayPosts(posts) {
            var container = $('#posts-container');
            container.empty();
        
            $.each(posts, function(index, post) {
                // Fetch user details separately
                $.ajax({
                    url: `api/v1/users/${post.author}/`,
                    method: 'GET',
                    async: false,
                    success: function(author) {
                        var profileUrl = `/profile/${author.user.username}/`;
                        var postUrl = `/post/${post.id}/`
                        var postHtml = `
                            <article class="media content-section">
                                <div class="row">
                                    <div class="col-md-1">
                                        <img class="rounded-circle article-img" src="${author.profile_pic}" alt="post's author profile picture">
                                    </div>
                                    <div class="col-md-10 ms-3">
                                        <div class="media-body">
                                            <div class="d-flex justify-content-between align-items-center">
                                                <div>
                                                    <a class="ms-1" href="${profileUrl}">${author.user.username}</a>
                                                    <small class="text-muted">${post.date_created}</small>
                                                </div>
                                            </div>
                                            <hr class="my-2"> <!-- Horizontal line between name/date and post title/content -->
                                            <h2><a class="article-title" href="${postUrl}">${post.title}</a></h2>
                                            <p class="article-content">${post.content}</p>
                                        </div>
                                    </div>
                                </div>
                            </article>
                        `;
                        container.append(postHtml);
                    },
                    error: function(error) {
                        console.error('Error fetching user details:', error);
                    }
                });
            });
        }
        

        // Function to display pagination links
        function displayPagination(data) {
            var paginationHtml = '';
            var current_num;
            var tot_num = Math.floor(parseInt(data.count)/data.results.length)
            if (parseInt(data.count) % data.results.length != 0) {
                tot_num += 1;
            }
        
            if (data.previous) {
                paginationHtml += `<a class="btn btn-outline-secondary mb-4" href="#" onclick="fetchPosts(1);">First</a>`;
                }

            if (!data.next) {
                if (data.previous) {
                    var match = data.previous.match(/page=(\d+)/)
                    tot_num = 2;
                    if (match) {
                        tot_num = parseInt(data.previous.match(/page=(\d+)/)[1]) + 1;
                    }
                }
                else {
                    tot_num = 1;
                }
            }
        
            if (tot_num > 0) {
                if (data.next) {
                    current_num = parseInt(data.next.match(/page=(\d+)/)[1]) - 1;
                }
                else if (data.previous) {
                    var match = data.previous.match(/page=(\d+)/)
                    current_num = 2;
                    if (match) {
                        current_num = parseInt(data.previous.match(/page=(\d+)/)[1]) + 1;
                    }
                }
                for (var i = Math.max(1, current_num - 3); i <= Math.min(current_num + 3, tot_num); i++) {
                    if (i != current_num) {
                        paginationHtml += `<a class="btn btn-outline-secondary mb-4" href="#" onclick="fetchPosts(${i});">${i}</a>`;
                    }
                    else {
                        paginationHtml += `<a class="btn btn-secondary mb-4" href="#" onclick="fetchPosts(${i});">${i}</a>`;
                    }
                }
                if (data.next) {
                    paginationHtml += `<a class="btn btn-outline-secondary mb-4" href="#" onclick="fetchPosts(${tot_num});">Last</a>`;
                }
            }
        
            $('#pagination-container').html(paginationHtml);
        }
        

        // Initial fetch when the page loads
        $(document).ready(function() {
            fetchPosts(1);
        });
