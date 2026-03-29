from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    try:
        visits = r.incr("counter")
    except:
        visits = "Redis not connected"

    return f"""
    <h1>🚀 DevOps Learning App</h1>
    <h2>You are visitor number: {visits}</h2>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
