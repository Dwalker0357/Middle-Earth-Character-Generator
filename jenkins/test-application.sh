# install pip3, pytest and flask-testing
sudo update -y
sudo upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip


# cd into the service-1 directory install requirments and run pytest
cd ./service-1
pip3 install -r requirements.txt
python3 -m pytest --cov application
cd ..



# cd into the service-2 directory and run pytest
cd ./service-2
python3 -m pytest --cov application
cd ..



# cd into the service-3 directory and run pytest
cd ./service-3
python3 -m pytest --cov application
cd ..



# cd into the service-4 directory and run pytest
cd ./service-4
python3 -m pytest --cov application
cd ..



# cd into the service-5 directory and run pytest
cd ./service-5
python3 -m pytest --cov application
cd ..