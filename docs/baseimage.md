# Mininet Docker Setup

## Purpose

The container extends `iwaseyusuke/mininet:latest` with our Python topology code and runs the topology automatically.

## Custom Entrypoint

The original Mininet image has `/ENTRYPOINT.sh`:

```bash
service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640
bash
service openvswitch-switch stop
```

It was designed for interactive use: it starts OVS, opens a Bash shell, then stops OVS when the shell exits.

That means our `CMD` would never run because the entrypoint always launches `bash`.

We therefore provide our own `entrypoint.sh`:

```bash
#!/usr/bin/env bash

set -e

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

"$@"

service openvswitch-switch stop
```

`"$@"` means **run the command supplied by Docker's `CMD`**.

Therefore the startup sequence becomes:

```text
Container starts
      ↓
entrypoint.sh
      ↓
Start Open vSwitch
      ↓
Configure OVS
      ↓
python3 main.py
      ↓
Mininet topology runs
      ↓
Python exits
      ↓
Stop Open vSwitch
      ↓
Container exits
```

## Running

`run.sh` starts the container with the privileges and mounts required by Mininet:

```bash
./run.sh
```

Use:

```bash
./run.sh --build
```

when the Docker image needs to be rebuilt.
