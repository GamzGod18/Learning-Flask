from  flask import Flask , request,

app =Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'


@app.route('/profile/<username>')
def profile(username):
    return 'Hey There %s' %username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ID is %s' % post_id


@app.route('/method', methods=['GET', 'POST'])
def used_method():
    if request.method == 'POST':
        return '<h2>Method used is POST</h2>'
    else:
        return '<h2>Method used is GET</h2>'


if __name__ =="__main__":
    app.run(debug=True)









