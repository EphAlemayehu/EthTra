from queue import Queue

Cities= {
    "Adama" :["Addis Ababa", "Assella", "Batu", "Matahara"],
    "Addis Ababa" :["Adama", "Ambo", "Debre Birhan"],
    "Adigrat" :["Adwa", "Mekele"],
    "Adwa" :["Adigrat", "Axum", "Mekele"],
    "Alamata" :["Mekele", "Samara", "Sekota", "Woldia"],
    "Ambo" :["Nekemete", "Wolkite"],
    "Arba Minch" :["Basketo", "Konso", "Wolita sodo"],
    "Assasa" :["Assella", "Dodolla"],
    "Assella" :["Adama", "Assasa"],
    "Assosa" :["Dembi Dollo", "Metekel"],
    "Awash" :["Chiro", "Gabi Rasu", "Matahara"],
    "Axum" :["Adwa", "Shire"],
    "Azezo" :["Bahirdar", "Gonder", "Metema"],
    "Babile" :["Harar", "Jigjiga"],
    "Bahirdar" :["Azezo", "Debre Tabor", "Finote Selam", "Injibara", "Metekel"],
    "Bale":["Dodolla", "Goba", "Liben", "Sof Oumer"],
    "Basketo" :["Arba Minch", "Benchi Maji", "Dawro", "Mezan Teferi"],
    "Batu" :["Adama", "Butajira", "Shashemene"],
    "Bedelle" :["Gore", "Jimma", "Nekemete"],
    "Benchi Maji" :["Basketo"],
    "Bonga" :["Dawro", "Jimma", "Mezan Teferi", "Tepi"],
    "Bule hora" :["Dilla", "Yabello"],
    "Butajira" :["Batu", "Worabe"],
    "Chiro" :["Awash", "Dire Dawa"],
    "Dawro" :["Basketo", "Bonga", "Wolita sodo"],
    "Debarke" :["Gonder", "Shire"],
    "Debre Birhan" :["Addis Ababa", "Debre Sina"],
    "Debre Markos" :["Debre Sina", "Finote Selam"],
    "Debre Sina" :["Debre Birhan", "Debre Markos", "Kemise"],
    "Debre Tabor" :["Bahirdar", "Lalibela"],
    "Dega habur" :["Goba", "Jigjiga", "Kebri Dehar"],
    "Dembi Dollo" :["Assosa", "Gambela", "Gimbi"],
    "Dessie" :["Kemise", "Woldia"],
    "Dilla" :["Bule hora", "Hawassa"],
    "Dire Dawa" :["Chiro", "Harar"],
    "Dodolla" :["Assasa", "Bale", "Shashemene"],
    "Dollo" :["Gode"],
    "Fanti Rasu" :["Kilbet rasu", "Samara"],
    "Finote Selam" :["Bahirdar", "Injibara"],
    "Gabi Rasu" :["Awash", "Samara"],
    "Gambela" :["Dembi Dollo", "Gore"],
    "Gimbi" :["Dembi Dollo", "Nekemete"],
    "Goba" :["Bale", "Dega habur", "Sof Oumer"],
    "Gode" :["Kebri Dehar", "Dollo"],
    "Gonder" :["Azezo", "Debarke", "Humera", "Metema"],
    "Gore" :["Bedelle", "Gambela", "Tepi"],
    "Harar" :["Babile", "Dire Dawa"],
    "Hawassa" :["Dilla", "Shashemene"],
    "Hossana" :["Shashemene", "Wolita sodo", "Worabe"],
    "Humera" :["Gonder", "Shire"],
    "Injibara" :["Bahirdar", "Finote Selam"],
    "Jigjiga" :["Babile", "Dega habur"],
    "Jimma" :["Bedelle", "Bonga", "Wolkite"],
    "Kebri Dehar" :["Dega habur", "Sof Oumer", "Werder"],
    "Kemise" :["Debre Sina", "Dessie"],
    "Kilbet rasu" :["Fanti Rasu"],
    "Konso" :["Arba Minch", "Yabello"],
    "Lalibela" :["Debre Tabor", "Sekota", "Woldia"],
    "Liben" :["Bale"],
    "Matahara" :["Adama", "Awash"],
    "Mekele" :["Adigrat", "Adwa", "Alamata", "Sekota"],
    "Metekel" :["Assosa", "Bahirdar"],
    "Metema" :["Azezo", "Gonder"],
    "Mezan Teferi" :["Basketo", "Bonga", "Tepi"],
    "Moyale" :["Yabello"],
    "Nekemete" :["Ambo", "Bedelle", "Gimbi"],
    "Samara" :["Alamata", "Fanti Rasu", "Gabi Rasu", "Woldia"],
    "Sekota" :["Alamata", "Lalibela", "Mekele"],
    "Shashemene" :["Batu", "Dodolla", "Hawassa", "Hossana"],
    "Shire" :["Axum", "Debarke", "Humera"],
    "Sof Oumer" :["Bale", "Goba", "Kebri Dehar"],
    "Tepi" :["Bonga", "Gore", "Mezan Teferi"],
    "Werder" :["Kebri Dehar"],
    "Woldia" :["Alamata", "Dessie", "Lalibela", "Samara"],
    "Wolita sodo" :["Dawro", "Hossana", "Arba Minch"],
    "Wolkite" :["Ambo", "Jimma", "Worabe"],
    "Worabe" :["Butajira", "Hossana", "Wolkite"],
    "Yabello" :["Bule hora", "Konso", "Moyale"]
}

visited = {}
level = {}
parent = {}
bfs_traversal_list = []
queue = Queue()

for city in Cities.keys():
    visited[city] = False
    parent[city] = None
    level[city] = -1

  
initial_city = input("Enter The Initial State: ") 
visited[initial_city] = True
level[initial_city] = 0
queue.put(initial_city)

while not queue.empty():
    u = queue.get()
    bfs_traversal_list.append(u)
    
    for v in Cities[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
       
print(bfs_traversal_list)