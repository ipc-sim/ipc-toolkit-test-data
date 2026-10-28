"""Settings for 13-turntable.glb, converted from the Rigid IPC fixture
13-turntable-mu=1.0.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/13-turntable.glb <this directory>/13-turntable-mu=1.0.py
"""

import numpy as np
from find_ipctk import ipctk

dt = 0.025
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys(['cylinder'], [True, True, True, True, False, True]),
}


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.8, 0.0])
    s.dhat = 0.001
    s.friction_coefficient = 1.0
    s.static_friction_speed_bound = 1e-05
    s.friction_iterations = -1
    s.velocity_conv_tol = 0.0001

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    scene.velocity('cylinder').rotation = np.array([0.0, 0.7853981633974483, 0.0])
    scene.body('cylinder').external_force = ipctk.Pose(np.array([0.0, 0.0, 0.0]), np.array([0.0, 1570.7963267948967, 0.0]))
