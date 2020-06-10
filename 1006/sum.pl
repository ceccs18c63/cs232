print "Enter two numbers \n" ;
$firstnumber = <STDIN> ;
$secondnumber = <STDIN> ;
$result = add($firstnumber, $secondnumber) ;
print "Result is $result \n" ;

sub add
{
    ($a,$b) = @_ ;
    $result = $a + $b ;
    return $result ;
}
