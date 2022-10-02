use IO::Socket;

$| = 1;

print "Enter Target/hostname : ";

chop ($target = <stdin>);
print "Start Port : ";
chop ($start_port = <stdin>);
&check_port($start_port);
print "End Port : ";
chop ($end_port = <stdin>);
&check_port($end_port);

foreach ($port = $start_port ; $port <= $end_port ; $port++) 
{

	print "\rScanning port $port";
	

	$socket = IO::Socket::INET->new(PeerAddr => $target , PeerPort => $port , Proto => 'tcp' , Timeout => 1);
	

	if( $socket )
	{
		print "\r = Port $port is open.\n" ;
	}
	else
	{
		
	}
}

print "\n\nFinished Scanning $target\n";

exit (0);

sub check_port {
    my $port = shift;

    if ($port =~ /\D+/ or $port >65535  or $port < 20) {
        print "Please check the format of port: $port\n";
        exit 1;
  }
}
