"""Settings for 06-codimensional-chain-net.glb, converted from the Rigid IPC fixture
06-codimensional-chain-net.json.

Run from ipc-toolkit/python/examples:
    python rigid.py <this directory>/06-codimensional-chain-net.glb <this directory>/06-codimensional-chain-net.py

Fixture fields with no simulator equivalent (ignored): coefficient_restitution.
"""

import numpy as np

dt = 0.01
convert_planes = True

# Per-DOF fixed flags [x, y, z, rx, ry, rz], read while loading the glTF
# (they cannot change afterwards).
is_dof_fixed = {
    **dict.fromkeys([
        'link',
        'link.2',
        'link.5',
        'link.7',
        'link.9',
        'link.11',
        'link.13',
        'link.15',
        'link.17',
        'link.19',
        'link.21',
        'link.23',
        'link.25',
        'link.27',
        'link.29',
        'link.73',
        'link.74',
        'link.118',
        'link.119',
        'link.163',
        'link.164',
        'link.208',
        'link.209',
        'link.253',
        'link.254',
        'link.298',
        'link.299',
        'link.343',
        'link.344',
        'link.388',
        'link.389',
        'link.433',
        'link.434',
        'link.478',
        'link.479',
        'link.523',
        'link.524',
        'link.568',
        'link.569',
        'link.613',
        'link.614',
        'link.658',
        'link.659',
        'link.660',
        'link.661',
        'link.662',
        'link.663',
        'link.664',
        'link.665',
        'link.666',
        'link.667',
        'link.668',
        'link.669',
        'link.670',
        'link.671',
        'link.672',
    ], [True, True, True, True, True, True]),
}


def configure(scene):
    s = scene.settings
    s.gravity = np.array([0.0, -9.81, 0.0])
    s.velocity_conv_tol = 0.001

    # Match Rigid IPC's Newton solver: a 3000-iteration budget, and accept
    # the last feasible iterate rather than aborting on non-convergence.
    # solver_params returns a copy, so we assign the whole dict back.
    solver_params = s.solver_params
    solver_params["max_iterations"] = 3000
    s.solver_params = solver_params
    s.abort_on_convergence_failure = False

    for name in scene.names:
        scene.body(name).density = 7680.0
