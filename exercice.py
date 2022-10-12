#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number<0:
        new=number+ (2*-number)

    return new


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [""]


def prime_integer_summation() -> int:
    somme=0
    for i in range(2,101,1):
        for j in range(i,1,-1):
            if i%j==0:
                continue
            if i%j==1:
                somme=somme+j
    return somme


def factorial(number: int) -> int:
    
    for i in range(number-1,1,-1):
        factorielle=number*i
    return factorielle


def use_continue() -> None:
    for i in range(1,10):
        if i==5:
            continue
        print(i)
    return 


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptable=[]
    for group in groups:
        if len(group)>10 or len(group)<=3:
                acceptable.append(False)
        if 25 in group:
            acceptable.append(True)
            if (min(group)<18) or (max(group)>70 and 50 in group):
                acceptable.append(False)
    return acceptable
#Le programme pour cet exo ne marchais pas parce que quand je fais .append je dois pas mettre de égal avant car cela ne fait pas de sens. je n'affecte pas de append a une variable.
#donc on ne dois jamais écrire acceptable=acceptable.append(False) mais bien acceptable.append

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
#group_acceptable= []
    #for group in groups:
       # for i in group:
            #if i==25:
                #group_acceptable= group_acceptable.append(group)
           # if len(group)>10 or len(group)<=3:
                ##continue
                #if i<18:
                    #continue
                #if i>70 and i==50:
                    #continue
                #group_acceptable=group_acceptable.append(group)
    #return group_acceptable