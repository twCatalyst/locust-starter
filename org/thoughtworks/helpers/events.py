from locust import events

from org.thoughtworks.helpers import scenarios


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--scenario", type=str, env_var="LOCUST_SCENARIO", default="")


@events.test_start.add_listener
def _(environment, **kw):
    if environment.parsed_options.scenario == "load":
        print("load scenario")
        scenarios.StagesShape
