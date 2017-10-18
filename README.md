
# 如何初始化本地开发环境
1. 配置数据库域名`127.0.0.1 db.dev.com`
1. 确保能以root:root访问本地数据库
1. 执行`python manage.py rebuild_db`安装数据库
1. 执行`behave -k --no-capture -t @full_init`初始化数据
1. 执行`python manage.py install`安装系统的初始化应用数据
1. 执行`start_service.bat`启动服务
1. 访问http://127.0.0.1:8004/console/，成功获取api console页面

## 如何集成到Ningx？ ##
1. 在hosts文件中添加如下域名
```
127.0.0.1 api.weapp.com
127.0.0.1 db.dev.com
```
2. 编辑Nginx的`nginx.conf`文件，在api.weapp.com配置中添加location

```
    location /peanut/ {
      #重写去掉url中server name部分
      rewrite ^/peanut(.*)/ /$1 break;
      #http 协议
      proxy_pass http://127.0.0.1:8004;
    }
```
