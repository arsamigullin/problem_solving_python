def triangle_test(a,b,c):


    try:
        int(a)
    except ValueError:
        print('the side a is not a number')

    try:
        int(b)
    except ValueError:
        print('the side a is not b number')

    try:
        int(c)
    except ValueError:
        print('the side a is not b number')

    if a<=0 or b<=0 or c<=0:
        print('one of the parameters is less than or equal zero')

    # check if it is possible to have triangle
    if a + b <=c or a+c<=b or c+b<=a:
        print('impossible to construct triangle as sum of any two side must be greater that third sides')

    # if all sides are equal
    if a==b==c:
        print('this is equilateral triangle')
        return

    if a==b or a==c or b==c:
        print('this is isosceles triangle')

    if a!=b!=c:
        print('this is scalene triangle')


