from oa.core.util import command_registry

from oa.modules.abilities.interact import say, play, mind
from oa.modules.abilities.other import read_news_feed, diagnostics, read_forecast
from oa.modules.abilities.other import say_day, say_last_command, say_time
from oa.modules.abilities.interface import volume, mute, unmute, media_next, media_prev, media_play, media_pause

kws = {}

command = command_registry(kws)
#todo: add application launcher
@command("root mind")
def hello_world():
    say('- Hello world!')

@command("close assistant")
def close_assistant():
    play('beep_close.wav')
    mind('boot')

@command(["list commands", "what can i say"])
def list_commands():
    say('- The currently available voice commands are:\n{}'.format(',\n'.join(kws.keys())))

@command("read world news")
def read_world_news():
    read_news_feed('https://www.reddit.com/r/worldnews/.rss', 'world')

@command("run diagnostics")
def run_diagnostics():
    diagnostics()

@command("sing a song")
def sing_a_song():
    play('daisy.wav')

@command("what day is it")
def what_day():
    say_day()

@command("what did I say")
def what_command():
    say_last_command('You just said:')

@command("what is the weather")
def what_weather():
    read_forecast()

@command("what time is it")
def what_time():
    say_time()

@command("sudo make me a sandwich")
def sandwich_sudo():
    say("ok, poof!, you're a sandwich")

@command(["volume up", "increase volume", "turn it up"])
def vol_up():
    volume(5)

@command(["volume down", "decrease volume", "turn it down"])
def vol_down():
    volume(-5)


@command(["next song", "skip song"])
def m_next():
    media_next()


@command("previous song")
def m_prev():
    media_prev()

@command(["play", "play song"])
def m_play():
    media_play()

@command(["pause", "pause song"])
def m_pause():
    media_pause()