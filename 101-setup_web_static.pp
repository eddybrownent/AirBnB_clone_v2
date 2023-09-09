# 101-setup_web_static.pp

# Install nginx if not installed
package { 'nginx':
  ensure => installed,
}

# Create directories if they don't exist
file { '/data/web_static/releases/test/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create an HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\nThis is a test Holberton School\n</body>\n</html>\n",
}

# Create or recreate a symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update nginx configuration
file_line { 'nginx_hbnb_static':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => '        location /hbnb_static/ { alias /data/web_static/current/; }',
  before => Service['nginx'],
}

# Restart nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['nginx_hbnb_static'],
}
