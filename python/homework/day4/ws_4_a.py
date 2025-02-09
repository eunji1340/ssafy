from conf import settings
from utils import create_url

result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)