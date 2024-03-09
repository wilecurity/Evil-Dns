# Linux Evil-DNS

Linux Evil-DNS is a Python script that enables users to redirect specified domain names to a custom IP address, without victim knowledge. This script can be used for various purposes such as testing network security, implementing content filtering, or conducting ethical hacking exercises.

## Features

- Redirect specified domain names to a custom IP address in the local machine's `/etc/hosts` file.
- Ability to run in the background while providing the user with their public IP address.
- Simple and easy-to-use command-line interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/linux-evil-dns.git



2.   ```bash
     cd linux-evil-dns


3.  ```bash
     python3 evil_dns.py



 Usage

    Enter the IP address you want to redirect to when prompted.
    Enter the domains you want to redirect (comma-separated) when prompted.
    The script will generate a Python script named generated_script.py which will perform the redirection.




