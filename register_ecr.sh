#!/bin/bash

# AWS credential 세팅
# aws configure

# ECR 로그인
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 558826674374.dkr.ecr.ap-northeast-2.amazonaws.com

# 새로운 태그 생성 (현재 날짜와 시간을 이용)
tag="v$(date +'%Y%m%d%H%M%S')"

# 새로운 이미지 빌드
docker build -t learn-fastapi .

# 새로운 이미지 태그 부여
docker tag learn-fastapi:latest 558826674374.dkr.ecr.ap-northeast-2.amazonaws.com/learn-fastapi:$tag

# 새로운 이미지 푸시
docker push 558826674374.dkr.ecr.ap-northeast-2.amazonaws.com/learn-fastapi:$tag
