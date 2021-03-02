#!/bin/bash
ssh 10.154.0.9 << EOF 

sudo rm LOTR_Character_Generator -rf


git clone https://github.com/Dwalker0357/LOTR_Character_Generator


cd LOTR_Character_Generator
 
 
cd nginx


sudo docker-compose down --rmi local


sudo docker-compose up -d
EOF