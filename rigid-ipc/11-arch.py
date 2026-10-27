"""Settings for 11-arch.glb, converted from the Rigid IPC fixture
11-arch.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/11-arch.glb <this directory>/11-arch.py
"""

import numpy as np

dt = 0.01
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys(['plane'], [True, True, True, True, True, True]),
}


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.8, 0.0])
    s.dhat = 0.001
    s.friction_coefficient = 0.5
    s.static_friction_speed_bound = 0.001
    s.friction_iterations = 1
    s.velocity_conv_tol = 0.001

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False
