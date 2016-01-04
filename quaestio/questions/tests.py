import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):
    def test_is_recent_for_various_created_dates(self):
        """
        is_recent() should return False for questions created in the future.
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


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('questions:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions created in the past should be displayed on the index page.
        """
        create_question(content="Past question.", days=-30)
        response = self.client.get(reverse('questions:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions created in the future should not be displayed on the index page.
        """
        create_question(content="Future question.", days=30)
        response = self.client.get(reverse('questions:index'))
        self.assertContains(response, "No questions available.",
                            status_code=200)
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(content="Past question.", days=-30)
        create_question(content="Future question.", days=30)
        response = self.client.get(reverse('questions:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(content="Past question", days=-30)
        create_question(content="Another past question", days=-5)
        response = self.client.get(reverse('questions:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Another past question>', '<Question: Past question>']
        )


class QuestionDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question created in the future should return a 404 not found.
        """
        future_question = create_question(content='Future question.', days=5)
        response = self.client.get(reverse('questions:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question created in the past should display the question's text.
        """
        past_question = create_question(content='Past Question.', days=-5)
        response = self.client.get(reverse('questions:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.content, status_code=200)


def create_question(content, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(content=content, created=time)
