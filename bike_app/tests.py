from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserAccount, Complaint, BikeInfo, Complaint
from django.urls import reverse

"""
Test User
"""
class UserAccountTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@test.com')
        self.user_account = UserAccount.objects.create(user=self.user, name='Test', surname='User')

    def test_user_account_str(self):
        self.assertEqual(str(self.user_account), 'testuser')


    def test_generate_unique_url(self):
        self.user_account.generate_unique_url()
        self.assertIsNotNone(self.user_account.random_url)

    def test_welcome_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('bike_app:welcome_user', args=[str(self.user_account.random_url)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


"""
Test Complaint
"""
class ComplaintTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='testuser@test.com')
        self.user_account = UserAccount.objects.create(user=self.user, name='Test', surname='User')
        self.complaint = Complaint.objects.create(user=self.user_account,
                                                 Descriptions="This is test. I am so mad.")

    def test_description_str(self):
        check_text = str(self.complaint.Descriptions)
        ans_text = "This is test. I am so mad."
        self.assertEqual(check_text, ans_text)

    def test_feedback_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('bike_app:feedback', args=[str(self.user_account.random_url)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


"""
Test Bikes
"""
class BikeInfoTest(TestCase):
    def setUp(self):
        self.bike = BikeInfo.objects.create(
            BikeCode='001', BikeName='Mountain Bike', BikeType='Mountain',
            Descriptions='Sturdy bike', isBroken=False)

    def test_bikeCode(self):
        check_code = str(self.bike.BikeCode)
        ans_code = "001"
        self.assertEqual(check_code, ans_code)

    def test_bikeName(self):
        check_name = str(self.bike.BikeName)
        ans_name = 'Mountain Bike'
        self.assertEqual(check_name, ans_name)

    def test_bikeType(self):
        check_type = str(self.bike.BikeType)
        ans_type = 'Mountain'
        self.assertEqual(check_type, ans_type)

    def test_description_str(self):
        check_text = str(self.bike.Descriptions)
        ans_text = 'Sturdy bike'
        self.assertEqual(check_text, ans_text)

    def test_isBroken(self):
        check_isBroken = self.bike.isBroken
        ans_isBroken = False
        self.assertEqual(check_isBroken, ans_isBroken)
