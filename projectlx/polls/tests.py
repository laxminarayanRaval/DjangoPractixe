from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """was_published_recently() returns False for questions whose pub_date is in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """was_published_recently() returns False for questions whose pub_date is older then 1 day."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """was_published_recently() returns True for questions whose pub_date is within the last day."""
        time =  timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True) 

    def create_question(que_text, days):
        """Create a question with the given 'que_text' and published the given number of 'days' offset to now 
        (negative for questions published in the past, positive for question that have yet to be published)"""
        time = timezone.now + datetime.timedelta(days=days)
        return Question.objects.create(que_text=que_text, pub_date=time)

    class QuestionIndexViewTests(TestCase):
        def test_no_questions(self):
            """If no Question Exists, Appropriate Message is displayed"""
            response = self.client.get(reverse('polls:index'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'No pollls are available.')
            self.assertQuerysetEqual(response.context['latest_que_list'],[])

        def test_past_question(self):
            """Question with a pub_date in the past are displayed on the index page."""
            question = create_question(que_text="This is past Question.", days=-30)
            response = self.client.get(reverse('polls:index'))
            self.assertQuerysetEqual(
                response.context['latest_que_list'],
                [question],
            )
        
        def test_future_question(self):
            """Question with a pub_date in the future aren't displayed on the index page."""
            create_question(que_text="Future Question", days=30)
            response = self.client.get(reverse('polls:index'))
            self.assertContains(response, "Polls will visible in near future.")
            self.assertQuerysetEqual(response.context['latest_question_list'],[])

        def test_future_question_and_past_question(self):
            """Even if both past and future questions exists, only past questions are displayed"""
            question = create_question(que_text="Past Question.", days=-30)
            create_question(que_text="Future Question.", days=30)
            response = self.client.get(reverse('polls:index'))
            self.assertQuerysetEqual(
                response.context['lastest_que_list'],
                [question],
            )

        def test_two_past_question(self):
            """The Question index page may display multiple questions."""
            que1 = create_question(que_text="Past Question 1", days=-30)
            que2 = create_question(que_text="Past Question 2", days=-5)
            response =  self.client.get(reverse('polls:index'))
            self.assertQuerysetEqual(
                response.context['latest_que_list'],
                [que1, que2],
            )
            