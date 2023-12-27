from flask import Flask, request, render_template_string, render_template, Blueprint
lab9 = Blueprint('lab9',__name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/zxc.html')

@lab9.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@lab9.errorhandler(500)
def not_found(err):
    return "шляпа", 500

@lab9.route('/lab9/postcard')
def postcard():
    recipient_name = request.args.get('recipient_name', '')
    recipient_gender = request.args.get('recipient_gender', '')
    sender_name = request.args.get('sender_name', '')
    if recipient_name and recipient_gender and sender_name:
        return render_template('postcard.html', recipient_name=recipient_name, recipient_gender=recipient_gender, sender_name=sender_name)
    else:
        return render_template('new_year_postcard.html')

if __name__ == '__main__':
    lab9.run(debug=True)