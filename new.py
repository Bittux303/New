import os
import time
import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Function to simulate sending a comment (not recommended for Facebook)
def send_comment(post_id, comment_text, headers, delay_seconds):
    # URL for sending a comment (if using Facebook Graph API, adjust accordingly)
    url = f"https://graph.facebook.com/{post_id}/comments"

    data = {
        'message': comment_text
    }

    # Simulating delay before sending the comment
    time.sleep(delay_seconds)

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        return "Comment sent successfully!"
    else:
        return f"Failed to send comment: {response.text}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_comment', methods=['POST'])
def comment_action():
    try:
        # Get input values from the form
        cookies_file = request.files['cookies_file']
        header_name = request.form['header_name']
        delay_seconds = int(request.form['delay_seconds'])
        comment_file = request.files['comment_file']

        # Read comment file
        comment_text = comment_file.read().decode('utf-8')

        # Here you would extract cookies (e.g., from cookies_file)
        cookies = cookies_file.read().decode('utf-8')

        # Simulate headers (you can add more details)
        headers = {
            'User-Agent': header_name,
            'Cookie': cookies  # This would contain the raw cookies, but this is just for demo purposes
        }

        # Example Post ID (Replace with actual logic for fetching post ID)
        post_id = "your_post_id_here"

        # Send comment
        result = send_comment(post_id, comment_text, headers, delay_seconds)

        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
  
