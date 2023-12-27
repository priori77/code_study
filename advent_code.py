import time

calibration_document = r'D:\textfile.txt'

start_time = time.time()

with open(calibration_document, "r", encoding="utf-8") as file:
  word_list = []
  for line in file:
    word_list.extend(line.split())

def calculate_calibration_value(line):
    first_digit = int(next(char for char in line if char.isdigit()))
    last_digit = int(next(char for char in reversed(line) if char.isdigit()))
    calibration_value = first_digit * 10 + last_digit

    return calibration_value

total_sum = sum(calculate_calibration_value(line) for line in word_list)
cnt = 1
sum = 0
for i in word_list:
    first_num = int(next(char for char in i if char.isdigit())) * 10
    last_num = int(next(char for char in reversed(i) if char.isdigit()))
    sum_num = first_num + last_num
    sum = sum + sum_num
    print(f"{cnt} 번째 입력된 코드는: {i} // 코드의 첫번째 숫자: {first_num} // 코드의 마지막 숫자: {last_num}")
    print(f"{cnt} 번째 코드의 값은 {sum_num}입니다.")
    print(f"{cnt} 번째 누적 합은 {sum} 입니다")
    cnt += 1

print("최종 산출 결괏값은:", total_sum)

end_time = time.time()
elapsed_time = end_time - start_time
print("코드 실행되는데 소요된 시간은 {:.6f} 초입니다".format(elapsed_time))
