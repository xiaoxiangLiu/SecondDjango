import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Questions
# Create your tests here.


class QuestionsMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        """
        在将来发布的问卷应该返回False
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Questions(pub_data=time)
        self.assertIs(future_question.was_published_recently(), False)


