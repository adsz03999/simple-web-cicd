# Simple Web CI/CD

基于 Flask 的 Web 应用 CI/CD 实验演示项目。

- **学号**: 2440666156
- **姓名**: 董浩林
- **服务器**: 阿里云 ECS Ubuntu 22.04 (8.163.32.142)
- **仓库**: https://github.com/adsz03999/simple-web-cicd

## 项目简介

一个极简的 Flask Web 应用，演示完整的 CI/CD 流程：
1. **持续集成 (CI)**: GitHub Actions 自动运行测试
2. **持续交付 (CD)**: 自动构建 Docker 镜像并部署到阿里云 ECS
3. **持续部署**: 推送到 main 分支后自动触发部署

## 技术栈

- **Web 框架**: Flask 3.1.0
- **测试框架**: pytest 8.3.4
- **容器化**: Docker (python:3.12-alpine)
- **CI/CD**: GitHub Actions
- **Python**: 3.12
- **部署目标**: 阿里云 ECS Ubuntu 22.04

## 快速开始

### 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行应用
python app.py
```

访问 http://localhost:8080

### Docker 运行

```bash
# 构建镜像
docker build -t simple-web:latest .

# 运行容器
docker run -p 8080:8080 simple-web:latest
```

### 测试

```bash
pytest test_app.py -v
```

## CI/CD 流程

本项目使用 GitHub Actions 实现自动化 CI/CD，流水线包含 4 个阶段：

1. **① 验证 & 测试**: 安装依赖，运行单元测试
2. **② 构建镜像**: 构建 Docker 镜像，导出为 tar.gz
3. **③ 部署至 ECS**: SCP 传输到阿里云 ECS，加载镜像并启动
4. **④ 结果通知**: 汇总各阶段执行结果

详细配置见 `.github/workflows/ci.yml`

## API 接口

| 路径 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 主页，显示部署信息 |
| `/health` | GET | 健康检查接口 |

## 目录结构

```
.
├── .github/workflows/ci.yml   # GitHub Actions 配置
├── app.py                     # Flask 应用主程序
├── test_app.py                # 单元测试
├── requirements.txt           # Python 依赖
├── Dockerfile                 # Docker 镜像构建
├── docker-compose.yml         # 本地开发 compose
├── docker-compose.prod.yml    # 生产环境 compose
├── .gitignore
└── README.md
```

## 实验步骤

1. 本地运行 git 命令下载源程序，修改源程序添加自己学号和姓名上传至 github
2. github 上自己的项目空间
3. CI/CD 跑通运行成功
4. 云服务器上部署成功
5. 修改本地代码 2.0 版本，再次推送，CI/CD 成功部署

## License

MIT
