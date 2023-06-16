from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def my_task(self):
        self.client.get("/booking")

class MyUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)


# Host: 'https://restful-booker.herokuapp.com'

# Normal UI Mode: locust -f org/thoughtworks/basicUI.py -H https://restful-booker.herokuapp.com
# Headless Mode: locust -f org/thoughtworks/basicUI.py --headless -H https://restful-booker.herokuapp.com -u 2 -r 1 -t 10s