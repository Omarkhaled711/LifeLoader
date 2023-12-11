from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from social_net.models import Post, Comment, Like
from social_net.api.v1.serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count, Subquery, OuterRef


class CustomPageNumberPagination(PageNumberPagination):
    """
    API view for retrieving a list of all posts ordered by creation date.

    Attributes:
        - page_size: The number of items to include on each page.
        - page_size_query_param: The query parameter to specify the page size.
        - max_page_size: The maximum allowed page size.
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 300


class PostListView(generics.ListAPIView):
    """
    API view for retrieving a list of all posts ordered by creation date.
    Each post is annotated with the counts of likes and comments.

    Returns:
        A paginated list of posts, serialized using PostSerializer, ordered by creation date.
    """
    queryset = Post.objects.annotate(likes_count=Count(
        'likes'), comments_count=Count('comments')).order_by('-date_created')
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination


class PostListViewTopLikes(generics.ListAPIView):
    """
    API view for retrieving a list of posts ordered by the number of likes 
    and comments.

    Each post is annotated with the counts of likes and comments, and the queryset
    is ordered in descending order based on the likes_count, comments_count, and
    date_created to handle ties.

    Parameters:
        - No additional parameters.

    Returns:
        A paginated list of posts, serialized using PostSerializer, ordered by likes
        and comments counts.

    Example:
        To retrieve the top liked posts:

        ```
        GET /api/v1/posts/top_likes/
        ```

    Note:
        This view uses Subquery and OuterRef to efficiently calculate the likes_count
        and comments_count for each post individually, ensuring accurate ordering.

    Pagination:
        The response is paginated using CustomPageNumberPagination.
    """
    queryset = Post.objects.annotate(
        likes_count=Subquery(
            Like.objects.filter(post=OuterRef('pk')).values('post').annotate(
                like_count=Count('id')).values('like_count')[:1]
        ),
        comments_count=Subquery(
            Comment.objects.filter(post=OuterRef('pk')).values('post').annotate(
                comment_count=Count('id')).values('comment_count')[:1]
        )
    ).order_by('-likes_count', '-comments_count', '-date_created')
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination


class PostListViewTopComments(generics.ListAPIView):
    """
    API view for retrieving a list of posts ordered by the number of comments 
    and likes.

    Each post is annotated with the counts of likes and comments, and the queryset
    is ordered in descending order based on the comments_count, likes_count, and
    date_created to handle ties.

    Parameters:
        - No additional parameters.

    Returns:
        A paginated list of posts, serialized using PostSerializer, ordered comments counts
        and likes count.

    Example:
        To retrieve the top commented posts:

        ```
        GET /api/v1/posts/top_likes/
        ```

    Note:
        This view uses Subquery and OuterRef to efficiently calculate the likes_count
        and comments_count for each post individually, ensuring accurate ordering.

    Pagination:
        The response is paginated using CustomPageNumberPagination.
    """
    queryset = Post.objects.annotate(
        likes_count=Subquery(
            Like.objects.filter(post=OuterRef('pk')).values('post').annotate(
                like_count=Count('id')).values('like_count')[:1]
        ),
        comments_count=Subquery(
            Comment.objects.filter(post=OuterRef('pk')).values('post').annotate(
                comment_count=Count('id')).values('comment_count')[:1]
        )
    ).order_by('-comments_count', '-likes_count', '-date_created')
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination


class UserPostListView(generics.ListAPIView):
    """
    API view for retrieving a list of posts by a specific user.

    Parameters:
        - username: The username of the target user.

    Returns:
        A paginated list of posts by the specified user, serialized using PostSerializer,
        ordered by creation date.
    """
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        # Annotate the queryset with counts of likes and comments
        queryset = Post.objects.filter(author=user).annotate(
            likes_count=Count('likes'),
            comments_count=Count('comments')
        ).order_by('-date_created')

        return queryset


class CommentListView(generics.ListCreateAPIView):
    """
    API view for retrieving and creating comments on a specific post.

      Parameters:
        - post_id: The ID of the target post.

    Returns:
        A paginated list of comments on the specified post, serialized using 
        CommentSerializer.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id).select_related('user')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)


class LikeListView(generics.ListCreateAPIView):
    """
    API view for retrieving and creating likes on a specific post.

        Parameters:
        - post_id: The ID of the target post.

    Returns:
        A paginated list of likes on the specified post, serialized
        using LikeSerializer.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)
