from database.repository.weblinks import WebLinkRepository
from database.repository.shares import ShareRepository

class SearchService:
    @staticmethod
    def create_weblink_dict(weblink, can_delete, can_edit):
        return {
            'id': weblink.id,
            'name': weblink.name,
            'url': weblink.url,
            'category': weblink.category,
            'shared': weblink.shared,
            'image_url': weblink.image_url,
            'can_delete': can_delete,
            'can_edit': can_edit
        }

    @staticmethod
    def create_my_weblink_dict(my_weblink):
        return [SearchService.create_weblink_dict(weblink, can_delete=True, can_edit=True) for weblink in my_weblink]
    
    @staticmethod
    def create_share_weblink_dict(share_weblink):
        weblink_data = []
        for share in share_weblink:
            can_edit = True if share.permission == 'write' else False
            weblink_dict = SearchService.create_weblink_dict(
                share.shared_by_weblink, 
                can_delete=False, 
                can_edit=can_edit
            )
            weblink_data.append(weblink_dict)
        return weblink_data

    @staticmethod
    def get_weblink(category, keyword, user):
        def get_weblink_data(category_filter=None):
            my_weblink = WebLinkRepository.get_weblink_by_created_by(user, keyword, category_filter)
            return SearchService.create_my_weblink_dict(my_weblink)

        def get_shared_weblink_data(category_filter=None):
            share_weblink = ShareRepository.get_share_by_shared_with_user(user, keyword, category_filter)
            return SearchService.create_share_weblink_dict(share_weblink)

        if category == 'all':
            my_weblink_data = get_weblink_data()
            share_weblink_data = get_shared_weblink_data()
            return my_weblink_data + share_weblink_data

        if category == 'shared':
            return get_shared_weblink_data()

        if category in ['favorites', 'work', 'reference', 'education']:
            my_weblink_data = get_weblink_data(category)
            share_weblink_data = get_shared_weblink_data(category)
            return my_weblink_data + share_weblink_data

        return []
