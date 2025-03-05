#  Here is the Python Code for Our Application.


from flask import Flask, request, render_template
import pickle

#  Flask App Creation.
app = Flask(__name__)

#  Load the Models.
best_model = pickle.load(open("./models/best_model.pkl", "rb"))
scaling_model = pickle.load(open("./models/label_encoder.pkl", "rb"))


# Create the Different Routes for Our Model.
@app.route("/")
def main():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    #  here we need to do some operation get the input data
    # from the form and scale it convert into the list and make Prediction.
    # 1. Take the input from the form Data.
    A1_Score = int(request.form["A1_Score"])
    A2_Score = int(request.form["A2_Score"])
    A3_Score = int(request.form["A3_Score"])
    A4_Score = int(request.form["A4_Score"])
    A5_Score = int(request.form["A5_Score"])
    A6_Score = int(request.form["A6_Score"])
    A7_Score = int(request.form["A7_Score"])
    A8_Score = int(request.form["A8_Score"])
    A9_Score = int(request.form["A9_Score"])
    A10_Score = int(request.form["A10_Score"])
    age = int(request.form["age"])
    gender = int(request.form["gender"])
    ethinicity = int(request.form["ethnicity"])
    jaundice = int(request.form["jaundice"])
    autism = int(request.form["autism"])
    country_of_res = int(request.form["country_of_res"])
    used_app_before = int(request.form["used_app_before"])
    result = int(request.form["result"])
    relation = int(request.form["relation"])

    # print(type(A1_Score))

    new_data = [
        A1_Score,
        A2_Score,
        A3_Score,
        A4_Score,
        A5_Score,
        A6_Score,
        A7_Score,
        A8_Score,
        A9_Score,
        A10_Score,
        age,
        gender,
        ethinicity,
        jaundice,
        autism,
        country_of_res,
        used_app_before,
        result,
        relation,
    ]

    #  till here we have the Input list now.
    prediction = best_model.predict([new_data])

    if prediction[0] == 0:
        final_result = "The person is predicted to have autism."
    else:
        final_result = "The person is predicted to dont have autism."

    return render_template("index.html", final_result=final_result)


@app.route("/templates/about.html")
def about():
    return render_template("about.html")


#  Main Function.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
