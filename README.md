# Locust Starter Kit
Locust Starter Kit for Performance Testing.
# Features:
1. Generic Locust Script - locustfile.py
2. Locust Script to perform Load Testing with different loads and shapes - locust_load.py
3. Locust Script to perform Spike Testing - locust_spike.py
4. Locust Script to perform Soak Testing - locust_soak.py
5. Dockerization
6. Distributed Testing using Docker

# Pre-requisites:

1. Installing all the required dependencies using requirements.txt file.

``` pip install -r requirements.txt ```

# Getting Started:

## 1. locustfile.py:

This is a generic locust script which can be run in both UI and headless mode. 

---> UI Mode: ``` locust -f org/thoughtworks/basicUI.py -H https://restful-booker.herokuapp.com ```

-H means the host on which we want to run the load tests.

Note: We need to provide Number od Users and Spawn Rate in the Locust UI as per our requirements

---> Headless Mode: ``` locust -f org/thoughtworks/basicUI.py --headless -H https://restful-booker.herokuapp.com -u 2 -r 1 -t 10s ```

-H means the host
<br /> -u means peak number of concurrent users with which we want to perform testing
<br /> -r means spawn rate (Rate at which users are created or spawned)
<br /> -t means total time for which we want to run the script

Note: When running in headless mode we need to provide number of users(-u), spawn rate(-r) and host(-H)
