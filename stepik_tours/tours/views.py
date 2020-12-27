from django.shortcuts import render
# from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View
from random import randint
from . import data
# def custom_handler404(request, exception):
#     return HttpResponseNotFound("Нет такой страницы")


# def custom_handler500(request):
#      return HttpResponseServerError("Ошибка на сервере")

class MainView(View):

    def get(self, request):

        rand_tours = {}
        num_tours = {}
        for x in range(6):
            num_tours[x + 1] = randint(1, 16)
            rand_tours[x + 1] = (data.tours[num_tours[x + 1]])

        context = {
            'tours': rand_tours,
            'num_tours': num_tours,
        }

        return render(request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure):

        n = 0
        tours_dep = {}
        country = data.departures[departure].split()
        end_of_word = ''
        price = []
        night = []

        for i, j in data.tours.items():
            if j["departure"] == departure:
                tours_dep[n] = j
                price.append(j["price"])
                night.append(j["nights"])
                n += 1

        price.sort()
        night.sort()

        if n != 1 and n >= 2 or n <= 4:
            end_of_word = 'а'
        else:
            end_of_word = 'ов'

        context = {
            'tours_dep': tours_dep,
            'n': n,
            'country': country[1],
            'end_of_word': end_of_word,
            'min_price': price[0],
            'max_price': price[-1],
            'min_night': night[0],
            'max_night': night[-1]
        }
        return render(request, 'departure.html', context=context)


class TourView(View):

    def get(self, request, id):

        tour = data.tours.get(id)
        print(tour['title'])
        star = '★' * int(tour["stars"])
        context = {
            'tour': tour,
            'star': star,

        }
        return render(request, 'tour.html', context=context)
