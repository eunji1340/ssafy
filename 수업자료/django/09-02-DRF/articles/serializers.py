from rest_framework import serializers 
from .models import Article, Comment


# 게시글의 일부 필드를 직렬화 하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):

    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

    def get_num_of_comments(self, obj):
        return obj.num_of_comments


# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
    
    comment_set = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        #read_only_fields = ('article',)