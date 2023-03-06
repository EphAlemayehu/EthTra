Eth_Cof={
"Addis Ababa": {"Ambo","Buta Jirra", "Adama"},
"Ambo":{"Gedo", "Nekemte"},
"Buta Jirra":{"Worabe", "Wolkite"},
"Adama":{"Dire Dawa", "Mojo"},
"Gedo":{"Shambu","Fincha"},
"Nekemte":{"Gimbi", "Limu"},
"Worabe":{"Hosana","Durame"},
"Wolkite":{"Benchi Naji","Tepi"},
"Mojo":{"Dilla","Kaffa"},
"Dire Dawa":{"Chiro","Harar"}
}
print("Addis Ababa")
terminal_utilities=["Shambu","Fincha","Gimbi","Limu","Hosana","Durame","Benchi Naji","Tepi","Kaffa","Dilla","Chiro","Harar"]
terminals = [4,5,8,8,6,5,5,6,7,9,6,10]
is_max = True
terminals_1 = []
choosen_cities =[]
for i in range(0,len(terminals),2): 
    if is_max:
        if terminals[i] > terminals[i+1]: 
            choosen_cities.append(terminal_utilities[i])
        else: 
            choosen_cities.append(terminal_utilities[i+1])
        terminals_1.append(max(terminals[i],terminals[i+1]))


graph = {
    "Fincha" : "Gedo", 
    "Limu" : "Nekemte", 
    "Hosana" : "Worabe", 
    "Tepi" : "Wolkite", 
    "Dilla" : "Mojo",
    "Harar":  "Dire Dawa"
}
is_max = False
choosen_cities_2 = [] 
terminals_2 = []

for i in range(0,len(terminals_1),2): 
    if not is_max:
        if terminals_1[i] > terminals_1[i+1]: 
            choosen_cities_2.append(graph[choosen_cities[i+1]])
        else: 
            choosen_cities_2.append(graph[choosen_cities[i]])
        terminals_2.append(min(terminals_1[i],terminals_1[i+1]))


graph_1={
"Gedo" : "Ambo",
"Worabe": "Buta Jirra",
"Mojo" : "Adama"}


max_city_ind = 0
if terminals_2[1] > terminals_2[max_city_ind]:
    max_city_ind = 1 
if terminals_2[2] > terminals_2[max_city_ind]:
    max_city_ind = 2


second_city = choosen_cities_2[max_city_ind]
first_choosen_city = graph_1[second_city]
print(first_choosen_city)
print(second_city)
third_city_options = Eth_Cof[second_city]
third_city = None
for c in third_city_options: 
    if c in graph:
        third_city = c 
print(third_city)