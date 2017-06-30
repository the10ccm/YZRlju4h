# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date, timedelta

from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CustomUser

User = get_user_model()

class TestCore(TestCase):
    """ Test Core Application """

    def test_model(self):
        """ Test the model """
        username = 'test123'
        password = '1234qwer'
        birthday = date.today()
        bizzfuzz = 30
        user = User.objects.create(username=username, password=password)
        profile = CustomUser.objects.create(user=user, birthday=birthday,
                                            bizzfuzz_number=bizzfuzz)
        self.assertEqual(profile.id, 1)
        self.assertEqual(profile.birthday, birthday)
        self.assertEqual(profile.bizzfuzz_number, bizzfuzz)

    def test_custom_user(self):
        """ Test views """
        date_format = '%Y-%m-%d'
        username = 'new_test123'
        password = '1234qwer'
        birthday = date.today()
        bizzfuzz = 30
        # Empty list
        response = self.client.get('/')
        self.assertNotContains(response, username)
        # Create a custom user
        data = {
            'username': username,
            'password1': password,
            'password2': password,
            'profile-0-birthday': birthday.strftime(date_format),
            'profile-0-bizzfuzz_number': str(bizzfuzz),
            'profile-TOTAL_FORMS': '1',
            'profile-INITIAL_FORMS':'0',
            'profile-MAX_NUM_FORMS':''}
        response = self.client.post('/user/create/', data)
        # Check off the list view
        self.assertEqual(response.status_code, 302)
        profile = CustomUser.objects.get(user__username=username)
        response = self.client.get('/')
        self.assertContains(response, username)
        self.assertContains(response, 'blocked')
        self.assertContains(response, 'BizzFuzz')
        profile.birthday = date.today() - timedelta(days=365*15)
        profile.bizzfuzz = 10
        profile.save()
        response = self.client.get('/')
        self.assertContains(response, 'allowed')
        self.assertContains(response, 'Fuzz')
        profile.bizzfuzz = 9
        profile.save()
        response = self.client.get('/')
        self.assertContains(response, 'Bizz')
        profile.bizzfuzz = 4
        profile.save()
        response = self.client.get('/')
        self.assertContains(response, '4')

        # Check the update view
        settings.DATE_INPUT_FORMATS = date_format
        response = self.client.get('/user/%s/' % profile.pk)
        self.assertContains(response, username)
        self.assertContains(response, profile.birthday.strftime(date_format))
        data = {
            'birthday': '1920-11-13',
            'bizzfuzz_number': 41
        }
        response = self.client.post('/user/%s/' % profile.pk, data)
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertContains(response, 'allowed')
        self.assertContains(response, '41')

        # Check the delete view
        response = self.client.get('/user/%s/delete/' % profile.pk)
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/')
        self.assertNotContains(response, username)
