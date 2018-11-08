from obs.libs.s3 import login as login_lib
from obs.libs.utils import log_utils


def list_object(session=None, bucket=None):
    if not session:
        session = login_lib.get_client_session()

    list_object = session.list_objects(Bucket=bucket)
    
    try:
        return list_object.get('Contents')
    except Exception as e:
        log_utils.log_err(e)
        exit()


def get_object(session=None, bucket=None, key=None, gettype=None):
    """
    Get object function include several variable
    session = session from where it called from
    bucket = your bucket name
    key = your object file name
    gettype = your type of object result None|acl|tagging|torrent
    """
    if not session:
        session = login_lib.get_client_session()

    if type is None:
        detail_object = session.get_object(Bucket=bucket, Key=key)
    elif type == 'acl':
        detail_object = session.get_object_acl(Bucket=bucket, Key=key)
    elif type == 'tagging':
        detail_object = session.get_object_tagging(Bucket=bucket, Key=key)
    elif type == 'torrent':
        detail_object = session.get_object_torrent(Bucket=bucket, Key=key)

    return detail_object
