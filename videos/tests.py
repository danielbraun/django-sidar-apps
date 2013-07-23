from django.test.testcases import TestCase
from django.core.urlresolvers import reverse
from videos.models import Video
from backoffice.models import Discipline


class ViewTests(TestCase):

    def test_video_list(self):
        """It should contain the link."""
        self.video = Video.objects.create(
            discipline=Discipline.objects.create(name_en='G', active=True),
            duration=10,
            year=2000
        )
        response = self.client.get(
            reverse('videos_index',
                    kwargs={'discipline': self.video.discipline.id}))
        self.assertIn(self.video, response.context['object_list'])
