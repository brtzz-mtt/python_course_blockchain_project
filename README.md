EvoCHAIN
========

[![MarkDown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/syntax/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)](https://www.json.org/json-en.html)
[![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://linuxfoundation.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)

Welcome to EvoCHAIN
===================

Main application runs a blockchain based gaming simulation after initialization through ./app/configuration.py (data-pool from ./app/simulation.py) with JavaScript-based AJAX calls to Flask's router, dynamically evolving it's status (see logic under ./pp/gaming.py) while file ./app/functions.py merely contains some helper functions.

Simulation adds automatically 60 + 6 nodes (with player as powered accounts) at application's start.

The 6 "super" nodes will compete for mining (as normal nodes) but simultaneously attacking (and being attacked by) other nodes, in order to steal their EVO tokens (initially 1 for players, null for normal nodes)

Logic and classes regarding blockchain-engine can be found under path ./app/modules:
- blockchain: main class, subcomponents (account, block, node and transaction) can be found under ./app/modules/_blockchain path)
- common: just a general class from which other can be extended (timestamped behavior, also to_json methods should find place here)
- contract: allowed operations on blockchain, including some methods for app's internal use
- logger: some simple logging for application's activity 
- player: extends blockchain's account component, adding some attributes and relative methods for gaming purposes
- utility: some general functions for generating hashes (MD5 and SHA256)

Press START button on top-right bar in order to begin the simulation (or to restart it after a pause..)

Script file at path ./cli.sh automatically runs tests specified in ./tst.py file, generates correspondent code-coverage (path ./htmlcov not includend in repository) and saves project-specific dependencies in ./req.txt running pipreqs

Requirements can be found in file ./req.txt, built automatically with [pipreqs](https://pypi.org/project/pipreqs/)

Copyright © 2021 Bertozzi Matteo (& Aurelian)
