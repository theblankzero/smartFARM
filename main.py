# Flask + Supabase inference script placeholder
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Fertilizer Recommendation System - ANN + IoT + Supabase"

if __name__ == '__main__':
    app.run(debug=True)
