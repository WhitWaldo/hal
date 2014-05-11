sudo git pull
cd ~/hal_private & git pull
sudo pip install -r dependencies/requirements.txt
grunt build
sudo killall uwsgi 
sudo service uwsgi start
sudo service nginx restart
