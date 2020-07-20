import nornir.core
import json
import pprint
import pathlib
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


######################################################################################################
######################################################################################################


# Backup Function / store file to backup folder
######################################################################################################
# def backup_config (task):
#     location = "backup/{}".format(date.today())
#     pathlib.Path(location).mkdir(parents=True, exist_ok=True)
#     result = task.run(task=netmiko_send_command,
#                 command_string="show run",
#                 enable=True)
#     task.run(task=write_file,
#               content=result.result,
#               filename="{}/{}-{}.txt".format(location,task.host,date.today()))
#     print("{}: Backup Successful!".format(task.host))
#
# cisco_all.run(name="Backup Configuration Files",
#               task=backup_config) # call the function send_command that i createc
#
######################################################################################################
# print(date.today().strftime("%d-%m-%y"))

# Push Bakcup Config to all Devices
######################################################################################################
# def push_config (task,config_date):
#     result = task.run(task=netmiko_send_config,
#              config_file="backup/{}/{}-{}.txt".format(config_date,task.host,config_date))
#     return result
#
# cisco_all.run(name="Push Config to devices",
#               task=push_config,
#               config_date="2020-07-20")
# print_result(push_config)
######################################################################################################

# Show version function
######################################################################################################
# def show_version(task):
#     result = task.run(task=netmiko_send_command,
#                       command_string="show version")
#     print(task.host)
#     print_result(result)
# 
# cisco_all.run(name="Show Version",
#               task=show_version)
######################################################################################################

#napalm_validate
# DO NOT WORK!
######################################################################################################
# def config_validate (task,souce_date):
#     result = task.run(task=netmiko_send_command,
#                       command_string="show run")
#
#     result_validate = task.run(task=napalm_validate,
#                     validation_source=result,
#                     src="backup/{}/{}-{}.txt".format(souce_date,task.host,souce_date))
#     print_result(result_validate)
#
# cisco_all.run(name="Check Config",
#               task=config_validate,
#               souce_date="2020-07-20")
######################################################################################################














######################################################################################################
#pyATS -- USE CLI RECOMMANDED
######################################################################################################
# from genie.testbed import load
# from genie.utils.diff import Diff
# import pyats 

# tb = load("pyATS-testbed/testbed.yml")

# Compare the differences
######################################################################################################
# r1 = tb.devices["R1"]
# r2 = tb.devices["R2"]

# r1.connect()
# r2.connect()
# result_1 = r1.parse("show ip interface brief")
# result_2 = r2.parse("show ip interface brief")
# diff = Diff(result_1,result_2)
# diff.findDiff()
# print(diff)

#result
# R2#
#  interface:
#   GigabitEthernet0/0:
# -  ip_address: 10.0.0.10
# +  ip_address: 10.0.0.11
######################################################################################################

######################################################################################################
#list all devices and parse show ip int bri to the devices ############ CLI IS MUCH EASYER
# push_command = {}
# push_command_2 = {}
# for name,device in tb.devices.items():
#     print ("The Device is {}".format(name))
#     device.connect()
#     push_command[name] = {}
#     push_command_2[name] = {}
#     push_command[name]['show-ip'] = device.parse('show ip interface brief')
#     push_command_2[name]['show-ip'] = device.parse('show ip interface brief')
######################################################################################################    

# ISP1 = tb.devices["ISP"]
# ISP1.connect()
# print ( ISP1.parse("show ip interface brief"))
