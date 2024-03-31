# aws credential 세팅 
# aws configure

# 로그인 
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 558826674374.dkr.ecr.ap-northeast-2.amazonaws.com

# make image
docker build -t learn-fastapi .
# image tagging
docker tag learn-fastapi:latest 558826674374.dkr.ecr.ap-northeast-2.amazonaws.com/learn-fastapi:latest
# image push
docker push 558826674374.dkr.ecr.ap-northeast-2.amazonaws.com/learn-fastapi:latest