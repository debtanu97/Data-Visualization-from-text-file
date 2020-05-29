import sys
import io
import matplotlib.pyplot as plt

count=0
temp=0
x_cor = []
y_cor = []
with io.open(sys.argv[1],'rb') as f:
	while True:
		line = f.readline()
		count=count+1

		if not line :
				break
		
		if(count >= temp+2 and temp != 0):
			line = line.decode('utf-8')
			x = list(map(float, line.split()))
			x_cor.append(x[0]/x[1])
			y_cor.append(x[2]/weight[0])
			
		else:
			x = list(line.split())
			if(x == [b'Torr', b'Torr', b'cc', b'sec']):
				temp=count
			if(len(x)>=4 and x[0] == b'Sample' and x[1] == b'weight:'):
				wt_str = x[2]
				wt_str = wt_str.decode('utf-8')
				weight = list(map(float, wt_str.split()))
				#print(weight)		


adsorption_point = max(x_cor)
split_pt = 0
ind = 0

for i in x_cor:
	if(i == adsorption_point):
		split_pt = ind
		break

	ind = ind+1

x_cor1 = x_cor[0: (ind+1)]
y_cor1 = y_cor[0: (ind+1)]
x_int = x_cor[ind :]
y_int = y_cor[ind :]
x_cor2 = x_cor[(ind+1) :]
y_cor2 = y_cor[(ind+1) :]

plt.xlabel('p/p0')
plt.ylabel('Vads(N2)(cc/gm)STP')

plt.plot(x_cor1,y_cor1)
plt.scatter(x_cor1,y_cor1)

plt.plot(x_int,y_int)
plt.scatter(x_cor2,y_cor2)

#plt.show()
#plt.text(0.1, 600, sys.argv[1])
save_name = sys.argv[1]+'.png'
plt.savefig(save_name)