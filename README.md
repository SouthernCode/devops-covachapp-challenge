# Southern Code Devops challenge 
## _We need to deploy our Covachapp!_

--------

Covachapp is a web app that allows users to publish housing options for rental, and other users to find those properties.
As of now it's on early development stages and we need someone to help us deploy it in a staging server...
We sorta know how to use Docker and Docker Compose (barelly) but we need help moving all the services and servers to Kubernetes!!
Currently we have one Frontend app and three services (Users, Products and Search), we need a way to glue them together!
We also need a lot of help with observability and secret environment variables! You can see we are n00bs in these regards :D

# Current architechture
- Frontend (Next.js)
- Auth service (Django)
    - Auth db (Postgresql)
- Products service (Fastapi) (Publishes messages to Rabbitmq)
    - Products db (Postgresql)
- Search service (golang Mux)
    - Search db (Mongodb)
    - Search consumer (Consumes messages from Rabbitmq)
- RabbitMQ

# Check the link bellow for a graphic schema
# [Excalidraw schema](https://excalidraw.com/#json=SuEz9hJp7PNMQqwuBYgW8,iGzIvhocOKmqSN3-EyAIXw)

## Notes

- Make sure the solution is private, not public. Only available for you and us. (OBVIOUSLY, WE KNOW :D)
- We have created some sample users. You can see the usernames and passwords inside the data/users.json file
- Be ready to clearly explain why you’re doing things a certain way.
- Feel free to add more features! Really, we’re curious about what you can think of. We’d expect the same if you worked with us.
- The 'product' and 'search' services are synched via RabbitMQ, we are using a free cloudamqp account [https://www.cloudamqp.com/]

## Tasks

- Create an account in Cloudampq or deploy a managed version of RabbitMQ
- Deploy the site with Kubernetes! (locally or in the cloud)
- Implement a web server (Nginx or similar) for the frontend
- As of now, the frontend needs to know the urls of each service, suggest and implement a better way!

## Bonus points

-  Creating a CI pipeline, using a tool of your choice, that deploys the web server to a cloud environment of your choice. (A free account for Microsoft Azure, AWS (Amazon Web Services)
- Set up static code analysis tool as a part of the pipeline to use as quality gate (SonarQube, etc)
- Suggest any solution to improve monitoring / alerting.
- Documentation and maintainability is a plus. (Providing a PNG diagram, mermaid diagram, anything better?)
- Use a configuration management tool (such as Terraform or Ansible) to bootstrap the server.
- Load balancing? Suggestions?
- Think security: Avoid exposing secrets in any way (Tip: use .env file for the composeing, and .gitignore it.
- We have added a postman collection with some basic tests. Add them to the pipeline using newman!
- The 'Auth' service has tests, you can run them by calling the "python manage.py test" command. Add them to the pipeline!
- We want to split this into different repositories, suggest as with a way of working in distributed repos, and local development without having to deploy every single service!
