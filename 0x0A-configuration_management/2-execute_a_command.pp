# puppet file to execute a commnad.
exec { 'pkill':
  path     => '/usr/bin, /sbin, /bin, /user/sbin',
  command  => 'pkill -f killmenow',
  provider => 'shell',
}