graph = {
  'Humera' :{'Shire':8,'Gondar':9},
  'Shire' : {'Axum':2, 'Debarke':7},
  'Gondar' : {'Metema':7,'Azezo':1,'Debarke':4,'Humera':9},
  'Axum' : {'Adwa':1,'Shire':2},
  'Debarke' : {'Gondar':4,'Shire':7},
  'Metema' : {'Azezo':7,'Gondar':7},
  'Azezo' : {'BahirDar':7,'Metema':7,'Gondar':1},
  'Adwa' : {'Axum':1,'Adigrat':4,'Mekelle':7},
  'BahirDar' : {'FinoteSelam':6,'Injibar':4,'Metekel':11,'Azezo':7,'DebreTabor':4},
  'Adigrat' : {'Adwa':4, 'Mekelle':4},
  'Mekelle' : {'Sekota':9, 'Alamata':5, 'Adwa':7, 'Adigrat':4},
  'FinoteSelam' : {'DebreMarkos':3,'Injibar':2,'BahirDar':6},
  'Injibar' : {'FinoteSelam':2,'BahirDar':4},
  'Metekel' : {},
  'DebreTabor' : {'Lalibela':8,'BahirDar':4},
  'Sekota' : {'Mekelle':9, 'Alamata':6, 'Lalibela':6},
  'Alamata' : {'Woldia':3, 'Sekota':6, 'Samara':11, 'Mekelle':5},
  'DebreMarkos' : {'FinoteSelam':3, 'DebreSina':17},
  'Assosa' : {},
  'Lalibela' : {'DebreTabor':8, 'Woldia':7, 'Sekota':6},
  'Woldia' : {'Dessie':6, 'Lalibela':7, 'Alamata':3, 'Samara':8},
  'Samara' : {'GabiRasu':9, 'Woldia':8, 'Alamata':11, 'FantiRasu':7},
  'DebreSina' : {'DebreBirhan':2, 'DebreMarkos':17, 'Kemise':6},
  'DembiDollo': {'Assosa':12, 'Gimbi':6, 'Gambella':4},
  'Dessie' : {'Kemise':4, 'Woldia':6},
  'GabiRasu' : {'Awash':5, 'Samara':9},
  'FantiRasu' : {'Samara':7,'KilbetRasu':6},
  'DebreBirhan': {'DebreSina':2, 'AddisAbaba':5},
  'DebreMarkos': {'FinoteSelam':3,'DebreSina':17},
  'Kemise' : {'Dessie':4,'DebreSina':6},
  'Awash' : {'GabiRasu':5,'Chiro':4,'Matahara':1},
  'KilbetRasu' :{},
  'AddisAbaba':{'DebreBirhan':5,'Ambo':5,'Adama':3},
  'Chiro' : {'Awash':4,'DireDawa':8},
  'Matahara' : {'Adama':3,'Awash':1},
  'Ambo': {'Wolkite':6,'Nekemete':9,'AddisAbaba':5},
  'Adama':{'AddisAbaba':3,'Matahara':3,'Batu':4,'Assella':4},
  'DireDawa':{'Chiro':8,'Harar':4},
  'Wolkite' : {'Ambo':6,'Jimma':8, 'Worabe':5},
  'Nekemete': {'Ambo':9,'Gimbi':4,'Bedelle':2},
  'Batu' : {'Adama':4, 'ButaJirra':2,'Shashemene':3},
  'Assella':{'Assasa':4,'Adama':4},
  'Harar' : {'DireDawa':4, 'Bablle':2},
  'Jimma' : {'Wolkite':8,'Bedelle':7,'Bonga':4},
  'Worabe': {'Wolkite':5,'Hossana':2,'ButaJirra':2},
  'Gimbi' : {'Nekemete':4, 'DembiDollo':6},
  'Bedelle': {'Nekemete':2,'Jimma':7, 'Gore':6},
  'ButaJirra' :{'Worabe':2,'Batu':2},
  'Shashemene':{'Batu':3,'Hossana':7,'Hawassa':1,'Dodolla':3},
  'Assasa' : {'Assella':4,'Dodolla':1},
  'Bablle' : {'Harar':3,'Jigjiga':3},
  'Bonga' : {'Jimma':4,'Dawaro':10,'Tepi':8,'MezanTeferi':4},
  'Hossana' : {'Worabe':2,'Shashemene':7,'WolaitaSodo':4},
  'Gore' : {'Bedelle':6,'Tepi':9, 'Gambella':5},
  'Hawassa' : {'Shashemene':1,'Dila':3},
  'Dodolla' : {'Shashemene':3,'Assasa':1,'Bale':13},
  'Jigjiga' : {'Bablle':3,'DegaHabur':5},
  'Dawaro'  : {'Bonga':10,'WolaitaSodo':6},
  'Tepi'    : {'Gore':9,'MezanTeferi':4,'Bonga':8},
  'MezanTeferi' : {'Tepi':4, 'Bonga':4},
  'WolaitaSodo' : {'Hossana':4, 'Dawaro':6, 'ArbaMinch':4},
  'Gambella' : {'DembiDollo':4,'Gore':5},
  'Dila' : {'Hawassa':3,'BuleHora':4},
  'Bale' : {'Dodolla':13,'Liben':11,'Goba':18,'SofOumer':23},
  'DegaHabur' : {'Jigjiga':5, 'KebriDehar':6},
  'Dawaro': {'WolaitaSodo':4,'Bonga':10},
  'ArbaMinch' : {'Konso':4,'Basketo':10,'WolaitaSodo':4},
  'Basketo' : {'ArbaMinch':10,'BenchiMaji':5},
  'BuleHora' : {'Dila':4,'Yabello':3},
  'Liben' :{},
  'Goba':{'Bale':18,'SofOumer':6,'Bablle':28},
  'SofOumer': {'Bale':23,'Goba':6,'Gode':23},
  'KebriDehar': {'DegaHabur':6,'Werder':6,'Gode':5},
  'Yabello' : {'BuleHora':3,'Konso':3,'Moyale':6},
  'BenchiMaji' :{} ,
  'Gode' :{'Dollo':17},
  'Dollo': {},
  'Werder':{},
  'Konso' :{'ArbaMinch':4,'Yabello':3},
  'Moyale':{}
}

from queue import PriorityQueue


def ucs(my_graph, start, goal):
    q = PriorityQueue()
    q.put((0, [start]))
    while not q.empty():
        current_tuple = q.get()
        if goal in current_tuple[1]:
            return current_tuple[1], cost
        current_vertex = current_tuple[1][-1]
        children = list(my_graph[current_vertex].items())
        for child, child_cost in children:
            cost = current_tuple[0] + child_cost
            path = current_tuple[1].copy()
            path.append(child)
            node = tuple([cost, path])
            q.put(node)


if __name__ == '__main__':
    print(ucs(graph,'AddisAbaba','Axum'))
