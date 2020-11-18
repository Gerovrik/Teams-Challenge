{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#put imports here\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import scipy.stats as st\n",
    "import os as _dir\n",
    "%matplotlib inline\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "working_dir = _dir.getcwd()\n",
    "csv_path = \"top10s.csv\"\n",
    "for root, dirs, files in _dir.walk(working_dir):\n",
    "    if csv_path in files:\n",
    "        csv_path = (_dir.path.join(root, csv_path))\n",
    "        \n",
    "song_df=pd.read_csv(csv_path,encoding=\"ISO-8859-1\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "song_df.drop(song_df.columns[song_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>artist</th>\n",
       "      <th>top genre</th>\n",
       "      <th>year</th>\n",
       "      <th>bpm</th>\n",
       "      <th>nrgy</th>\n",
       "      <th>dnce</th>\n",
       "      <th>dB</th>\n",
       "      <th>live</th>\n",
       "      <th>val</th>\n",
       "      <th>dur</th>\n",
       "      <th>acous</th>\n",
       "      <th>spch</th>\n",
       "      <th>pop</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hey, Soul Sister</td>\n",
       "      <td>Train</td>\n",
       "      <td>neo mellow</td>\n",
       "      <td>2010</td>\n",
       "      <td>97</td>\n",
       "      <td>89</td>\n",
       "      <td>67</td>\n",
       "      <td>-4</td>\n",
       "      <td>8</td>\n",
       "      <td>80</td>\n",
       "      <td>217</td>\n",
       "      <td>19</td>\n",
       "      <td>4</td>\n",
       "      <td>83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Love The Way You Lie</td>\n",
       "      <td>Eminem</td>\n",
       "      <td>detroit hip hop</td>\n",
       "      <td>2010</td>\n",
       "      <td>87</td>\n",
       "      <td>93</td>\n",
       "      <td>75</td>\n",
       "      <td>-5</td>\n",
       "      <td>52</td>\n",
       "      <td>64</td>\n",
       "      <td>263</td>\n",
       "      <td>24</td>\n",
       "      <td>23</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>TiK ToK</td>\n",
       "      <td>Kesha</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2010</td>\n",
       "      <td>120</td>\n",
       "      <td>84</td>\n",
       "      <td>76</td>\n",
       "      <td>-3</td>\n",
       "      <td>29</td>\n",
       "      <td>71</td>\n",
       "      <td>200</td>\n",
       "      <td>10</td>\n",
       "      <td>14</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bad Romance</td>\n",
       "      <td>Lady Gaga</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2010</td>\n",
       "      <td>119</td>\n",
       "      <td>92</td>\n",
       "      <td>70</td>\n",
       "      <td>-4</td>\n",
       "      <td>8</td>\n",
       "      <td>71</td>\n",
       "      <td>295</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Just the Way You Are</td>\n",
       "      <td>Bruno Mars</td>\n",
       "      <td>pop</td>\n",
       "      <td>2010</td>\n",
       "      <td>109</td>\n",
       "      <td>84</td>\n",
       "      <td>64</td>\n",
       "      <td>-5</td>\n",
       "      <td>9</td>\n",
       "      <td>43</td>\n",
       "      <td>221</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  title      artist        top genre  year  bpm  nrgy  dnce  \\\n",
       "0      Hey, Soul Sister       Train       neo mellow  2010   97    89    67   \n",
       "1  Love The Way You Lie      Eminem  detroit hip hop  2010   87    93    75   \n",
       "2               TiK ToK       Kesha        dance pop  2010  120    84    76   \n",
       "3           Bad Romance   Lady Gaga        dance pop  2010  119    92    70   \n",
       "4  Just the Way You Are  Bruno Mars              pop  2010  109    84    64   \n",
       "\n",
       "   dB  live  val  dur  acous  spch  pop  \n",
       "0  -4     8   80  217     19     4   83  \n",
       "1  -5    52   64  263     24    23   82  \n",
       "2  -3    29   71  200     10    14   80  \n",
       "3  -4     8   71  295      0     4   79  \n",
       "4  -5     9   43  221      2     4   78  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "song_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The r-value is:0.126\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "(slope, intercept, rvalue, pvalue, stderr)=st.linregress(bpm,eng)\n",
    "regress_values=bpm * slope + intercept\n",
    "\n",
    "plt.xlabel(\"BPM Rating\")\n",
    "plt.ylabel(\"Energy Rating\")\n",
    "line_eq=\"y=\"+ str(round(slope,2)) + \"x +\" +str(round(intercept,2))\n",
    "plt.scatter(bpm,eng, marker=\"o\", facecolors=\"blue\", edgecolors=\"black\")\n",
    "plt.plot(bpm,regress_values,\"r-\")\n",
    "plt.annotate(line_eq,(10,10),fontsize=15,color=\"red\")\n",
    "print(f'The r-value is:{round(rvalue,3)}')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### No correlation between the Beats per minute and energy rating\n",
    "   No correlation when compared as a whole. Not group by year"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [],
   "source": [
    "pop=song_df['pop']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The r-value is:0.019\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "(slope, intercept, rvalue, pvalue, stderr)=st.linregress(bpm,pop)\n",
    "regress_values=bpm * slope + intercept\n",
    "\n",
    "plt.xlabel(\"BPM Rating\")\n",
    "plt.ylabel(\"POP Rating\")\n",
    "line_eq=\"y=\"+ str(round(slope,2)) + \"x +\" +str(round(intercept,2))\n",
    "plt.scatter(bpm,eng, marker=\"o\", facecolors=\"blue\", edgecolors=\"black\")\n",
    "plt.plot(bpm,regress_values,\"r-\")\n",
    "plt.annotate(line_eq,(10,10),fontsize=15,color=\"red\")\n",
    "print(f'The r-value is:{round(rvalue,3)}')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The r-value is:-0.058\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "(slope, intercept, rvalue, pvalue, stderr)=st.linregress(eng,pop)\n",
    "regress_values=bpm * slope + intercept\n",
    "\n",
    "plt.xlabel(\"Energy Rating\")\n",
    "plt.ylabel(\"POP Rating\")\n",
    "line_eq=\"y=\"+ str(round(slope,2)) + \"x +\" +str(round(intercept,2))\n",
    "plt.scatter(bpm,eng, marker=\"o\", facecolors=\"blue\", edgecolors=\"black\")\n",
    "plt.plot(bpm,regress_values,\"r-\")\n",
    "plt.annotate(line_eq,(10,10),fontsize=15,color=\"red\")\n",
    "print(f'The r-value is:{round(rvalue,3)}')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Scatter plots show no significant correaltion between groups \n",
    "Data maybe too broad so group by year to find any correalation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "years_df=song_df.groupby(['year'])\n",
    "#years_df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create box and whisker to see how spread out the data is "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bpm_stats=years_df['bpm'].describe()\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.set_title('Box and Whisker ')\n",
    "\n",
    "ax1.set_ylabel('BPM by Year')\n",
    "ax1.boxplot(bpm_stats)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "eng_stats=years_df['nrgy'].describe()\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.set_title('Box and Whisker ')\n",
    "\n",
    "ax1.set_ylabel('Energy Rating by Year')\n",
    "ax1.boxplot(eng_stats)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEICAYAAACwDehOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAc5klEQVR4nO3df7QU9Znn8fcH/EFQEVBwiIrgxpMgbIx6xziBOCKZGU00uhnN6oyRIBl0V4mJZjMok0WTYY45mh/GMTtBMeIk4DBqVidxHV1ADZsV96Imam48GhXFoJCIgjEK6LN/VN2muXb3LbjdVXVvf17n1Onuqu76PvfevvXU90d9SxGBmZkZwKCiAzAzs/JwUjAzswonBTMzq3BSMDOzCicFMzOrcFIwM7MKJwWzPpD0WUkrm7Sv4yWtbbD9nyR9JcN+npP0sWbEZO3HScFKIz2Y/UHS65I2SvqJpIOLjmtXSfp3SV+uen2gpKiz7o96219EnB8RX2tVvGbgpGDlc0pE7A2MAV4Gri04nr54APjTqtfHAb+qse6piHgpz8B6I2m3omOwYjgpWClFxJvArcDh3esk7SvpZkkbJK2R9HeSBkkaKWmtpFPS9+0t6WlJ59Tat6QZkrokbZb0jKTzqrYdn+7rEknrJa2TNKNq+36S7pS0SdJDwH9o8GM8AEyW1P1/9lHg20BHj3UP9IivXtk3Sfr79Pn+kn4s6VVJr0j6adU+q/f1AUnPSjozfX2ypEfTz/1M0ger3vucpL+V9Avg904M7clJwUpJ0lDgPwMPVq2+FtgXOJTkbPscYEZEvAKcC1wvaTTwLeDRiLi5zu7XAycDw4AZwLckHVW1/Y/Scg4EZgLXSRqRbrsOeJOkJnNuutTzELAncET6+jjgXuDpHuuqk0KjsqtdAqwFRgEHAJcBO8xZk/5M9wCzI+KW9PWNwHnAfsD3gDsl7Vn1sbOATwDDI2Jbg5/NBignBSub/ynpVWAT8GfAVQCSBpMkiUsjYnNEPAd8A/gMQETcA/wrsIzkoHbeu3ediIifRMSvI3E/yYHzo1Vv2Qp8NSK2RsRdwOvA+9MY/hL47xHx+4h4HFjUoJy3gFXAcZJGkhxonwF+WrXucOD+3squsfutJInpkPS9P40dJzL7KHAnMD0ifpyu+xvgexGxKiLejohFwFvAsVWf+05EvBARf6j3c9nA5qRgZXNaRAwnOcO+ELg/7YTdH9gDWFP13jUkZ9TdFgCTgO9HxO/qFSDpJEkPps0urwIfT/ff7Xc9zpLfAPYmOSvfDXihRwyNPEBSG/go0D1KaWXVuhcionof9cru6SqSGsc9aRPYnB7bzwd+FhErqtYdAlySNh29mv7sBwPvrXpP9c9mbchJwUopPZO9HXgbmAL8luTs+JCqt40FXoRKTeJ7wM3Af5H0vlr7TZtKbgOuBg5IE9BdgDKEtQHYRnIgrY6hkQdIDv7HkdQQAP4PMJl3Nx1lltaWLomIQ4FTgIslTat6y/nAWEnfqlr3AjA/IoZXLUMjYkn1rnclHhs4nBSslJQ4FRgBdEXE28BSYL6kfSQdAlwM/CD9yGXp47kkB/yb00TR0x4ktZANwDZJJwF/niWmNIbbgcslDZV0ODC9l4/9DBgOnE2aFCJiY1r+2exiUkg7jN8nSSRNbW+nS7fNwIkkzVRXpuuuB86X9OH097uXpE9I2mdXYrCByUnByubfJL1OcqCbT9Im/kS6bTbwe+AZkiaYxcCNko4mSRDnpAfur5Oc8fZsUiEiNgOfJ0kwG4G/Iml7z+pCkuacl4CbgO83enNEvAGsJklEj1dt+ikwml1MCsBhwP8m6XP4v8B3I+K+HmW/StIvc5Kkr0VEJ0m/wj+S/OxPA5/dxfJtgJJvsmNmZt1cUzAzswonBTMzq3BSMDOzCicFMzOr6Ndzm+y///4xbty4osMwM+tXVq9e/duIGFVrW79OCuPGjaOzs7PoMMzM+hVJda/Ed/ORmZlVOCmYmVmFk4KZmVW0LClIujG9UcjjVetGSrpX0lPp44iqbZemN0Z5UtJftCouMzOrr5U1hZtIJuSqNgdYFhGHkcx7PwcgnVjsTGBi+pnv1pnMzMzMWqhlSSEiHgBe6bH6VLbflGQRcFrV+lsi4q2IeJZkoq5jWhWbmZnVlnefwgERsQ4gfRydrj+QHW/usZYdb55SIWmWpE5JnRs2bGhpsGZm7aYsHc21bnBSc/rWiFgQER0R0TFqVM1rL8zMbBflnRReljQGIH1cn65fy453szoI+E3OsZmZlY6kTEuz5J0U7mT7naqmA3dUrT9T0p6SxpPcQOShnGMzMyudiNhhqbWumffFadk0F5KWAMcD+0taC8wDrgSWSpoJPA+cARART0haCvyS5B64F6R30DIzsxy1LClExFl1Nk2rtTIi5pPcftHMzApSlo5mMzMrAScFMzOrcFIwM7MKJwUzM6vo1zfZMRtIso41b+bwQ7OenBTMSqLnwV6SE4Dlzs1HZmZW4aRgZmYVTgpmZlbhpGBmZhVOCmZmVuGkYGZmFU4KZmZW4aRgZmYVTgpmZlbhpGBmZhVOCmZmVuGkYGZmFZ4QzwrlmUHNysVJwQpV62Dv2UHNiuOkYGal4xpkcZwUzKx0fG+J4rij2YzkoNPbYu2niO/FyJEjey2vt5hGjhy5y+W7pmCGz0yttiK+Fxs3buxzGX1JVq4pmJlZhZOCmZlVuPnIzHaQpenBTWsDl5OCme3A/Svtre2Sgs+CzMzqa7uk4LMgM7P62i4pmJmVWcwbBpfv2/d97KJCkoKkLwKfAwJ4DJgBDAX+BRgHPAd8OiI2FhGfmVlRdMWmplynEJfv2mdzH5Iq6UDg80BHREwCBgNnAnOAZRFxGLAsfT0gZblK0lfQmlkRirpOYTfgPZJ2I6kh/AY4FViUbl8EnFZQbC0XEe9aaq03M8tb7kkhIl4ErgaeB9YBr0XEPcABEbEufc86YHStz0uaJalTUueGDRvyCntAcm3FzHoqovloBEmtYDzwXmAvSWdn/XxELIiIjojoGDVqVKvCbAuurZhZT0U0H30MeDYiNkTEVuB24CPAy5LGAKSP6wuIzcysrRWRFJ4HjpU0VEn7xDSgC7gTmJ6+ZzpwRwGxmZm1tdyHpEbEKkm3Ag8D24BHgAXA3sBSSTNJEscZecdm1o5GjhzJxo2NR3836l8aMWIEr7zySrPDsoIUcp1CRMwD5vVY/RZJrcHMctTX+fs9IGFg8dTZZgUp+g5bZrV4mguzghR9hy2zWlxTMDNL9bX2NhBqbq4pmJml3L/imoKZmVVxUjAzswonBTMzq3BSMDOzCieFNuKRFWbWG48+aiMeWWFl1depNsDTbTSLk4KZFc4X8pWHm48sV701YbkZy6xYDWsKkgYBp0fE0pzisQHOZ4Rm5dawphAR7wAX5hSLmZkVLEvz0b2SviTpYEkju5eWR2ZmZrnL0tF8bvp4QdW6AA5tfjhmZsWJecPg8n379vl+rtekEBHj8wjEzKxoumJTn4dtx+XNi6cImYakSpoEHA4M6V4XETe3KigzMytGr0lB0jzgeJKkcBdwErAScFIwMxtgsnQ0n05y7+SXImIGcASwZ0ujGmA8Nt/M+osszUd/iIh3JG2TNAxYTz/qZO7r5fPNuHTeY/PLpwzfC9uurx28lX1Yn2VJCp2ShgPXA6uB14GHWhpVE3m+n+08smI7fy+2K8P3oq8dvDAwOnnLQDvzh5A0DhgWEb9oVUA7o6OjIzo7Oxu+R1LfRxM048s6APZRhhjKso9mxNDXM+Pt+3mtTx8vw+9ioOyjDDFk2Yek1RHRUWtblo5mAX8NHBoRX5U0VtIxEdFvagtWHm4m2M5nx1ZGWZqPvgu8A5wAfBXYDNwG/HEL47IBygdCs3LLkhQ+HBFHSXoEICI2StqjxXGZmVkBsgxJ3SppMMnUFkgaRVJzMDOzAaZuUpB0SPr0O8CPgNGS5pNcuPYPOcRmZmY5a9R8tEzSDcDVJENRpwECTouIrjyCMzOzfDVqPjoSOIAkIYyOiOsi4h+dEMzMBq66NYWI2Ax8UdLRJLWGtSR9CUo2xwdzitHMzHLS2+04TwCuAW4ArqNJHczpFdI3AJNIOrDPBZ4E/gUYBzwHfDoiGs9DkEEZrtY0M+sv6iYFSbcABwJ/FRGPNbnca4C7I+L0dHjrUOAyYFlEXClpDjAH+Nu+FuT50c3MsmvY0RwR1ze7wHRSveOAzwJExBZgi6RTSaboBlgE3EcTkoJZLa5BmtW2U3MfNaVA6UPAAuCXJNNwrwYuAl6MiOFV79sYESNqfH4WMAtg7NixR69Zs6a38gqfy8Rz3Ay8fZQhhrLsowwxlGUfZYghyz4azX1URFLoAB4EJkfEKknXAJuA2VmSQjVPiJfvPsoQQ1n2UYYYyrKPMsRQln2UIYYs+2iUFLJc0dxsa4G1EbEqfX0rcBTwsqQxAOnj+gJiM7M219sNsRotI0Y0PI/tF3pNCpI6JV0gqSk/bUS8BLwg6f3pqmkkTUl3AtPTddOBO5pRnplZVhHRcOntPQPhxktZJsQ7E5gB/D9JncD3gXuib/Wb2cAP05FHz6T7HwQslTQTeB44ow/7NzPrt/p6E6e+1Fh6TQoR8TQwV9JXgJOBG4F3JN0IXBMRO50aI+JRoFZ71rSd3ZeZ2UDS2/l2Uwa/NJCpT0HSB4FvAFeR3EvhdJLO4eUti8zMzHKX5c5rq4FXgYXAnIh4K920StLkVgZnZu2jyCYT2y5Ln8IZEfFMrQ0R8akmx2NmbajoJhPbLkvz0WuSviPpYUmrJV0jab+WR2ZmZrnLkhRuATYAf0nSl7CBZOI6MzMbYLI0H42MiK9Vvf57Sae1KiAzMytOlprCCklnShqULp8GftLqwMzMLH+Nps7eTHKvAwEXA/+cbhoMvA7Ma3l0ZmaWq0Z3Xtsnz0DMzKx4RUyIZ2ZmJeWkYGZmFU4KZmZWkWXq7KslTcwjGDMzK1aWmsKvgAWSVkk6X1KT7i1pZmZl02tSiIgbImIycA4wDviFpMWSprY6ODMzy1fWqbMHAx9Il98CPwculnRLC2MzM7OcZZk6+5vAKST3TviHiHgo3fR1SU+2MjgzM8tXlrmPHgf+LiLeqLHtmCbHY23A8+ablVeW5qO/7pkQJC0DiIjXWhKVDVi93Ri9XW6OblZWjeY+GgIMBfaXNIJkDiSAYcB7c4jNzMxy1qj56DzgCyQJ4OGq9ZuA61oZlJnlqy9Nem7OG1gaTYh3DXCNpNkRcW2OMZm1jTL0r/hWmFatUfPRCRGxHHhR0rvuxRwRt7c0MrMWK/rs2AdjK6NGzUd/SjIM9ZQa2wJwUrB+ywdks9oaNR/NkzQI+F8RsTTHmMzMrCANh6RGxDvAhTnFYmZmBctyncK9kr4k6WBJI7uXlkdmZlYwSTss9dYNJFmuaD43fbygal0AhzY/nIGrDKNMzGzntGO/Uq9JISLG5xHIQJbli+WOTTMrgyw1BSRNAg4HhnSvi4ibWxWUmZkVI8ssqfOA40mSwl3AScBKwEnBzGyAydLRfDowDXgpImYARwB79rVgSYMlPSLpx+nrkZLulfRU+ti0RvSeHUM7s7gt38zaSZak8Id0aOo2ScOA9TSnk/kioKvq9RxgWUQcBixLX/eZZ+Q063+yjPoZiCN/yiBLUuiUNBy4HlhNMjneQ40/0pikg4BPADdUrT4VWJQ+XwSc1pcyzKz/yjLFugdmtEaW0Uf/NX36T5LuBoZFxC/6WO63gS8D+1StOyAi1qVlrpM0utYHJc0CZgGMHTu2j2GYmVm1RhPiHdVoW0Q8XG97I5JOBtZHxGpJx+/s5yNiAbAAoKOjw6cKZmZN1Kim8I0G2wI4YRfLnAx8UtLHSYa4DpP0A+BlSWPSWsIYkr4LMzPLUaMJ8aa2osCIuBS4FCCtKXwpIs6WdBUwHbgyfbyjFeWbmVl9Wa5TOKfW+hZcvHYlsFTSTOB54Iwm79/MzHqR5YrmP656PoTkmoWHacLFaxFxH3Bf+vx36b7NzKwgWUYfza5+LWlf4J9bFpGZmRUmy3UKPb0BHNbsQMzMrHhZ+hT+jWS0EcBgYALgO7GZmQ1AWfoUrq56vg1YExFrWxSPmZkVqNfmo4i4H3gS2BcYSZIYzMxsAOo1KUj6HMlcR58imTH1QUnnNv6UmZn1R1maj/4bcGQ6ZBRJ+wE/A25sZWBmZpa/LKOP1gKbq15vBl5oTThmZlakLDWFF4FVku4gGYV0KvCQpIsBIuKbLYzPzMxylCUp/DpdunXPSbRPjfeamVk/luWK5isAJO2TvIzXWx6VmZkVIsvoo0mSHgEeB56QtFrSxNaHZmZmecvSfLQAuDgiVkBluuvrgY+0MC4zM4Oa96Kuta5ZtyfNkhT26k4IacH3SdqrKaWbmVlDed+LOktSeEbSV9g+M+rZwLOtC8laqdYZRlYjRoxoYiRmVkZZksK5wBXA7enrB4AZLYvIWqa3Mw5JuZ+VmFm51E0KkoYA5wPvAx4DLomIrXkFZmZm+Ws0+mgR0EGSEE4CrsolIjMzK0yj5qPDI+I/AkhaSDIpnllT1evj6LnezVpm+WiUFCpNRRGxrS8dlGb1+GBvVi6NksIRkjalzwW8J30tkiubh7U8OjMzy1XdpBARg/MMxMzMipdl6mwzM2sTTgpmZlbhpGBmZhVOCmZmVuGkYGZmFU4KZmZW4aRgZmYVTgpmZlbhpGBmZhW5JwVJB0taIalL0hOSLkrXj5R0r6Sn0kff0cXMLGdF1BS2kdybYQJwLHCBpMOBOcCyiDgMWJa+NjOzHOWeFCJiXUQ8nD7fDHQBBwKnktzDgfTxtLxjMzNrd4X2KUgaBxwJrAIOiIh1kCQOYHSdz8yS1Cmpc8OGDXmFambWFgpLCpL2Bm4DvhARm3p7f7eIWBARHRHRMWrUqNYFaGbWhgpJCpJ2J0kIP4yI29PVL0sak24fA6wvIjYzs3ZWxOgjAQuBroj4ZtWmO4Hp6fPpwB15x2Zm1u4a3XmtVSYDnwEek/Rouu4y4EpgqaSZwPPAGQXEZmbW1nJPChGxkuSWnrVMyzMWMzPbka9oNjOziiKaj8ysxJJuv8brIiKvcCxnTgoFqPVPV2u9//GsCP7etTcnhQL4n658fHZslnBSMMMHfLNu7mi20liyZAmTJk1i8ODBTJo0iSVLlhQdUq4k7bDUWlev6dGsWVxTsFJYsmQJc+fOZeHChUyZMoWVK1cyc+ZMAM4666yCo8uHaytWBq4pWCnMnz+fhQsXMnXqVHbffXemTp3KwoULmT9/ftGhmbUV9eezk46Ojujs7Nypz2Spfvfn30lfSCrsZx88eDBvvvkmu+++e2Xd1q1bGTJkCG+//XYhMZkNVJJWR0RHrW1tV1OIiF4Xy9+ECRNYuXLlDutWrlzJhAkTCorIyqDd+5mK0HZJwcpp7ty5zJw5kxUrVrB161ZWrFjBzJkzmTt3btGhWUG6+5muvfZa3nzzTa699lrmzp3rxNBqWc6cy7ocffTRYc2TfB2Ks3jx4pg4cWIMGjQoJk6cGIsXLy40HivWxIkTY/ny5TusW758eUycODH3WAbadxPojDrH1bbrU7D6iuxTMOupLP1M9UbGzZ8/v9+OjHOfgpn1O2XpZ2q3kXFOCmZWSmXpZ+rq6mLKlCk7rJsyZQpdXV25xpFXp7svXjOzUupumpk9ezZdXV1MmDChkCab7hrL1KlTK+vyrrHkenFnvc6G/rC4o7m5KLij2ayMFi9eHOPHj4/ly5fHli1bYvny5TF+/PhcO5ub3elOg47mwg/sfVkGQlIo06gGJwWz2or+Px00aFBs2bJlh3VbtmyJQYMG7dL+GiUFNx8VyPP9mPUPZ511VqH/k7k2YdXLFv1h6e81hTKNw45wTcGsrJrdhIWvUyinsozD7ubrFMzKa8mSJcyfP7/S6T537txdrr00uk7BzUcFKsOoBjPrH/JqwvJ1CgUqyzhsM7NurikUqCzjsM3MurlPwSrcp2DWHjz3kZmZZeKkYGZmFU4KZmZW4aRgZmYVTgpmZlbhpGBmZhWlSwqSTpT0pKSnJc1pVTl53bDC+pcyfC/KEEOZ4rCc1ZsUqYgFGAz8GjgU2AP4OXB4vffv6oR4ZZgfvYxo8wnxyvC9KEMMZYrDWoP+cj8F4E+Af696fSlwab3372pSKNvspGXR7kmhDN+LMsRQpjisNRolhVJd0SzpdODEiPhc+vozwIcj4sKq98wCZgGMHTv26DVr1ux0OWWbnbQoknp9T5m+H61Whu9FGWIoUxzWGv3piuZaR6kdjkoRsSAiOiKiY9SoUbtUSPfspNXacXbSemcKsWPtrW2U4XtRhhjKFIcVIMuBIa+FnJqP3F5qtZThe1GGGMoUh7UG/ahPYTfgGWA82zuaJ9Z7f1/uvFb0PVetnMrwvShDDGWKw5qvUVIoVZ8CgKSPA98mGYl0Y0TMr/dez5JqZrbz+tWd1yLiLuCuouMwM2tHZetoNjOzAjkpmJlZhZOCmZlVOCmYmVlF6UYf7QxJG4Cdv6R5R/sDv21COH1VhjjKEAOUIw7HsF0Z4ihDDFCOOJoRwyERUfPq336dFJpBUme9oVntFkcZYihLHI6hXHGUIYayxNHqGNx8ZGZmFU4KZmZW4aQAC4oOIFWGOMoQA5QjDsewXRniKEMMUI44WhpD2/cpmJnZdq4pmJlZhZOCmZlVtG1SkHSjpPWSHi8whoMlrZDUJekJSRcVFMcQSQ9J+nkaxxVFxJHGMljSI5J+XGAMz0l6TNKjkgqZhlfScEm3SvpV+v34kwJieH/6O+heNkn6QgFxfDH9Xj4uaYmkIQXEcFFa/hN5/g5qHackjZR0r6Sn0scRzSyzbZMCcBNwYsExbAMuiYgJwLHABZIOLyCOt4ATIuII4EPAiZKOLSAOgIuAroLKrjY1Ij5U4Jj0a4C7I+IDwBEU8DuJiCfT38GHgKOBN4Af5RmDpAOBzwMdETGJZEr9M3OOYRLwN8AxJH+LkyUdllPxN/Hu49QcYFlEHAYsS183TdsmhYh4AHil4BjWRcTD6fPNJP/4BxYQR0TE6+nL3dMl9xEIkg4CPgHckHfZZSJpGHAcsBAgIrZExKvFRsU04NcR0dcZBHbFbsB7JO0GDAV+k3P5E4AHI+KNiNgG3A/8pzwKrnOcOhVYlD5fBJzWzDLbNimUjaRxwJHAqoLKHyzpUWA9cG9EFBHHt4EvA+8UUHa1AO6RtFrSrALKPxTYAHw/bUq7QdJeBcRR7UxgSd6FRsSLwNXA88A64LWIuCfnMB4HjpO0n6ShwMeBg3OOodoBEbEOkhNLYHQzd+6kUAKS9gZuA74QEZuKiCEi3k6bCQ4CjkmrzLmRdDKwPiJW51luHZMj4ijgJJImveNyLn834Cjgf0TEkcDvaXITwc6QtAfwSeBfCyh7BMmZ8XjgvcBeks7OM4aI6AK+DtwL3E1ym+BtecaQJyeFgknanSQh/DAibi86nrSZ4j7y72+ZDHxS0nPALcAJkn6QcwwARMRv0sf1JG3ox+QcwlpgbVVt7VaSJFGUk4CHI+LlAsr+GPBsRGyIiK3A7cBH8g4iIhZGxFERcRxJc85TecdQ5WVJYwDSx/XN3LmTQoEkiaTduCsivllgHKMkDU+fv4fkH/FXecYQEZdGxEERMY6kqWJ5ROR6RgggaS9J+3Q/B/6cpPkgNxHxEvCCpPenq6YBv8wzhh7OooCmo9TzwLGShqb/L9MooNNd0uj0cSzwKYr7fQDcCUxPn08H7mjmzkt3j+a8SFoCHA/sL2ktMC8iFuYcxmTgM8BjaXs+wGXpfarzNAZYJGkwyYnC0ogobEhowQ4AfpQcf9gNWBwRdxcQx2zgh2nTzTPAjAJiIG1D/zPgvCLKj4hVkm4FHiZpsnmEYqaauE3SfsBW4IKI2JhHobWOU8CVwFJJM0mS5hlNLdPTXJiZWTc3H5mZWYWTgpmZVTgpmJlZhZOCmZlVOCmYmVmFk4KZmVU4KZiZWcX/B10BvmnFxSeoAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pop=years_df['pop'].describe()\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.set_title('Box and Whisker ')\n",
    "\n",
    "ax1.set_ylabel('Popularity by Year')\n",
    "ax1.boxplot(pop)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "bpm_year=years_df['bpm'].mean()\n",
    "engy_year=years_df['nrgy'].mean()\n",
    "pop_year=years_df['pop'].mean()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Correlation of bpm and energy is 0.7232\n",
      "Correlation of bpm and popularity is -0.7136\n",
      "Correlation of energy and popularity is -0.5727\n"
     ]
    }
   ],
   "source": [
    "corr_bpm_engy=st.pearsonr(bpm_year,engy_year)\n",
    "print(f'Correlation of bpm and energy is {round(corr_bpm_engy[0],4)}')\n",
    "corr_bpm_pop=st.pearsonr(bpm_year,pop_year)\n",
    "print(f'Correlation of bpm and popularity is {round(corr_bpm_pop[0],4)}')\n",
    "corr_engy_pop=st.pearsonr(engy_year,pop_year)\n",
    "print(f'Correlation of energy and popularity is {round(corr_engy_pop[0],4)}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A correlation exist between BPM vs. Popularity, and BPM vs. Energy with a smaller sample size.\n",
    "Wanting to explore the relationship between BPM and Popularity\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "yearavg=pd.DataFrame({'BPM Avgs':bpm_year,'Energy Avgs':engy_year,'Popularity Avgs':pop_year})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "yearavg.boxplot()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### A box and whisker to see how far apart the values lie "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "#bpm_yearstats=years_df['bpm'].describe()\n",
    "#engy_yearstats=years_df['nrgy'].describe()\n",
    "#pop_yearstats=years_df['pop'].describe()\n",
    "bpm_yearstats=years_df['bpm']\n",
    "engy_yearstats=years_df['nrgy']\n",
    "pop_yearstats=years_df['pop']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The r-value is:-0.714\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "(slope, intercept, rvalue, pvalue, stderr)=st.linregress(bpm_year,pop_year)\n",
    "regress_values=bpm_year * slope + intercept\n",
    "\n",
    "plt.xlabel(\"BPM\")\n",
    "plt.ylabel(\"POP Rating\")\n",
    "line_eq=\"y=\"+ str(round(slope,2)) + \"x +\" +str(round(intercept,2))\n",
    "plt.scatter(bpm_year,pop_year, marker=\"o\", facecolors=\"blue\", edgecolors=\"black\")\n",
    "plt.plot(bpm_year,regress_values,\"r-\")\n",
    "plt.annotate(line_eq,(114,80),fontsize=15,color=\"red\")\n",
    "print(f'The r-value is:{round(rvalue,3)}')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The difference between graphs are the switching the x and y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The r-value is:-0.714\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "(slope, intercept, rvalue, pvalue, stderr)=st.linregress(pop_year,bpm_year)\n",
    "regress_values=pop_year * slope + intercept\n",
    "\n",
    "plt.xlabel(\"Popularity Rating\")\n",
    "plt.ylabel(\"Beats per minute\")\n",
    "line_eq=\"y=\"+ str(round(slope,2)) + \"x +\" +str(round(intercept,2))\n",
    "plt.scatter(pop_year,bpm_year, marker=\"o\", facecolors=\"blue\", edgecolors=\"black\")\n",
    "plt.plot(pop_year,regress_values,\"r-\")\n",
    "plt.annotate(line_eq,(70,120),fontsize=15,color=\"red\")\n",
    "print(f'The r-value is:{round(rvalue,3)}')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16.918977604620448"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crit_val=st.chi2.ppf(q=0.95, df=9)\n",
    "crit_val"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Power_divergenceResult(statistic=224.76939709489903, pvalue=2.0767822775428557e-43)"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.chisquare(pop_year,bpm_year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "#artist=song_df.groupby(['artist'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>artist</th>\n",
       "      <th>top genre</th>\n",
       "      <th>year</th>\n",
       "      <th>bpm</th>\n",
       "      <th>nrgy</th>\n",
       "      <th>dnce</th>\n",
       "      <th>dB</th>\n",
       "      <th>live</th>\n",
       "      <th>val</th>\n",
       "      <th>dur</th>\n",
       "      <th>acous</th>\n",
       "      <th>spch</th>\n",
       "      <th>pop</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Hey, Soul Sister</td>\n",
       "      <td>Train</td>\n",
       "      <td>neo mellow</td>\n",
       "      <td>2010</td>\n",
       "      <td>97</td>\n",
       "      <td>89</td>\n",
       "      <td>67</td>\n",
       "      <td>-4</td>\n",
       "      <td>8</td>\n",
       "      <td>80</td>\n",
       "      <td>217</td>\n",
       "      <td>19</td>\n",
       "      <td>4</td>\n",
       "      <td>83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Love The Way You Lie</td>\n",
       "      <td>Eminem</td>\n",
       "      <td>detroit hip hop</td>\n",
       "      <td>2010</td>\n",
       "      <td>87</td>\n",
       "      <td>93</td>\n",
       "      <td>75</td>\n",
       "      <td>-5</td>\n",
       "      <td>52</td>\n",
       "      <td>64</td>\n",
       "      <td>263</td>\n",
       "      <td>24</td>\n",
       "      <td>23</td>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>TiK ToK</td>\n",
       "      <td>Kesha</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2010</td>\n",
       "      <td>120</td>\n",
       "      <td>84</td>\n",
       "      <td>76</td>\n",
       "      <td>-3</td>\n",
       "      <td>29</td>\n",
       "      <td>71</td>\n",
       "      <td>200</td>\n",
       "      <td>10</td>\n",
       "      <td>14</td>\n",
       "      <td>80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bad Romance</td>\n",
       "      <td>Lady Gaga</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2010</td>\n",
       "      <td>119</td>\n",
       "      <td>92</td>\n",
       "      <td>70</td>\n",
       "      <td>-4</td>\n",
       "      <td>8</td>\n",
       "      <td>71</td>\n",
       "      <td>295</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Just the Way You Are</td>\n",
       "      <td>Bruno Mars</td>\n",
       "      <td>pop</td>\n",
       "      <td>2010</td>\n",
       "      <td>109</td>\n",
       "      <td>84</td>\n",
       "      <td>64</td>\n",
       "      <td>-5</td>\n",
       "      <td>9</td>\n",
       "      <td>43</td>\n",
       "      <td>221</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>598</th>\n",
       "      <td>Find U Again (feat. Camila Cabello)</td>\n",
       "      <td>Mark Ronson</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2019</td>\n",
       "      <td>104</td>\n",
       "      <td>66</td>\n",
       "      <td>61</td>\n",
       "      <td>-7</td>\n",
       "      <td>20</td>\n",
       "      <td>16</td>\n",
       "      <td>176</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>599</th>\n",
       "      <td>Cross Me (feat. Chance the Rapper &amp; PnB Rock)</td>\n",
       "      <td>Ed Sheeran</td>\n",
       "      <td>pop</td>\n",
       "      <td>2019</td>\n",
       "      <td>95</td>\n",
       "      <td>79</td>\n",
       "      <td>75</td>\n",
       "      <td>-6</td>\n",
       "      <td>7</td>\n",
       "      <td>61</td>\n",
       "      <td>206</td>\n",
       "      <td>21</td>\n",
       "      <td>12</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>600</th>\n",
       "      <td>No Brainer (feat. Justin Bieber, Chance the Ra...</td>\n",
       "      <td>DJ Khaled</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2019</td>\n",
       "      <td>136</td>\n",
       "      <td>76</td>\n",
       "      <td>53</td>\n",
       "      <td>-5</td>\n",
       "      <td>9</td>\n",
       "      <td>65</td>\n",
       "      <td>260</td>\n",
       "      <td>7</td>\n",
       "      <td>34</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>601</th>\n",
       "      <td>Nothing Breaks Like a Heart (feat. Miley Cyrus)</td>\n",
       "      <td>Mark Ronson</td>\n",
       "      <td>dance pop</td>\n",
       "      <td>2019</td>\n",
       "      <td>114</td>\n",
       "      <td>79</td>\n",
       "      <td>60</td>\n",
       "      <td>-6</td>\n",
       "      <td>42</td>\n",
       "      <td>24</td>\n",
       "      <td>217</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>602</th>\n",
       "      <td>Kills You Slowly</td>\n",
       "      <td>The Chainsmokers</td>\n",
       "      <td>electropop</td>\n",
       "      <td>2019</td>\n",
       "      <td>150</td>\n",
       "      <td>44</td>\n",
       "      <td>70</td>\n",
       "      <td>-9</td>\n",
       "      <td>13</td>\n",
       "      <td>23</td>\n",
       "      <td>213</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>67</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>603 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                 title            artist  \\\n",
       "0                                     Hey, Soul Sister             Train   \n",
       "1                                 Love The Way You Lie            Eminem   \n",
       "2                                              TiK ToK             Kesha   \n",
       "3                                          Bad Romance         Lady Gaga   \n",
       "4                                 Just the Way You Are        Bruno Mars   \n",
       "..                                                 ...               ...   \n",
       "598                Find U Again (feat. Camila Cabello)       Mark Ronson   \n",
       "599      Cross Me (feat. Chance the Rapper & PnB Rock)        Ed Sheeran   \n",
       "600  No Brainer (feat. Justin Bieber, Chance the Ra...         DJ Khaled   \n",
       "601    Nothing Breaks Like a Heart (feat. Miley Cyrus)       Mark Ronson   \n",
       "602                                   Kills You Slowly  The Chainsmokers   \n",
       "\n",
       "           top genre  year  bpm  nrgy  dnce  dB  live  val  dur  acous  spch  \\\n",
       "0         neo mellow  2010   97    89    67  -4     8   80  217     19     4   \n",
       "1    detroit hip hop  2010   87    93    75  -5    52   64  263     24    23   \n",
       "2          dance pop  2010  120    84    76  -3    29   71  200     10    14   \n",
       "3          dance pop  2010  119    92    70  -4     8   71  295      0     4   \n",
       "4                pop  2010  109    84    64  -5     9   43  221      2     4   \n",
       "..               ...   ...  ...   ...   ...  ..   ...  ...  ...    ...   ...   \n",
       "598        dance pop  2019  104    66    61  -7    20   16  176      1     3   \n",
       "599              pop  2019   95    79    75  -6     7   61  206     21    12   \n",
       "600        dance pop  2019  136    76    53  -5     9   65  260      7    34   \n",
       "601        dance pop  2019  114    79    60  -6    42   24  217      1     7   \n",
       "602       electropop  2019  150    44    70  -9    13   23  213      6     6   \n",
       "\n",
       "     pop  \n",
       "0     83  \n",
       "1     82  \n",
       "2     80  \n",
       "3     79  \n",
       "4     78  \n",
       "..   ...  \n",
       "598   75  \n",
       "599   75  \n",
       "600   70  \n",
       "601   69  \n",
       "602   67  \n",
       "\n",
       "[603 rows x 14 columns]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#artist.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Katy Perry        17\n",
       "Justin Bieber     16\n",
       "Maroon 5          15\n",
       "Rihanna           15\n",
       "Lady Gaga         14\n",
       "                  ..\n",
       "Martin Solveig     1\n",
       "will.i.am          1\n",
       "Galantis           1\n",
       "Ne-Yo              1\n",
       "Lewis Capaldi      1\n",
       "Name: artist, Length: 184, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#song_df['artist'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Avgs    96.0\n",
       "Name: Lewis Capaldi, dtype: float64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#artistmean=artist['pop'].mean()\n",
    "#meansum=pd.DataFrame({\"Avgs\":artistmean})\n",
    "#pd.set_option(\"display.max_rows\", None, \"display.max_columns\", None)\n",
    "#meansum.loc[meansum['Avgs'].idxmax()]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
