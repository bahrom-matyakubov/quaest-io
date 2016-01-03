import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_is_recent_for_various_created_dates(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        now = timezone.now()
        long_ago = now - datetime.timedelta(days=30)
        future = now + datetime.timedelta(days=30)

        future_question = Question(created=future)
        recent_question = Question(created=now)
        old_question = Question(created=long_ago)
        self.assertFalse(future_question.is_recent(), 'Future questions cannot be recent')
        self.assertFalse(old_question.is_recent(), 'Old questions cannot be recent')
        self.assertTrue(recent_question.is_recent(), 'Recent question must be recent')
