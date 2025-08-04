def solution_optimized():
  num = int(input()) # 입력받을 문자열 개수 지정.
  word = list(input()) # 첫번째 입력 문자열을 리스트로 저장.
  for _ in range(num-1): # 기준 문자열을 제외한 횟수만큼 문자열 입력받기.
    word_2 = input() # 입력되는 문자열 저장할 변수.
    for i in range(len(word)): # 한 글자씩 비교하는 반복문.
      if word[i] != word_2[i]: # 다른 문자일 경우.
        word[1] = '?'  # 기준 문자열의 해당 위치의 문자를 ?로 변경.
  print(''.join(word)) # 리스트의 문자들을 아무 구분자 없이 모두 이어붙인다.