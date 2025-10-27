##########################################
# Plourde, Camille, <2480389>
##########################################

# Question 1

import random as rd
def question1():
    for i in range(10):
        temperature = rd.uniform(20, 35)
        temperature_arrondie = round(temperature, 1)
        jours = 0
        print("Jour", i + 1, ":", temperature_arrondie)
        if temperature_arrondie > 30:
            print("Trop chaud")
        elif temperature_arrondie < 24:
            print("Trop froid")
        else:
            print("OK")
    print("Fin")
question1()

# Question 2

import numpy as np
import matplotlib.pyplot as plt
def question2():
    population_bacteries_initiale = int(input("Entrez la population de bactéries initiale :"))
    for i in range(10):
        heures = 0
        taux_augmentation = np.pi/1.5
        croissance_population_bacteries = population_bacteries_initiale * taux_augmentation

    plt.figure(figsize=(5, 5))
    plt.title("Croissance bactérienne")
    plt.xlabel("Heures")
    plt.ylabel("Population")
    plt.xlim(0, 10)
    plt.ylim(0, 160000)
    plt.plot([heures, croissance_population_bacteries], "*")
    plt.grid()
    plt.show()

question2()

# il me manque le y = 50000 pour le seuil de population (je ne me rappelais plus comment du mot à mettre après le plt pour faire cela)
# je ne parvenais pas à faire en sorte que les points affichent une croissance

