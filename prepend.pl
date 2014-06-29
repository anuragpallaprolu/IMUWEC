#!/usr/bin/perl
# prepend.pl - adds line number to beginning of every line in a file
use strict;
use warnings;

while (<>) {

if ($_ =~ /^$/)
  {

  }
  else
  {
    s/^/$. /;
    print;
 
  }

}
