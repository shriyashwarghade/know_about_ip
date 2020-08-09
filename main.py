"""
Check If IPv4 address is valid or not. If Valid Return IP Information Using Threatminer API.
Threatminer documentation - https://www.threatminer.org/api.php.
"""

import ipaddress
import json
from datetime import datetime, timedelta

import requests
from flask import Flask, render_template, request

from elasticsearch_operations import get_object, set_object, delete_object

# API To Get IP Info
URL = "https://api.threatminer.org/v2/host.php?q={}&rt=1"

# Error Messages
ENTER_IP_ADDRESS = "Enter IP Address"
DETAILS_NOT_FOUND = "OOPS!! IP Address Details Not Found."
ERROR_IN_GETTING_INFO = "OOPS!! Error In Getting Info."
ONLY_IP_V4_ALLOWED = "Only IPV4 Address Is Allowed"
INVALID_IP = "{} does not appear to be an IPv4 address"

app = Flask(__name__, static_url_path="/static", static_folder="static")


@app.route("/", methods=['GET', 'POST'])
def index():
    """
    :return: Template
    """
    if request.method == 'GET':
        return render_template('search_ip.html')
    elif request.method == 'POST':
        try:
            ip_address = ipaddress.ip_address(request.form.get('ip'))
            if ip_address.version == 4:
                data_from_elasticsearch = get_object(request.form.get('ip'))
                if data_from_elasticsearch:
                    if datetime.strptime(
                            data_from_elasticsearch['_source']['inserted_on'],
                            "%Y-%m-%dT%H:%M:%S.%f") > (datetime.now() - timedelta(hours=48)):
                        return render_template('info_display.html',
                                               data=data_from_elasticsearch['_source'])
                    delete_object(request.form.get('ip'))
                response = requests.get(URL.format(ip_address))
                if response.status_code == 200:
                    response_body = json.loads(response.text)
                    if response_body.get('status_code') == "404":
                        return render_template('search_ip.html', message=DETAILS_NOT_FOUND)
                    data = {
                        'ip_address': request.form.get('ip'),
                        'ip_address_type': f'IPV{ip_address.version}',
                        'results': response_body.get("results"),
                        'inserted_on': datetime.now(),
                    }
                    set_object(request.form.get('ip'), data)
                    data.update({'inserted_on': str(data['inserted_on'])})
                    return render_template('info_display.html', data=data)
                message = ERROR_IN_GETTING_INFO
            else:
                message = ONLY_IP_V4_ALLOWED
        except ValueError:
            message = INVALID_IP.format(request.form.get('ip'))
        except Exception as exception:
            message = exception
        return render_template('search_ip.html', message=message)
    else:
        return render_template('search_ip.html')


if __name__ == "__main__":
    app.run()
