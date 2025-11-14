# Minecraft Server Save Script

A Python utility script for managing and monitoring a Dockerized Minecraft server. This script allows you to send commands to a running Minecraft server container and verify responses.

## Description

This script provides a simple way to interact with a Minecraft server running in a Docker container. It can check if the container is running, send commands to the server, and verify that expected responses are received.

## Prerequisites

- Python 3.x
- Docker
- A running Minecraft server in a Docker container named `mc-server`

## Features

- Check if the Minecraft server Docker container is running
- Send commands to the Minecraft server via Docker exec
- Wait for and verify expected responses from server commands
- Execute multiple commands in sequence

## Usage

### Basic Usage

Run the script directly:

```bash
python save_mc-server.py
```

### Default Commands

The script includes example commands that are executed by default:

1. **list** - Check players online
2. **version** - Display Minecraft version
3. **say Hello** - Broadcast a message
4. **time query daytime** - Query the current game time
5. **save-all** - Save the game state

### Customizing Commands

Edit the `commands` list in the script to add or modify commands:

```python
commands = [
    {"command": "your-command", "expected": "expected-response-text"},
    # Add more commands as needed
]
```

## Configuration

### Container Name

The default container name is `mc-server`. To change it, modify the `_container_name` variable:

```python
_container_name = "your-container-name"
```

## Functions

### `is_container_running(container_name)`

Checks if a Docker container with the specified name is currently running.

**Parameters:**
- `container_name` (str): The name of the Docker container to check

**Returns:**
- `bool`: True if the container is running, False otherwise

### `send_command_wait_for_response(command, expected)`

Sends a command to the Minecraft server and checks for an expected response.

**Parameters:**
- `command` (str): The Minecraft server command to execute
- `expected` (str): The expected text in the response

**Returns:**
- `bool`: True if the expected response was found, False otherwise

## Example Output

```
Command 'list' succeeded.
Command 'version' succeeded.
Command 'say Hello' succeeded.
Command 'time query daytime' succeeded.
Command 'save-all' succeeded.
```

## Error Handling

The script includes basic error handling:
- Checks if the container is running before sending commands
- Displays error messages from Docker commands
- Verifies expected responses are received

## Notes

- Ensure your Docker container is named `mc-server` or update the `_container_name` variable
- The script uses `docker exec -i` to send commands without allocating a TTY
- Commands are executed sequentially, not in parallel

## License

This project is provided as-is for managing Minecraft servers.

## Author

robertbiv
