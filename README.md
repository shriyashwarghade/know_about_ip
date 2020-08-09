# Know About IP

  1. Web frontend in Python using jinja templating which presents user with an input form and accepts IPv4 address. 
  2. The given IPv4 address is checked in backend if it is valid or not. If it is not correct, error message is displayed to the user. 
  3. If the IPv4 address is correct, IP information is fetched using API - "https://api.threatminer.org/v2/host.php?q=<PLACE_IP_ADDRESS_HERE>&rt=1". Threatminer documentation - https://www.threatminer.org/api.php.
  4. Result is display in tabular format. If there is no result for given IP, appropriate message is displayed to the user.
  5. Every time a user enters the IP address, it is looked in Elasticsearch for pre-existing result for that IP. If the result exists in Elasticsearch and is not more than 48 hours old, than that result is displayed to user immediately else information is fetched from Threatminer API, result is displayed to user and stored in elasticsearch.
    

# Steps To Run

1. Install Python 3

    For Windows: https://phoenixnap.com/kb/how-to-install-python-3-windows
    
    For Ubuntu: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
    
    For Mac: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos
    
2. Create Virtual Environment
    
    For Windows: https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/
    
    For Ubuntu: https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/
    
    For Mac: https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux
    
3. Install Required Packages
    
    pip install flask
    
    pip install elasticsearch
    
4. Update Elasticsearch Details
    
    
    Open elasticsearch_operations.py and update IP, PORT
    
    Check if index "ip_address_info" is created in elasticsearch engine else create one.
    

5. Command To Run Project
    
    python main.py
    
# Technology Stack

1. Python
2. Bootstrap
3. Jinja Templating
4. Elasticsearch

# Pylint Score

    1. main.py: Code has been rated at 9.55/10
    2. elasticsearch_operations.py: Code has been rated at 9.60/10 
