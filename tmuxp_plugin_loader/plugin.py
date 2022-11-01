import os
import libtmux
from tmuxp.plugin import TmuxpPlugin
import datetime

Session = libtmux.session.Session
Window = libtmux.window.Window


class Loader(TmuxpPlugin):
    def __init__(self):
        config = {"tmuxp_min_version": "1.6.2"}
        TmuxpPlugin.__init__(self, plugin_name="tmuxp-plugin-loader", **config)

    def before_workspace_builder(self, session: Session):
        project_name = os.getenv("PROJECT_NAME")
        if not project_name:
            raise OSError("PROJECT_NAME is not defined")
        workspace = os.getenv("WORKSPACE")
        if not workspace:
            raise OSError("WORKSPACE is not defined")
        session.set_environment("WORKSPACE", workspace)
        session.set_environment("PROJECT_NAME", project_name)
        # session._info

    def on_window_create(self, window: Window):
        ...
        # window._info

    def after_window_finished(self, window: Window):
        ...

    def before_script(self, session: Session):
        "[ -f .func.sh ] && source .func.sh || return 0"
        ...

    def reattach(self, session: Session):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        session.rename_session("session_{}".format(now))
