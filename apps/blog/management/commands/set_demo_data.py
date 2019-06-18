# -*- coding: utf-8 -*-
from django.core.management import BaseCommand

from blog.models import Post
from users.models import User

text = """
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tortor id aliquet lectus proin nibh nisl condimentum id venenatis. Libero justo laoreet sit amet cursus sit amet dictum sit. Non diam phasellus vestibulum lorem sed risus. Suspendisse interdum consectetur libero id faucibus nisl tincidunt. Lorem sed risus ultricies tristique nulla aliquet. Interdum consectetur libero id faucibus nisl. Dui sapien eget mi proin. Adipiscing at in tellus integer feugiat scelerisque. Arcu non odio euismod lacinia at quis risus. Velit sed ullamcorper morbi tincidunt ornare massa eget. Elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at. Purus gravida quis blandit turpis cursus. Ante metus dictum at tempor commodo ullamcorper a lacus. Morbi leo urna molestie at elementum eu facilisis sed. Turpis massa tincidunt dui ut ornare lectus sit amet est. Quisque sagittis purus sit amet volutpat consequat mauris. Sed blandit libero volutpat sed cras. Enim nulla aliquet porttitor lacus. Ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue.</p>
<p>Ac orci phasellus egestas tellus rutrum tellus pellentesque eu. Sapien nec sagittis aliquam malesuada bibendum arcu vitae elementum curabitur. Ut morbi tincidunt augue interdum velit. Sagittis id consectetur purus ut. Viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper eget. Hac habitasse platea dictumst quisque sagittis. Fermentum odio eu feugiat pretium nibh. Arcu odio ut sem nulla pharetra. In egestas erat imperdiet sed. Ac turpis egestas integer eget aliquet nibh praesent tristique magna. Malesuada fames ac turpis egestas integer. Sit amet nisl suscipit adipiscing bibendum est. Ornare arcu odio ut sem nulla pharetra diam sit amet. Imperdiet massa tincidunt nunc pulvinar sapien. Sed viverra tellus in hac habitasse platea dictumst. Tincidunt ornare massa eget egestas.</p>
<p>Tellus orci ac auctor augue mauris augue neque gravida. Sit amet volutpat consequat mauris nunc congue nisi vitae suscipit. Turpis egestas maecenas pharetra convallis posuere morbi leo urna. Praesent semper feugiat nibh sed pulvinar. Volutpat diam ut venenatis tellus. Eu sem integer vitae justo eget magna fermentum iaculis eu. Tortor id aliquet lectus proin nibh. Egestas tellus rutrum tellus pellentesque eu. Lorem dolor sed viverra ipsum nunc aliquet bibendum enim. Elit sed vulputate mi sit amet mauris commodo quis.</p>
<p>Pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. Nunc scelerisque viverra mauris in aliquam sem. Elementum curabitur vitae nunc sed velit dignissim sodales ut eu. Vulputate ut pharetra sit amet. Risus nullam eget felis eget nunc lobortis mattis aliquam faucibus. Donec ultrices tincidunt arcu non. Tincidunt arcu non sodales neque. Urna nunc id cursus metus aliquam eleifend. Vestibulum morbi blandit cursus risus at ultrices. Nunc sed velit dignissim sodales ut eu sem integer vitae.</p>
<p>Est ante in nibh mauris cursus mattis molestie a iaculis. Nec ullamcorper sit amet risus nullam. Placerat duis ultricies lacus sed turpis. Libero enim sed faucibus turpis in. Volutpat est velit egestas dui. Enim lobortis scelerisque fermentum dui faucibus in ornare. Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Tortor aliquam nulla facilisi cras fermentum. Mi sit amet mauris commodo quis. Vitae nunc sed velit dignissim. Tellus molestie nunc non blandit massa enim. Elit sed vulputate mi sit amet mauris. Quis auctor elit sed vulputate mi. Donec pretium vulputate sapien nec sagittis aliquam malesuada. Condimentum id venenatis a condimentum vitae sapien pellentesque. Lobortis scelerisque fermentum dui faucibus in.</p>
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

