import multiprocessing
from multiprocessing import Process
import time
import os
import shutil
import glob
import math


def check_even(number: int):
    if number % 2 == 0:
        return True
    else:
        return False


def remove_and_make_directory(dir_path: str):
    try:
        shutil.rmtree(dir_path)
    except:
        pass
    finally:
        os.makedirs(dir_path, exist_ok=True)


def processing(loop_range: range, result_path: str):
    for i in loop_range:
        if check_even(i):
            with open(result_path, 'a') as f:
                f.write(f'{str(i).zfill(5)}\n')

# 추가된 함수
#


def processing_multi(loop_range: range, result_dict: list):
    for i in loop_range:
        if check_even(i):
            result_dict[i] = f'{str(i).zfill(5)}\n'


def run_without_multiprocessing(loop_range: range, result_path: str):
    processing(loop_range, result_path)


def run_with_multiprocessing(loop_range: range,  result_path: str, worker_num: int):
    # 이곳에 ranges 정의 코드 작성
    #
    ranges = []
    stop_value = loop_range.stop
    divide_value = math.trunc(stop_value/worker_num)  # 소수점 아래 버림

    for i in range(worker_num):
        if i == (worker_num-1):
            ranges.append(range(divide_value*i, stop_value))
            break
        ranges.append(range(divide_value*i, divide_value*(i+1)))

    print(f'Splited Ranges: {ranges}')

    # 이곳에 procs 정의 코드 작성
    #
    procs = []
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    for i in ranges:
        procs.append(Process(target=processing_multi, args=(i, return_dict)))

    [proc.start() for proc in procs]
    [proc.join() for proc in procs]

    # 이곳에 후처리 코드 작성
    #
    return_dict = sorted(return_dict.items())
    result = ''.join(value for index, value in return_dict)
    with open(result_path, 'a') as f:
        f.write(result)


def check_sameness(path_1, path_2):
    with open(path_1, 'r') as f:
        target_1 = f.readlines()

    with open(path_2, 'r') as f:
        target_2 = f.readlines()
    return target_1 == target_2


if __name__ == '__main__':
    target_range_list = [range(0, 480), range(0, 1000), range(0, 10010), range(0, 31450)]

    for target_range in target_range_list:
        result_dir_1 = 'without_multiprocessing'
        remove_and_make_directory(result_dir_1)
        result_path_1 = os.path.join(result_dir_1, 'result.txt')

        start = time.time()
        run_without_multiprocessing(target_range, result_path_1)
        print(f'Without Multiprocessing: {time.time() - start}')

        workers = 8
        result_dir_2 = 'with_multiprocessing'
        remove_and_make_directory(result_dir_2)
        result_path_2 = os.path.join(result_dir_2, 'result.txt')

        start = time.time()
        run_with_multiprocessing(target_range, result_path_2, workers)
        print(f'With Multiprocessing: {time.time() - start}')

        assert check_sameness(result_path_1, result_path_2)
        print('Results are same.')
        print()
