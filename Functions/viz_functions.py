# This file is going to have functions for the visualizations.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

from datetime import datetime

sns.set_theme()

plt.rcParams.update({
    "text.usetex": True#,
#    "font.family": "Helvetica"
})


def viz_lines(num_cntr_lines: int) -> None:
	range_kda = num_cntr_lines
	colors = cm.plasma.colors
	index_color = int(len(colors)/range_kda)
	color_line = 0
	
	# deaths
	d = [x for x in range(0,20)]

	_, ax = plt.subplots()

	for c in range(range_kda):    
		ka = [c*d for d in d]
		ax.plot(d, ka, label=r"$r_{KDA}$"+f"$=${c}", color=colors[color_line])
		color_line += index_color

		ax.set_xlabel("Deaths")
		ax.set_ylabel("Kills + Assists")
		ax.set_title("Kills+Assists vs Deaths from multiple KDA ratios")
		plt.legend();
	return None



