from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from ..mongo import get_mongo_client



def get_collections():
    db = get_mongo_client()
    buyers_collection = db['buyers']
    sellers_collection = db['sellers']

    return buyers_collection, sellers_collection


__all__ = ['make_password', 'check_password', 'Response', 'status', 'get_collections']
