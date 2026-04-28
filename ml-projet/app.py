from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form["area"])
    prediction = model.predict([[area]])
    return render_template("index.html", prediction_text=f"Price: {prediction[0]:.2f} lakhs")

if __name__ == "__main__":
    app.run()