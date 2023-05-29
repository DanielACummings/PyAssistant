from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQL configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'DanielACummings.mysql.pythonanywhere-services.com'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Index/PyAssistant
@app.get('/')
def index():
    return render_template('index.html')


# QuickList
class Ql_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f'<Content {self.content}>'

db.create_all()

ql_lists = Ql_list.query.all()


@app.get('/quick-list')
def ql_home():
    return render_template('quick-list.html', ql_lists=ql_lists)


@app.post('/add-list')
def ql_add_list():
    form_data = request.form['ql_list']
    if not form_data:
        return 'Error'

    ql_list = Ql_list(form_data)
    db.session.add(ql_list)
    db.session.commit()
    return redirect(url_for('ql_home'))


if __name__ == '__main__':
    app.run(debug=True)
