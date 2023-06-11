from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Reservation
from django.shortcuts import redirect            # Rediret

# For Login and Logout
from .models import UserAccount                  # User Account model
from django.views.generic import TemplateView    # Template
from .forms import AccountForm, AddAccountForm   # User Account Form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Complain
from .models import Complaint
from .models import BikeInfo
from .forms import ComplaintForm

# User Register
class AccountRegistration(TemplateView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params = {
            "AccountCreate": False,
            "account_form": AccountForm(),
            "add_account_form": AddAccountForm(),
        }

    # Get
    def get(self, request, *args, **kwargs):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request, "UserAuthentication/register.html", context=self.params)

    # Post
    def post(self, request, *args, **kwargs):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        # Check if given data is valid
        if self.params["account_form"].is_valid():
            # Save account info in DB
            account = self.params["account_form"].save()
            # Hash password
            account.set_password(account.password)
            # Update hash password
            account.save()

            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1
            add_account.user = account
            # save the model
            add_account.save()

            # Upgrade user account creation
            self.params["AccountCreate"] = True

        else:
            # If the form is not valid
            print(self.params["account_form"].errors)

        return render(request, "UserAuthentication/register.html", context=self.params)

# Log In
def Login(request):
    # POST
    if request.method == 'POST':
        # Get email and password from form
        userid = request.POST.get('userid')
        password = request.POST.get('password')

        # Django Authentication function
        user = authenticate(username=userid, password=password)

        # Check if it is valid user
        if user:
            # Check activate of user
            if user.is_active:
                # Login
                login(request, user)

                # Get the associated UserAccount object
                user_account = UserAccount.objects.get(user=user)

                # Valid account, then go to homepage with unique url
                return HttpResponseRedirect(reverse('bike_app:welcome_user', args=[user_account.random_url]))

            else:
                # Invalid account
                return HttpResponse("Invalid Account")
        # Fail user authentication
        else:
            return HttpResponse("Email or Password is wrong :(")
    # GET
    else:
        return render(request, 'UserAuthentication/login.html')


# Log out
@login_required
def Logout(request):
    logout(request)
    # Redirect to the login page
    return redirect('bike_app:login')


# Home Page before log in
def welcome(request):

    if request.user.is_authenticated:
        # If user has logged in => Redirect to user page
        return redirect(reverse('bike_app:welcome_user', args=[request.user.useraccount.random_url]))
    else:
        # If user has not logged in => Redirect to login page
        return render(request, 'Main/welcome_user.html', {'login_url': '/login/'})


# Home Page after log in
@login_required
def welcome_user(request, url_uuid):
    try:
        user_account = UserAccount.objects.get(random_url=url_uuid)
    except UserAccount.DoesNotExist:
        # URL is not valid
        return HttpResponseNotFound("Page not found")

    params = {"userid": request.user, }
    return render(request, "Main/welcome_user.html", context=params)


@login_required
def FeedBack_page(request, url_uuid):

    # Check user login and he has unique url
    try:
        user_account = UserAccount.objects.get(random_url=url_uuid)
    except UserAccount.DoesNotExist:
        # URL is not valid
        return HttpResponseNotFound("Page not found")

    # If this is a POST request then process the Form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding):
        form = ComplaintForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            complaint = form.save(commit=False)
            # user_account = UserAccount.objects.get(user=request.user)
            user_account = UserAccount.objects.get(random_url=url_uuid)
            complaint.user = user_account
            complaint.save()
            params = {"userid": request.user, 'form': form}
            return render(request, 'Feedback/successComplaining.html', context=params)
    else:
        form = ComplaintForm()

    params = {"userid": request.user, 'form': form}

    return render(request, 'Feedback/complaint.html', context=params)


def bikeList_page(request, url_uuid):
    # Check user login and he has unique url
    try:
        user_account = UserAccount.objects.get(random_url=url_uuid)
    except UserAccount.DoesNotExist:
        # URL is not valid
        return HttpResponseNotFound("Page not found")

    bike = BikeInfo.objects.all()

    params = {"userid": request.user, "bike_list": bike, }

    return render(request, "Main/bikeList.html", params)


class Reservation_Page(CreateView):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('home')
    template_name = 'bike_app/reservation.html'


def FAQ(request):
    return render(request, "Main/FAQ.html",)