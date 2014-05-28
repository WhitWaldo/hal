#!/bin/bash
kill()
{
    printf "Killing the uwsgi service\n"
    sudo killall uwsgi
}

start()
{
    printf "Starting the uwsgi service\n"
    sudo service uwsgi start
}

restart()
{
    kill
    printf "Restarting nginx\n"
    sudo service nginx restart
    start
}

deploy()
{
    printf "Pulling in new changes from hal\n"
    sudo git pull
    printf "Pulling in new changes from hal_private\n"
    cd /home/dan/hal_private & sudo git pull
    printf "Installing/updating dependencies\n"
    sudo pip install -r dependencies/requirements.txt
    printf "Compiling SASS and JST Templates\n"
    sudo grunt build
    restart
}

help()
{
    printf "The following options are available:\n  deploy -d\n  restart -r\n  kill -k\n  start -s\n"
}

if [[ "$*" == "" ]]
then
    printf "NO ARGUMENTS PROVIDED\n"
    help
    exit 1
fi

case "$1"
in
    -h) help;;
    -k) kill;;
    -s) start;;
    -r) restart;;
    -d) deploy;;
     *)
         echo $"$1 is not a recognized argument."
         printf "\n"
         help
         exit 1
esac
