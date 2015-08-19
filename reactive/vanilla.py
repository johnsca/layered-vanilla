import pwd
import os
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.templating import render
from charms.reactive import when, when_not
from charms.reactive import set_state, remove_state


@when('apache.available', 'database.available')
def setup_vanilla(mysql):
    render(source='vanilla_config.php',
           target='/var/www/vanilla/conf/config.php',
           owner='www-data',
           perms=0o775,
           context={
               'db': mysql,
           })
    uid = pwd.getpwnam('www-data').pw_uid
    os.chown('/var/www/vanilla/cache', uid, -1)
    os.chown('/var/www/vanilla/uploads', uid, -1)
    set_state('apache.start')
    status_set('maintenance', 'Starting Apache')


@when('apache.available')
@when_not('database.connected')
def missing_mysql():
    remove_state('apache.start')
    status_set('blocked', 'Please add relation to MySQL')


@when('database.connected')
@when_not('database.available')
def waiting_mysql(mysql):
    remove_state('apache.start')
    status_set('waiting', 'Waiting for MySQL')


@when('apache.started')
def started():
    status_set('active', 'Ready')
