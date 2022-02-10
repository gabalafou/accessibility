import nox
from pathlib import Path

# global variables
FILE = Path(__file__)
TEST_DIR = FILE.parent
ENV_FILE = TEST_DIR / "environment.yml"

# can be ran as: nox -s a11y_tests
@nox.session(venv_backend="mamba", reuse_venv=True)
def a11y_test(session):
    session._run(
        *[
            "conda",
            "env",
            "update",
            "--prefix",
            session.virtualenv.location,
            "--file",
            str(ENV_FILE),
        ],
        # conda options
        silent=True,
    )
    session.run("yarn", "install")
    session.run("yarn", "playwright", "install", "chromium")
    session.run("yarn", "run", "test")
