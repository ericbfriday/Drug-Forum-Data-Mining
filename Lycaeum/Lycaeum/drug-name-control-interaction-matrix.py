import json 

import matplotlib.pyplot as plt 
import Graphics as artist 
import numpy as np 

from matplotlib import rcParams
from collections import Counter

rcParams['text.usetex'] = True

drug_names = json.load(open('lycaeum-forum-processed-has-drug-names.json','r'))
filtered_list = open('deduplicated-curated-drug-names').read().splitlines()


drug_names = [drug for item in drug_names.itervalues() for drug in item['drugs']]
interaction_name_frequencies = np.diag(np.load('interaction_matrix-2015-11-28-w-deduped-curated-drug-names.npy'))/2.
cutoff=200

drug_name_frequencies = Counter(drug_names)
name, frequency = zip(*drug_name_frequencies.most_common(cutoff))
idx = range(len(frequency))

#- Numerical comparison
for drug,f in zip(name,frequency):
	if drug in filtered_list:
		print '%s %d'%(drug,f-interaction_name_frequencies[filtered_list.index(drug)])
'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(idx,frequency, color='k')

artist.adjust_spines(ax)
ax.set_ylabel(artist.format('No. of mentions'))
ax.set_xticks(np.array(range(len(name)))+0.4)
ax.set_xticklabels(map(artist.format,name), rotation=90)

a = plt.axes([.65, .6, .2, .2])
_,full_frequencies = zip(*drug_name_frequencies.most_common())
a.hist(full_frequencies, color='k')
artist.adjust_spines(a)
a.set_xlabel(artist.format('No. of mentions'))
a.set_ylabel(artist.format('No. of substances'))
plt.yscale('log', nonposy='clip')
for label in a.get_xticklabels()[1::2]:
    label.set_visible(False)
plt.tight_layout()
plt.savefig('drug-name-control-frequency-lycaeum.png')
'''
