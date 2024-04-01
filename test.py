import requests
from bs4 import BeautifulSoup

# 뉴스 사이트 URL
#url = 'https://www.newsis.com/'
url = 'https://www.newsis.com/realnews/?cid=realnews&day=today&page=1'

# requests를 사용하여 웹페이지 가져오기
response = requests.get(url)

print(response)

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# # 헤드라인과 링크 추출을 위한 셀렉터 설정, 사이트 구조에 따라 변경될 수 있음
# headlines = soup.select('.txtCont .tit a')  # 예시 셀렉터, 실제 사이트 구조에 맞게 수정 필요
# #print(headlines)

# # 추출된 정보 출력
# for headline in headlines:
#     # 헤드라인 텍스트와 링크 추출
#     text = headline.text.strip()  # 텍스트 공백 제거
#     link = headline['href']  # 링크 URL 추출
#     print(f'Headline: {text}\nLink: {link}\n')

with open('output_file.txt', 'w', encoding='utf-8') as f:
     f.write(str(soup))

# '.txtCont' 셀렉터를 사용하여 각 뉴스 블록 선택
news_blocks = soup.select('.txtCont')

# 각 뉴스 블록 내에서 필요한 정보 추출
for block in news_blocks:
    if block.select_one('.tit a'):
    # 'tit a' 태그의 텍스트(제목)와 'href'(링크) 추출
        #print(block)
        title_link = block.select_one('.tit a')
        description = block.select_one('.txt a')
        #print(description)
        description_txt = description.text.strip()
        title = title_link.text.strip()
        link = title_link['href']
        # 'time' 클래스의 텍스트(시간 정보) 추출
        time_info = block.select_one('.time').text.strip()
        time_info2 = block.select_one('.time').span.text.strip()
        #print(time_info.span.extract())
        test = block.select_one('.time')

        # <span> 태그를 제거하고 남은 텍스트에서 시간 정보 추출
        #test.find('span').decompose()
        #time_text = test.text.strip()

        #print(test)
        #print(time_text)
        #print(time_info2)
        #print(f'Title: {title}\nLink: {link}\nTime: {time_info}\n')
        print(f'Title: {title}\nDescription: {description_txt}\nLink: {link}\nTime: {time_info}\n')
    else: 
        break
