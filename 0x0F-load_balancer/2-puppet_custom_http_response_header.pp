# seting up new nginx ubuntu server and adding a custom HTTP header
# Author: Bismark-K

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://youtube.com permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'HTTP header':
	command => 'sed -i "/listen 80 default_server;/a add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
