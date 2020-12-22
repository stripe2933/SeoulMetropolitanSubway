import requests, json

api_key = ''
with open('keys/KakaoApiKey.txt', 'r') as f:
    api_key = f.readline()

api_header = {"Authorization": "KakaoAK "+api_key}

def get_coord_by_keyword(keyword: str):
    '''주어진 키워드를 카카오 로컬 API를 이용해 검색합니다.
    해당하는 장소의 경도와 위도 값을 리스트의 형태로 반환합니다.
    
    keyword: 검색할 질의어(키워드)
    '''
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + keyword

    try:
        res = requests.get(url, headers=api_header)
        res.encoding = None
        result = json.loads(res.text)

        if len(result['documents']) == 0:
            raise RuntimeError('%s: 반환된 값이 없습니다.' % keyword)
        
        match_first = result['documents'][0]
        return float(match_first['x']), float(match_first['y'])
    except Exception as e:
        print(e)
        return None, None