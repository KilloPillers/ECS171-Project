from flask import Flask, render_template, request
import joblib 
from pydantic import BaseModel
import numpy as np

app = Flask(__name__)

# Load pre-trained machine learning model here
model = joblib.load("random_forest.joblib")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user input from the form
        age = float(request.form.get("age"))
        sex = float(request.form.get("sex"))
        pclass = float(request.form.get("pclass"))
        sibsp = float(request.form.get("sibsp"))
        parch = float(request.form.get("parch"))
        fare = float(request.form.get("fare"))
        embarked = float(request.form.get("embarked"))
        
        if (sibsp == 0 and parch == 0):
            alone = 1.0
        else:
            alone = 0.0
        
        familiars = 1 + sibsp + parch

        print(f"----{age=}")
        print(f"----{sex=}")
        print(f"----{pclass=}")
        print(f"----{sibsp=}")
        print(f"----{parch=}")
        print(f"----{fare=}")
        print(f"----{embarked=}")

        # Convert input data to a numpy array
        input_features = np.array([[pclass, sex, age, sibsp, parch, fare, 1.0, embarked, alone, familiars]])

        # scale features
        scaler = joblib.load("scaler.joblib")
        input_features = scaler.transform(input_features)

        # Make prediction
        prediction = model.predict(input_features)
        
        # Format the prediction for display
        survival = prediction[0]  # 0 -> dead, 1 -> alive
        if survival == 0:
            return render_template("result_dead.html")
        else:
            return render_template("result_alive.html")

    else:
        return "Something went wrong. Please try again."

if __name__ == "__main__":
    app.run(debug=True)