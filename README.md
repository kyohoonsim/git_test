# Git 명령어 테스트 레포지토리

Git 명령어 테스트용 레포지토리입니다.

## 명령어 정리

상태 확인
- git status

수정사항 확인
- git diff
- git diff [기준커밋해시] [커밋해시]

스테이징
- git add .

스테이징 취소
- git restore --staged .

수정 취소
- git restore .

커밋
- git commit -m "커밋 메시지"

최신 커밋 취소
- git reset HEAD^

최신 커밋 취소(스테이지에서는 내리지 않음)
- git reset --soft HEAD^

최신 커밋 취소(수정한 내용도 제거)
- git reset --hard HEAD^

특정 버전으로 돌아가기
- git reset [커밋해시]

특정 커밋만 취소
- 특정 커밋만을 취소하고, 그것을 기록하기 위해 새 커밋을 생성
- reset은 지정한 커밋의 이후 모든 커밋을 취소해버림
- git revert [취소할커밋해시]

하나의 브랜치에 그것의 부모 브랜치에서 만들어진 커밋을 최신 상태로 업데이트 하는 과정. 업데이트하려는 브랜치에서 명령어 rebase를 부모 브랜치의 이름과 함께 실행하면 됨. 그러면 git은 자식 브랜치에서 작업하던 커밋을 삭제하고, 부모 브랜치에서 만들어졌던 새 커밋을 자식 브랜치 팁에 추가. 그 후 삭제했던 커밋을 업데이트해 다시 브랜치에 추가.
- git rebase

푸시(push)
- git push -u origin master

강제 푸시
- git push origin +[브랜치명]
- git push origin [브랜치명] -f

풀(pull)
- git pull origin master
- git pull --rebase

원격 레포지토리에 올라간 파일 또는 폴더 삭제
- git rm --cached -r [폴더명 or 파일명]

브랜치 목록 확인
- git branch

브랜치 생성
- git branch [브랜치명]

브랜치 전환
- git switch [브랜치명]

브랜치 삭제
- git branch -d [브랜치명]

브랜치 강제 삭제
- git branch -D [브랜치명]

원격 레포지토리 브랜치 삭제
- git push origin --delete [브랜치명]

머지(merge)
- git merge [현재브랜치로merge할브랜치명]

원격 브랜치에서 변경 사항 확인 및 로컬 저장소와 원격 저장소 동기화
- git fetch
- git fetch --all (모든 원격 브랜치의 변경 사항을 가져오도록 지시)

원격 브랜치에서 로컬로 가져온 브랜치 중에서 원격 저장소에서 삭제된 브랜치를 정리하는데 사용
- git remote prune origin