from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,FormView
from django.views import View
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import OrderForm
from .models import PizzaMenu,OrderModel
from django.urls import reverse_lazy
# Create your views here.

class Main(TemplateView):
    template_name='mainSite.html'

class ContactView(TemplateView):
    template_name='contact.html'

class MenuView(ListView):
    model=PizzaMenu
    template_name='menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        if query:
            results = PizzaMenu.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
            context['results'] = results
            context['query'] = query
        return context


class OrderView(FormView):
    form_class=OrderForm
    template_name='order.html'

    success_url=reverse_lazy('pizza:main')

    def form_valid(self, form):
        # Pobierz dane z formularza
        pizza_name = form.cleaned_data['pizzaName']
        size = form.cleaned_data['size']
        city = form.cleaned_data['city']
        house_Number = form.cleaned_data['houseNumber']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phoneNumber']

        # Stwórz nowy obiekt OrderModel i zapisz go do bazy danych
        order = OrderModel(pizzaName=pizza_name, size=size, city=city, house_Number=house_Number, email=email, phoneNumber=phone_number)
        order.save()

        # Przekieruj użytkownika na stronę success_url
        return super().form_valid(form)
    
    
class RestaurantsView(TemplateView):
    template_name='restaurants.html'

class SearchMenuView(TemplateView):
    template_name='searchMenu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        if query:
            results = PizzaMenu.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
            context['results'] = results
            context['query'] = query
        return context
    
class TestView(TemplateView):
    template_name="test.html"

class ImageView(TemplateView):
    template_name="image.html"