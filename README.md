# Engineering_BLOG

## 1. 프로젝트 소개
Python, Django, Nginx, MySQL, Linux 등 프로그래밍과 관련된 모든 기술의 이슈를 정리하는 블로그입니다.

### 1.2 역할분담
개인 프로젝트

## 2. 목표와 기능
### 2.1 목표
Django를 이용하여 기술 블로그를 만들고 개발하며 생기는 이슈를 정리하는 것이 목표입니다.

### 2.2 기능
- 블로그 메인 페이지
- 게시글 리스트 페이지
- 게시글 검색
- 로그인, 회원가입  
- 게시글 작성, 수정, 삭제
- 게시글 내 댓글

## 3. 개발 환경
<div align=center>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<br>
  
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</div>

## 4. 개발 일정
![image](https://github.com/abcdqwer1/project_blog/assets/68181016/05180271-c294-451f-acc7-d67f6e35b92a)
<br>
https://docs.google.com/spreadsheets/d/1T2Jk1f3INWnJgWd8X1gpVTpYAEZ_OzIpdwCJ0moCY0k/edit#gid=0

## 5 프로젝트 구조
### 5.1 디렉토리 구조
```
📦project_blog
┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂blog
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂main
 ┃ ┣ 📂migrations
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┗ 📂blog
 ┣ 📂projectblog
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📂assets
 ┃ ┃ ┣ 📂img
 ┃ ┣ 📂css
 ┃ ┃ ┣ 📜styles.css
 ┃ ┃ ┗ 📜styles2.css
 ┃ ┣ 📂js
 ┃ ┃ ┗ 📜scripts.js
 ┣ 📂templates
 ┃ ┣ 📂accounts
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┗ 📜profile.html
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📜form.html
 ┃ ┃ ┣ 📜post_confirm_delete.html
 ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┣ 📜post_detail_new.html
 ┃ ┃ ┗ 📜post_list.html
 ┃ ┣ 📂main
 ┃ ┃ ┗ 📜index.html
 ┃ ┗ 📜base.html
 ┣ 📂venv
```
### 5.2 프로젝트 구조
![image](https://github.com/abcdqwer1/project_blog/assets/68181016/ef686a88-efb3-46ff-960d-f3f5bbfa5c06)
<br>
https://www.mindmeister.com/app/map/2922826653

## 6. DB 모델링
![image](https://github.com/abcdqwer1/project_blog/assets/68181016/6dc6d799-bad7-4a7f-a940-4eddc16ee3e4)
<br>
https://dbdiagram.io/d/project_blog-6539babbffbf5169f0783396

## 7. UI
![image](https://github.com/abcdqwer1/project_blog/assets/68181016/ef5b0927-bb4c-479d-9120-744c8999f866)

- 메인 페이지
- 화면 상단 네이게이션 메뉴에는 1.웹 사이트 제목, 2.(블로그, 로그인, 회원가입, 로그아웃, 프로필)이 구현되어있습니다.
- 각 메뉴는 눌렀을때 페이지 이동되며 Engineering BLOG를 누르면 메인페이지로 이동, 상단 블로그나 아래 3.포스트 보러가기를 누르면 블로그 게시글 리스트 페이지로 이동합니다.

<br>

![image](https://github.com/abcdqwer1/project_blog/assets/68181016/ad752b8e-cd30-4d35-923f-8cf7718fca28)
- 로그인을 하면 로그아웃과 프로필 메뉴가 보여집니다.

<br>

![image](https://github.com/abcdqwer1/project_blog/assets/68181016/6dd13a1f-1bc9-4281-b64e-e45da8562493)
- 로그아웃을 하면 로그인과 회원가입 메뉴가 보여집니다.

<br>

![image](https://github.com/abcdqwer1/project_blog/assets/68181016/130e1f59-d8c3-482c-84f8-bf13a58395cc)
- 블로그 게시글 리스트 페이지
- 화면 오른쪽에 1.글쓰기를 눌러 글 작성이 가능합니다.
- 글쓰기 아래 2.검색 기능이 구현되어있습니다.
- 게시글을 확인하려면 3번 자세히보기 버튼이나 게시글의 썸네일이미지를 클릭하면 됩니다.
<br>

![image](https://github.com/abcdqwer1/project_blog/assets/68181016/2e66b1fb-0fe3-48f0-b0db-383a34d565b5)

- 게시글 페이지
- 게시글 내용에는 제목, 게시글 생성일자, 조회수, 태그, 내용, 댓글이 있습니다.
- 하단에는 목록, 수정, 삭제 버튼이 있습니다.
- 수정, 삭제 버튼은 해당 게시글을 작성한 아이디만 보여지며, 사용 또한 마찬가지입니다.
<br>

![image](https://github.com/abcdqwer1/project_blog/assets/68181016/bc7051ff-b80b-4b60-8d8a-f3c4f0c0978e)
- 댓글을 남기게되면 아이디, 댓글내용, 작성일자로 이루어진 댓글이 생성됩니다.
<br>

https://github.com/abcdqwer1/project_blog/assets/68181016/5187e080-9a3a-4a31-83b0-a2fcac53dbdc

- 네이게이션바 확인

https://github.com/abcdqwer1/project_blog/assets/68181016/c131ea34-af19-4a88-abf4-c3d4f747e922

- 댓글 기능 

https://github.com/abcdqwer1/project_blog/assets/68181016/ab953a9d-65cd-43d0-8429-ae98fcf77d0a

- 로그인, 로그아웃

https://github.com/abcdqwer1/project_blog/assets/68181016/79b6b986-9ac8-499b-9b33-17b5af64a2ef

- 글수정, 검색기능



## 8. 트러블슈팅

1. DEBUG 설정을 True -> False로 변경한 경우 static, media 폴더를 사용 할 수 없는 문제


404 페이지 확인을 위해 sattings.py 에 DEBUG 설정을 False 로 변경했을때 블로그에 썸네일 이미지가 전부 나오지 않는걸 확인하고 해당 에러를 발견했다.  


runserver시 --insecure 옵션을 주면 static 폴더는 사용 할 수 있는것으로 확인됐지만 media는 여전히 사용 불가했고, 심지어 배포 후 실서비스는 WEB, WAS를 나누어 웹서버에서 정적파일을 서비스하는 경우가 많았다.  


여기저기 확인 해본 결과 urls.py에 직접 경로 설정을 해주었고 정상 동작하는것을 확인했다.  


urls.py 추가내용
from django.views.static import serve  
from django.urls import re_path  


urlpatterns += re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),  
urlpatterns += re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),



