#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Animation de la méthode de Newton (recherche de zéros)
Généré le 23 Mai 2021
@author: Th. G

Ce script est mis à disposition sous licence Creatice Commons 
(Pas d'utilisation commerciale, Partage dans les mêmes conditions).
"""


import numpy as np
import matplotlib.pyplot as plt

# La fonction considérée
def fonction(x):
    y = x*x + 3*x - 5
    return (y)

# Sa dérivée
def derivee(x):
    y = 2*x + 3 
    return (y)


tab_x_newton = [] # Les listes pour les points des tangentes
tab_y_newton = [] 

# La méthode de Newton, choisir le epsilon ici !
def newton( x, epsilon=0.000001):
    n   = 0
    dif = 2 * epsilon 
    while dif > epsilon :
        tab_x_newton.append(x)
        tab_y_newton.append(fonction(x))
        x1   = x - fonction(x) / derivee(x)
        dif  = abs(x1 - x)
        x    = x1
        n    = n+1
        tab_x_newton.append(x1)
        tab_y_newton.append(0)
    return (x, n)


x0 = float(input("Choisir une valeur de départ : "))

(x,n) = newton(x0)

print('x=%f n=%d' % (x, n) )

tab_x = np.linspace(-6,20,100)
tab_y = fonction(tab_x)


plt.plot(tab_x,tab_y, color='red') # On trace la fonction en rouge
plt.plot(tab_x_newton[0:2], tab_y_newton[0:2], 'o--', color="tab:blue") # On trace la première tangente
plt.grid()
ax = plt.gca()

# Une textbox pour avoir les infos
textstr = '\n'.join((
                r'$x_0=%.1f$' % (x0, ),
                r'$x_f=%.3f$' % (tab_x_newton[1], ),
                r'$n=%d$' % (1, )))

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
box = ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props)

# On gère ici les évènements du clavier (flèche droite pour avancer, gauche pour reculer)
i = 0
def on_keyboard(event):
    global i
    
    #plt.clf()
    
    if event.key == 'right':
        
        
        if i <= len(tab_x_newton):
            
            if i%2 == 0:
                plot_tangente(i)
                i += 1
                textstr = '\n'.join((
                r'$x_0=%.1f$' % (x0, ),
                r'$x_f=%.3f$' % (tab_x_newton[i], ),
                r'$n=%d$' % (i/2+1, )))
                box.set_text(textstr)

            else:
                plot_vertical(i)
                i += 1
        else:
            i = len(tab_x_newton)
            
    elif event.key == 'left':
    
        if len(ax.lines) >= 2:
            #if i%2 == 0:
            remove_series()
            i-=1
        else:
            i=0
            
    
    
    print(i)
    plt.draw()
    
    # Si vous voulez sauvegarder une image à chaque étape (pour faire un gif par exemple), décommenter la ligne suivante
    # plt.savefig('img'+str(i)+'.png')
    
# On trace les tangentes...
def plot_tangente(i):
    sublist_x = tab_x_newton[i:i+2]
    sublist_y = tab_y_newton[i:i+2]
    plt.plot(sublist_x, sublist_y, 'o--', color="tab:blue", label = "tangente"+str(i))

# ... et les projections
def plot_vertical(i):
    sublist_x = tab_x_newton[i:i+2]
    sublist_y = tab_y_newton[i:i+2]
    plt.plot(sublist_x, sublist_y, ':', color="tab:green", label = "vlines"+str(i))
   
# Suppression des plots matplotlib quand on revient en arrière
def remove_series():
  ax.lines.remove(ax.lines[-1])
  

plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Méthode de Newton : $f(x) = x^2 +3x-5 ; \epsilon = 10^{-6}$")
plt.show()