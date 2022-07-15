from flask import Flask, render_template, request
import json
import os


app = Flask(__name__, template_folder=os.getcwd())

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get("register_name"):  # мне кажется странным такой способ определения, но в основном я вижу такое
            login, password, confirm = request.form.values()
            if password != confirm:
                return "Пароли не совпадают!"
            with open("database.json", "r") as file:
                data = json.load(file)
                if data.get(login):
                    return "Такой аккаунт уже существует"
            data[login] = password
            with open("database.json", "w") as file:
                json.dump(data, file)
            return "Успех"
        elif request.form.get("login"):
            login, password = request.form.values()
            with open("database.json", "r") as file:  # вообще файлы можно открыть один раз в начале кода и потом использовать
                data = json.load(file)
            if not data.get(login):
                return "Не зарегистрирован"
            if data.get(login) != password:
                return "Неправильный пароль"
            return render_template("suc.html")
    return render_template("index.html")



app.run()