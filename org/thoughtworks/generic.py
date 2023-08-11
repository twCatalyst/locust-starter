from locust import HttpUser, task, between, events
import sys
import signal
import os


class MyUser(HttpUser):
    host = None

    wait_time = between(1, 3)

    @task
    def my_task(self):
        if self.host:
            self.client.get(self.host)


# Event hook to handle the case when no host is provided
@events.init.add_listener
def _(environment, **kw):
    try:
        if not environment.host:
            raise ValueError("Please provide the host as a command-line argument using --host=<your_host>")
        MyUser.host = environment.host
    except Exception as e:
        print(f"Error: {str(e)}")
        os.kill(os.getpid(), signal.SIGTERM)


@events.quitting.add_listener
def _(environment, **kw):
    # Stop the Locust process
    os.kill(os.getpid(), signal.SIGTERM)


if __name__ == "__main__":
    import sys
    from locust.main import main
    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
    sys.exit(main())


# Need to handle Duration, run mode - headless, number of users, spawn rate
# We can keep docker container running
