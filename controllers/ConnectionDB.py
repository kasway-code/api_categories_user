import xmlrpc
import os
from dotenv import load_dotenv, find_dotenv
import ssl
load_dotenv(find_dotenv())

def ConnectionDB():

    host        = os.environ.get('host')
    db          = os.environ.get('db')
    username    = os.environ.get('username')
    password    = os.environ.get('password')
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(host), allow_none=True, verbose=False, use_datetime=True,context=ssl._create_unverified_context())
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(host), verbose=False, use_datetime=True,context=ssl._create_unverified_context())
    uid = common.authenticate(db, username, password, {})
    return models,db,uid,password


    