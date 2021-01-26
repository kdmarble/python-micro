# MicroShop
MicroShop is a platform to gauge interest in products. Admins can create, edit, and delete products in the admin dashboard. Users can view all listed products, and "Like" them to show their interest. [Check out the Frontend Repo](https://github.com/kdmarble/python-micro-frontend)

# Demo
![MicroShop Demo](Postman.gif)

# Tech Stack
MicroShop backend was build with Python using a microservice architecture. The admin backend is build using Django, and the public backend is build using Flask. Both backends communicate via AMQP producer/consumer messaging queue system, utilizing CloudAMQP. A MySQL instance is utilized for the datastore. Both microservices utilize Docker to build a container with the backend api, queue, and database images necessary to communicate together. 
