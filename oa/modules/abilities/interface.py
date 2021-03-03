import oa.legacy
import dbus
import re
from oa.modules.abilities.core import info, put
from oa.modules.abilities.interact import say
from oa.modules.abilities.system import find_file, sys_exec

session_bus = dbus.SessionBus()


# TODO: make volume control work
def volume(move=2):
    """ Change volume level.
        Positive `move`: Volume Up
        Negative `move`: Volume Down 
    """
    if move > 0:
        sys_exec('amixer set Master' % move)
    else:
        sys_exec('amixer set Master' % (-move))


# unmute does not work correctly
def mute(mute=True):
    """ Mute or unmute speakers. """
    if oa.legacy.sys.os == 'win':
        wshell.SendKeys(chr(173))
    elif oa.legacy.sys.os in ('linux', 'mac'):
        sys_exec('amixer set Master %smute' % (((not mute) and 'un') or ''))
    else:
        info('Unknown operating system.')


def unmute():
    """ Unmute speakers. """
    mute(False)


def get_mpris():
    for service in session_bus.list_names():
        if re.match('org.mpris.MediaPlayer2.', service):
            return service


# Media control via MPRIS2 on dbus
def media_next():
    player = dbus.SessionBus().get_object(get_mpris(), '/org/mpris/MediaPlayer2')
    player.Next(dbus_interface='org.mpris.MediaPlayer2.Player')


def media_prev():
    player = dbus.SessionBus().get_object(get_mpris(), '/org/mpris/MediaPlayer2')
    player.Previous(dbus_interface='org.mpris.MediaPlayer2.Player')


def media_play():
    player = dbus.SessionBus().get_object(get_mpris(), '/org/mpris/MediaPlayer2')
    player.Play(dbus_interface='org.mpris.MediaPlayer2.Player')


def media_pause():
    player = dbus.SessionBus().get_object(get_mpris(), '/org/mpris/MediaPlayer2')
    player.Pause(dbus_interface='org.mpris.MediaPlayer2.Player')