import time

sec = time.time()
sec = time.time()
strt = time.strftime('%b %d %Y')
print('Second since January 1, 1970: ', end='')
print(f'{sec:,} or {sec:.2e} in scientific notation')
print(strt)
