import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

lines = 29449  # 改为自己生成的train_log_loss.txt中的行数
result = pd.read_csv('train_log_loss.txt', error_bad_lines=False, names=['loss', 'avg', 'rate', 'seconds', 'images'])
result.head()

result['loss'] = result['loss'].str.split(' ').str.get(1)
result['avg'] = result['avg'].str.split(' ').str.get(1)
result['rate'] = result['rate'].str.split(' ').str.get(1)
result['seconds'] = result['seconds'].str.split(' ').str.get(1)
result['images'] = result['images'].str.split(' ').str.get(1)

result['loss'] = pd.to_numeric(result['loss'], errors='ignore')
result['avg'] = pd.to_numeric(result['avg'], errors='ignore')
result['rate'] = pd.to_numeric(result['rate'], errors='ignore')
result['seconds'] = pd.to_numeric(result['seconds'], errors='ignore')
result['images'] = pd.to_numeric(result['images'], errors='ignore')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result['loss'].values, label='avg_loss')
ax.legend(loc='best')
ax.set_title('The loss curves')
ax.set_xlabel('batches')
fig.savefig('avg_loss')
