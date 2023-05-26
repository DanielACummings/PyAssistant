from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Index/PyAssistant
@app.get('/')
def index():
    return render_template('index.html')

# QuickList
ql_lists = ['test1', 'test2']

@app.get('/quick-list')
def ql_base():
    return render_template('quick-list.html', ql_lists=ql_lists)
