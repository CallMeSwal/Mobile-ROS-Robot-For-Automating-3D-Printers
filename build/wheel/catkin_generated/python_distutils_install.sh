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
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/mangokid/wombat/src/wheel"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/mangokid/wombat/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/mangokid/wombat/install/lib/python2.7/dist-packages:/home/mangokid/wombat/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/mangokid/wombat/build" \
    "/usr/bin/python2" \
    "/home/mangokid/wombat/src/wheel/setup.py" \
     \
    build --build-base "/home/mangokid/wombat/build/wheel" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/mangokid/wombat/install" --install-scripts="/home/mangokid/wombat/install/bin"
