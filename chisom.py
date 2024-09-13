# This code is a simple one that calculates the length of the passed argument, Version 1 of app 
# Name of this app is --Jenkins-comment (python-app in Jenkinsfile)--------
# Updated docker info 3
#This comment was added to initiate the second build 

# This bucket is designed to hold version 2 of the code 
# Added additional functions  for a web interface

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    comment = data['comment']
    length = len(comment)
    words = len(comment.split())
    sentiment = "Positive" if "enjoy" in comment else "Neutral"  # Simplified sentiment analysis

    return jsonify({
        'length': length,
        'word_count': words,
        'sentiment': sentiment
    })

if __name__ == '__main__':
    # Bind Flask app to host 0.0.0.0 and port 8084
    app.run(host='0.0.0.0', port=8084)