
# iCore - iHome的api服务

### 依赖
rust

### 如何初始化本地开发环境
1. 创建本地本地数据库
2. 执行`python manage.py run_dev_server 127.0.0.1`启动服务
3. 访问http://127.0.0.1:8000/console/，成功获取api console页面

## 如何集成到Ningx？ ##
1. 在hosts文件中添加如下域名
```
127.0.0.1 api.home.com
127.0.0.1 db.home.com
```
2. 编辑Nginx的`nginx.conf`文件，在api.home.com配置中添加location

```
    location /icore/ {
      #重写去掉url中server name部分
      rewrite ^/icore(.*)/ /$1 break;
      #http 协议
      proxy_pass http://127.0.0.1:8000;
    }
```
