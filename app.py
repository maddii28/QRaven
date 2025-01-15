from flask import Flask, request, jsonify, send_file, redirect
import qrcode
import io
import json
import uuid
import datetime
import requests

def get_ngrok_url():
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json()["tunnels"]
        for tunnel in tunnels:
            if tunnel["proto"] == "https":
                return tunnel["public_url"]
    except Exception as e:
        print(f"Error fetching ngrok URL: {e}")
    return None


app = Flask(__name__)

# File to store the mappings
DATA_FILE = 'data.json'

# Function to read JSON data
def read_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to write JSON data
def write_data(data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to {DATA_FILE}: {e}")

@app.route('/')
def home():
    return "Welcome to QRaven! Generate QR codes dynamically."

@app.route('/generate', methods=['GET'])
def generate_qr():
    # Load existing mappings
    data = read_data()

    # Generate unique ID
    unique_id = str(uuid.uuid4())

    # Get user-provided content or use default content
    user_content = request.args.get('content', 'https://example.com/dynamic-content')

    # Get time-based conditions for the dynamic content
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        condition = "morning"
        redirect_link = "https://example.com"
    elif 12 <= current_hour < 18:
        condition = "afternoon"
        redirect_link = "https://chatgpt.com"
    else:
        condition = "evening"
        redirect_link = "https://gmail.com"

    # Add new mapping with timestamp, condition, and link
    data[unique_id] = {
        "timestamp": datetime.datetime.now().isoformat(),
        "condition": condition,
        "redirect_link": redirect_link
    }
    
    # Save updated data back to JSON file
    write_data(data)

    # Get ngrok URL for dynamic link
    ngrok_url = get_ngrok_url()
    if not ngrok_url:
        return "Ngrok URL could not be determined. Please ensure ngrok is running.", 500
    
    # Create dynamic link
    dynamic_link = f"{ngrok_url}/dynamic/{unique_id}"

    # Generate QR code for the dynamic link
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dynamic_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Return QR code image
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/dynamic/<unique_id>', methods=['GET'])
def dynamic_redirect_with_location(unique_id):
    # Load data
    data = read_data()

    # Fetch the mappings for the unique ID
    if unique_id in data:
        entry = data[unique_id]

        # Extract the redirect link
        redirect_link = entry.get("redirect_link", "")

        if redirect_link:
            # Log user's location if available
            user_ip = request.remote_addr
            user_location = request.args.get('location', 'Unknown')

            # Update entry with user location details
            entry['scans'] = entry.get('scans', [])
            entry['scans'].append({
                "ip": user_ip,
                "location": user_location,
                "timestamp": datetime.datetime.now().isoformat()
            })

            # Save updated data back to JSON
            data[unique_id] = entry
            write_data(data)

            return redirect(redirect_link)
        else:
            return "No link found for this QR code.", 404
    else:
        return "Invalid QR Code or content not found.", 404


if __name__ == '__main__':
    app.run(debug=True)
