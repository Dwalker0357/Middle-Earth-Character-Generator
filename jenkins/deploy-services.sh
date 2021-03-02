#! /bin/bash
ssh 10.154.0.12 << EOF 

sudo rm -rf LOTR_Character_Generator

  
git clone https://github.com/Dwalker0357/LOTR_Character_Generator


cd LOTR_Character_Generator


sudo docker login
 
 
sudo docker stack deploy --compose-file docker-compose.yaml lotr
EOF