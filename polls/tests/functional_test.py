from selenium import webdriver
import datetime

from django.test import TestCase, LiveServerTestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


class FunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpTestData(cls):
        """Setup question and its choices"""
        time = timezone.now()
        question = Question.objects.create(question_text='Question 1', pub_date=time)
        question.choice_set.create(choice_text='Choice 1')
        # question.choice_set.create(choice_text='Choice 2')

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_contain_hot_topic_heading(self):
        """Test if `h1` tag contains 'Hot Topics' """
        url = reverse('polls:index')
        self.browser.get("%s%s" % (self.live_server_url, url))
        h1_tag = self.browser.find_element_by_tag_name('h1')
        self.assertEqual(h1_tag.text, 'Hot Topics')
    