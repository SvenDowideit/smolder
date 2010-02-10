#!perl

use CGI::Application::Emulate::PSGI;
use Plack::Builder; 
use Plack::Loader;
use Smolder::Conf qw(Port HostName LogFile HtdocsDir DataDir PidFile);
use Smolder::Dispatch;

# Pieces from Smolder::Server which still need handling: 
#  - auto-upgrade logic
#  - STDERR/logging

# Some amount of Apache config would be still be necessary
# to have to have the make "/" correspond to the root, and 
# to send traffic below that to this dispatcher. 

Plack::Loader->auto->run(
    builder {
        mount '/'    => CGI::Application::Emulate::PSGI->handler(sub { Smolder::Redirect->new->run });
        mount '/app' => builder {
            enable "Plack::Middleware::Static",
                path => qr{^/(images/|style/|js/|robots.txt)}, root => HtdocsDir;
            CGI::Application::Emulate::PSGI->handler(sub { Smolder::Dispatch->dispatch });
        }
    };

);
