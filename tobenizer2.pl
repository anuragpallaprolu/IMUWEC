#!/usr/bin/perl
$filename = $ARGV[0];
open FILE,"<$filename" or die "Sorry";

while($line = <FILE>){
	chomp;	
	if($line =~ m/gyrox =/)
		{
	@words = split(" ",$line);
		$gyrox = $words[2];
		open(GYROX, '>>gyrox.txt');
		print GYROX "$gyrox\n";
		
	}
	
	elsif($line =~ m/gyrox =/)
		{
	@words = split(" ",$line);
		$gyrox = $words[2];
		open(GYROX, '>>gyrox.txt');
		print GYROX "$gyrox\n";
		
	}
	
	elsif($line =~ m/gyrox =/)
		{
	@words = split(" ",$line);
		$gyrox = $words[2];
		open(GYROX, '>>gyrox.txt');
		print GYROX "$gyrox\n";
		
	}
	
	elsif($line =~ m/gyrox =/)
		{
	@words = split(" ",$line);
		$gyrox = $words[2];
		open(GYROX, '>>gyrox.txt');
		print GYROX "$gyrox\n";
		
	}
	
	
	
	
}
close (GYROX);
close (FILE);
