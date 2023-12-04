from logging import getLogger

from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.conf import settings
from danielAgency.forms import SignUpForm, TripModelForm, BookingForm, ContactForm
from danielAgency.models import Trip, City
from danielAgency.permissions import StaffRequiredMixin

LOGGER = getLogger()

class TripCardView(ListView):
    template_name = 'card_trip.html'
    model = Trip

    def get_queryset(self):
        genre = self.kwargs.get('trip')
        queryset = super().get_queryset()
        if genre:
            return queryset.filter(genre__name=genre)
        return queryset


class TripDetailView(DetailView):
    template_name = 'detail_trip.html'
    model = Trip


class WatchTour(DetailView):
    template_name = 'watch_tour.html'
    model = Trip


def about_us(request):
    return render(request, 'about_us.html')


class SubmittableLoginView(LoginView):
    template_name = 'login.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('list')


class TripListView(ListView):
    template_name = 'list_trip.html'
    model = Trip


class TripCreateView(StaffRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'new_form.html'
    form_class = TripModelForm
    success_url = reverse_lazy('list')
    permission_required = 'danielAgency.create_trip'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)

class TripUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'new_form.html'
    model = Trip
    form_class = TripModelForm
    success_url = reverse_lazy('list')
    # permission_required = 'danielAgency.change_trip'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a trip.')
        return super().form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Trip updated successfully.')  # Add a success message if needed
        return response


class TripDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'trip_confirm_delete.html'
    model = Trip
    success_url = reverse_lazy('list')
    permission_required = 'danielAgency.delete_trip'

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class SignUpView(CreateView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('trip')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Assign the user to the "Basic Permission" group
        user = self.object
        basic_permission_group = Group.objects.get(name='Basic Permission')
        user.groups.add(basic_permission_group)

        # Set the user as active
        user.is_active = True
        user.save()

        return response



def book_now(request, pk):
    trip = Trip.objects.get(pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            date_of_birth = form.cleaned_data["date_of_birth"]
            number_of_persons = form.cleaned_data["number_of_persons"]

            send_mail(
                f"FROM: {name}",
                email,
                phone_number,
                settings.ADMINS,
                fail_silently=False,
                html_message=f"<div><p><em>From:</em> {name}</p><p>{email}</p><p>{phone_number}</p><p>{date_of_birth}</p><p>{f'Number of Persons: {number_of_persons}'}</p></div>"
            )

            return redirect('trip_detail', pk=pk)
    else:
        form = BookingForm()

    return render(request, 'book_now.html', {'form': form, 'trip': trip})




def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data.get("subject", "Greetings from your website!")
            message = form.cleaned_data["message"]

            send_mail(
                subject,
                f"FROM: {name}\n{message}",
                email,
                settings.ADMINS,
                fail_silently=False,
                html_message=f"<div><p><em>From:</em> {name}</p><p>{email}</p><p>{message}</p></div>",
            )
            return redirect("contact_view")
    else:
        form = ContactForm()
    return render(request, "kontakt.html", context={"form": form})
