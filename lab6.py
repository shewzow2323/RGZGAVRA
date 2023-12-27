from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from db import db
from db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('lab6', __name__)

@lab6.route("/lab6")
def mainpage():
    try:
        username = (users.query.filter_by(id=current_user.id).first()).username
        return render_template("lab6.html", username = username)
    except:
         return render_template("lab6.html", username = "Аноним")

@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route("/lab6/checkarticles")
def checkarticles():
    all_articles= articles.query.all()
    print(all_articles)
    return "result in console!"

@lab6.route("/lab6/register", methods=['GET', 'POST'])
def register():
    errors = []
    if request.method == "GET":
        return render_template("register.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username=username_form).first()
    if username_form == '':
        errors = 'Пустое имя!'
        return render_template("register.html", errors=errors)
    else:
        if isUserExist is not None:
            errors = 'Такой пользователь уже существует!'
            return render_template("register.html", errors=errors)
        else:
            if len(password_form) < 5:
                errors = 'Пароль должен быть длиннее 5 символов!'
                return render_template("register.html", errors=errors)
            else:
                hashedPswd = generate_password_hash(password_form, method="pbkdf2")
                newUser = users(username=username_form, password=hashedPswd)

                db.session.add(newUser)
                db.session.commit()

    return redirect("/lab6/login")

@lab6.route("/lab6/login", methods = ['GET', 'POST'])
def login():
    errors = ''
    if request.method == "GET":
        return render_template("login.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username=username_form).first()

    my_user = users.query.filter_by(username=username_form).first()
    if username_form is None and password_form is None:
        errors = 'Заполните все поля!'
        return render_template("login.html", errors=errors)
    else:
        if my_user is not None:
            if check_password_hash(my_user.password, password_form):
                login_user(my_user, remember=False)
                return redirect("/lab6")
            else:
                errors = 'Неверный пароль!'
                return render_template("login.html", errors=errors)
        else:
            errors = 'Пользвателя с таким именем не существует!'
            return render_template("login.html", errors=errors)

    return render_template("login.html")

@lab6.route("/lab6/articles")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=int(current_user.id)).all()
    print(my_articles[0])
    return render_template("article_list.html", articles_list=my_articles)
    
@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6/login")

@lab6.route("/lab6/new_article", methods=['GET', 'POST'])
@login_required
def createArticle():
    errors = ''
    if request.method=='GET':
        return render_template('note.html')
    else:
        userID = current_user.id
        text_article = request.form.get("text_article")
        title = request.form.get("title_article")

        if text_article == '' or title == '':
            errors =  "Заполните все поля!"
            return render_template('note.html', errors=errors)
        else:
            is_public = request.form.get('publish')
            if is_public == 'False':
                is_public = None
            else:
                is_public = True
            newArticle = articles(user_id = userID, article_title = title, article_text=text_article, is_public=is_public)

            db.session.add(newArticle)
            db.session.commit()
            

    return redirect(f"/lab6/articles/{new_article_id}")


@lab6.route("/lab6/article_list")
@login_required
def article_list():
    username = (users.query.filter_by(id=current_user.id).first()).username
    articles_list = articles.query.filter_by(user_id=current_user.id).all()

    return render_template("article_list.html", username=username, articles_list=articles_list)

@lab6.route("/lab6/articles/<string:article_id>")
@login_required
def getArticle(article_id):
    username = (users.query.filter_by(id=current_user.id).first()).username
    title = articles.query.filter_by(id=article_id).first().article_title
    text = articles.query.filter_by(id=article_id).first().article_text
    return render_template("articleN.html", article_title=title, article_text=text, username=username)

@lab6.route("/lab6/article_publish_list", methods = ['GET', 'POST'])
@login_required
def published():
    username = (users.query.filter_by(id=current_user.id).first()).username
    if articles.query.filter_by(is_public=True).all() is None:
        list = 'Нет опубликованных статей'
        return render_template("article_published_list.html", article_published_list=list, username = username)
    else:
        list = articles.query.filter_by(is_public=True).all()
        return render_template("article_published_list.html", article_published_list=list, username = username)




            


