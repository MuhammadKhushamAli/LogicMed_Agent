from dotenv import load_dotenv
load_dotenv()

import os
from fast_api_server.server import app
import uvicorn

PORT: int = int(os.getenv("PORT"))
HOST: str = os.getenv("HOST")

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)