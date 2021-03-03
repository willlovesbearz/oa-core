import oa.legacy

from oa.core.util import command_registry

from oa.modules.abilities.interact import say, play, mind


kws = {}
command = command_registry(kws)

@command("boot mind")
def response_sound():
  play('r2d2.wav')

@command("open assistant")
def open_root():
  play('beep_open.wav')
  mind('root')

#@command(["list commands", "help"])
#def list_commands():
#    say('The currently available voice commands are..')
#    [say(cmd) for cmd in kws.keys()]

@command("stop listening")
def do_exit():
    oa.legacy.hub.finished.set()
