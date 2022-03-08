from talon import Context, Module, actions, speech_system
from talon.grammar import Phrase

mod = Module()
mod.mode('german', desc='german language mode')

ctx = Context()
ctx.matches = r'mode: user.german'
ctx.settings = {
	'speech.language': 'de_DE'
}
phrase_stack = []
def on_pre_phrase(d):  phrase_stack.append(d)
def on_post_phrase(d): phrase_stack.pop()

speech_system.register('pre:phrase', on_pre_phrase)
speech_system.register('post:phrase', on_pre_phrase)

@mod.action_class 
class Actions:
	def german_recognize(phrase: Phrase):
		"Replay speech into vosk"
        # NOTE: this is pretty much all considered an experimental API
        # and this script is just for demo purposes, for the beta only
		current_phrase = phrase_stack[-1]
		ts = current_phrase['_ts']
		start = phrase.words[0].start - ts
		end   = phrase.words[-1].end - ts
		samples = current_phrase['samples']
		pstart  = int(start * 16_000)
		pend    = int(end   * 16_000)
		samples = samples[pstart:pend]
		
		actions.mode.enable("user.german")
		try:
			# NOTE: the following API is completely private and subject to change with no notice
			speech_system._on_audio_frame(samples)
		finally:
			actions.mode.disable("user.german")