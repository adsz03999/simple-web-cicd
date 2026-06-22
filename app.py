"""
极简 Flask Web 应用 — CI/CD 实验演示
学号: 2440666156
姓名: 董浩林
"""
import logging
import socket
import platform
import datetime
from flask import Flask, render_template_string

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD 实验 — Flask App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
        }
        .card {
            background: #fff; border-radius: 16px; padding: 48px 40px;
            max-width: 500px; width: 90%; box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 { color: #333; font-size: 28px; margin-bottom: 8px; }
        .version { color: #764ba2; font-size: 14px; font-weight: 600; margin-bottom: 24px; }
        .status { display: inline-block; background: #e8f5e9; color: #2e7d32;
                  padding: 6px 16px; border-radius: 20px; font-size: 14px; margin-bottom: 24px; }
        .info { background: #f5f5f5; border-radius: 8px; padding: 16px;
                text-align: left; font-size: 13px; color: #666; line-height: 1.8; }
        .info span { color: #333; font-weight: 600; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 CI/CD 部署成功！</h1>
        <p class="version">Flask App v2.0 | Python {{ python_version }}</p>
        <div class="status">✅ 服务运行正常</div>
        <div class="info">
            <p><span>学号：</span>2440666156</p>
            <p><span>姓名：</span>董浩林</p>
            <p><span>容器 ID：</span>{{ hostname }}</p>
            <p><span>部署时间：</span>{{ deploy_time }}</p>
            <p><span>环境：</span>{{ environment }}</p>
        </div>
    </div>
</body>
</html>"""

@app.route("/")
def index():
    logger.info("=== 开始处理首页请求 ===")
    try:
        python_version = platform.python_version()
        hostname = socket.gethostname()
        deploy_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        environment = "Production" if app.config.get("ENV") == "production" else "Development"

        logger.info(f"Python 版本: {python_version}")
        logger.info(f"主机名: {hostname}")
        logger.info(f"部署时间: {deploy_time}")
        logger.info(f"运行环境: {environment}")

        result = render_template_string(
            HTML,
            python_version=python_version,
            hostname=hostname,
            deploy_time=deploy_time,
            environment=environment,
        )
        logger.info("=== 首页请求处理完成 ===")
        return result
    except Exception as e:
        logger.error(f"首页请求处理异常: {str(e)}", exc_info=True)
        raise

@app.route("/health")
def health():
    logger.info("=== 开始处理健康检查请求 ===")
    try:
        response = {"status": "healthy"}
        logger.info(f"健康检查结果: {response}")
        logger.info("=== 健康检查请求处理完成 ===")
        return response, 200
    except Exception as e:
        logger.error(f"健康检查请求处理异常: {str(e)}", exc_info=True)
        return {"status": "unhealthy", "error": str(e)}, 500

@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 错误 - 请求路径: {error.description}")
    return {"error": "Not Found", "message": "请求的资源不存在"}, 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 内部错误: {str(error)}", exc_info=True)
    return {"error": "Internal Server Error", "message": "服务器内部错误"}, 500

@app.before_request
def before_request():
    try:
        logger.info(f"收到请求 - 方法: {app.request.method}, 路径: {app.request.path}")
    except Exception:
        pass

@app.after_request
def after_request(response):
    try:
        logger.info(f"请求完成 - 状态码: {response.status_code}, 路径: {app.request.path}")
    except Exception:
        pass
    return response

if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("Flask 应用启动中...")
    logger.info(f"Python 版本: {platform.python_version()}")
    logger.info(f"Flask 环境: {app.config.get('ENV', 'development')}")
    logger.info(f"调试模式: {app.debug}")
    logger.info(f"主机名: {socket.gethostname()}")
    logger.info("=" * 50)
    app.run(host="0.0.0.0", port=8080, debug=True)
