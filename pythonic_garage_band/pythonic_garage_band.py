from abc import ABC, abstractmethod
class Band:
    allBands = []
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.allBands.append({'name':name,'members':members})

    def play_solos(self):
        play_solos_arr=[]
        for v in self.members:
            if str(v).split()[-1] == 'guitar':
                play_solos_arr.append('face melting guitar solo')
            if str(v).split()[-1] == 'bass':
                play_solos_arr.append('bom bom buh bom')
            if str(v)).split()[-1] == 'drums':
                play_solos_arr.append('rattle boom crash')
        return play_solos_arr

    def __str__(self):
        return f"The band {self.name} has the following members {self.members.join(',')}"
        
    def __repr__(self):
        return f'<Band: {self.name}> <Members: {self.members.join(",")}>'
       
       
    @classmethod
    def to_list(cls):
        return cls.allBands 



class Musician:
    
    def __init__(self,name,instrument,role,solo_play):
        self.name=name
        self.instrument=instrument
        self.role=role
        self.solo_play = solo_play
        

    
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'
    
    def __repr__(self):
        return f'{self.role} instance. Name = {self.name}'


    def get_instrument(self):
        return f'{self.instrument}'


    def play_solo(self):
        return f'{self.solo_play}'





class Guitarist(Musician):
    role= 'Guitarist'
    instrument = 'guitar'
    solo_play = 'face melting guitar solo'
    def __init__(self, name):
        super().__init__(name,Guitarist.instrument,Guitarist.role,Guitarist.solo_play)
        
    
        

    
        


class Bassist(Musician):
    role= 'Bassist'
    instrument = 'bass'
    solo_play = 'bom bom buh bom'
    def __init__(self, name):
        super().__init__(name,Bassist.instrument,Bassist.role,Bassist.solo_play)



class Drummer(Musician):
    role= 'Drummer'
    instrument = 'drums'
    solo_play = 'rattle boom crash'
    def __init__(self, name):
        super().__init__(name,Drummer.instrument,Drummer.role,Drummer.solo_play)