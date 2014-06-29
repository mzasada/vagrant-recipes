from fabric.api import task
from fabric.operations import sudo, run, put

from fabtools import require
from fabtools.vagrant import vagrant

@task
def provision():
    elasticsearch()
    kibana()
    # logstash()


def elasticsearch(version='1.2.1'):
    require.deb.package('openjdk-7-jre-headless', update=True)

    run('wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-%s.deb' % version)
    sudo('dpkg -i elasticsearch-%s.deb' % version)
    sudo('service elasticsearch start')
    sudo('update-rc.d elasticsearch defaults 95 10')

    sudo('/usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head')


@task
def kibana(version='3.1.0'):
    install_nginx()
    install_kibana(version)

    sudo('service nginx restart')


def install_nginx():
    require.deb.package('nginx', update=True)
    sudo('cp ~/fabric/templates/nginx.conf /etc/nginx/sites-available/default')


def install_kibana(version):
    run('wget https://download.elasticsearch.org/kibana/kibana/kibana-%s.tar.gz' % version)
    run('tar -xf kibana-%s.tar.gz' % version)
    sudo('mkdir -p /var/www/kibana')
    sudo('cp -R ~/kibana-%s/* /var/www/kibana/' % version)
    sudo('cp ~/fabric/templates/config.js /var/www/kibana/config.js')


def logstash(version='1.4.2-1-efd53ef_all'):
    require.deb.package('openjdk-7-jre-headless', update=True)
    run('wget https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash-contrib_%s.deb' % version)
    sudo('dpkg -i logstash-contrib_%s.deb' % version)

    # run('logstash agent -f logstash.conf')