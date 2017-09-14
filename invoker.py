import importlib, pkgutil, traceback

class Command:
    """ Wrapper class that every command should use when being created.

    The default run method should never be called, and any instance of the
    class should override this method on creation of the instance.

    Commands should also implement any private methods they may need for completion

    Attributes:
        cmdTriggers: List, list of every trigger that should be used to invoke
        this method.
        altHtml: Bool, true if the command has alternate output if HTML is supported.
    """
    def __init__(self, triggers, nonAbsRun = None, html = False):
        self.cmdTriggers = triggers
        self.altHtml = html
        # This will hide the default run method if it is given on object creation
        self.run = nonAbsRun if nonAbsRun else self.run
    def run(self, robot, cmd, room, params, user):
        """Abstract method for executing a command after it has been found. Each command
        has to reimplement this function to work.

        Args:
            robot: PokemonShowdownBot, the instance of PokemonShowdownBot that called this function.
            cmd: string, the command that was send.
            room: Room, the room object that the command was sent from.
            params: string, additional paramters that the command may need.
            user: User, the user object of the user who sent the command.
        Returns:
            ReplyObject.
        Raises:
            NotImplementedError if not implemented, otherwise unknown. """
        raise NotImplementedError('Command#run method not implemented')

class ReplyObject:
    """ Class for returning information from a command to the core program.

    Parameters used for creating this class defines the behaviour of the main
    program when it comes across the reply object.

    Attrpbutes:
        text: str, the content of the reply.
        ignoreEscaping: bool, default every reply is escaped to not allow
        arbitrary commands to be executed through replies. Some commands require
        to be able to use PS commands, which is when this should be overwritten.
        ignoreBroadcastPermission: bool, ignore the global broadcast permission
        for the reply if this is true.
        gameCommand: bool, unused, pending removal.
        canPmReply: bool, override the default request for users without broadcast
        permission to pm the command and instead return the result of the action.
        isException: bool, if a command throws an exception this will be true.
    """
    def __init__(self, res = '', reply = False, escape = False, broadcast = False, game = False, pmreply = False):
        self.text = str(res)
        self.samePlace = reply
        self.ignoreEscaping = escape
        self.ignoreBroadcastPermission = broadcast
        self.gameCommand = game
        self.canPmReply = pmreply
        self.isException = isinstance(res, Exception)

    def __eq__(self, other):
        try:
            return (self.text == other.text
                and self.samePlace == other.samePlace
                and self.ignoreEscaping == other.ignoreEscaping
                and self.ignoreBroadcastPermission == other.ignoreBroadcastPermission
                and self.gameCommand == other.gameCommand
                and self.canPmReply == other.canPmReply
                and self.isException == other.isException
            )
        except:
            # This only happens if the other object isn't a matching object
            return False

    def response(self, text):
        self.text = text
        return self

class CommandInvoker:
    def __init__(self):
        self.cmdInvokers = {}
        self.buildInvokerTable()

    def buildInvokerTable(self):
        print('Loading commands...')
        for importer, modname, ispkg in self._iterPackages():
            spec = importer.find_spec(modname)
            importedModule = importlib.import_module(modname)
            try:
                # Look through the module and see if any commands have been defined
                commands = getattr(importedModule, 'commands')
                for command in commands:
                    # build the invoker table for each command
                    for trigger in command.cmdTriggers:
                        if trigger in self.cmdInvokers:
                            print('{} already exists as a command'.format(trigger))
                            continue
                        self.cmdInvokers[trigger] = command
            except AttributeError:
                # Module contains no commands, this is expected and should be ignored
                pass

    def _iterPackages(self):
        for importer, modname, ispkg in pkgutil.walk_packages(path = '.', onerror = lambda x: None):
            yield importer, modname, ispkg

    def execute(self, robot, cmd, room, params, user):
        if cmd in self.cmdInvokers:
            try:
                return self.cmdInvokers[cmd].run(robot, cmd, room, params, user)
            except Exception as e:
                # Something went wrong, but we don't know what
                traceback.print_tb(e)
                return ReplyObject(e)

        return ReplyObject('{command} is not a valid command.'.format(command = cmd))