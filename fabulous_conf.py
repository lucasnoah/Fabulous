import os.path

fabconf = {}

#  Do not edit
fabconf['FABULOUS_PATH'] = os.path.dirname(__file__)

# Username for connecting to EC2 instaces
fabconf['SERVER_USERNAME'] = "ubuntu"

# Full local path for .ssh
fabconf['SSH_PATH'] = "/home/lucas/Downloads/"

# Name of the private key file you use to connect to EC2 instances
fabconf['EC2_KEY_NAME'] = "key.pem"

# Don't edit. Full path of the ssh key you use to connect to EC2 instances
fabconf['SSH_PRIVATE_KEY_PATH'] = '%s/%s' % (fabconf['SSH_PATH'], fabconf['EC2_KEY_NAME'])

# Project name: polls
fabconf['PROJECT_NAME'] = "zentertainme"

# Where to install apps
fabconf['APPS_DIR'] = "/home/%s/webapps" % fabconf['SERVER_USERNAME']

# Where you want your project installed: /APPS_DIR/PROJECT_NAME
fabconf['PROJECT_PATH'] = "%s/%s" % (fabconf['APPS_DIR'], fabconf['PROJECT_NAME'])

# App domains
fabconf['DOMAINS'] = "zentertain.me www.zentertain.me"

# Path for virtualenvs
fabconf['VIRTUALENV_DIR'] = "/home/%s/.virtualenvs" % fabconf['SERVER_USERNAME']

# Email for the server admin
fabconf['ADMIN_EMAIL'] = "lucas.bird.noah@gmail.com"

# Git username for the server
fabconf['GIT_USERNAME'] = "Server"

# Name of the private key file used for github deployments
fabconf['GITHUB_DEPLOY_KEY_NAME'] = "github"

# Don't edit. Local path for deployment key you use for github
fabconf['GITHUB_DEPLOY_KEY_PATH'] = "%s/%s" % (fabconf['SSH_PATH'], fabconf['GITHUB_DEPLOY_KEY_NAME'])

# Path to the repo of the application you want to install
fabconf['GITHUB_REPO'] = "https://github.com/gcollazo/Blank-django-Project.git"

# Virtualenv activate command
fabconf['ACTIVATE'] = "source /home/%s/.virtualenvs/%s/bin/activate" % (fabconf['SERVER_USERNAME'], fabconf['PROJECT_NAME'])

# Name tag for your server instance on EC2
fabconf['INSTANCE_NAME_TAG'] = "ZENSERVER
# EC2 key. http://bit.ly/j5ImEZ
ec2_key = 'AKIAJRKCWXWGJQ4BVWKA'

# EC2 secret. http://bit.ly/j5ImEZ
ec2_secret = '58+24V3kyotvuGYLBaexMOJYYeGh+gMpuDPfpBB8'

#EC2 region. http://amzn.to/12jBkm7
ec2_region = 'us-east-1'

# AMI name. http://bit.ly/liLKxj
ec2_amis = ['ami-1335f37a']

# Name of the keypair you use in EC2. http://bit.ly/ldw0HZ
ec2_keypair = 'key'

# Name of the security group. http://bit.ly/kl0Jyn
ec2_secgroups = ['default']

# API Name of instance type. http://bit.ly/mkWvpn
ec2_instancetype = 't1.micro'
