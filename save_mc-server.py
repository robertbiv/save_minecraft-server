import subprocess
import os

_container_name = "mc-server"

def is_container_running(container_name):
    # Check if the Docker container is running
    result = subprocess.run(f"docker ps --filter name={container_name} --format '{{{{.Names}}}}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error checking container status: {result.stderr.decode()}")
        return False
    return container_name in result.stdout.decode().splitlines()

def send_command_wait_for_response(command, expected):
    if not is_container_running(_container_name):
        print(f"Container '{_container_name}' is not running.")
        return False

    # Run the command inside the Docker container with TTY
    docker_command = f"docker exec -i {_container_name} {command}"
    result = subprocess.run(docker_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check the result
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode()}")
        return False
    else:
        output = result.stdout.decode()
        for line in output.splitlines():
            if expected in line:
                return True
        print(f"Expected response not found. Output: {output}")
        return False

# Example usage
commands = [
    {"command": "list", "expected": "players online"},
    {"command": "version", "expected": "Minecraft"},
    {"command": "say Hello", "expected": "Hello"},
    {"command": "time query daytime", "expected": "Daytime"},
    {"command": "save-all", "expected": "Saved the game"}
]

for cmd in commands:
    success = send_command_wait_for_response(cmd["command"], cmd["expected"])
    if not success:
        print(f"Command '{cmd['command']}' failed.")