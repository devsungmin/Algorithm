import math

def solution(progresses, speeds):
    result= []
    # remaining_pro = 100-progresses[i]
    # remaining_spd = remaining_pro/speeds[i]
    # passed_day = math.ceil(remaining_spd)
    passed_day = [math.ceil((100-remaining_pro)/remaining_spd) for remaining_pro,remaining_spd in zip(progresses, speeds)]
    cnt = 0
    
    for i in range(len(passed_day)):
        if passed_day[cnt] < passed_day[i]:
            result.append(i-cnt)
            cnt = i
    result.append(len(passed_day)-cnt)
    return result
