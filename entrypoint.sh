#!/usr/bin/env bash

set -e

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

"$@"

service openvswitch-switch stop
