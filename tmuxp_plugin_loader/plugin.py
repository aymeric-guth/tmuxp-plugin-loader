import os
import libtmux
from tmuxp.plugin import TmuxpPlugin

Session = libtmux.session.Session
Window = libtmux.window.Window


class Loader(TmuxpPlugin):
    def __init__(self):
        config = {"tmuxp_min_version": "1.6.1"}
        TmuxpPlugin.__init__(self, plugin_name="tmuxp-plugin-loader", **config)

    def _pass_version_check(self, version, vmin, vmax, incompatible):
        return True

    def after_config_loaded(self, config):
        # pdb.set_trace()
        if not config.get("session_name") and os.getenv("PROJECT_NAME"):
            config.update({"session_name": "$PROJECT_NAME"})
        if not config.get("start_directory") and os.getenv("WORKSPACE"):
            config.update({"start_directory": "$WORKSPACE"})

        return config

    def before_workspace_builder(self, session: Session):
        def raiser(varname):
            var = os.getenv(varname)
            if not var:
                import pdb

                pdb.set_trace()
                raise OSError(f"{varname} is not defined")
            return var

        project_name = raiser("PROJECT_NAME")
        workspace = raiser("WORKSPACE")
        session.set_environment("WORKSPACE", workspace)
        session.set_environment("PROJECT_NAME", project_name)

    def on_window_create(self, window: Window):
        # window._info
        ...

    def after_window_finished(self, window: Window):
        ...

    def before_script(self, session: Session):
        ...

    def reattach(self, session: Session):
        ...
        # now = datetime.datetime.now().strftime("%Y-%m-%d")
        # session.rename_session("session_{}".format(now))
