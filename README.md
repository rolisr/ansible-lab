# RabbitMQ Installation and Post-Installation Setup

This document provides step-by-step instructions for installing RabbitMQ via Ansible, configuring firewall rules, updating RabbitMQ settings, and testing the service with a producer script.

---

## Step 1: Install RabbitMQ Service Using Ansible

Run the following command on your control node. When prompted for the vault password, use **oxylabs**:

```bash
ansible-playbook -i inventory.yml playbook.yml --ask-vault-pass
```

## Step 2: Upload the post-install Directory to the Server
Transfer the entire post-install directory to your target server. For example, using scp:

```bash
scp -r post-install/ user@your_server_ip:/path/to/destination
```
Then, log in to your server and change into the post-install directory:

```bash
cd /path/to/destination/post-install
```
## Step 3: Apply Firewall Rules
In the post-install directory, execute the firewall configuration script to apply the iptables rules:

```bash
./iptables.sh
```
This script applies the necessary firewall rules to secure your RabbitMQ installation.

## Step 4: Apply New RabbitMQ Configuration
To configure RabbitMQ to listen only on localhost, copy the new configuration file and restart the service. Run:

```bash
sudo cp rabbitmq.conf /etc/rabbitmq/ && sudo service rabbitmq-server restart
```

## Step 5: Test RabbitMQ Service with a Producer Script
Before testing, ensure that the Python package pika is installed. If not, install it with:

```bash
pip3 install pika
```
Next, run the provided producer.py script to send sample messages to RabbitMQ:

```bash
python3 producer.py
```
