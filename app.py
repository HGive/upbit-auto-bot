from dotenv import load_dotenv

load_dotenv()

# 이제 환경변수에 접근할 수 있습니다.
import os
access_key = os.getenv("UPBIT_OPEN_API_ACCESS_KEY")
secret_key = os.getenv("UPBIT_OPEN_API_SECRET_KEY")