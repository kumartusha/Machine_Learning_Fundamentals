#  Here is the Python Code for Our Application.


from flask import Flask, request, render_template
import pickle

#  Flask App Creation.
app = Flask(__name__)

#  Load the Models.
# best_model = pickle.load(open("./models/best_model.pkl", "rb"))
# scaling_model = pickle.load(open("./models/label_encoder.pkl", "rb"))


# Create the Different Routes for Our Model.
@app.route("/")
def main():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    return render_template("index.html")


@app.route("/templates/about.html")
def about():
    return render_template("about.html")


#  Main Function.
if __name__ == "__main__":
    app.run(debug=True, port=5001)
