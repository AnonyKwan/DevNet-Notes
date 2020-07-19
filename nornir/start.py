import nornir.core
import json
import pprint
from datetime import date
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F
from nornir.plugins.tasks.networking import napalm_get, napalm_validate, netmiko_send_command, tcp_ping, netmiko_send_config
from nornir.plugins.tasks.files import write_file

# 1. Import the module that we need to use from
# [https://nornir.readthedocs.io/en/latest/plugins/index.html]
# the module Name [nornir.plugins.tasks.networking.netconf_get_config]
# can be read as from nornir.plugins.tasks.networking import netconf_get_config

# 2. Import the config file follow to the nornir docs
# [https://nornir.readthedocs.io/en/latest/tutorials/intro/initializing_nornir.html]

nr = InitNornir(config_file="config.yaml")

# 3. filter out a device or devices (Group) as a target machine

cisco_all = nr.filter(F(groups__contains="CISCO"))

# 4. execution
#  the keywork [task=] can be ignore
#  the Parameters need to refer to the plugins

# result = cisco_all.run(netmiko_send_command,
#                   command_string="show ip int bri")

# result = cisco_all.run(task=napalm_get,
#                        getters=("config"),
#                        retrieve="all")

# ip = "1.1.1.1"
# result = cisco_all.run(task=tcp_ping,
#                        ports=80,
#                        host=ip)

#result = cisco_all.run(task=netmiko_send_config,
#                        config_commands=["int lo 1", "desc config via nornir" , "ip addr 1.1.1.1 255.255.255.255"])

# Pushing Config file
#result = cisco_all.run(task=netmiko_send_config,
#                       config_file="config-files/delete-lo1.txt")



# Backup Function / store file to backup folder
######################################################################################################
def backup_config (task,commands):
     result = task.run(task=netmiko_send_command,
                command_string=commands,
                enable=True)
     task.run(task=write_file,
              content=result.result,
              filename="backup/{}-{}.txt".format(task.host,date.today()))
     print("{}: Backup Successful!".format(task.host))

cisco_all.run(name="Backup Configuration Files",
              task=backup_config, # call the function send_command that i createc
              commands="show run")
######################################################################################################
# print(date.today().strftime("%d-%m-%y"))