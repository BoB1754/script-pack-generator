# script-pack-generator

마인크래프트 BE 스크립트 행동팩을 생성해줍니다.
만약 manifest.json의 양식이 변경되거나 다른 이유로 수정할 일이 생기면, 
lib/manifest_form.json을 원하는 형식으로 수정해주면 됩니다.

# 사용법
0. python을 설치합니다.
1. execute.bat 파일을 실행시킵니다. 
2. 터미널에 팩 이름과 팩 설명을 입력합니다. (버전은 1.0.0)
3. pack 폴더 안에 manifest.json을 포함한 필수 파일들이 생성됩니다.
4. 생성된 pack 폴더를 원하는 이름으로 수정한 뒤, development_behavior_packs 또는 behavior_packs에 넣어줍니다.
5. 마크를 실행하고 행동팩 목록에서 추가한 행동팩을 확인합니다. 
