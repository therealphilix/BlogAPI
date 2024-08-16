from rest_framework import serializers 
from .models import *
import logging

logger = logging.getLogger(__name__)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'title', 'slug'
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'category',
            'created_at', 'published_at', 'status' 
        ]
       
    def create(self, validated_data):
        author_id = self.context['author_id']
        logger.debug(f"Creating post with author_id: {author_id}")
        return Post.objects.create(author_id=author_id, **validated_data)
    
class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'status','content', 'updated_at'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id', 'phone', 'birth_date','topic'
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'content']

    def create(self, validated_data):
        post_id = self.context['post_id']
        author_id = self.context['author_id']
        return Comment.objects.create(post_id=post_id, author_id=author_id, **validated_data)