"""Settings for 08-wrecking-ball.glb, converted from the Rigid IPC fixture
08-wrecking-ball.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/08-wrecking-ball.glb <this directory>/08-wrecking-ball.py

Fixture fields with no simulator equivalent (ignored): coefficient_restitution.
"""

import numpy as np

dt = 0.01
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys(['link'], [True, True, True, True, True, True]),
}


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.81, 0.0])

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    for name in [
        'link',
        'link.1',
        'link.2',
        'link.3',
        'link.4',
        'link.5',
        'link.6',
        'link.7',
        'link.8',
        'link.9',
        'link.10',
        'link.11',
        'link.12',
        'ball',
    ]:
        scene.body(name).density = 7680.0
