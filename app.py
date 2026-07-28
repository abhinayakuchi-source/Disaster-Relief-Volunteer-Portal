from flask import Flask, render_template, request
from firebase_config import db, auth
from firebase_client import auth as firebase_login
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        try:
            user = firebase_login.sign_in_with_email_and_password(
                email,
                password
            )

            return render_template(
                "volunteer_dashboard.html",
                email=email
            )

        except Exception as e:
            return "Invalid Email or Password"

    return render_template("login.html")
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        # Create user in Firebase Authentication
        user = auth.create_user(
    email=email,
    password=password
)

        # Store additional details in Firestore
        db.collection("volunteers").document(user.uid).set({
            "name": name,
            "email": email,
            "phone": phone,
            "role": "volunteer"
        })

        return "Volunteer Registered Successfully!"

    return render_template("register.html")

@app.route('/request-help', methods=['GET','POST'])
def request_help():

    if request.method == "POST":

        data = {
            "name": request.form["name"],
            "location": request.form["location"],
            "problem": request.form["problem"]
        }

        db.collection("help_requests").add(data)

        return "Help Request Submitted Successfully!"

    return render_template("request_help.html")

@app.route('/volunteer-dashboard')
def volunteer_dashboard():
    return render_template('volunteer_dashboard.html')

@app.route('/victim-dashboard')
def victim_dashboard():
    return render_template('victim_dashboard.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/ngo-dashboard')
def ngo_dashboard():
    return render_template('ngo_dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)