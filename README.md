# Machine_learning_project

This is a end to end project developed by Adarsh Singh

There are some pre requisite that should be there to develope a full fleged machine learning project.

### Software and Account Requirements.

1.[GitHub Account](https://github.com)

2.[Heroku Account](https://dashboard.heroku.com/login)

3.[VS code ide](https://code.visualstudio.com/download)

4.[GIT cli](https://git-scm.com/downloads)
...

creating conda environment
...

conda create -p venv python==3.7 -y
...

conda activate venv/

OR 

conda activate venv
....

pip install -r requriements.txt 
...

To add files to git
...

git add .

OR

git add <file_name>
...

To ignore file or folder from git we can use name of file and folder to the .gitignore file.
...

git status
...

To check all version maintained by git 
...

git log
...

To create version/commit all the changes by git
...

git commit -m "message"
...

to send version/changes to github
...

git push origin main
...

to check remote url
...

git remote -v
...

To setup CI/CD pipeline in heroku we need 3 information 

1. HEROKU_EMAIL - adarshriit2017@gmail.com
2. HEROKU_API_KEY - <>
3. HEROKU_APP_NAME - ml-projects-1

BUILD DOCKER IMAGE
...

docker build -t <image_name>:<tagname> .
...

>Note: Image name for docker must be lowercase

To list docker image 
...

docker images
...

Run docker image
...

docker run -p 5000:5000 -e PORT = 5000 51c573c4df7e
...

To check running containers in docker
...

docker ps
...

To stop docker container 
...

docker stop <container_id>
...


...

python setup.py install
...

