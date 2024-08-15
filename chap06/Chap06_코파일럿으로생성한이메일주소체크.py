import re

def is_valid_email(email):
    # 이메일 주소를 검사하는 정규식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 예시 이메일 주소 리스트
emails = [
    "user@example.com",
    "john.doe@company.co.kr",
    "invalid_email",
    "noatsign.com",
    "missing@domain",
]

for email in emails:
    if is_valid_email(email):
        print(f"{email}은(는) 올바른 이메일 주소입니다.")
    else:
        print(f"{email}은(는) 올바르지 않은 이메일 주소입니다.")
