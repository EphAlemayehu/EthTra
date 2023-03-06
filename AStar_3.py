heuristic_value_ET = {
     
    'Adama': 23,
    'AddisAbaba': 26, 
    "Adigrat": 62,
    'Adwa': 65,
    'Alamata': 53,
    'Ambo': 31,
    'ArbaMinch': 13,
    'Assasa': 18,
    'Assella': 22,
    'Assosa': 51,
    'Awash': 27,
    'Axum': 66,
    'Azezo': 55,
    'Bablle': 37,
    'BahirDar': 48,
    'Basketo': 23,
    'Batu': 19,
    'Bedelle': 40,
    'BenchiMaji': 28,
    'Bonga': 33,
    'BuleHora': 8,
    'ButaJirra': 21,
    'Chiro': 31,
    'Dawaro': 23,
    'Debarke': 60,
    'DebreBirhan': 31,
    'DebreMarkos': 39,
    'DebreSina': 33,
    'DebreTabor': 52,
    'DegaHabur': 45,
    'DembiDollo': 49,
    'Dessie': 44,
    'Dila': 12,
    'DireDawa':31 ,
    'Dodolla': 19,
    'Dollo': 18,
    'FantiRasu': 49,
    'FinoteSelam': 42,
    'GabiRasu': 32,
    'Gambella': 51,
    'Gimbi': 43,
    'Goba': 40,
    'Gode': 35,
    'Gondar': 56,
    'Gore': 56,
    'Harar': 65,
    'Hawassa': 15,
    'Hossana': 21,
    'Humera': 65,
    'Injibara': 44,
    'Jigiga': 40,
    'Jimma': 33,
    'KebriDehar': 40,
    'Kemise': 40,
    'KilbetRasu': 55,
    'Konso': 9,
    'Lalibela': 54,
    'Liben': 11,
    'Matahara': 26,
    'Mekelle': 58,
    'Metekel': 59,
    'Metema': 62,
    'MezanTeferi': 37,
    'Moyale': 0,
    'Nekemete': 39,
    'Robe': 22,
    'Samara': 42,
    'Sekota': 59,
    'Shashemene': 16,
    'Shire': 67,
    'SofOumer': 45,
    'Tepi': 41,
    'Werder': 46,
    'Woldia': 50,
    'WolaitaSodo': 17,
    'Wolkite': 25,
    'Worabe': 22,
    'Yabello':  6,

    }

graph_ET = {
      'Humera': {'Shire': 8,'Gondar': 9},
      'Shire': {'Axum': 2, 'Debarke': 7},
      'Gondar': {'Metema': 7,'Azezo': 1,'Debarke': 4,'Humera': 9},
      'Axum': {'Adwa':1,'Shire':2},
      'Debarke': {'Gondar':4,'Shire':7},
      'Metema': {'Azezo':7,'Gondar':7},
      'Azezo': {'BahirDar':7,'Metema':7,'Gondar':1},
      'Adwa': {'Axum':1,'Adigrat':4,'Mekelle':7},
      'BahirDar': {'FinoteSelam':6,'Injibara':4,'Metekel':11,'Azezo':7,'DebreTabor':4},
      'Adigrat': {'Adwa':4, 'Mekelle':4},
      'Mekelle': {'Sekota':9, 'Alamata':5, 'Adwa':7, 'Adigrat':4},
      'FinoteSelam': {'DebreMarkos':3,'Injibara':2,'BahirDar':6},
      'Injibara': {'FinoteSelam':2,'BahirDar':4},
      'Metekel': {},
      'DebreTabor': {'Lalibela':8,'BahirDar':4},
      'Sekota': {'Mekelle':9, 'Alamata':6, 'Lalibela':6},
      'Alamata': {'Woldia':3, 'Sekota':6, 'Samara':11, 'Mekelle':5},
      'DebreMarkos' : {'FinoteSelam':3, 'DebreSina':17},
      'Assosa': {},
      'Lalibela': {'DebreTabor':8, 'Woldia':7, 'Sekota':6},
      'Woldia': {'Dessie':6, 'Lalibela':7, 'Alamata':3, 'Samara':8},
      'Samara': {'GabiRasu':9, 'Woldia':8, 'Alamata':11, 'FantiRasu':7},
      'DebreSina': {'DebreBirhan':2, 'DebreMarkos':17, 'Kemise':6},
      'DembiDollo': {'Assosa':12, 'Gimbi':6, 'Gambella':4},
      'Dessie': {'Kemise':4, 'Woldia':6},
      'GabiRasu': {'Awash':5, 'Samara':9},
      'FantiRasu': {'Samara':7,'KilbetRasu':6},
      'DebreBirhan': {'DebreSina':2, 'AddisAbaba':5},
      'DebreMarkos': {'FinoteSelam':3,'DebreSina':17},
      'Kemise': {'Dessie':4,'DebreSina':6},
      'Awash': {'GabiRasu':5,'Chiro':4,'Matahara':1},
      'KilbetRasu':{},
      'AddisAbaba':{'DebreBirhan':5,'Ambo':5,'Adama':3},
      'Chiro': {'Awash':4,'DireDawa':8},
      'Matahara': {'Adama':3,'Awash':1},
      'Ambo': {'Wolkite':6,'Nekemete':9,'AddisAbaba':5},
      'Adama': {'AddisAbaba':3,'Matahara':3,'Batu':4,'Assella':4},
      'DireDawa': {'Chiro':8,'Harar':4},
      'Wolkite': {'Ambo':6,'Jimma': 8, 'Worabe':5},
      'Nekemete': {'Ambo':9,'Gimbi': 4,'Bedelle':2},
      'Batu': {'Adama':4, 'ButaJirra': 2,'Shashemene':3},
      'Assella': {'Assasa':4,'Adama': 4},
      'Harar' : {'DireDawa':4, 'Bablle': 2},
      'Jimma' : {'Wolkite':8,'Bedelle': 7,'Bonga':4},
      'Worabe': {'Wolkite':5,'Hossana': 2,'ButaJirra':2},
      'Gimbi' : {'Nekemete':4, 'DembiDollo':6},
      'Bedelle': {'Nekemete':2,'Jimma':7, 'Gore':6},
      'ButaJirra' :{'Worabe':2,'Batu':2},
      'Shashemene':{'Batu':3,'Hossana':7,'Hawassa':1,'Dodolla':3},
      'Assasa' : {'Assella':4,'Dodolla':1},
      'Bablle' : {'Harar':3,'Jigiga': 3},
      'Bonga' : {'Jimma':4,'Dawaro':10,'Tepi':8,'MezanTeferi':4},
      'Hossana': {'Worabe': 2,'Shashemene': 7,'WolaitaSodo': 4},
      'Gore' : {'Bedelle':6,'Tepi':9, 'Gambella':5},
      'Hawassa' : {'Shashemene':1,'Dila':3},
      'Dodolla' : {'Shashemene':3,'Assasa':1,'Robe':13},
      'Jigiga' : {'Bablle':3,'DegaHabur':5},
      'Dawaro'  : {'Bonga':10,'WolaitaSodo':6},
      'Tepi'    : {'Gore':9,'MezanTeferi':4,'Bonga':8},
      'MezanTeferi' : {'Tepi':4, 'Bonga':4},
      'WolaitaSodo' : {'Hossana': 4, 'Dawaro':6, 'ArbaMinch':4},
      'Gambella' : {'DembiDollo':4,'Gore':5},
      'Dila' : {'Hawassa': 3,'BuleHora':4},
      'Robe' : {'Dodolla':13,'Liben':11,'Goba':18,'SofOumer':23},
      'DegaHabur' : {'Jigiga': 5, 'KebriDehar':6},
      'Dawaro': {'WolaitaSodo':4,'Bonga':10},
      'ArbaMinch' : {'Konso':4,'Basketo':10,'WolaitaSodo':4},
      'Basketo' : {'ArbaMinch':10,'ButaJirra':5},
      'BuleHora' : {'Dila':4,'Yabello':3},
      'Liben' :{},
      'Goba':{'Robe':18,'SofOumer':6,'Bablle':28},
      'SofOumer': {'Robe':23,'Goba':6,'Gode':23},
      'KebriDehar': {'DegaHabur':6,'Werder':6,'Gode':5},
      'Yabello' : {'BuleHora':3,'Konso':3,'Moyale':6},
      'ButaJirra' :{} ,
      'Gode' :{'Dollo':17},
      'Dollo': {},
      'Werder':{},
      'Konso' :{'ArbaMinch':4,'Yabello':3},
      'Moyale':{},
}
import heapq
class PriorityQueue:
    def init(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]


def reconstruct_path(came_from, start, goal):
    current = goal
    path =[current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def a_star_search(graph, heuristic, start, goal):
    frontier = PriorityQueue()
    frontier.push(start, 0)
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while not frontier.is_empty():
        current_node = frontier.pop()

        if current_node == goal:
            return reconstruct_path(came_from, start, goal), g_score[goal]

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor]= current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                if neighbor not in frontier.elements:
                    frontier.push(neighbor, f_score[neighbor])

    return None, None
print(a_star_search(graph_ET, heuristic_value_ET, 'AddisAbaba', 'Moyale'))

