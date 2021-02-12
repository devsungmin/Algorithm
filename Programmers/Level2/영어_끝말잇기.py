def solution(n, words):
    use = [words[0]] # 첫번째 단어는 사용하기 때문에 추가하여 시작
    last_alphabet = words[0][-1] # 끝말잇기에 사용될 단어
    result = [] # 결과 값
    
    cnt, use_word = 0,0
    
    for i in range(1, len(words)):
        if words[i] not in use and words[i][0] == last_alphabet:
            use.append(words[i])
            last_alphabet = words[i][-1]
        else:
            cnt = i%n+1
            use_word = (i//n)+1
            break
            
    result.append(cnt)
    result.append(use_word)
    
    return result
