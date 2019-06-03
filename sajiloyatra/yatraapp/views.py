from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import EventForm
from .models import Food, Festival, Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def foodview(request):
    # if request.method == "POST":
    # import ipdb
    # ipdb.set_trace()

    place = request.POST.get('place')

    check_in = request.POST.get('check_in')

    check_out = request.POST.get('check_out')
    cate = request.POST.get('cate')
    print(cate)

    foods = Food.objects.all()

    if place:
        foods = foods.filter(location=place)

    if check_in:
        foods = foods.filter(checkin=check_in)

    if check_out:
        foods = foods.filter(checkout=check_out)

    if cate:
        foods = foods.filter(category=cate)

    page = request.GET.get('page', 1)
    paginator = Paginator(foods, 6)
    try:
        food = paginator.page(page)
    except PageNotAnInteger:
        food = paginator.page(1)
    except EmptyPage:
        food = paginator.page(paginator.num_pages)
    return render(request, 'food.html', {'food': food})


@login_required
def categoryview(request):
    return render(request, 'food.html')

@login_required
def festivalview(request):
    festival = Festival.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(festival, 6)
    try:
        festival = paginator.page(page)
    except PageNotAnInteger:
        festival = paginator.page(1)
    except EmptyPage:
        festival = paginator.page(paginator.num_pages)
    return render(request, 'festival.html' , {'festival' : festival})


def homeview(request):
   return render(request, 'home.html')

@login_required
def contactview(request):
    return render(request, 'contact.html')

# @login_required
class EventView(ListView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'event_list'
        return context

    def get_queryset(self):
        events = Event.objects.all()
        location = self.request.GET.get('location')
        if location:
            events = events.filter(location = location)

        return events


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    # fields = ['location', 'event_name', 'description', 'month', 'date_created']
    success_url = reverse_lazy('event_list')


class EventUpdateView(UpdateView):
    model = Event
    fields = ['location','event_name', 'description', 'month', 'date_created']
    template_name_suffix = '_form'
    success_url = reverse_lazy('event_list')

@login_required
def eventcompletion(request, pk):
    event = Event.objects.get(pk=pk)
    event.active = False
    event.save()
    return redirect('event_list')



