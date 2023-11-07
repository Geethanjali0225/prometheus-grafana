from prometheus_client import start_http_server, Summary
import time

# Create a summary metric to measure the time it takes to execute your code
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing requests')

# Your "Hello World" function
@REQUEST_TIME.time()
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    # Start an HTTP server to expose the metrics on port 5000 and bind to all available network interfaces
    start_http_server(5000, addr='0.0.0.0')

    # Your application logic
    while True:
        hello_world()
        time.sleep(1)
