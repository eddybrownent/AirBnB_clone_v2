# Define the Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure /data directory exists with the right permissions
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  require => Package['nginx'],
}

# Ensure /data/web_static directory structure exists
exec { 'create_web_static_dirs':
  command => 'sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
  creates => ['/data/web_static/releases/test/', '/data/web_static/shared/'],
  path    => ['/bin', '/usr/bin'],
  require => File['/data'],
}

# Create an HTML file in /data/web_static/releases/test
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\nThis is a test Holberton School\n</body>\n</html>\n",
  require => Exec['create_web_static_dirs'],
}

# Create or recreate a symbolic link
exec { 'create_web_static_link':
  command => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  creates => '/data/web_static/current',
  path    => ['/bin', '/usr/bin'],
  require => File['/data/web_static/releases/test/index.html'],
}

# Update the Nginx configuration
file_line { 'nginx_hbnb_static':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => '        location /hbnb_static/ { alias /data/web_static/current/; }',
  require => Service['nginx'],
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['nginx_hbnb_static'],
}
