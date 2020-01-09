import os 

class Config(object):
    SECRECT_KEY = os.environ.get('SECRECT_KEY') or b'7\xeb\xe3\x18\xf7W\x8dQ\xaf3<$\x88F?k'

    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}