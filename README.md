# Scikit-Learn API in Docker

Before making the Docker container, we can first clone the git repository of this project to your local computer. 

```
git clone https://github.com/idoali/sklearn_api_in_docker.git
```

This `Dockerfile` needs to be run. We can run this file using Command Prompt by writing some command lines. But before we can execute this `Dockerfile` and build a Docker container, first we need to change our working directory. Change the working directory to where `Dockerfile` is located. After that we can run this command to build our container.

```
docker build -t sklearn-api .
```

Using this command, we are building an image container named `sklearn-api`. After this command is done executing, we need to execute this line below in order to run the image container.

 

```
docker run -t -i sklearn-api
```

After that we can go to [http://127.0.0.1/docs](http://127.0.0.1/docs) to interact with the API.
