from teknos_rajz import *

up()                    # fölemeli a ceruzát 
goto(-150, 50)          # balra felmegy
# tíz piros, sorbarendezett négyzetet rajzol:

i = 0 
while i < 10:    
    down()              # leteszi a ceruzát    
    negyzet(25, 'red')    # egy négyzetet rajzol    
    up()                # fölemeli a ceruzát    
    forward(30)         # távolabb megy    
    i = i + 1
    
a = input()             # vár
