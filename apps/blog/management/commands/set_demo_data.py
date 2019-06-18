# -*- coding: utf-8 -*-
from django.core.management import BaseCommand

from blog.models import Post
from users.models import User

text = """
<div><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sodales ut etiam sit amet nisl purus. Ultricies leo integer malesuada nunc vel risus commodo viverra maecenas. Eros donec ac odio tempor orci dapibus. Dictum at tempor commodo ullamcorper a. Sed euismod nisi porta lorem mollis aliquam ut porttitor leo. Est ultricies integer quis auctor elit sed vulputate mi sit. Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Placerat duis ultricies lacus sed turpis tincidunt id aliquet. Enim nunc faucibus a pellentesque sit amet porttitor eget dolor.</p>
<p>Vel pharetra vel turpis nunc eget lorem. Nulla malesuada pellentesque elit eget gravida cum. Nunc aliquet bibendum enim facilisis gravida neque convallis. Quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus. Leo in vitae turpis massa. Odio euismod lacinia at quis risus sed vulputate odio ut. Sit amet nulla facilisi morbi tempus iaculis urna id volutpat. Ac turpis egestas maecenas pharetra convallis. Et netus et malesuada fames. Eleifend donec pretium vulputate sapien. Volutpat diam ut venenatis tellus in. Ut morbi tincidunt augue interdum velit euismod in. Faucibus nisl tincidunt eget nullam non nisi est. Convallis aenean et tortor at. Non diam phasellus vestibulum lorem sed. Nisl condimentum id venenatis a. Libero id faucibus nisl tincidunt eget nullam non nisi est. Accumsan sit amet nulla facilisi morbi tempus iaculis urna. Elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue. Massa enim nec dui nunc mattis enim ut tellus.</p>
<p>Pretium nibh ipsum consequat nisl vel pretium. Orci phasellus egestas tellus rutrum tellus. Lectus nulla at volutpat diam ut. Nunc mattis enim ut tellus elementum sagittis vitae et. Felis eget nunc lobortis mattis aliquam. Feugiat in ante metus dictum at tempor commodo. Laoreet id donec ultrices tincidunt arcu non. Neque laoreet suspendisse interdum consectetur libero. Nisl tincidunt eget nullam non nisi est. Diam maecenas sed enim ut sem viverra aliquet. Elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus.</p>
<p>Ultrices tincidunt arcu non sodales. Auctor urna nunc id cursus metus aliquam eleifend mi. Vivamus arcu felis bibendum ut tristique et egestas. Ultricies integer quis auctor elit. Risus quis varius quam quisque id. Nisl nisi scelerisque eu ultrices vitae auctor. Vitae elementum curabitur vitae nunc sed velit dignissim sodales ut. Et sollicitudin ac orci phasellus. Volutpat commodo sed egestas egestas fringilla phasellus faucibus. Iaculis eu non diam phasellus vestibulum lorem sed risus ultricies. Blandit aliquam etiam erat velit scelerisque in dictum. Non blandit massa enim nec dui nunc. Velit sed ullamcorper morbi tincidunt ornare massa eget. Nulla pellentesque dignissim enim sit. Malesuada fames ac turpis egestas sed. Vitae tempus quam pellentesque nec nam. Magnis dis parturient montes nascetur ridiculus. Pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat. Aliquam eleifend mi in nulla.</p>
<p>Sit amet purus gravida quis. Elementum curabitur vitae nunc sed. Tristique senectus et netus et malesuada fames ac turpis. Sit amet mauris commodo quis imperdiet massa tincidunt. Eu facilisis sed odio morbi quis commodo odio aenean sed. Tempus urna et pharetra pharetra massa. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper. Arcu vitae elementum curabitur vitae nunc sed velit dignissim. Vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa. Tempus egestas sed sed risus pretium quam vulputate dignissim suspendisse. Platea dictumst quisque sagittis purus sit amet volutpat consequat. Donec adipiscing tristique risus nec feugiat. Mattis aliquam faucibus purus in massa tempor nec. Tortor id aliquet lectus proin nibh nisl condimentum id venenatis. Sit amet massa vitae tortor condimentum lacinia quis vel.</p></div>
"""


class Command(BaseCommand):
    help = 'Set initial data to database'

    def add_arguments(self, parser):
        parser.add_argument('-u', type=int, default=6, dest='users')
        parser.add_argument('-b', type=int, default=6, dest='blogs')

    def handle(self, *args, **options):
        self.stdout.write('Start')

        # create users
        for i in range(1, options['users']+1):
            self.stdout.write(f'{i}')
            data = {
                'username': f'user_{i}',
                'email': f'useremail{i}@domain.com'
            }
            user, created = User.objects.get_or_create(**data)
            if created:
                user.set_password(f'password{i}')
                user.save()

            # create blogs
            for j in range(1, options['blogs'] + 1):
                data = {
                    'title': f'Some Title {j} Author {user.username}',
                    'text': f'{text}',
                    'author': user,
                }
                Post.objects.create(**data)

