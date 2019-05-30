from rest_framework import *

from .views import *

router = router.SimpleRouter()
router.register(r'news', NewsListViewSet)
urlpatterns = router.urls