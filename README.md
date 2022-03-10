# 게시물, 댓글 API서버
<img width="431" alt="image" src="https://user-images.githubusercontent.com/98328569/157632990-b352469c-764d-417e-b543-dfde9313c0bb.png">


1. 게시물 전체

   > -GET
   >
   > > - url/api/postlist/
   > > - 형식 : json

2. 게시물
   > - 게시불 올리기 POST
   >   > - url/api/post/
   >   > - 형식 : json
   >   > - 필드 : content, title
   > - 게시불 자세히보기 GET
   >   > - url/api/post/<id>
   >   > - 형식 : json
   >   > - 필드 : content, title
3. 댓글
   > - 댓글 올리기 POST
   >   > - url/api/post/<게시물id>
   >   > - 형식 : json
   >   > - 필드 : comment
   > - 게시물 댓글 전체보기 GET
   >   > - url/api/post/<게시물id>
   >   > - 형식 : json
   >   > - 필드 : comment

## 데이터베이스 위치 : pgdb -> practiceserver -> postgres
