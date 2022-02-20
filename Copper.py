###################################################################
###### Copper
### Cu 55
data_Cu1 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 004.Chn')[1]
data_Cu1 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 005.Chn')[1]
data_Cu1 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 012.Chn')[1]
data_Cu1 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 013.Chn')[1]
data_Cu1 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 015.Chn')[1]
data_Cu1 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 018.Chn')[1]
data_Cu1 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/55/02 Copper/02 Copper 55 degrees 019.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu1)
plt.title('Angle 55 - Copper')
plt.show()

Cu_55peak_x = 613
Cu_55param = Fit(data_Cu1, 100, Cu_55peak_x)
Cu_55chi = Chi(Cu_55param[0], data_Cu1, 100, Cu_55peak_x)

### Cu 65
data_Cu2 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 008.Chn')[1]
data_Cu2 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 015.Chn')[1]
data_Cu2 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 016.Chn')[1]
data_Cu2 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 018.Chn')[1]
data_Cu2 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/65/02 Copper/02 Copper 65 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu1)
plt.title('Angle 65 - Copper')
plt.show()

Cu_65peak_x = 637
Cu_65param = Fit(data_Cu2, 100, Cu_65peak_x)
Cu_65chi = Chi(Cu_65param[0], data_Cu2, 100, Cu_65peak_x)

### Cu 75
data_Cu3 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 001.Chn')[1]
data_Cu3 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 002.Chn')[1]
data_Cu3 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 009.Chn')[1]
data_Cu3 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 013.Chn')[1]
data_Cu3 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 024.Chn')[1]
data_Cu3 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 025.Chn')[1]
data_Cu3 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/75/02 Copper/02 Copper 75 degrees 035.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu3)
plt.title('Angle 75 - Copper')
plt.show()

Cu_75peak_x = 685
Cu_75param = Fit(data_Cu3, 100, Cu_75peak_x)
Cu_75chi = Chi(Cu_75param[0], data_Cu3, 100, Cu_75peak_x)

### Cu 85
data_Cu4 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 003.Chn')[1]
data_Cu4 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 004.Chn')[1]
data_Cu4 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 020.Chn')[1]
data_Cu4 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/85/02 Copper/02 Copper 85 degrees 028.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu4)
plt.title('Angle 85 - Copper')
plt.show()

Cu_85peak_x = 752
Cu_85param = Fit(data_Cu4, 100, Cu_85peak_x)
Cu_85chi = Chi(Cu_85param[0], data_Cu4, 100, Cu_85peak_x)

### Cu 95
data_Cu5 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 009.Chn')[1]
data_Cu5 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 014.Chn')[1]
data_Cu5 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 023.Chn')[1]
data_Cu5 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 027.Chn')[1]
data_Cu5 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 031.Chn')[1]
data_Cu5 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/95/02 Copper/02 Copper 95 degrees 038.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu5)
plt.title('Angle 95 - Copper')
plt.show()

Cu_95peak_x = 825
Cu_95param = Fit(data_Cu5, 100, Cu_95peak_x)
Cu_95chi = Chi(Cu_95param[0], data_Cu5, 100, Cu_95peak_x)

### Cu 105
data_Cu6 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 003.Chn')[1]
data_Cu6 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 007.Chn')[1]
data_Cu6 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 025.Chn')[1]
data_Cu6 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/105/02 Copper/02 Copper 105 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu6)
plt.title('Angle 105 - Copper')
plt.show()

Cu_105peak_x = 903
Cu_105param = Fit(data_Cu6, 100, Cu_105peak_x)
Cu_105chi = Chi(Cu_105param[0], data_Cu6, 100, Cu_105peak_x)

### Cu 125
data_Cu7 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 013.Chn')[1]
data_Cu7 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 017.Chn')[1]
data_Cu7 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 021.Chn')[1]
data_Cu7 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 026.Chn')[1]
data_Cu7 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 027.Chn')[1]
data_Cu7 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/125/02 Copper/02 Copper 125 degrees 031.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu7)
plt.title('Angle 125 - Copper')
plt.show()

Cu_125peak_x = 1133
Cu_125param = Fit(data_Cu7, 100, Cu_125peak_x)
Cu_125chi = Chi(Cu_125param[0], data_Cu7, 100, Cu_125peak_x)

### Cu 135
data_Cu8 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 009.Chn')[1]
data_Cu8 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 015.Chn')[1]
data_Cu8 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 022.Chn')[1]
data_Cu8 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/135/02 Copper/02 Copper 135 degrees 033.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu8)
plt.title('Angle 135 - Copper')
plt.show()

Cu_135peak_x = 1284
Cu_135param = Fit(data_Cu8, 100, Cu_135peak_x)
Cu_135chi = Chi(Cu_135param[0], data_Cu8, 100, Cu_135peak_x)

### Cu 220
data_Cu9 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 010.Chn')[1]
data_Cu9 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 011.Chn')[1]
data_Cu9 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 020.Chn')[1]
data_Cu9 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 028.Chn')[1]
data_Cu9 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 030.Chn')[1]
data_Cu9 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/220/02 Copper/02 Copper 220 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu9)
plt.title('Angle 220 - Copper')
plt.show()

Cu_220peak_x = 1363
Cu_220param = Fit(data_Cu9, 100, Cu_220peak_x)
Cu_220chi = Chi(Cu_220param[0], data_Cu9, 100, Cu_220peak_x)

### Cu 230
data_Cu10 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 007.Chn')[1]
data_Cu10 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 009.Chn')[1]
data_Cu10 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 012.Chn')[1]
data_Cu10 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/230/02 Copper/02 Copper 230 degrees 018.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu10)
plt.title('Angle 230 - Copper')
plt.show()

Cu_230peak_x = 1230
Cu_230param = Fit(data_Cu10, 100, Cu_230peak_x)
Cu_230chi = Chi(Cu_230param[0], data_Cu10, 100, Cu_230peak_x)

### Cu 240
data_Cu11 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 008.Chn')[1]
data_Cu11 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 010.Chn')[1]
data_Cu11 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 013.Chn')[1]
data_Cu11 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 027.Chn')[1]
data_Cu11 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 028.Chn')[1]
data_Cu11 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/240/02 Copper/02 Copper 240 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu11)
plt.title('Angle 240 - Copper')
plt.show()

Cu_240peak_x = 1103
Cu_240param = Fit(data_Cu11, 100, Cu_240peak_x)
Cu_240chi = Chi(Cu_240param[0], data_Cu11, 100, Cu_240peak_x)

### Cu 250
data_Cu12 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 004.Chn')[1]
data_Cu12 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 010.Chn')[1]
data_Cu12 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 021.Chn')[1]
data_Cu12 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/250/02 Copper/02 Copper 250 degrees 032.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu12)
plt.title('Angle 250 - Copper')
plt.show()

Cu_250peak_x = 982
Cu_250param = Fit(data_Cu12, 100, Cu_250peak_x)
Cu_250chi = Chi(Cu_250param[0], data_Cu12, 100, Cu_250peak_x)

### Cu 260
data_Cu13 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 000.Chn')[1]
data_Cu13 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 009.Chn')[1]
data_Cu13 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 011.Chn')[1]
data_Cu13 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 021.Chn')[1]
data_Cu13 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 031.Chn')[1]
data_Cu13 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/260/02 Copper/02 Copper 260 degrees 036.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu13)
plt.title('Angle 260 - Copper')
plt.show()

Cu_260peak_x = 879
Cu_260param = Fit(data_Cu13, 100, Cu_260peak_x)
Cu_260chi = Chi(Cu_260param[0], data_Cu13, 100, Cu_260peak_x)

### Cu 280
data_Cu14 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 016.Chn')[1]
data_Cu14 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 020.Chn')[1]
data_Cu14 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 027.Chn')[1]
data_Cu14 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 032.Chn')[1]
data_Cu14 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/280/02 Copper/02 Copper 280 degrees 038.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu14)
plt.title('Angle 280 - Copper')
plt.show()

Cu_280peak_x = 722
Cu_280param = Fit(data_Cu14, 100, Cu_280peak_x)
Cu_280chi = Chi(Cu_280param[0], data_Cu14, 100, Cu_280peak_x)

### Cu 300
data_Cu15 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 003.Chn')[1]
data_Cu15 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 010.Chn')[1]
data_Cu15 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 012.Chn')[1]
data_Cu15 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 017.Chn')[1]
data_Cu15 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 021.Chn')[1]
data_Cu15 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 029.Chn')[1]
data_Cu15 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/300/02 Copper/02 Copper 300 degrees 035.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu15)
plt.title('Angle 300 - Copper')
plt.show()

Cu_300peak_x = 637
Cu_300param = Fit(data_Cu15, 100, Cu_300peak_x)
Cu_300chi = Chi(Cu_300param[0], data_Cu15, 100, Cu_300peak_x)

### Cu 310
data_Cu16 = mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 005.Chn')[1]
data_Cu16 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 009.Chn')[1]
data_Cu16 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 021.Chn')[1]
data_Cu16 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 022.Chn')[1]
data_Cu16 += mphys.data.load_chn('D:/Downloads/Compton-main/Compton-main/Compton/Angles/310/02 Copper/02 Copper 310 degrees 025.Chn')[1]

plt.scatter(np.arange(0, 2048), data_Cu16)
plt.title('Angle 310 - Copper')
plt.show()

Cu_310peak_x = 583
Cu_310param = Fit(data_Cu16, 100, Cu_310peak_x)
Cu_310chi = Chi(Cu_310param[0], data_Cu16, 100, Cu_310peak_x)