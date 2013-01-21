# bootalert script for Arch Linux / systemd

This script is meant to run on boot of an Arch Linux server. 

It sends an email alerting that the server has been booted, including the ip address of the server.

## Requirements

* systemd (Arch Package systemd)
* postfix (Arch Package postfix)

Postfix also needs to be enabled with systemd

    systemctl enable postfix

## Configuration

The script will attempt to get mailto and mailfrom addresses from a configuration file: /etc/conf.d/bootalert. 

If no configuration file is found it will send the message to root from root.

## License

This script is distributed under the MIT License (see LICENSE)
