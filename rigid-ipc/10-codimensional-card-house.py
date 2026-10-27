"""Settings for 10-codimensional-card-house.glb, converted from the Rigid IPC fixture
10-codimensional-card-house.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/10-codimensional-card-house.glb <this directory>/10-codimensional-card-house.py
"""

import numpy as np

dt = 0.01
convert_planes = True


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.8, 0.0])
    s.dhat = 0.001
    s.friction_coefficient = 0.9
    s.static_friction_speed_bound = 1e-05
    s.friction_iterations = 1
    s.velocity_conv_tol = 0.001

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    for name in [
        'plane.1',
        'plane.2',
        'plane.3',
        'plane.4',
        'plane.5',
        'plane.6',
        'plane.7',
        'plane.8',
        'plane.9',
        'plane.10',
        'plane.11',
        'plane.12',
        'plane.13',
        'plane.14',
        'plane.15',
    ]:
        scene.body(name).density = 50.0
    for name in ['cube', 'cube.17']:
        scene.body(name).density = 7680.0
