"""Settings for wedge-in-crack.glb, converted from the Rigid IPC fixture
wedge-in-crack.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/wedge-in-crack.glb <this directory>/wedge-in-crack.py

Fixture fields with no simulator equivalent (ignored): coefficient_restitution.
"""

import numpy as np
from find_ipctk import ipctk

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

    scene.body('crack').convert_to_static()

    scene.velocity('wedge').position = np.array([1.0, 0.0, 0.0])
    scene.body('wedge').external_force = ipctk.Pose(np.array([10.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]))
