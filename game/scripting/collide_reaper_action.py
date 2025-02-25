from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideReaperAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(ESPIRITU_GROUP)
        racket = cast.get_first_actor(REAPER_GROUP)
        
        ball_body = ball.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_collided(ball_body, racket_body):
            ball.bounce_y()
            sound = Sound(COLLIDE_SOUND)
            self._audio_service.play_sound(sound)    