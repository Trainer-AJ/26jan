## Level-1
```bash
docker run hello-world
# get the code
git clone https://github.com/Trainer-AJ/26jan.git 

cd 26jan

# create / build docker image
docker build -t my-first-docker-image:latest .

# list all image
docker images

# run docker container 
docker run my-first-docker-image:latest

```

## Level-2

```sh
git pull

# get code
cd nginx

# create new image
docker build -t simple-img:latest .

# run container
docker run -p 80:80 simple-img:latest
```

1. **Now click on open port option**
2. **type 80**
3. **click ok**
4. `A web page should be visible now`
