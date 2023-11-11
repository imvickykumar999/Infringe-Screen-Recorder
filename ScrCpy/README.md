
# One Time Connect (TCP / IP) ...

    >>> adb devices
        * daemon not running; starting now at tcp:5037
        * daemon started successfully
        List of devices attached

    >>> adb tcpip 5555
    >>> adb devices

    >>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
    >>> adb connect 192.168.0.103:5555


# Screen Copy (scrcpy) ...

    >>> adb devices -l
    >>> adb connect 192.168.0.103

    >>> scrcpy
    >>> scrcpy --tcpip=192.168.0.103

    # Run in Folder address bar to Power ON / OFF
    >>> adb -s 192.168.0.103 shell input keyevent 26
    >>> scrcpy -r recording.mp4

    >>> adb disconnect 192.168.0.103
    >>> adb disconnect
