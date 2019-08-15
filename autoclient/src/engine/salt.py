from .base import SshAndSaltHandler


class SaltHandler(SshAndSaltHandler):

    def cmd(self, command, hostname=None):
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])

        return result

