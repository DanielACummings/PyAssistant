from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Index/PyAssistant
@app.get('/')
def index():
    return render_template('index.html')



# QuickList
ql_lists = ['test1', 'test2']

@app.get('/quick-list')
def ql_home():
    return render_template('quick-list.html', ql_lists=ql_lists)


@app.post('/add-list')
def ql_add_list():
    ql_list = request.form['ql_list']
    ql_lists.append(ql_list)
    return redirect(url_for('ql_home'))



if __name__ == '__main__':
    app.run(debug=True)
