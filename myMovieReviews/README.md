구현한 기능: 1,2,3,4,5,6,7,8,9,10,11
구현하지 못한 기능: X


🔥 백엔드 챌린지 참여합니다! 🔥

구현한 기능: 장르 선택 기능, 러닝 타임 시간 단위 출력

장르 선택 기능은 charfield의 choices 기능을 이용하여 만들었습니다.

러닝 타임 시간 단위 출력은 둘 다 함수 내에서 먼저 hour과 minute을 계산하여 render 함수의 context 인자로 넘겨주는 방식으로 했는데, 리스트 부분은 여러 배열의 인덱스를 요구했기 때문에 custom template filter를 적용해 forloop.counter0를 인덱스로 사용할 수 있도록 구현했습니다. 

custom template filter 링크: https://stackoverflow.com/questions/4651172/reference-list-item-by-index-within-django-template
적용 방법: https://wayhome25.github.io/django/2017/06/22/custom-template-filter/
