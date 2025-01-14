# QRaven - Dynamic QR Code Generator and Tracker

**QRaven** is a versatile web application that enables users to generate dynamic QR codes. Each QR code is linked to unique content that can change based on conditions like the time of day. This project offers a combination of QR code generation, dynamic redirection, and location-based content.

With plans to integrate more advanced features like user authentication, analytics, and real-time user location tracking, QRaven is a growing tool for businesses and personal projects.

## Features

### Current Features:
- **Dynamic QR Code Generation**: QR codes that redirect users to different content based on the time of day (e.g., morning, afternoon, or evening links).
- **Custom URL Mapping**: Users can input their custom URL, and a dynamic QR code will be generated.
- **Ngrok Integration**: Allows the application to run locally and provide a public-facing URL for QR code testing.
- **Backend Data Management**: Stores QR code mappings and user data in a `data.json` file.
- **Frontend Interface**: Simple and interactive interface to generate and view QR codes.

### Planned Features:
- **User Authentication**: Users can create accounts, log in, and manage their QR codes.
- **Analytics Dashboard**: Users will be able to view detailed analytics on the scans of their QR codes, including time, location, and frequency of scans.
- **Location-based QR Code Content**: Automatically change QR code redirection based on the user's location.
- **Abusive Content Monitoring**: Detection of offensive language in URLs or user input, with the ability to provide warnings or block content.
- **Mobile App Integration**: The QR code generation and dynamic content will be accessible via mobile devices.

## Technologies Used

- ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white): Web framework to build the app and handle routing.
- ![QR Code](https://img.shields.io/badge/QR%20Code-000000?style=flat&logo=qr%20code&logoColor=white): Python's `qrcode` library to generate the QR codes.
- ![JSON](https://img.shields.io/badge/JSON-000000?style=flat&logo=json&logoColor=white): For storing and managing mappings, user data, and QR code metadata.
- ![Ngrok](https://img.shields.io/badge/Ngrok-000000?style=flat&logo=ngrok&logoColor=white): Provides a public-facing URL for testing the app locally.
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white): For creating the basic frontend interface.
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white): For styling the frontend of the application.
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black): Will be used for future frontend interactivity and real-time updates.


## Installation

To set up the project locally, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/QRaven.git

2. Navigate to the project directory:
   ```bash
   cd QRaven
   
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

4. Install dependencies:
   ```bash
   pip install -r requirements.txt

5. Start the Flask application:
   ```bash
   python run.py
