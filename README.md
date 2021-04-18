![](/service-1/application/static/pics/Title.png)


Trello:
https://trello.com/b/iq9xkiwX/lord-of-the-rings-character-generator
<br>

Middle Earth Character Generator was designed and created for my second SFIA project with QA-academy, it utilizes a collection of five micro-services that are containerized and deployed via docker-swarm stack and Jenkins CI pipeline.

The five micro-services are written in python and utilise python flask API to communicate and exchange information between each other,
the first service is the front end python flask to html jinja2 template that imports all the necessary information to be displayed on the page.

The second, third and fourth micro-service generates random objects from a predefined list at random. the five and final micro-service uses predefined rules via if statements to change the values and modify the imported objects from services 1-4 then posts the results back to service 1.


<h1>The initial goals of the project were the following:</h1>

• Create a front-end service that displays all the imported data in a clean readable manner. 
<br>
• Generate random objects for Race, Stature, Location, Rank and Profession.
<br>
• Generate random objects for Grade, Weapon, Stance, Trait_1, Trait_2 and Trait_3.
<br>
• Generate random objects for Melee_Prowess, Archery_Prowess, Strength, Endurance, Intelligence, Awareness, Dexterity and Dodge.   
<br>
• The ability to reassign the attributes generated in service 4 among other objects using if statements based on class e.g. Wizards are given more Intelligence and less Strength.  
<br>
• The ability to create, display, update and delete (CRUD) character entries using the external mysql database 
<br>
• Achieve 80% test coverage or above in each and every individual service along with a variety and range of tests.
<br>
• Deploy my micro-service with continuous integration via Jenkins Pipeline and github Webhooks.  
<br>

![](/service-1/application/static/pics/Trello.png)

<br>

<h2> MYSQL Database / DB.model For Storing character entries <h2>

![](/service-1/application/static/pics/model.png)


__**<h1>POST And GET API Requests</h1>**__

<br>

The API requests from the front-end service to retrieve the necessary objects from the other services:
![](/service-1/application/static/pics/service-2-get-request.png) 
![](/service-1/application/static/pics/service-3-get-request.png)
![](/service-1/application/static/pics/service-5-get-request.png)

__**<h1>Risk Assessment</h1>**__

<br>

![](/service-1/application/static/pics/risk_assessment.jpeg) 

__**<h1>Challenges faced and project evolution</h1>**__

<br>
My first challenge was implementing post request API's to transfer generated objects around my services and getting them to relay back to my front-end, I solved this by importing non-modified variables directly into my front end and by using a post request from service 1 combined with a get request from service 2 and 4 to retrieve all the information I needed to modify.   
<br>
<br>
My second challenge was getting my containerised MYSQL database working with my front-end service whilst in a swarm-stack, after troubleshooting many possible solutions I decided the best use of my limited time was to make an external MYSQL database and connect it to my services.
<br>
<br>
My third and final challenge was getting the jenkins user to execute all the required commands in my scripts because of the lack of sudo permissions, I solved this problem by editing a config file as root and adding the line jenkins ALL= NOPASSWD: ALL which allows jenkins to utilise sudo commands without issue.
<br>
<br>
Due to unforeseen complications with the development and deployment of the Jenkins pipeline I was sadly unable to implement CRUD into my micro-services therefore the data generated is only stored in the external MYSQL database.

<br>
<br>

__**<h1>Completed Services:</h1>**__

![](/service-1/application/static/pics/Html_page.png)

<br>
<br>
<h1>Pytest Service Coverage Reports:</h1>
<br>

Service 1 

![](/service-1/application/static/pics/service-1-test.png)

Service 2 

![](/service-1/application/static/pics/service-2-test.png)

Service 3 

![](/service-1/application/static/pics/service-3-test.png)

Service 4 

![](/service-1/application/static/pics/service-4-test.png)

Service 5 

![](/service-1/application/static/pics/service-5-test.png)


<h1>Test Analysis</h1>

Service-1:

Mock POST and GET data request example:
<br>
<br>

![](/service-1/application/static/pics/service-1-test-example.png)

 

<br>
Service-2:

Mock GET data request example with high range coverage:
<br>
<br>

![](/service-1/application/static/pics/service-2-test-example.png)


<br>
Service-3:

Mock GET data request example with high range coverage:
<br>
<br>

![](/service-1/application/static/pics/service-3-test-example.png)

<br>
Service-4:

Mock GET data request example with high range coverage:
<br>
<br>

![](/service-1/application/static/pics/service-4-test-example.png)

<br>
Service-5:

Mock POST and GET data request example with high range coverage:
<br>
<br>

![](/service-1/application/static/pics/service-5-test-example.png)

<br>

Overall I achieved 96%, 100%, 100%, 100% and 100% test coverage while testing all the services functionality with a high range of mock data, the only function I did not test was the form data input, the other improvement would be to find a way to test my service-5 with a iteration loop or similar method because to achieve 100% coverage I had to write 1300 lines of test code.  

<br>
<br>

<h1>Continuous Integration With Jenkins PipeLine</h1>
<br>
<h3>Deployment Diagram:<h3> 
<br>

![](/service-1/application/static/pics/CI.jpeg)

<br>
<h3>Jenkins Pytest Deployment:<h3>

<br>

![](/service-1/application/static/pics/jenkins-pytest.png)

<br>

<h3>Jenkins Ansible Deployment:<h3>

<br>

![](/service-1/application/static/pics/jenkins-ansible.png)

<br>

<h3>Jenkins Swarm Deployment:<h3>

<br>

![](/service-1/application/static/pics/jenkins-swarm.png)

<br>

<h3>Jenkins Nginx Deployment:<h3>

<br>

![](/service-1/application/static/pics/jenkins-Nginx.png)

<br>

<h3>Jenkins Git WebHooks:<h3>

<br>

![](/service-1/application/static/pics/webhook.png)

<br>

<h3>Jenkins Complete CI Pipeline:<h3>

<br>

![](/service-1/application/static/pics/jenkins-pipeline.png)

<br>


<h1> Future Improvements </h1>

• Read, Update And Delete Functionality
<br>
• Containerised MYSQL Database
<br>
• Better Front-End layout and input form
<br>
• More efficient testing methods
<br>
• Form authentication rules to stop duplicate database entries
<br>
• Expanded list of possible randomly generated objects 
<br>
• Generation of secondary weapon 
<br>
• Generation of jenkins artifacts
<br>
• Use of environmental variables to hide sensitive information like MYSQL instance log in details 
<br>
• Tagged docker images so I can perform a rollback
<br> 
• Better source code management
<br>

<br>

<h1> Conclusion </h1>
In conclusion I think this project went really well with only medium to minor issues encounter along the way, my knowledge of docker and all its modules have expanded massively and it is now my favorite deployment method, Ansible can have some major issues with its syntax and caused me a little trouble but overall its a very useful piece of configuration software to have learned.  

<br>
<br>

Jenkins on the other hand, well its a brilliant and revolutionary piece of automation software when you manage to get it working, but getting there is another issue, compared to my peers I had less issues with it since I found a way to bypass jenkins sudo permissions early on but it still has a high learning curve and am I yet to utilize its full capabilities. 



