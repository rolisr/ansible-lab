# RabbitMQ Installation and Post-Installation Setup

This document provides step-by-step instructions for installing RabbitMQ via Ansible, configuring firewall rules, updating RabbitMQ settings, and testing the service with a producer script.

---

## Step 1: Install RabbitMQ Service Using Ansible

Run the following command on your control node. When prompted for the vault password, use **oxylabs**:

```bash
ansible-playbook -i inventory.yml playbook.yml --ask-vault-pass
```

## Step 2: If all went good, the last output of the ansible script should be:
```
ok: [lxc] => {
    "script_output.stdout_lines": [
        "Sent: Sample message 1",
        "Sent: Sample message 2",
        "Sent: Sample message 3",
        "Sent: Sample message 4",
        "Sent: Sample message 5"
    ]
}
```
