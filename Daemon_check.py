import subprocess

def check_running_daemons():
    try:
        # Get the list of all running daemons
        output = subprocess.check_output(['systemctl', '--type', 'service', '--state', 'running', '--quiet']).decode('utf-8')

        # Split the output into individual lines
        lines = output.strip().split('\n')

        # Print the name of each running daemon
        for line in lines:
            daemon_name = line.strip().split('.service')[0]
            print(daemon_name)

    except subprocess.CalledProcessError as e:
        print("Error occurred while checking running daemons:", e)

# Run the function to check running daemons
check_running_daemons()
