import requests


class Post:
    def __init__(self):
        URL = "https://api.npoint.io/c0d395667a3246bce849"
        response = requests.get(URL)
        self.blog_posts = response.json()

    def get_specified_blog(self, blog_id):
        for item in self.blog_posts:
            if blog_id == item['id']:
                return item
        return None
