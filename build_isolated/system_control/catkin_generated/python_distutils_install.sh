#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/mangokid/wombat/src/system_control"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/mangokid/wombat/install_isolated/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/mangokid/wombat/install_isolated/lib/python2.7/dist-packages:/home/mangokid/wombat/build_isolated/system_control/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/mangokid/wombat/build_isolated/system_control" \
    "/usr/bin/python" \
    "/home/mangokid/wombat/src/system_control/setup.py" \
    build --build-base "/home/mangokid/wombat/build_isolated/system_control" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/mangokid/wombat/install_isolated" --install-scripts="/home/mangokid/wombat/install_isolated/bin"
