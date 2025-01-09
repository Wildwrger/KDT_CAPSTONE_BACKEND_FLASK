from flask import Flask, Response
import requests
import json

app = Flask(__name__)

# 네이버 API 정보
CLIENT_ID = 'm1ehrdynlqBavqqPCVab'
CLIENT_SECRET_PWD = 'J3c36ztXGC'

# 해당 카테고리의 뉴스를 가져오는 함수
def get_news (category, query = None):
    url = f"https://openapi.naver.com/v1/search/news.json?query={category}"
    if query:
        url += f"&query={query}"
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET_PWD
    }
    response = requests.get(url, headers=headers)
    return response.json()

def index(request):
    print(f"Received request: {request.url}")  # 요청 URL 출력
    category = 'IT'  # 기본 카테고리 IT로 설정
    search_query = request.args.get('search')  # GET 요청에서 'search' 파라미터 가져오기

    if search_query:
        print(f"Search query received: {search_query}")  # 검색어 출력
        news = get_news(category, search_query)
    else:
        print("No search query received.")  # 기본 카테고리 요청
        news = get_news(category)

    # JSON 데이터를 UTF-8로 인코딩하여 반환
    json_data = json.dumps({"items": news['items']}, ensure_ascii=False, indent=4)  # ensure_ascii=False로 한글 처리
    return Response(json_data.encode('utf-8'), content_type='application/json; charset=utf-8')
