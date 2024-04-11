from rest_framework import generics
from .models import *
from .serializers import *

class VideoArticlePostListCreate(generics.ListCreateAPIView):
    queryset = VideoArticlePost.objects.all()
    serializer_class = VideoArticlePostSerializer

class TokenCoinListCreate(generics.ListCreateAPIView):
    queryset = TokenCoin.objects.all()
    serializer_class = TokenCoinSerializer

class SocialMediaChannelListCreate(generics.ListCreateAPIView):
    queryset = SocialMediaChannel.objects.all()
    serializer_class = SocialMediaChannelSerializer

class AnalystListCreate(generics.ListCreateAPIView):
    queryset = Analyst.objects.all()
    serializer_class = AnalystSerializer

class VideoArticlePostAnalysisListCreate(generics.ListCreateAPIView):
    queryset = VideoArticlePostAnalysis.objects.all()
    serializer_class = VideoArticlePostAnalysisSerializer

class VerificationConfirmationListCreate(generics.ListCreateAPIView):
    queryset = VerificationConfirmation.objects.all()
    serializer_class = VerificationConfirmationSerializer

class AdditionalInformationListCreate(generics.ListCreateAPIView):
    queryset = AdditionalInformation.objects.all()
    serializer_class = AdditionalInformationSerializer

class AnalystDetailsListCreate(generics.ListCreateAPIView):
    queryset = AnalystDetails.objects.all()
    serializer_class = AnalystDetailsSerializer

