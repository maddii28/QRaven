QRaven is a versatile web application that enables users to generate dynamic QR codes. Each QR code is linked to unique content that can change based on conditions like the time of day. This project offers a combination of QR code generation, dynamic redirection, and location-based content.

With plans to integrate more advanced features like user authentication, analytics, and real-time user location tracking, QRaven is a growing tool for businesses and personal projects.

Features

Current Features:
Dynamic QR Code Generation: QR codes that redirect users to different content based on the time of day (e.g., morning, afternoon, or evening links).
Custom URL Mapping: Users can input their custom URL, and a dynamic QR code will be generated.
Ngrok Integration: Allows the application to run locally and provide a public-facing URL for QR code testing.
Backend Data Management: Stores QR code mappings and user data in a data.json file.
Frontend Interface: Simple and interactive interface to generate and view QR codes.
Planned Features:
User Authentication: Users can create accounts, log in, and manage their QR codes.
Analytics Dashboard: Users will be able to view detailed analytics on the scans of their QR codes, including time, location, and frequency of scans.
Location-based QR Code Content: Automatically change QR code redirection based on the user's location.
Abusive Content Monitoring: Detection of offensive language in URLs or user input, with the ability to provide warnings or block content.
Mobile App Integration: The QR code generation and dynamic content will be accessible via mobile devices.
Technologies Used

Flask: Web framework to build the app and handle routing.
QR Code Generation: Python's qrcode library to generate the QR codes.
JSON: For storing and managing mappings, user data, and QR code metadata.
Ngrok: Provides a public-facing URL for testing the app locally.
HTML/CSS: For creating the basic frontend interface.
JavaScript: Will be used for future frontend interactivity and real-time updates.
Installation

To set up the project locally, follow the steps below:

Clone the repository:
git clone https://github.com/yourusername/QRaven.git
Navigate to the project directory:
cd QRaven
Create a virtual environment (optional but recommended):
python -m venv venv
Install dependencies:
pip install -r requirements.txt
Start the Flask application:
python run.py
Open the app in your browser:
The app should now be accessible at http://127.0.0.1:5000/.
Usage

Home Page:
Navigate to the home page to input custom content for the QR code.
The generated QR code will be displayed on the screen.
Generate QR Code:
Input the URL you want to associate with your QR code.
The app will dynamically generate a QR code based on the time of day or user input.
Scan the QR Code:
Scan the generated QR code using any QR code scanner, and the app will redirect you to the mapped URL.
Folder Structure

QRaven/
│
├── app/                        # Main application folder
│   ├── __init__.py              # Initialize Flask app
│   ├── routes.py                # All routes and views
│   ├── utils.py                 # Utility functions (e.g., data handling, QR code generation)
│   ├── models.py                # Data models (e.g., for handling user authentication, etc.)
│   └── config.py                # Configuration for the app (e.g., secret keys, environment settings)
│
├── data/                        # Folder for storing dynamic content
│   └── data.json                # Stores mappings, time conditions, user data (for now)
│
├── static/                      # For storing static assets like images, JS, CSS files
│   └── /images                  # Images (e.g., generated QR codes)
│   └── /css                     # Custom CSS for frontend
│   └── /js                      # Custom JS for frontend interactions
│
├── templates/                   # HTML templates (frontend views)
│   └── index.html               # Home page template
│   └── generate_qr.html         # Template for QR code generation
│   └── analytics.html           # Template for analytics dashboard (in the future)
│   └── login.html               # Template for user login (in the future)
│   └── register.html            # Template for user registration (in the future)
│
├── requirements.txt             # Python dependencies (e.g., Flask, Requests, etc.)
├── .gitignore                   # Git ignore file (e.g., for venv, config secrets)
├── README.md                    # Project documentation
└── run.py                       # To run the application (useful for production or local)
Contributing

If you'd like to contribute to the QRaven project, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.
License

This project is licensed under the MIT License - see the LICENSE file for details.

