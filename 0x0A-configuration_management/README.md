# 0x0A. Configuration management

## INTRODUCTION
Welcome to the Puppet Learning directory in our DevOps Engineering repository! 🚀 .
This space is dedicated to helping you understand and master Puppet,
a powerful configuration management and automation tool.
## DESCRIPTION
Puppet is a configuration management tool that enables you to automate the provisioning and management of infrastructure.
Whether you are a beginner or looking to enhance your Puppet skills,
this directory provides a structured learning path with hands-on examples and exercises.

## Requirements
### General

    All your files will be interpreted on Ubuntu 20.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp
## Install puppet

$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

Puppet 5 Docs
Install puppet-lint

$ gem install puppet-lint
