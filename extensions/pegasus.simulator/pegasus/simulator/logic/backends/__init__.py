"""
| Author: Marcelo Jacinto (marcelo.jacinto@tecnico.ulisboa.pt)
| License: BSD-3-Clause. Copyright (c) 2023, Marcelo Jacinto. All rights reserved.
"""

from omni.isaac.core.utils.extensions import get_extension_id

from .backend import Backend
from .mavlink_backend import MavlinkBackend, MavlinkBackendConfig

if get_extension_id("omni.isaac.ros2_bridge") is not None:
    from .ros2_backend import ROS2Backend
