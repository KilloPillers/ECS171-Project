from flask import Flask, render_template, request
import joblib  # Replace with your machine learning model import

app = Flask(__name__)

# Load your pre-trained machine learning model here
model = joblib.load("random_forest.joblib")  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get user input from the form
        age = int(request.form.get("age"))
        sex = int(request.form.get("sex"))
        pclass = int(request.form.get("pclass"))
        sibsp = int(request.form.get("sibsp"))
        parch = int(request.form.get("parch"))
        fare = float(request.form.get("fare"))
        parch = int(request.form.get("parch"))
        

        print(f"----{age=}")


        # Preprocess the input data for your model (if needed)
        # ... your data preprocessing code here ...

        preprocessed_data = input_data

        # Make prediction using your model
        prediction = model.predict([preprocessed_data])  # Assuming a list input

        # Format the prediction for display
        predicted_class = prediction[0]  # Assuming single class output

        return render_template("result.html", prediction=predicted_class)

    else:
        return "Something went wrong. Please try again."

if __name__ == "__main__":
    app.run(debug=True)