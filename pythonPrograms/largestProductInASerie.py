# @Author: Diego Sarceno
# 19.07.2020

# Problem 8 of Project Euler

'''
Tomamos el numero propuesto y vamos tomando paquetes de 13 y multiplicamos
cada uno de los digitos de los paquetes.
'''
# tomamos el numero dado en el problema
n = '731671765313306249192251196744265747423553491949349698352031277450\
63262395783180169848018694788518438586156078911294949545950137958331952\
85320880551112540698747158523863050715693290963295227443043557668966489\
50445244523161731856403098711121722383113622289342338030813533627661428\
28064444866452387493035890729629049156044077239071381051585930796086670\
17242712188399879790879227492190169972088809377665727333001053367881220\
23542180975125454059475224352584907711670556013604839586446706324415722\
15539753697817977846174064955149290862569321978468622482839722413756570\
56057490261407972968652414535100474821663704844031998900088952434506585\
41227588666881164271714799244429282308634656748139191231628245861786645\
83591245665294765456828489128831426076900422421902267105562632111110937\
05442175069416589604080719840385096245544436298123098787992724428490918\
88458015616609791913387549920052406368991256071760605886116467109405077\
54100225698315520005593572972571636269561882670428252483600823257530420\
752963450'


# se divide el 'n' en intervalos de 13 digitos y se multiplican esos digitos
mayor = 0
for i in range(0,988):
    x = n[i:i + 13]
    prod = 1
    for j in x:
        prod *= int(j)
    if prod >= mayor:
        mayor = prod

print(mayor)