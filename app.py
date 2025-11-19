from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# In-memory database
items = []

def add_item_to_list(list, item):
    list.append(item)

def remove_item_from_list(list, index):
    if index < len(list):
        list.pop(index)

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        add_item_to_list(items, item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        remove_item_from_list(items, index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
