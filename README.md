# AZURE
----------------------------------

**Azure**,  is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers. I made this project to facilitate the use of Azure and Ansible.


## Requirements
----------------------------------
- Azure account
- OS Centos or Ubuntu
- Ansible 2.8.4
- azure-cli 2.0.69


## Installation
---------------------------------

First, you need to install [Azure modules] for Ansible (https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html) on your machine.I presume that azure-cli and Ansible already installed.

```bash
pip install ansible[azure]
```

Then, you need to create an Azure AD application and service principal with this Python script [Azure Service Principal](https://github.com/amine7777/azure-service-principal).

```bash
python service_principal.py
```
After getting the credentials you need to create a file to save them.
```bash
vi ~/.azure/credentials
```
In case you need to create a virtual machine. You need to set the value of state to *present*





## Usage
---------------------------------


This project contain many Ansible playbooks to create instances on Azure. For example if you need to create a resource group you need to run these command.

```bash
git clone https://github.com/amine7777/azure
cd azure
ansible-playbook deploy_irc.yaml --tags "resource_group"
```

In case you need to create a virtual machine. You need to set the value state to **present** and then run this command.

```bash
ansible-playbook deploy_vm.yaml
```
To destroy the virtual machine you just need to set the value state to **absent** and run this command.

```bash
ansible-playbook destroy_vm.yaml
```
The folder vm_all contain all the instances in one file.







## Contributing
---------------------------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Next improvements
----------------------------------
- Add load balancer playbook
- Add VMSS playbook

## Author
----------------------------------
- **Amine Kahlaoui**, DevOps engineer

## Acknowlegement
----------------------------------
You can also create the same thing with Terraform.
