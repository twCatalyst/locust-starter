from locust import HttpUser, task, constant, LoadTestShape, SequentialTaskSet


class UserJourney(SequentialTaskSet):

    @task
    def demo_get_test(self):
        print("Get Users")
        self.client.get("/api/users?page=2", name='Users List')

    @task
    def demo_post_test(self):
        print("Create User")
        post_url = "/api/users"

        request_body = {
            "name": "morpheus",
            "job": "leader"
        }
        self.client.post(post_url, request_body, name='Create User')

    @task
    def demo_put_test(self):
        print("Update Users")
        post_url = "/api/users/2"

        request_body = {
            "name": "morpheus",
            "job": "Zion Resident"
        }
        self.client.put(post_url, request_body, name='Update User')

    @task
    def demo_login_test(self):
        print("User Login")
        post_url = "/api/login"

        request_body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        self.client.post(post_url, request_body, name='Login Token')


class DemoHttpUser(HttpUser):
    tasks = [UserJourney]
    constant(2)


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 100, "users": 100, "spawn_rate": 10},
        {"duration": 180, "users": 100, "spawn_rate": 10},
        {"duration": 220, "users": 100, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None