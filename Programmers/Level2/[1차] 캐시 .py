def solution(cacheSize, cities):
    # cities에 있는 값을 모두 소문자로 바꿈 -> lower() 사용
    cities = [city.lower() for city in cities]
    time = 0  # 실행 시간
    cache = []

    if cacheSize != 0:
        for c in cities:
            if c in cache: # cache hit
                cache.pop(cache.index(c))
                cache.append(c)
                time += 1
            else: # cache miss
                if len(cache) < cacheSize:
                    cache.append(c)
                    time += 5
                else:
                    cache.pop(0) # cache안에 모든 값을 pop 해준다
                    cache.append(c)
                    time += 5
    else:
        # 캐쉬 사이즈가 0인 경우모든 경우가 cache miss이기 때문에 시간을 +5 해준다
        time += len(cities)*5
    
    return time