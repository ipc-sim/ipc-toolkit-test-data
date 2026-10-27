"""Settings for spike-and-wedge.glb, converted from the Rigid IPC fixture
spike-and-wedge.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/spike-and-wedge.glb <this directory>/spike-and-wedge.py

Fixture fields with no simulator equivalent (ignored): coefficient_restitution.
"""

import numpy as np

dt = 0.01
convert_planes = True


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.8, 0.0])

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    scene.body('wedge').convert_to_static()
