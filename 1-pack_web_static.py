from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        time = datetime.now()
        str_time = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_name = "versions/web_static_{}.tgz".format(str_time)
        execute = local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
