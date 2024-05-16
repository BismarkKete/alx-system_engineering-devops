# Increasing the number of traffics our nginx server can handle
# Author: Bismark-K

# Increase default file
exec { 'fix--for-nginx':
  # changing the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # path specifier
  path    => '/usr/local/bin/:/bin/',
}

# restarting nginx
exec { 'nginx-restart':
  # restart nginx
  command => '/etc/init.d/nginx restart',
  # path specifier
  path    => '/etc/init.d/',
}

