from flask import Blueprint, render_template, request
import math
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/form1')
def form():
    errors={}
    user = request.args.get('user')
    age = request.args.get('age')
    if user == '':
        errors['user'] = 'Заполните поле'
    if age == '':
        errors['age'] = 'Заполните поле'
    sex =  request.args.get('sex')
    return render_template('lab3.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    drink = request.args.get('drink')
    milk = request.args.get('milk')
    sugar = request.args.get('sugar')
    return render_template('order.html', drink=drink, milk=milk,sugar=sugar)

@lab3.route('/lab3/pay')
def pay():
    errors = {}
    price=0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price=120
    elif drink == 'black tea':
        price=80
    else:
        price=70

    if request.args.get('milk') == 'on':
        price+=30
    if request.args.get('sugar') == 'on':
        price +=10
    
    
    card = request.args.get('card')
    name = request.args.get('name')
    cvv = request.args.get('cvv')

    if card == '':
        errors['card'] = 'Заполните поле'
    if name == '':
        errors['name'] = 'Заполните поле'
    if cvv == '':
        errors['cvv'] = 'Заполните поле'
    
    return render_template('pay.html', price=price, card=card, name=name, cvv=cvv, errors=errors)

@lab3.route('/lab3/ticket')
def ticket():
    errors={}
    user = request.args.get('user')
    age =  request.args.get('age')
    ticket_type = request.args.get('ticket_type')
    shelf_type = request.args.get('shelf_type')
    baggage = request.args.get('baggage')
    exit_point =  request.args.get('exit_point')
    destination =  request.args.get('destination')
    date =  request.args.get('date')

    if user == '':
         errors['user'] = 'Заполните поле'
    if age == '':
         errors['age'] = 'Заполните поле'
    if exit_point == '':
         errors['exit_point'] = 'Заполните поле'
    if destination == '':
         errors['destination'] = 'Заполните поле'
    if date == '':
         errors['date'] = 'Заполните поле'

    return render_template('ticket.html',  user=user, age=age, ticket_type=ticket_type,
    exit_point=exit_point, destination=destination, shelf_type=shelf_type,
    baggage=baggage, date=date, errors=errors)

@lab3.route('/lab3/defend')
def defend():
    x = request.args.get('x')
    n = request.args.get('n')

    result = 0
    if n and x:
        if int(n) > 0:
            n = int(n)
            x = float(x)

            result = x

            for i in range(n):
                result += (((-1**i)*(x**(2*i+1)))/(math.factorial(2*i+1)))
        else:
            result = 'error'

    return render_template('l3defend.html', x=x, n=n, result=result)

@lab3.route('/lab3/defend2')
def defend2():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')


    result = 0
    if a and b and c and d:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if a == b == c:
            result = 4
        elif a == b == d:
            result = 3
        elif a == c == d:
            result = 2
        else:
            result = 1
            
    return render_template('l3defend2.html', a=a, b=b, c=c, d=d, result=result)