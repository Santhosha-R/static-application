import subprocess
import os
import shutil



def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


if shutil.which("nginx"):
    print("Nginx is already installed.")
else:
    command = "sudo apt-get update && sudo apt-get install -y nginx "
    run(command)

run("sudo mv ./culturehub.info.config /etc/nginx/sites-available/culturehub.info")
run("sudo ln -s /etc/nginx/sites-available/culturehub.info /etc/nginx/sites-enabled/culturehub.info")
run("sudo rm -f /etc/nginx/sites-enabled/default")

run("sudo mkdir -p /var/www/culturehub.info/html")
run("sudo mv /tmp/index.html /var/www/culturehub.info/html/index.html")

run("sudo nginx -t && sudo systemctl reload nginx")

