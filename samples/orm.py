from mongoengine import *

c = connect('project1', host='localhost', port=27017)

print(c)


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


class SampleNew(object):
    def __new__(cls):
        print("Creating instance")
        return super(SampleNew, cls).__new__(cls)

    def __init__(self):
        print("Init is called")


# ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()

users = User.objects()
for user in users:
    print(user.email)


a = SampleNew()