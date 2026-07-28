# Disaster Relief Volunteer Portal

## Project Overview

The Disaster Relief Volunteer Portal is a cloud-based web application developed using Flask and Firebase. It helps manage disaster relief activities by allowing volunteers to register, log in, and participate in relief operations. The system also allows victims to submit help requests, which are stored securely in the cloud.

## Features

- Volunteer Registration
- Volunteer Login
- Firebase Authentication
- Cloud Firestore Database
- Victim Help Request Form
- Volunteer Dashboard
- Admin Dashboard
- NGO Dashboard
- Responsive Web Interface

## Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Bootstrap 5
- Firebase Authentication
- Firebase Cloud Firestore
- VS Code

## Project Structure

```
DisasterReliefVolunteerPortal/
│── app.py
│── firebase_config.py
│── firebase_client.py
│── requirements.txt
│── .gitignore
│── templates/
│── static/
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DisasterReliefVolunteerPortal.git
```

2. Navigate to the project folder:

```bash
cd DisasterReliefVolunteerPortal
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Add your Firebase service account key:

```
serviceAccountKey.json
```

5. Run the application:

```bash
python app.py
```

6. Open your browser and visit:

```
http://127.0.0.1:5000
```

## Firebase Services Used

- Firebase Authentication
- Cloud Firestore

## Modules

### Volunteer
- Register
- Login
- View Dashboard

### Victim
- Submit Help Request

### Admin
- Manage Volunteers
- Monitor Requests

### NGO
- Coordinate Relief Activities

## Future Enhancements

- Real-time notifications
- GPS-based volunteer tracking
- File upload for disaster reports
- Email notifications
- Mobile application

## Author

**Abhinaya Kuchi**

B.Tech - Artificial Intelligence and Data Science

## License

This project is developed for educational purposes.
