# CMake generated Testfile for 
# Source directory: /home/mangokid/wombat/src/diff_drive
# Build directory: /home/mangokid/wombat/build_isolated/diff_drive
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_diff_drive_nosetests_tests "/home/mangokid/wombat/build_isolated/diff_drive/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/mangokid/wombat/build_isolated/diff_drive/test_results/diff_drive/nosetests-tests.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/mangokid/wombat/build_isolated/diff_drive/test_results/diff_drive" "/usr/bin/nosetests-2.7 -P --process-timeout=60 --where=/home/mangokid/wombat/src/diff_drive/tests --with-xunit --xunit-file=/home/mangokid/wombat/build_isolated/diff_drive/test_results/diff_drive/nosetests-tests.xml")
subdirs(gtest)
