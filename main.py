import math

koef_A = int(input('введите коэффициент а: '))
koef_B = int(input('введите коэффициент b: '))
koef_C = int(input('введите коэффициент c: '))

discrimiant = koef_B**2 - 4*koef_A*koef_C
if discrimiant > 0 :
    koren_x1 = (-koef_B+math.sqrt(discrimiant))/(2*koef_A)
    koren_x2 = (-koef_B-math.sqrt(discrimiant))/(2*koef_A)
    print("Корни квадратного уравнения: ")
    print("Первый корень = ", round(koren_x1))
    print("Второй корень = ", round(koren_x2))
if discrimiant == 0 :
    koren_x1 = -(koef_B/(2*koef_A))
    print('Корни квадратного уравнения: ')
    print("Первый корень = ", round(koren_x1))
    print("Второй корень = ", round(koren_x1))
if discrimiant < 0 :
    print('Корней квадратного уравнения не существует')