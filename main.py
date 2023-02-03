import os
import shutil
import json
import uuid

"""
사용자로부터 받을 입력
- pack name
- pack description

생성될 파일 구조
/pack
    /scripts
        - main.js
    - manifest.json <- 사용자 입력
    - pack_icon.png
"""

# 스크립트 팩 이름/설명 입력
pack_name = input("팩 이름을 입력해주세요: ")
pack_description = input("팩 설명을 입력해주세요: ")

# 입력 건너뛰었을 시, 기본값 대입
if not pack_name: pack_name = "script pack"
if not pack_description: pack_description = "script pack description"

# manifest_form 형식에 맞추어서 새로운 manifest 파일 생성
with open("lib/manifest_form.json", "r", encoding="utf-8") as file:
    manifest = json.load(file)

    manifest["header"]["name"] = pack_name
    manifest["header"]["description"] = pack_description
    manifest["header"]["uuid"] = str(uuid.uuid4())

    manifest["modules"][0]["uuid"] = str(uuid.uuid4())
    manifest["modules"][1]["uuid"] = str(uuid.uuid4())

# 스크립트 팩 구성
os.makedirs("pack/scripts")
shutil.copyfile("lib/pack_icon.png", "pack/pack_icon.png")
with open("pack/scripts/main.js", "w") as script_file:
    script_file.write('import {\n\tworld\n} from "@minecraft/server";\n')
with open("pack/manifest.json", "w", encoding="utf-8") as manifest_file:
    json.dump(manifest, manifest_file, indent="\t", ensure_ascii=False)


# 파일 생성 결과 표시
print(f"""
폴더 이름: pack
팩 이름: {pack_name}
팩 설명: {pack_description}
생성된 팩 파일 구조
/pack
    /scripts
        - main.js
    - manifest.json
    - pack_icon.png

성공적으로 팩이 생성되었습니다.
""")
input("종료하려면 엔터...")
