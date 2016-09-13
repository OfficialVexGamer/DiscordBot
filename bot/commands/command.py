class Command:
    def requiresAdmin(self):
        return False

    async def do(self, client, message):
        pass