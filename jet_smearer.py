# Custom (hacky) jet pT smearer

import numpy as np
import scipy.stats

input_dir = 'data_files/1_unsmeared_lhco'
output_dir = 'data_files/2_smeared_lhco'

resolution = .25
resolution_str = '25'

input_files = ['background_ZZ_mumubb_unsmeared.lhco', 'signal_ZH_mumubb_unsmeared.lhco']
output_files = [f'background_ZZ_mumubb_smeared_{resolution_str}.lhco', f'signal_ZH_mumubb_smeared_{resolution_str}.lhco']
seeds = [1, 2]

for i in range(2):
	input_file = f'{input_dir}/{input_files[i]}'
	output_file = f'{output_dir}/{output_files[i]}'
	np.random.seed(seeds[i])
	
	with open(input_file) as fin:
		lines = fin.readlines()
	
	with open(output_file, 'w') as fout:
		for line in lines:
			split_line = line.split()
			if len(split_line) >= 6 and split_line[5] == '4.7':
				split_line[4] = str(float(split_line[4]) * scipy.stats.truncnorm.rvs(-1/resolution, np.inf, 1, resolution))
				to_write = split_line[0] + '     ' + '  '.join(split_line[1:]) + '\n'
				fout.write(to_write)
			else:
				fout.write(line)
