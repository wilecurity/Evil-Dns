import socket

# Function to generate the Python script with user's inputs
def generate_script(ip, domains):
    script_content = """
import subprocess
import socket
import threading

# Function to get the public IP address
def get_public_ip():
    try:
        # Use a public DNS server to resolve the hostname
        public_ip = socket.gethostbyname(socket.gethostname())
        print("Your public IP address is:", public_ip)
    except Exception as e:
        print("Error:", e)

# Function to redirect domains to a specified IP address
def redirect_domains(ip, domains):
    # Redirect domains to the specified IP address
    with open('/etc/hosts', 'a') as hostsfile:
        hostsfile.write('\\n')
        for domain in domains:
            hostsfile.write(ip + " " + domain + "\\n")
            hostsfile.write(ip + " www." + domain + "\\n")

    print("Domains redirected successfully!")

# Function to perform both tasks concurrently
def run_tasks(ip, domains):
    # Create threads for each task
    redirect_thread = threading.Thread(target=redirect_domains, args=(ip, domains))
    ip_thread = threading.Thread(target=get_public_ip)

    # Start both threads
    redirect_thread.start()
    ip_thread.start()

    # Wait for both threads to finish
    redirect_thread.join()
    ip_thread.join()

# Run the tasks with user-provided IP address and domains
run_tasks('{ip}', {domains})
""".format(ip=ip, domains=repr(domains))

    with open('generated_script.py', 'w') as file:
        file.write(script_content)

    print("Generated script 'generated_script.py' successfully!")

# Get user input for IP address and domains
ip = input("Enter the IP address you want to redirect to: ")
domains_str = input("Enter the domains you want to redirect (comma-separated): ")
domains = [domain.strip() for domain in domains_str.split(',')]

# Generate the Python script with user-provided inputs
generate_script(ip, domains)
