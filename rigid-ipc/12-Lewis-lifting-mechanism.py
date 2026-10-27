"""Settings for 12-Lewis-lifting-mechanism.glb, converted from the Rigid IPC fixture
12-Lewis-lifting-mechanism.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/12-Lewis-lifting-mechanism.glb <this directory>/12-Lewis-lifting-mechanism.py
"""

import numpy as np
from find_ipctk import ipctk

dt = 0.01
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys(['center'], [False, False, False, True, True, True]),
}


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.8, 0.0])
    s.friction_coefficient = 0.3

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    scene.body('center').type = ipctk.RigidBody.Type.KINEMATIC

    scene.velocity('center').position = np.array([0.0, 0.5, 0.0])
    scene.drive('center', ipctk.demo.KinematicDriver.velocity_driven(4.0))
