from flask import Flask, render_template, request
from flask_cors import CORS
from models import get_recommendations, get_result

app = Flask (__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    title = request.form.get('title')
    res = get_result (title)
    rec = get_recommendations (title)
    if rec.count == 0:
        return render_template ('index.html', rec='No movie found')
    else:
        return render_template ('index.html', res=res, rec = rec)


if __name__ == '__main__':
    app.run(debug=True)
