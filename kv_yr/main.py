a = float(input('Write a: '))
b = float(input('Write b: '))
c = float(input('Write c: '))

d = (b ** 2) - (4 * a * c)

if d < 0:
    print('there is no solution')

if d == 0:
    print('there is one solution')
    x = (-b + d ** 0.5) / (2 * a)
    print(x)

if d > 0:
    print('there are two solutions')
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    print(f'first solution:  {x_1}\n'
          f'second solution:  {x_2}')

