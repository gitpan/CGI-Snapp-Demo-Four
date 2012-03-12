#!/usr/bin/env perl

use CGI::Snapp::Demo::Four::Wrapper;

# ----------------------------

my($doc_root)    = $ENV{DOC_ROOT} || '/dev/shm/html';
my($config_dir)  = "$doc_root/assets/config/cgi/snapp/demo/four";
my($config_file) = "$config_dir/config.logger.conf";

CGI::Snapp::Demo::Four::Wrapper -> new(config_file => $config_file, maxlevel => 'debug') -> run;
