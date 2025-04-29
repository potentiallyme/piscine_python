import sys
import shutil
import time


def ft_tqdm(lst: range) -> None:
    '''
    ft_tqdm mimics the tqdm function behaviour:
    Shows a progress bar for a loop and given range.

    Args:
        lst (range): range to loop through

    Yields:
        Current item from range
    '''
    start = time.time()
    length = len(lst)
    ilen = len(str(length))

    term_width = shutil.get_terminal_size().columns
    overhead = 4 + 3 + ilen * 2 + 28 + 2
    bar_width = term_width - overhead

    for i, item in enumerate(lst, start=1):
        prog = int(i / length * bar_width)
        ttime = time.time() - start
        speed = i / ttime
        eta = (length - i) / speed if i < length else 0

        tm, ts = divmod(ttime, 60)
        em, es = divmod(eta, 60)
        ftime = f'{int(tm):02d}:{int(ts):02d}'
        teta = f'{int(em):02d}:{int(es):02d}'

        bar = f'|{"█" * prog:<{bar_width}}|'
        perc = prog * 100 // bar_width
        info = f'{perc:>3}%{bar} {i:>{ilen}}/{length}'
        finfo = f' [{ftime}<{teta}, {speed:7.2f}it/s]'

        print(f"\r{info} {finfo}", end='', flush=True)
        yield item


def main():
    try:
        assert len(sys.argv) != 2, 'format: ft_tqdm [range]'
        for _ in ft_tqdm(range(sys.argv[1])):
            pass
    except AssertionError as e:
        print('AssertionError:', e)


if __name__ == "__main__":
    main

