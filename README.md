# Random Photos API

本项目是一个简单的 Flask 应用，通过 `/api/images` 路由从本地目录随机返回一张图片。

## 项目结构

```
random-photos-api
├── src
│   ├── main.py          # 应用入口
│   ├── api
│   │   └── photos.py    # 图片接口
│   └── utils
│       └── file_utils.py # 文件工具函数
├── requirements.txt      # Python依赖包列表
├── Dockerfile            # 容器构建文件
├── deploy.yaml           # K8s部署文件（含PVC和Ingress）
└── README.md             # 项目说明
```

## 安装与运行

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 启动应用：
   ```
   python src/main.py
   ```

3. 访问接口：
   ```
   http://localhost:5000/api/images
   ```

## Docker运行

构建镜像并运行容器（假设本地图片目录挂载到 `/photos`）：
```
docker build -t random-photos-api .
docker run -p 5000:5000 -v /你的本地图片目录:/photos random-photos-api
```

## Kubernetes部署

参考 `deploy.yaml`，包含 PVC 持久化存储、Service 和 Ingress 路由。部署后可通过 Ingress 访问 `/api/images` 路径获取随机图片。

## License

MIT License