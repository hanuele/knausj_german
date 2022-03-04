from talon import Context, Module, actions, speech_system
from talon.grammar import Phrase

mod = Module()
mod.mode('english', desc='english language mode')#

ctx = Context()
ctx.matches = r'mode: user.english'
ctx.settings = {
	"speech.engine": "w2l",
	'speech.language': 'en_US'
}



