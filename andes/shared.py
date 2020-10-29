"""
Shared constants and delayed imports.
"""

#
# Known issues of LazyImport ::
#
#     1) High overhead when called hundreds of thousands times.
#     For example, NumPy must not be imported with LazyImport.
#

from andes.utils.lazyimport import LazyImport

import math
import coloredlogs         # NOQA
import numpy as np         # NOQA
from numpy import ndarray  # NOQA
from tqdm import tqdm      # NOQA

try:
    import kvxopt       # NOQA
except ImportError:
    kvxopt = None

from cvxopt import spmatrix
if hasattr(spmatrix, 'ipadd'):
    IP_ADD = True
else:
    IP_ADD = False

if IP_ADD or (kvxopt is None):
    from cvxopt import umfpack                           # NOQA
    from cvxopt import spmatrix, matrix, sparse, spdiag  # NOQA
    from cvxopt import mul, div                          # NOQA
    from cvxopt.lapack import gesv                       # NOQA
    try:
        from cvxoptklu import klu  # NOQA
    except ImportError:
        klu = None
else:
    from kvxopt import umfpack, klu                      # NOQA
    from kvxopt import spmatrix, matrix, sparse, spdiag  # NOQA
    from kvxopt import mul, div                          # NOQA
    from kvxopt.lapack import gesv                       # NOQA


from andes.utils.texttable import Texttable          # NOQA
from andes.utils.paths import get_dot_andes_path     # NOQA

# --- constants ---

deg2rad = math.pi/180
jac_names = ('fx', 'fy', 'gx', 'gy')
jac_types = ('c', '')

jac_full_names = list()
for jname in jac_names:
    for jtype in jac_types:
        jac_full_names.append(jname + jtype)

# --- lazy import packages ---

pd = LazyImport('import pandas')
cupy = LazyImport('import cupy')
mpl = LazyImport('import matplotlib')
unittest = LazyImport('import unittest')
yaml = LazyImport('import yaml')

plt = LazyImport('from matplotlib import pyplot')
Pool = LazyImport('from pathos.multiprocessing import Pool')
Process = LazyImport('from multiprocess import Process')

newton_krylov = LazyImport('from scipy.optimize import newton_krylov')
fsolve = LazyImport('from scipy.optimize import fsolve')
solve_ivp = LazyImport('from scipy.integrate import solve_ivp')
odeint = LazyImport('from scipy.integrate import odeint')
