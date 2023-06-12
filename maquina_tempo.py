import os 

ano = int(input('Digite o ano: '))

os.system('cls') or None

if ano <= 1917 and ano >= 1700:
    if ano % 4 == 0:
        print(f'O dia do programador em {ano}, na Rússia é: \n 12/09/{ano}')
    else:
        print(f'O dia do programador em {ano}, na Rússia é: \n 11/09/{ano}')
elif ano >= 1919 and ano <= 2700:
    if ano % 4 == 0:
        print(f'O dia do programador em {ano}, na Rússia é: \n 14/09/{ano}')
    else:
        print(f'O dia do programador em {ano}, na Rússia é: \n 13/09/{ano}')
elif ano == 1918:
    print(f'O dia do programador em 1918, na Rússia é: \n 26/09/1918')