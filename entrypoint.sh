#!/bin/bash
set -e

# Start the Locust process in the background
locust -f /locust/generic.py --host=$HOST &

# Save the PID of the Locust process
LOCUST_PID=$!

# Function to gracefully stop the Locust process
function stop_locust {
    echo "Stopping Locust..."
    kill -SIGTERM $LOCUST_PID
    wait $LOCUST_PID

}

# Register the stop_locust function to be called on SIGTERM signal
trap stop_locust SIGTERM

# Wait for the Locust process to exit
wait $LOCUST_PID
