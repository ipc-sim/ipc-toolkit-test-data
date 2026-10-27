"""Settings for 5-cubes.glb, converted from the Rigid IPC fixture
5-cubes.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/5-cubes.glb <this directory>/5-cubes.py
"""

import numpy as np

dt = 0.01
convert_planes = True


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.8, 0.0])
    s.velocity_conv_tol = 1e-05

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False
