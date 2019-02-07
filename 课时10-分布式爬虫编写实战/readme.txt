分布式爬虫
1、安装docker，启动docker
2、恢复镜像
docker load --input mycrawl.tar

3、启动镜像
4、启动mysql，设置用户
5、启动redis
6、创建子节点
docker run -it -d -name c1 --link center 3a54

7、部署爬虫代码到各个节点python mycrawl.py运行即可