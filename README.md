# pyremote
## v0.0.1-beta.2 Release: May 14, 2022
See [CHANGELOG.md](CHANGELOG.md) for details

`pyremote` creates models using the *interest index* to determine which sports games are most worth watching in various sports. This project is a work-in-progress and does not promise any results. See [docs](docs) for a comprehensive list of functions and functionality. 

## Important Information

This project currently draws requested MLB game info from mlb.com and uses their most up-to-date information

## Installation
pyremote may be installed via the repo:
```bash
git clone https://github.com/mqandil/pyremote
cd pyremote
pip install -e .
```
or with pip: 
```bash
pip install git+https://github.com/mqandil/pyremote.git
```

This is the most up-to-date version of `pyremote`

## MLBLiveData
`MLBLiveData` determines the most interesting live baseball game using non-linear modeling and returns various information on live games

### Interest Index
Retreive a dataframe of live MLB games and their corresponding interest index values (sorted) with `get_interest_index_df()`. 
```python
>>> from pyremote import interest_index_scoring as iis
>>> mlblivedata = iis.MLBLiveData()
>>> interest_index_df = mlblivedata.get_interest_index_df()
>>> print(interest_index_df)
```

### Live Situations
Retreive a dataframe of live MLB games and relevant information with `get_live_situation_df()`.
```python
>>> from pyremote import interest_index_scoring as iis
>>> mlblivedata = iis.MLBLiveData()
>>> live_situation_df = mlblivedata.get_live_situation_df()
>>> print(live_situation_df)
```
### Interest Index Calculations
Retreive a dataframe of interest index values and variables with `get_ii_calculations()`.
```python
>>> from pyremote import interest_index_scoring as iis
>>> mlblivedata = iis.MLBLiveData()
>>> ii_calculations_df = mlblivedata.get_ii_calculations()
>>> print(ii_calculations_df)
```
