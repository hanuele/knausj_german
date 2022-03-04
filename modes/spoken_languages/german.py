from talon import Context, Module, actions, speech_system
from talon.grammar import Phrase

mod = Module()
mod.mode('german', desc='german language mode')

ctx = Context()
ctx.matches = r'mode: user.german'
ctx.settings = {
	"speech.engine": "w2l",
	'speech.language': 'de_DE'
}

