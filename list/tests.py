from django.test import TestCase,Client
from django.contrib.auth.models import User
from .models import List
# Create your tests here.
class Listtest(TestCase):
    def setUp(self):
        #create user
        self.user=User.objects.create_user('peter','peter@email.com','123456')

        #assign client role to the user
        self.client_user=self.user

        #create list
        list1=List.objects.create(user=self.user,text='finish the project')
        list2=List.objects.create(user=self.user,text='call my baby')
        list3=List.objects.create(user=self.user,text='clean the house')
        list4=List.objects.create(user=self.user,text='get some sleep')

    def test_list(self):
        lists=List.objects.all()
        self.assertEqual(lists.count(),4)

    def test_index(self):
        self.client.login(username='peter',password='123456')
        response=self.client.get('')
        self.assertEqual(len(response.context['lists']),4)

        

