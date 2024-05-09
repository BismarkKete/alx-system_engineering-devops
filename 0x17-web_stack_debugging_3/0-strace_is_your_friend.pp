# Finding out why Apache is returing a 500 error and fixing it
# Author: Bismark-K

exec { 'fix wordpress site':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path    => '/usr/local/bin/:/bin/',
	provide => shell
}
