from rest_framework import serializers
from .models import VideoArticlePost, TokenCoin, SocialMediaChannel, Analyst, VideoArticlePostAnalysis, VerificationConfirmation, AdditionalInformation, AnalystDetails

class VideoArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoArticlePost
        fields = '__all__'

class TokenCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenCoin
        fields = '__all__'

class SocialMediaChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaChannel
        fields = '__all__'

class AnalystSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyst
        fields = '__all__'

class VideoArticlePostAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoArticlePostAnalysis
        fields = '__all__'

class VerificationConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationConfirmation
        fields = '__all__'

class AdditionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInformation
        fields = '__all__'

class AnalystDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalystDetails
        fields = '__all__'
