from fabric.api import task, run
from fabric.contrib.files import comment

from fabtools.require import deb


@task
def provision():
    mongodb()


def mongodb(version='2.6.4'):
    deb.key('7F0CEB10', keyserver='keyserver.ubuntu.com')
    deb.source('mongodb', 'http://downloads-distro.mongodb.org/repo/ubuntu-upstart', 'dist', '10gen')
    deb.package('mongodb-org', version=version, update=False)

    comment("/etc/mongod.conf", "^bind_ip.*", char='#', use_sudo=True)
    run('sudo service mongod restart')
