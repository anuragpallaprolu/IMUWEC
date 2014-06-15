#!/usr/bin/perl
use Switch;
$filename = $ARGV[0];
open FILE,"<$filename" or die "Sorry";

while($line = <FILE>){
	chomp;
	switch($line){
		case($line =~ m?gyrox =?){
			@words = split(" ",$line);
			$gyrox = $words[2];
			open(GYROX, '>>gyrox.txt');
			print GYROX "$gyrox\n";
		}
		case($line =~ m?gyroy =?){
			@words = split(" ",$line);
			$gyroy = $words[2];
			open(GYROY, '>>gyroy.txt');
			print GYROY "$gyroy\n";
		}
		case($line =~ m?gyroz =?){
			@words = split(" ",$line);
			$gyroz = $words[2];
			open(GYROZ, '>>gyroz.txt');
			print GYROZ "$gyroz\n";
		}
		case($line =~ m?temp =?){
			@words = split(" ",$line);
			$temp = $words[2];
			open(TEMP, '>>temp.txt');
			print TEMP "$temp\n";
		}
		case($line =~ m?accx =?){
			@words = split(" ",$line);
			$accx = $words[2];
			open(ACCX, '>>accx.txt');
			print ACCX "$accx\n";
		}
		case($line =~ m?accy =?){
			@words = split(" ",$line);
			$accy = $words[2];
			open(ACCY, '>>accy.txt');
			print ACCY "$accy\n";
		}
		case($line =~ m?accz =?){
			@words = split(" ",$line);
			$accz = $words[2];
			open(ACCZ, '>>accz.txt');
			print ACCZ "$accz\n";
		}
		
	}
}
close (GYROX);
close (GYROY);
close (GYROZ);close (TEMP);close (ACCX);close (ACCY);close (ACCZ);
close (FILE);
