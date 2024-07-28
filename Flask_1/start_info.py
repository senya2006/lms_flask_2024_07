from flask import Flask

app = Flask(__name__)


# ця функція називається view
@app.route("/admin")    # /admin я повинен вписати до айпі бо без цього не покажеться сайт
def hello_world():
    return "<p>Hello, Semen!</p>"


# https://flask.palletsprojects.com:443/en/2.0.x/quickstart/

# не можна викростивувати спец. символи наприклад: ? & : @ + ~ / \ #

# https - протокол це спосіб передачі данних, комунікаціїї. Простими слоами, визначенний спосіб передачі
# http - не захищенний, https - захищенний, тут є SSL сертифікат який шифрує данні

# flask.palletsprojects.com - доменне ім'я, DNS сервера роблять це вайпі але щоб нам було зручно придумали назви
# приклад facebook.com -> 157.240.234.35

# 443 - це порт https, бо на одному сервері може бути багато сервісів
# 80 - http
# 5432 - postgres
# 587 - smtp для відправки емейлів використовується
# 22 - ssh

# en/2.0.x/quickstart/ - це вже сам вебсайт де ми пишемо код на фласку, зона відповідальності, все що раніше то був шлях


if __name__ == "__main__":
    app.run(
        port=5000, debug=True
    )
