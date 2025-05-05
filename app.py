from flask import Flask, Response

# Create Flask application instance
app = Flask(__name__)

# Define route handler for all paths
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    # Return 'Hello, World!' with a newline, exactly matching the Node.js implementation
    return Response('Hello, World!\n', mimetype='text/plain')

if __name__ == '__main__':
    # Bind to localhost:3000, matching the Node.js implementation
    hostname = '127.0.0.1'
    port = 3000
    
    # Log server startup information, similar to the Node.js implementation
    print(f"Server running at http://{hostname}:{port}/")
    
    # Start the Flask application
    app.run(host=hostname, port=port)