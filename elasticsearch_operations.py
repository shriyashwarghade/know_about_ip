"""
Basic Elasticsearch Operations
"""
from elasticsearch import Elasticsearch

# CONSTANTS
IP = "localhost"
PORT = "9200"
INDEX = "ip_address_info"

try:
    es_obj = Elasticsearch([{"host": IP, "port": int(PORT)}])
except:
    raise Exception("Error In Connection To ElasticSearch Engine.")


def get_object(ip_address):
    """
    :param ip_address: IP Address
    :return: Document if document is available in ElasticSearch Engine Else False
    """
    try:
        return es_obj.get(index=INDEX, id=ip_address)
    except ConnectionError:
        raise Exception("Error In Connection.")
    except:
        return False


def set_object(ip_address, data):
    """
    :param ip_address:IP Address
    :param data: Document Which is to be stored in  ElasticSearch Engine
    :return: None
    """
    try:
        es_obj.index(index=INDEX, id=ip_address, body=data)
    except ConnectionError:
        raise Exception("Error In Connection.")


def delete_object(ip_address):
    """
    :param ip_address:IP Address
    :return: None
    """
    try:
        es_obj.delete(index=INDEX, id=ip_address)
    except ConnectionError:
        raise Exception("Error In Connection.")
