scriptnameEN = "SeroScript"
scriptnameKR = "새로스크립트"

scriptversion = "1.0"

def 강제종료(errorcode):
    print(f"\n프로그램이 강제 종료 됬습나다. 종료 품목 번호: {errorcode}")
    exit()

def warning(input):
    print(f"\033[91m{input}\033[0m")

def 출력(input):
    try:
        print(input)
    except:
        warning("출력의 입력 형식이 올바르지 않습니다.")
        강제종료(1)
def 만약(ifstatementfunc, executedcode):
    try:
        if f"{ifstatementfunc}":
            exec(executedcode)
    except:
        warning("만약: 형식 오류")
        강제종료(1)

def 길이(listinput):
    return(len(listinput))

def 목록(listinput):
    return(list(listinput))

def 반올림(numberinput):
    return(int(round(numberinput)))

def 참일때(forstatementfunc, executedcode):
    while f"{forstatementfunc}":
        exec(executedcode)

def 입력(output):
    return(input(output))

def 변수(variable, function, value):
    globalvar = globals()
    if variable not in globalvar:
        globalvar[variable] = 0

    if function == "더하기":
        globalvar[variable] += value
    elif function == "설정":
        globalvar[variable] = value
    elif function == "wassp":
        globalvar[variable] = value


def 변수값(variable):
    try:
        globalvar = globals()
        return globalvar[variable]
    except:
        warning("변수값 형식이 틀리거나 변수가 정의되지 않았습니다.")
        강제종료(1)

def 예외처리(trycode,exceptcode):
    try:
        exec(trycode)
    except:
        exec(exceptcode)

def 숫자변환(number):
    try:
        return(int(number))
    except:
        warning("숫자변환 입력이 올바른 정수가 아닙니다.")
        강제종료(1)

def 글자변환(input):
    try:
        return(str(input))
    except:
        warning("글자 변환 입력이 올바르지 않습니다.")
        강제종료(1)

def 경고(input):
    warning(input)

def 줄바꿈(times):
    for i in range(times):
        print()

def 도움이():
    print(f"{scriptnameKR} {scriptversion} 도움이:")
    print(f"{scriptnameEN} {scriptversion} Documentation:")
    print("문서 자료가 아직 없습니다.")

def 버전():
    print(f"{scriptnameKR} {scriptversion} 버전입니다.")
    print(f"{scriptnameEN} V{scriptversion} by nohYoom")

def 도움이():
    print(f"{scriptnameKR} {scriptversion} 도움이:")
    print(f"{scriptnameEN} {scriptversion} Documentation:")
    print("문서 자료가 아직 없습니다.")

def 버전():
    print(f"{scriptnameKR} {scriptversion} 버전입니다.")
    print(f"{scriptnameEN} V{scriptversion} by nohYoom")