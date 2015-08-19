<?php if (!defined('APPLICATION')) exit();
$Configuration['Database']['Host'] = '{{ db.host() }}';
$Configuration['Database']['Name'] = '{{ db.database() }}';
$Configuration['Database']['User'] = '{{ db.user() }}';
$Configuration['Database']['Password'] = '{{ db.password() }}';
?>
