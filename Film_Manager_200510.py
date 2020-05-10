# Python 3.8.2
# -*- coding: utf-8 -*-
# Programmation orientée objet

#Film manager

import datetime

date = datetime.datetime.today()
nb_films = 0
nb_shots = 0

class Folder: #ensemble de films
    def __init__(self, films):
        self.films = []

class Film: #ensemble de vues
    def __init__(self, film_index, shots):
        self.film_index  = film_index
        self.shots = []
        global nb_films
        nb_films += 1

    def new_shot(self, shot_index, date):
        shot = Vue(shot_index, date) #Initialisation objet Vue
        self.shots.append(shot) #Ajout de l'objet dans la liste vues
        global nb_shots
        nb_shots += 1

class Vue:
    def __init__(self, shot_index, date):
        self.shot_index = vue_index #index de vue 0 à 36
        self.date = date #date de la prise de vue


print("Film manager is running")




