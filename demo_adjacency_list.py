Elements = [
(1, 3, 'R', 0.5),  # 0:R₀
(0, 2, 'R', 2.5),  # 1:R₁
(2, 3, 'R', 6.0),  # 2:R₂
(3, 5, 'R', 1.5),  # 3:R₃
(4, 5, 'R', 0.5),  # 4:R₄
(0, 1, 'U', 18.0), # 5:U₀
(2, 4, 'U', 45.0)  # 6:U₁
]

Adjacency_list = []

def Adjacency():
	for a in range(6):
		a = []
		Adjacency_list.append(a)
		
	for i in range(6):
		for k in range(7):
			if Elements[k][0] == i or Elements[k][1] == i:
					Adjacency_list[i].append(Elements.index(Elements[k]))
	return Adjacency_list

print(Adjacency())

		

