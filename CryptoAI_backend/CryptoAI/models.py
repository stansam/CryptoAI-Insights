from django.db import models

class VideoArticlePost(models.Model):
    title = models.CharField(max_length=255)
    channel_name = models.CharField(max_length=100)
    url = models.URLField()
    date_published = models.DateField()
    platform = models.CharField(max_length=100)
    category_topic = models.CharField(max_length=100)
    description = models.TextField()

class TokenCoin(models.Model):
    video_article_post = models.ForeignKey(VideoArticlePost, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    NETWORK_CHOICES = [
        ('Ethereum', 'Ethereum'),
        ('Binance Smart Chain', 'Binance Smart Chain'),
        ('Solana', 'Solana'),
        # Add more choices as needed
    ]
    network = models.CharField(max_length=100, choices=NETWORK_CHOICES)
    RECOMMENDATION_CHOICES = [
        ('Buy', 'Buy'),
        ('Hold', 'Hold'),
        ('Sell', 'Sell'),
    ]
    recommendation_type = models.CharField(max_length=10, choices=RECOMMENDATION_CHOICES)
    timestamp_link = models.URLField(blank=True, null=True)
    reason_for_recommendation = models.TextField()
    associated_tags_keywords = models.TextField()
    channel_tags_keywords = models.TextField()
    CATEGORY_CHOICES = [
        ('DeFi', 'DeFi'),
        ('NFT', 'NFT'),
        ('Privacy', 'Privacy'),
        ('Smart Contract', 'Smart Contract'),
        # Add more choices as needed
    ]
    category_tag = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

class SocialMediaChannel(models.Model):
    name = models.CharField(max_length=100)

class Analyst(models.Model):
    name = models.CharField(max_length=100)
    date_of_analysis = models.DateField()
    rating = models.FloatField(null=True)
    OVERALL_SENTIMENT_CHOICES = [
        ('Positive', 'Positive'),
        ('Neutral', 'Neutral'),
        ('Negative', 'Negative'),
    ]
    overall_sentiment = models.CharField(max_length=10, choices=OVERALL_SENTIMENT_CHOICES)

class VideoArticlePostAnalysis(models.Model):
    video_article_post = models.OneToOneField(VideoArticlePost, on_delete=models.CASCADE)
    main_topics_covered = models.TextField()
    key_takeaways = models.TextField()

class VerificationConfirmation(models.Model):
    verified = models.BooleanField()
    additional_comments_verification_notes = models.TextField()

class AdditionalInformation(models.Model):
    video_article_post = models.OneToOneField(VideoArticlePost, on_delete=models.CASCADE)
    other_relevant_channels = models.TextField()
    notes_comments = models.TextField()

class AnalystDetails(models.Model):
    analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE)
    date_of_analysis = models.DateField()
