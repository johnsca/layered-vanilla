from charmhelpers.core.templating import render
from charms.reactive import when
from charms.reactive import set_state


@when('apache.available', 'mysql.available')
def setup_vanilla(mysql):
    render(source='vanilla_config.php',
           target='/var/www/vanilla/conf/config.php',
           context={
               'db_host': mysql.host(),
               'db_database': mysql.database(),
               'db_user': mysql.user(),
               'db_password': mysql.password(),
           })
    set_state('apache.start')
