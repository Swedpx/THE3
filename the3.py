from evaluator import *
liste=get_data()
def new_move():
	sonuc = []
	def force(mass): #mass sadece kutle degil; [mass,initial_x,initial_y,...]
		force_x=0
		force_y=0
		for i in liste[2:]:
			if mass != i:
					uzaklik=((i[1]-mass[1])**2+(i[2]-mass[2])**2)**(0.5)
					force = (liste[0]*i[0]*mass[0])/(uzaklik**2)
					force_x += force * ((i[1]-mass[1])/uzaklik)
					force_y += force * ((i[2]-mass[2])/uzaklik)
		return force_x,force_y
	for i in liste[2:]:#koordinatlari guncelleme
		deltalar= [float(i[3])*liste[1],float(i[4])*liste[1]]
		sonuc.append(deltalar)
		i[1]+=float(i[3])*liste[1]
		i[2]+=float(i[4])*liste[1]
	for i in liste[2:]: #hizlari guncelleme
		i[3]+=(force(i)[0]/i[0])*liste[1]
		i[4]+=(force(i)[1]/i[0])*liste[1]
	return sonuc