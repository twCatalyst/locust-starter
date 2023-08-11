from locust import HttpUser, task, between, events
import sys
import argparse

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_task(self):
        if self.host:
            self.client.get(self.host)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Locust load testing script")
    parser.add_argument("--host", type=str, required=True, help="Host to load test (e.g., http://example.com)")
    parser.add_argument("--locust-file", type=str, required=True, help="Locust file to run")
    return parser.parse_args()

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    args = parse_arguments()
    MyUser.host = args.host

    # Dynamically load the specified locust file
    locust_file = args.locust_file
    try:
        environment.locust_classes = [locust_file]
    except Exception as e:
        print(f"Error: Failed to load locust file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parse_arguments()
