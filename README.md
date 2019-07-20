# network-shutdown

A little script that exposes an API for power management over the network

**WARNING:** Do NOT use this in insecure or publicly available networks. There is currently no authentication mechanism to prevent unauthorized access.

## Installation

Clone the repository, create a virtual environment in the directory `.venv` and install all dependencies:
```
git clone https://github.com/danieldirks/network-shutdown.git
cd network-shutdown
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```

*If you want to use an other name for the virtual environment or want to use the system interpreter (which I would not recommend), you need to change the references in [start.sh](start.sh).*

You can now create an autostart job for [start.sh](start.sh) to run the server on every startup.

## Configuration

The [config.ini](config.ini) contains all configuration keys and is mostly self-explaining. It currently uses systemctl for power management to allow running without privileges.

The default port for the API is `48080`.

## Features

I wrote the script to let my smart home system shutdown my computer.

The script exposes a REST API with [flask-restful](https://github.com/flask-restful/flask-restful) which allows the following requests:

- `/shutdown` - Runs the [shutdown command](config.ini)
- `/reboot` - Runs the [reboot command](config.ini)
- `/suspend` - Runs the [suspend command](config.ini)
- `/lock` - Runs the [lock command](config.ini)
