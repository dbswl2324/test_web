from django.db import models


# 리뷰 데이터 분석결과
class ReviewAnalysis(models.Model):
    # primary key
    id = models.IntegerField(primary_key=True)

    # 블로그 게시글 고유 코드
    blog_code=models.varchar(max_length=30)

    #검색 물품의 코드
    article_code=models.IntegerField()

    #광고 분류
    check_advertise=models.TextField()
    
    #글요약
    content_summary=models.TextField()

    #긍정적인글
    content_positive=models.TextField()

    #부정적인글
    content_negative=models.TextField()

# 검색 물품 기록
class ArticleInfo(models.Model):
    # primary key
    article_code= models.IntegerField(primary_key=True)
    
    #검색된 게시물 이름
    search_name=models.vachar(max_length=30)

    # 리뷰 게시물 개수
    article_review_cnt= models.IntegerField()

    #순수 리뷰 게시물 개수
    article_pure_review_cnt= models.IntegerField()

    #검색 카운트
    search_cnt= models.IntegerField()


