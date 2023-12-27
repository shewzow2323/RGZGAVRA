function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    }

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб.`;
        document.querySelector('#order').style.display = 'block';
        document.querySelector('#pay').style.display = 'block';
    })
};

function Pay() {
    const card_number = document.querySelector('[name=card_number]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const obj = {
        "method": "pay",
        "params": {
            card_num: card_number,
            cvv: cvv,
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
         return resp.json();
    })
    .then(function(data) {
        if (data.result) {
            document.querySelector('#price').style.display = 'none';
            document.querySelector('#calc').style.display = 'none';
            document.querySelector('#error').style.display = 'none';
            document.querySelector('#pay').style.display = 'none';
            document.querySelector('#order').style.display = 'none';
            document.querySelector('#pay_result').style.display = 'block';
            document.querySelector('#pay_result').style.color = 'green';
            document.querySelector('#pay_result').innerHTML = `${data.result}`;
            document.querySelector('#refund').style.display = 'block';
        }
        if (data.error) {
            document.querySelector('#pay_result').style.display = 'none';
            document.querySelector('#error').style.display = 'block';
            document.querySelector('#error').style.color = 'red';
            document.querySelector('#error').innerHTML = `${data.error}`;
        };
    })
};

function Refund() {
    const card_number = document.querySelector('[name=card_number]').value;
    const cvv = document.querySelector('[name=cvv]').value;
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const obj = {
        "method": "refund",
        "params": {
            card_num: card_number,
            cvv: cvv,
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
         return resp.json();
    })
    .then(function(data) {
        document.querySelector('#refund').style.display = 'none';
        document.querySelector('#pay_result').innerHTML = `${data.result}`;

    })
};