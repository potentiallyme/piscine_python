import tqdm
import shutil
import time

def ft_tqdm(lst: range) -> None:
    start = time.time()
    length = len(lst)
    width = shutil.get_terminal_size().columns - 40
    for i, item in enumerate(lst, start=1):
        prog = int(i / length * width)
        ttime = time.time() - start
        speed = i / ttime
        eta = (length - i) / speed

        tm, ts = divmod(ttime, 60)
        em, es = divmod(eta, 60)
        ftime = f'{int(tm):02d}:{int(ts):02d}'
        teta = f'{int(em):02d}:{int(es):02d}'

        bar = f'|{">" * prog:<{width}}|'
        perc = prog * 100 // width
        info = f'{perc}%{bar} {i}/{length}'
        finfo = f'[{ftime}<{teta}, {speed:.2f}it/s]'

        print(f"\r{info} {finfo}", end='', flush=True)
        yield item


def main():
    for _ in ft_tqdm(range(333)):
        pass


if __name__ == "__main__":
    main
