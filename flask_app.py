from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Задайте URI для вашей БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=False, nullable=False)

# Создание базы данных и таблиц
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template('index.html')

# Маршрут для обработки формы 
@app.route('/submit', methods=['POST']) 
def submit_form(): 
    # Получаем данные из формы 
    email = request.form['textInput'] 
    email = email.lower() 
    cobakaCounter = email.count('@') 
    
    if cobakaCounter == 1: 
        emailSplit = email.split('@') 
        domen = emailSplit[1] 
        tCounter = domen.count('.') 
        
        if tCounter >= 1: 
            # Создаем новую запись
            new_user = User(email=email)
            
            # Добавляем запись в базу данных
            db.session.add(new_user)
            db.session.commit()
            
            # Перенаправляем на главную страницу или другую страницу
            return redirect(url_for('index'))

@app.route("/blog")
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
