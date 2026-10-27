"""Settings for 09-anchor.glb, converted from the Rigid IPC fixture
09-anchor.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/09-anchor.glb <this directory>/09-anchor.py

Fixture fields with no simulator equivalent (ignored): coefficient_restitution.
"""

import numpy as np
from find_ipctk import ipctk

dt = 0.01
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys(['spool'], [True, True, True, False, True, True]),
}


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

    for name in scene.names:
        scene.body(name).density = 7680.0

    scene.body('spool').type = ipctk.RigidBody.Type.KINEMATIC

    scene.velocity('spool').rotation = np.array([-1.7453292519943295, 0.0, 0.0])
