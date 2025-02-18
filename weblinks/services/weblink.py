from .image_url import ImageUrlService
from database.repository.weblinks import WebLinkRepository

class WebLinkService:
    @staticmethod
    def create_weblink(data, user):
        image_url = ImageUrlService.generate_image_url(data.get('url'))

        inputdata = {
            'created_by': user, 
            'name': data.get('name'),  
            'url': data.get('url'),
            'category': data.get('category'),
            'image_url': image_url,
        }

        WebLinkRepository.create(inputdata)
