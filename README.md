# BugBounty Platform

bug bounty platform is a platform made under the supervision of Mr.Ahmed Chabchoub, Mr.Mostfa Hamza for the Isetcom security event as a start.
the platform is a bug reporting interface for contesters to report vulnerabilities and proof of concept.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python3
Flask
MongoDB
```

### Installing

Please follow these steps to successfully deploy the web app in your local environment.


Step1: cloning the repository in your machine.

```
git clone https://github.com/HoussemCharf/BugBounty_Platform.git
```
Step2: start bin
```
source env/bin/activate
```
Step3: start MongoDB service

```
service mongod start
```
step4: create database

```
mongo

use iset_bugbounty;

```

### Coding style

Please follow those coding style techniques for a better code readability  


Variable names:
```
UserCurrentName="Houssem"
```
Function name:
```
def encode_auth_token(self, user_id):
```
Comments:
```
def encode_auth_token(self, user_id):
"""
Generates the Auth Token
:return: string
"""

```


## Deployment

Notes
## Built With

* [Flask](http://flask.pocoo.org/) - Flask (A Python Microframework)



## Versioning

For the versions available, see the [tags on this repository](https://github.com/HoussemCharf/BugBounty_Platform/tags). 

## Authors

* **Houssem Charfeddine** - *BBP* - [HoussemCharf](https://github.com/HoussemCharf)
* **Souheil Barhoumi** - *BBP* - [harloNzz](https://github.com/harloNzz)


## Acknowledgments
this platform is a property of Calynga Startup and its copyrights go for the authors. 
Many thanks for the following people because they made this happen:

* Mr.Ahmed Chabchoub
* Mr.Mostfa Hamza
