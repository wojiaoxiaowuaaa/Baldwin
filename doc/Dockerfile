################################################
#
################################################
#
#生成SSH服务的ubuntu镜像
#安装python运行环境
#
################################################

#基于哪个镜像生成新的镜像
FROM ubuntu:20.04

#作者名
MAINTAINER haibin253

#设置环境变量
ENV TZ Asia/Shanghai
ENV LANG zh_CN.UTF-8

#执行命令
#替换为阿里源
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.aliyun.com/#' /etc/apt/sources.list \
    && sed -i 's#http://security.ubuntu.com/#http://mirrors.aliyun.com/#' /etc/apt/sources.list

#更新软件源并安装软件
RUN apt-get update -y \
    && apt-get -y install iputils-ping \
    && apt-get -y install wget \
    && apt-get -y install net-tools \
    && apt-get -y install vim \
    && apt-get -y install openssh-server \
    && apt-get -y install python3.9 \
    && apt-get -y install python3-pip python3-dev \
    && cd /usr/local/bin \
    && rm -f python \
    && rm -f python3 \
    && rm -f pip \
    && rm -f pip3 \
    && ln -s /usr/bin/python3.9 python \
    && ln -s /usr/bin/python3.9 python3 \
    && ln -s /usr/bin/pip3 pip \
    && ln -s /usr/bin/pip3 pip3 \
    && python -m pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

#设置密码
RUN echo 'root:root' |chpasswd

#允许root用户登入
RUN sed -ri 's/^#PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

#创建sshd目录
RUN mkdir /var/run/sshd

# 声明端口
EXPOSE 22

#开始ssh服务
CMD ["/usr/sbin/sshd", "-D"]
