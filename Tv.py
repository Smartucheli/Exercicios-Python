class TV:

    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume
    
    def diminui_volume(self, quantidade):
        if self.volume > 0:
            self.volume -= 1

    def aumenta_volume(self):
        if self.volume < 100:
            self.volume += 1

    def muda_canal(self, canal):
        self.canal = canal

tv = TV(12, 10)
i = tv.volume


while i < 55:
    tv.aumenta_volume()
    print(tv.volume)
    i += 1

