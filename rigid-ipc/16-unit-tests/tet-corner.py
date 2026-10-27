"""Settings for tet-corner.glb, converted from the Rigid IPC fixture
tet-corner.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/tet-corner.glb <this directory>/tet-corner.py

Fixture fields with no simulator equivalent (ignored): coefficient_restitution.
"""

import numpy as np

dt = 0.01
convert_planes = True


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.81, 0.0])
    s.dhat = 0.0001

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    for name in ['cube', 'cube.2', 'cube.3']:
        scene.body(name).convert_to_static()
