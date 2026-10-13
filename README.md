# japan-exhibitions

일본 주요 도시(도쿄 · 요코하마 · 교토 · 오사카 · 고베 · 나라 · 나고야 · 가나자와 · 히로시마 · 후쿠오카 · 삿포로) 미술관 · 박물관의 기획전 · 특별전 일정입니다.
iOS 앱 "전시 아카이브"의 **일본 전시** 탭이 `japan-exhibitions.json`을 12시간마다 받아 씁니다.

- 매달 1일 아침(서울 시간)에 Claude 예약 작업이 조사해서 갱신합니다.
- 범위: 실행일부터 약 4개월 안에 열려 있거나 새로 시작하는 전시. 상설전 · 소규모 갤러리전은 넣지 않습니다.
- 참고: [아이엠 인터넷뮤지엄](https://www.museum.or.jp/), [観仏三昧](http://www.kanbutuzanmai.com/), [美術展ナビ](https://artexhibition.jp/), 각 미술관 공식 사이트
- 일정은 바뀔 수 있으니 가기 전에 공식 사이트를 확인해 주세요.

## 형식

```json
{"updatedAt": "yyyy-MM-dd", "exhibitions": [{
  "id": "같은 전시는 매달 같은 값",
  "title": "한국어 제목", "originalTitle": "일본어 제목(선택)",
  "venue": "관 이름(한국어)", "city": "도쿄|요코하마|교토|오사카|고베|나라|나고야|가나자와|히로시마|후쿠오카|삿포로",
  "area": "도시 안 동네", "start": "yyyy-MM-dd", "end": "yyyy-MM-dd",
  "genre": "jp|west|cont|craft|sci", "tentative": true, "note": "선택",
  "url": "전시 공식 페이지(있으면)", "venueUrl": "미술관 · 박물관 공식 사이트"
}]}
```

앱의 "공식 사이트에서 보기"는 `url`(전시 페이지)이 있으면 그곳을, 없으면 `venueUrl`(기관 사이트)을 엽니다.
