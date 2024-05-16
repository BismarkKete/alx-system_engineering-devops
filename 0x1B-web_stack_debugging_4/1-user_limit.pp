# Allowing the user: holberton to log in and handle files without error
# Author: Bismark-K

# increasing limit for holberton
exec { 'increase-hard-limit':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# increasing soft limit
exec { 'increase-soft-limit':
  command => "sed -i '/^holberton soft/s/5/50000/' /etc/security/limits.conf
",
  path    => '/usr/local/bin/:/bin/',
}

