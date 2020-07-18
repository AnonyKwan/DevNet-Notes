# DevNet
Learning Network Automation 

# Ansible Cheat-Sheet - Configuration & Operation

> **local hosts & ansible.cfg override the default**

>ansible --list-hosts ISP # **Display Group ISP**

>ansible --list-hosts ISP,Routers # **Display Group ISP & Routers**

>ansible --list-hosts \!ISP # **Exclude Group ISP**

>ansible -m ping --vault-password-file ansible-pwd all # **Import Vault File for password** !!!!! ERROR

> sed 's/\\n/\n/g' unreadable_backup_file > human_readable_file # **Conver Unreable file to IOS output**

---
>**Playbooks** - Essential

---
> [Ansible Network Docs](https://docs.ansible.com/ansible/latest/network/)


# pyATS  Cheat-Sheet - Operational Automation (Verification/Testing)
---
>Run in Virtual Enviroment

* python3 -m venv .

* source bin/activate .
---
> pyats create testbed interactive --output YAML/testbed.yaml --encode-password   **# Create Testbed File with interaction mode**

>pyats parse "show ip interface brief" --testbed-file YAML/testbed.yaml --output test1   **# Save the resuult to a location**

>pyats learn ospf --testbed-file YAML/testbed.yaml --output ospf   **# Learn OSPF Configuration for later compare**

>pyats learn ospf bgp rip eigrp --testbed-file YAML/testbed.yaml --output ospf   **# Learn multiple Configuration for later compare**

>pyats diff test1 test2   **# Compare the differences**

>**Python coding**

---
> [Genie API Link](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/)

> [Models List = pyats Learn](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models)

> [Parsers List = pyats parse](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers)


