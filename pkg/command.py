class Commands():
    def __init__(self) -> None:
        self.commands = {}
    def add_cmd(self, name, ref):
        self.commands[name] = ref
    async def call_cmd(self, name, client, message, args):
        await self.commands[name](client, message, args)