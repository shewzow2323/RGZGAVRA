from flask import Blueprint, render_template, request, make_response
lab4=Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'julia' and password == '1':
        return render_template('success.html')
    error = 'Неверные логин и/или пароль'
    if username == '':
        error='Вы не ввели логин'
    if password == '':
        error='Вы не ввели пароль'

    return render_template('login.html',error=error,
                           username=username, password=password)



@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge(): 
    msg = ''
    if request.method =='GET':
        return render_template('fridge.html', msg=msg)
    
    temperature = request.form.get('temperature')

    if temperature == '':
        msg ='Не задана температура'
    else:
        temperature = int(temperature)
        if temperature < (-12):
            msg ='Не удалось установить температуру — слишком низкое значение'
        elif temperature > (-1):
            msg = 'Не удалось установить температуру — слишком высокое значение'
        elif (temperature >= (-12)) and (temperature <= (-9)):
            msg = f'Установлена температура: {temperature}°С ❄️❄️❄️'
        elif (temperature >= (-8)) and (temperature <= (-5)):
            msg = f'Установлена температура: {temperature}°С ❄️❄️'
        elif (temperature >= (-4)) and (temperature <= (-1)):
            msg = f'Установлена температура: {temperature}°С ❄️'
    return render_template('fridge.html', temperature=temperature, msg=msg)
                        
@lab4.route('/lab4/seeds', methods=['GET', 'POST'])
def seeds():
    sale = ''
    error = ''
    total = 0
    max_weight = 500
    seed_types = {
        'barley': 'ячмень',
        'oats': 'овёс',
        'wheat': 'пшеница',
        'rye': 'рожь'
    }

    seed_prices = {
        'barley': 12000,
        'oats': 8500,
        'wheat': 8700,
        'rye': 14000
    }

    if request.method =='GET':
        return render_template('seeds_order.html', error=error)
    
    seed = request.form.get('seed_type')
    weight = request.form.get('weight')

    if weight == '':
        error = 'Не указан вес'
    else:
        weight = int(weight)
        if weight > 0:
            if weight > 50:
                total = (seed_prices[seed] * weight) * 0.9
                sale = f'Добавлена скидка 10% ({(seed_prices[seed] * weight) * 0.1} руб.) из-за веса более 50 тонн!'
            elif weight > max_weight:
                error = 'Такого объёма сейчас нет в наличии'
            else:
                total = seed_prices[seed] * weight
        else:
            error = 'Неверное значение веса'

    return render_template('seeds_order.html', error=error, seed=seed_types[seed], weight=weight, total=total, sale=sale)

@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    error = ''
    resp = make_response(render_template('cookies.html', error=error))
    color = request.form.get('color')
    b_color = request.form.get('background-color')
    f_size = request.form.get('font-size')
    if color and b_color and f_size:
        if color == b_color:
            error = 'Цвет фона и цвет текста должен отличаться!'
            return make_response(render_template('cookies.html', error=error))
        resp.set_cookie('color', color)
        resp.set_cookie('background-color', b_color)
        resp.set_cookie('font-size', f"{f_size}px")
    return resp


@lab4.route('/lab4/defend', methods=['GET', 'POST'])
def defend():
    return render_template('lab4defend.html')