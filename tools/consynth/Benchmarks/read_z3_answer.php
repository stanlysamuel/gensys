<?php

// The script expects one argument, the file to read from:
// - 1st line: ignore 'sat' or exit(-1) for 'unsat'
// - next, foreach '(define-fun xxx () Int yyy)', print 'name2value(xxx, yyy).'
include 'sexp.php';

$in = @fopen($argv[1], "r"); // Open file for read.

if ($in) {
   $buffer = fgets($in, 4096); // Read a line
   if ($buffer == "unsat\n") exit(-1);
   if ($buffer != "sat\n") { echo "weird1"; exit(-1); }
   $contents = fread($in, filesize($argv[1]));
   $sexp = new DrSlump\Sexp();
   $arr = $sexp->parse($contents);
   array_shift($arr);
   echo ":- multifile name2value/2.\n:- dynamic name2value/2.\n";
   foreach ($arr as $fun) {
     if (count($fun) <= 4) { echo "weird2"; exit(-1); }
     if ($fun[0] == "define-fun") {
        $val = is_array($fun[4]) ? implode('', $fun[4]) : $fun[4];
	echo "name2value($fun[1], $val).\n";
     } else { echo "weird3"; exit(-1); }
   } 
   fclose($in); // Close the file.
}