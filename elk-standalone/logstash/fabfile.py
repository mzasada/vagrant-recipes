from fabric.operations import run, sudo
from fabtools import require


def install_logstash(version='1.4.2-1-efd53ef_all'):
    require.deb.package('openjdk-7-jre-headless', update=True)
    run('wget https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash-contrib_%s.deb' % version)
    sudo('dpkg -i logstash-contrib_%s.deb' % version)

    # run('logstash agent -f logstash.conf')