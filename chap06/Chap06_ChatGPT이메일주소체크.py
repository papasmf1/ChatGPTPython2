#Chap06_ChatGPT이메일주소체크.py 

import re

def check_email(email):
    # 이메일 주소의 패턴을 정의합니다.
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # 패턴과 일치하는지 확인합니다.
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 데이터 10개 생성
emails = [
    "example@example.com",
    "example_123@example.co.uk",
    "user.name+tag+sorting@example.com",
    "user@sub.example.com",
    "user@123.123.123.123",
    "user@[IPv6:2001:db8::1]",
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@domain.com"
]

# 이메일 주소가 유효한지 테스트
for email in emails:
    print(f"{email}: {check_email(email)}")
