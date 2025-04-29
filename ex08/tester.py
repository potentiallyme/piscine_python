from tqdm import tqdm
from time import sleep
from Loading import ft_tqdm

for i in ft_tqdm(range(333)):
    sleep(0.005)
print()
for i in tqdm(range(333)):
    sleep(0.005)
print()
