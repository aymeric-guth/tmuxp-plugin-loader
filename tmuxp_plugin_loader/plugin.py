from tmuxp.plugin import TmuxpPlugin
import datetime


class Loader(TmuxpPlugin):
    def __init__(self):
        """
        Initialize my custom plugin.
        """
        # Optional version dependency configuration. See Plugin API docs
        # for all supported config parameters
        config = {"tmuxp_min_version": "1.6.2"}

        TmuxpPlugin.__init__(self, plugin_name="tmuxp-plugin-loader", **config)

    def before_workspace_builder(self, session):
        session.rename_session("testin-tests")

    def reattach(self, session):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        session.rename_session("session_{}".format(now))
