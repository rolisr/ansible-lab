# Install iptables
sudo apt install -y iptables iptables-persistent

# Block all incomging traffic
sudo iptables -P INPUT DROP

# Allow all traffic on loopback interface
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow console access from outside
sudo iptables -A INPUT -p tcp --dport 15672 -j ACCEPT

# Allow ssh traffic from outside
sudo iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT

# Allow established connections
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Save rules to survive reboot
iptables-save > /etc/iptables/rules.v4
