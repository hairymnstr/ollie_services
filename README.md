# Scripts to run Ollie Mk3

These scripts run our racing robot.  They are run on the Raspberry Pi and coordinate all the system functions.

The scripts use [Zenoh](https://github.com/eclipse-zenoh) to share data.  To install the requirements on the current Raspberry Pi OS Lite you need to run the following commands:

    sudo apt install python3-pip
    pip3 install eclipse-zenoh

## Setting up the systemd services

The scripts themselves are in the scripts folder, but mostly we want them to run automatically on startup.  To do this we've used systemd service files which are in the systemd folder.  The scripts are all designed to be run by the user ollie and from a folder in the home directory called ollie\_services which contains this repository.  To enable each service you must use `systemctl enable` for example to enable the battery alarm service:

    sudo systemctl enable /home/ollie/ollie_services/systemd/battery-alarm.service

Once you've enabled the service you can use `systemctl` to start it (or reboot and it should start automatically):

    sudo systemctl start battery-alarm

To check for any error messages (e.g. you've fogotten to install Zenoh as described above) have a look at the output in the log:

    journalctl -u battery-alarm
