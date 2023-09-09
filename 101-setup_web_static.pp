# Install Nginx if not already installed
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
file { ['/data/web_static', '/data/web_static/releases', '/data/web_static/shared']:
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  require => File['/data'],
}

# Create an HTML file in /data/web_static/releases/test
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
  content => "<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\nThis is a test Holberton School\n</body>\n</html>\n",
  require => File['/data/web_static/releases/test'],
}

# Ensure /data/web_static/current symbolic link exists and is up to date
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test/',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test/index.html'],
  before  => Service['nginx'],
}

# Give ownership of the /data/ folder to the ubuntu user and group recursively
exec { 'change_ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin'],
  onlyif  => "test \$(stat -c %U /data) != 'ubuntu'",
}

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file_line { 'nginx_hbnb_static':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => '        location /hbnb_static/ { alias /data/web_static/current/; }',
  require => Service['nginx'],
}

# Restart Nginx to apply the updated configuration
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['nginx_hbnb_static'],
}

