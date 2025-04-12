import sys
from SeroScriptModule import *
import SeroScriptModule
import inspect

safe_globals = {}

for name, obj in inspect.getmembers(SeroScriptModule, inspect.isfunction):
    if not name.startswith('_'):
        safe_globals[name] = obj

safe_globals["__builtins__"] = {
    "None": None,
    "True": True,
    "False": False,
    "range": range,
}
def shell():
    print(f"{scriptnameKR} {scriptversion} 버전입니다. (2025 04월 4일 개정) 좋은 하루이에요.")
    print("종료하려면 (/강제종료)를 입력하세요. 더 많은 정보가 필요하면 (도움이()), (버전())을 입력해보세요.")
    while True:
        command = input(">_ : ")
        if command.strip() == "/강제종료":
            강제종료(2)
        else:
            try:
                exec(command, safe_globals)
            except Exception as e:
                warning(f"문법 오류: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if filename.endswith(".sero"):
            try:
                with open(filename, "r", encoding="utf-8") as file:
                    hanpy_code = file.read()
                    exec("from SeroScriptModule import *")
                    exec(hanpy_code, safe_globals)
            except Exception as e:
                warning(f"파일 실행 중 오류 발생: {e}")
                강제종료(3)
        else:
            try:
                exec(f"{filename}()")
            except:
                warning("알 수 없는 명령이 입력되었습니다.")
    else:
        shell()