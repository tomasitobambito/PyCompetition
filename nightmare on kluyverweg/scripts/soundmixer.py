import pygame as pg

class SoundMixer():
    def __init__(self, soundfolder):
        self.sounds = {
            'music': None,
            'metal_pipe_falling': None,
            'question_correct': None,
            'question_wrong': None,
            'caught': None,
        }

        self.import_sounds(soundfolder)

    def import_sounds(self, soundfolder):
        for sound in self.sounds.keys():
            self.sounds[sound] = pg.mixer.Sound(f"{soundfolder}/{sound}.wav")
        
        self.set_volumes()

    def set_volumes(self):
        self.sounds['music'].set_volume(0.2)
        self.sounds['metal_pipe_falling'].set_volume(0.6)
        self.sounds['question_correct'].set_volume(1.6)
        self.sounds['question_wrong'].set_volume(1.4)
        self.sounds['caught'].set_volume(0.8)



        