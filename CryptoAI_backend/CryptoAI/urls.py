from django.urls import path
from .views import *
app_name = 'CryptoAI'
urlpatterns = [
    path('video-article-posts/', VideoArticlePostListCreate.as_view(), name='video-article-post-list-create'),
    path('token-coins/', TokenCoinListCreate.as_view(), name='token-coin-list-create'),
    path('social-media-channels/', SocialMediaChannelListCreate.as_view(), name='social-media-channel-list-create'),
    path('analysts/', AnalystListCreate.as_view(), name='analyst-list-create'),
    path('video-article-post-analyses/', VideoArticlePostAnalysisListCreate.as_view(), name='video-article-post-analysis-list-create'),
    path('verification-confirmations/', VerificationConfirmationListCreate.as_view(), name='verification-confirmation-list-create'),
    path('additional-informations/', AdditionalInformationListCreate.as_view(), name='additional-information-list-create'),
    path('analyst-details/', AnalystDetailsListCreate.as_view(), name='analyst-details-list-create'),
]