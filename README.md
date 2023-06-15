# Git 사용법 정리

스테이징
- git add .

스테이징 취소
- git restore --staged .

수정 취소
- git restore .

커밋
- git commit -m "커밋 메시지"

커밋 취소
- 최신 커밋 취소: git reset HEAD^
- 최신 커밋 취소(스테이지에서는 내리지 않음): git reset --soft HEAD^
- 최신 커밋 취소(수정한 내용도 제거): git reset --hard HEAD^
- 특정 버전으로 돌아가기: git reset [커밋해시]

이전 커밋으로 돌아가기 
- 특정 커밋으로 돌아가기 위해 새 커밋을 생성  
- git revert [커밋해시]

하나의 브랜치에 그것의 부모 브랜치에서 만들어진 커밋을 최신 상태로 업데이트 하는 과정. 업데이트하려는 브랜치에서 명령어 rebase를 부모 브랜치의 이름과 함께 실행하면 됨. 그러면 git은 자식 브랜치에서 작업하던 커밋을 삭제하고, 부모 브랜치에서 만들어졌던 새 커밋을 자식 브랜치 팁에 추가. 그 후 삭제했던 커밋을 업데이트해 다시 브랜치에 추가.
- git rebase

푸시
- git push -u origin master

풀
- git pull origin master

브랜치 목록 확인
- git branch

브랜치 생성
- git branch [브랜치명]

브랜치 전환
- git switch [브랜치명]

브랜치 삭제 
- git branch -d [브랜치명]


---
feature 브랜치에서 작업