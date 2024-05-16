# Handles user limit allowing holberton to log in and open files without error
# Author: Bismark-K

exec {'change-soft-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['change-hard-limit'],
}

exec {'change-hard-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}

