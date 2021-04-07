# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/mangokid/wombat/devel_isolated/system_control;/home/mangokid/wombat/devel_isolated/robot_setup_tf;/home/mangokid/wombat/devel_isolated/realsense2_description;/home/mangokid/wombat/devel_isolated/realsense2_camera;/home/mangokid/wombat/devel_isolated/keyboard_pub;/home/mangokid/wombat/devel_isolated/keyboard_cont;/home/mangokid/wombat/devel_isolated/joy_cmd;/home/mangokid/wombat/devel_isolated/diff_drive;/opt/ros/kinetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/mangokid/wombat/devel_isolated/wheel/env.sh')

output_filename = '/home/mangokid/wombat/src/wheel/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
