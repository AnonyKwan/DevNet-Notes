# **DevNet**
Learning Network Automation 

# **Ansible Cheat-Sheet** - CLI-based (Configuration & Operation)

> **local hosts & ansible.cfg override the default**

>ansible --list-hosts ISP # **Display Group ISP**

>ansible --list-hosts ISP,Routers # **Display Group ISP & Routers**

>ansible --list-hosts \!ISP # **Exclude Group ISP**

> sed 's/\\n/\n/g' unreadable_backup_file > human_readable_file # **Conver Unreable file to IOS output**

> ansible-vault encrypt_string --vault-id ansible_ssh@prompt 'CISCO123' --name 'ansible_password' # **Vault ID can be anything, CISCO123 is the str that need to be encrypted**

>ansible -i hosts-yaml -m ping --ask-vault-pass all # **Import Vault File for password**

---
> [Ansible Network Docs](https://docs.ansible.com/ansible/latest/network/)

# **NorNir Cheat-Sheet** - Python-Based (Configuration & Operation) Most efficient **Preferred**

> Go through the tutorial of the official Documentation

> ref the code i wrote

---
>[Nornir Docs  >> Most Important <<](https://nornir.readthedocs.io/en/latest/index.html)

>[Nornir Plugins](https://nornir.readthedocs.io/en/latest/plugins/index.html)

# **pyATS  Cheat-Sheet** - CLI & Python-Based (Operation) (Verification/Testing) 

>Run in Virtual Enviroment

* python3 -m venv .

* source bin/activate .
---
> pyats create testbed interactive --output YAML/testbed.yaml --encode-password   **# Create Testbed File with interaction mode**

>pyats parse "show ip interface brief" --testbed-file YAML/testbed.yaml --output test1   **# Save the resuult to a location**

>pyats learn ospf --testbed-file YAML/testbed.yaml --output ospf   **# Learn OSPF Configuration for later compare**

>pyats learn ospf bgp rip eigrp --testbed-file YAML/testbed.yaml --output ospf   **# Learn multiple Configuration for later compare**

>pyats diff test1 test2   **# Compare the differences**

>pyats create testbed file --path  SampleTestbedFile.xlsx --output my_testbed.yaml # **Cover CSV file to YAML testbed**

---
> [Genie API Link](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/)

> [Models List = pyats Learn](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/models)

> [Parsers List = pyats parse](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/parsers)



