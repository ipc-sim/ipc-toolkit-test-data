"""Settings for 02-bike-chain.glb, converted from the Rigid IPC fixture
02-bike-chain.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/02-bike-chain.glb <this directory>/02-bike-chain.py
"""

import numpy as np
from find_ipctk import ipctk

dt = 0.01
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys(['sprocket-20teeth', 'sprocket-8teeth'], [True, True, True, True, True, False]),
}


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.81, 0.0])
    s.dhat = 1e-05

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    scene.body('sprocket-20teeth').type = ipctk.RigidBody.Type.KINEMATIC

    scene.velocity('sprocket-20teeth').rotation = np.array([0.0, 0.0, -0.4363323129985824])
