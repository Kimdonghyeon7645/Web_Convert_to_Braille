# Web_Convert_to_Braille
#### 웹페이지 문서를 읽어 점자로 변환하는 파이썬 라이브러리 만들기

이 저장소는 시각장애인들을 위한 서비스를 개발하는, 레구레테론과 연계됩니다.
> https://github.com/LeguLeteron

## 선행조사

미리 관련되있는, 보통의 문서를 점자로 변환하는 서비스를 여러번 찾아봤다.  
한컴에서는, 
> https://www.youtube.com/watch?v=5gkBuU1iF40

위같이 워드문서를 점자 문서로 변환하는 기능이 존재하고,

'점자세상' 사이트에서 온라인 점역 프로그램의 자취를 봤는데,  
링크로 들어갔을때, 점자세상으로 접속되고, 오픈돼있는 API를 구하지는 못했다.
> http://alja.net/web/board.php?board=kkkdata&page=4&category=14&command=body&no=759

그외에서 개인, 팀별 프로젝트에서 웹페이지를 점자 신호로 변환하는 프로젝트는 봤어도,  
공개된 기능에 대한 데이터나, 오픈된 API를 구하기는 어려웠다.

물론 이 조사는 틈생길때 은근히 이어가야 겠지만, 내가 만족할만한 기능을 찾는것은 어려울 것 같다.


## 큰그림

간단하게, 그러나 다양하고 친절하게,  
파이썬을 활용해 웹 페이지를 읽고, 점자로 변환도 할 수 있는 패키지? 라이브러리를 만들어볼 계획이다.

조금 구체화하면,
- 웹페이지 문서를 가져오는 기능
(이 기능은 웹문서를 변환하기 위한 부가 기능으로, 필요에 따라서 구현을 생략할만도 함.)

- 문서의 내용을 분리하고 초성, 중성, 종성으로 한글을 분리하는 기능
(사실상 여러 깃허브나 블로그에서 한글 문자를 제어하는 기능은 많이 개발되어 있다. 그러나 원리도 어렵지는 않아서 직접 만들어 볼것이다.)
> (http://dream.ahboom.net/entry/%ED%95%9C%EA%B8%80-%EC%9C%A0%EB%8B%88%EC%BD%94%EB%93%9C-%EC%9E%90%EC%86%8C-%EB%B6%84%EB%A6%AC-%EB%B0%A9%EB%B2%95)

- 한글을 점자 문자로 변환하는 기능
(이것도 유니코드의 점자 문자를 이용해서 변환해 주는것이 핵심이다.)

- 점자 문자를 문서의 일부(문장, 문단, 단어, 콘텐츠요소, 제목요소)만 골라서도 변환하는 기능
(웹 요소의 제어와 위의 변환기능을 합친 기능이 되겠다.)