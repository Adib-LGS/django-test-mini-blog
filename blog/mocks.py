from django.http import Http404

class Post():

    POSTS = [
        {'id': 1, 'title': 'First Post', 'body':'What ze first'},
        {'id': 2, 'title': 'Second Post', 'body':'Second One'},
        {'id': 3, 'title': 'Third Post', 'body':'Tres Amigos'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS
        
    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            raise Http404('POST {} NOT FOUND'.format(id))