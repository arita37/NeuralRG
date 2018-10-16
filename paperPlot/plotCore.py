import numpy as np

import matplotlib.pyplot as plt

T = np.array([2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7])

LOSS = [[-2629.52734375, -2517.732666015625, -2382.603759765625, -2298.070556640625, -2224.263427734375, -2153.560791015625, -2093.03466796875, -2027.9017333984375], [-2631.32763671875, -2514.2529296875, -2382.027587890625, -2299.52783203125, -2223.913818359375, -2153.96630859375, -2092.310302734375, -2027.9427490234375], [-2612.1435546875, -2473.8828125, -2381.14892578125, -2298.51416015625, -2224.610595703125, -2155.95458984375, -2091.288818359375, -2027.9691162109375], [-2564.12109375, -2465.0751953125, -2375.82958984375, -2298.653076171875, -2225.330810546875, -2155.19580078125, -2091.646728515625, -2027.3924560546875], [-2524.79931640625, -2434.591796875, -2352.68994140625, -2277.39697265625, -2207.934326171875, -2143.44921875, -2083.259521484375, -2027.4788818359375]]

STD = [[8.059191703796387, 11.621288299560547, 10.177864074707031, 9.973454475402832, 8.8748140335083, 9.274510383605957, 8.281795501708984, 8.605486869812012], [13.325190544128418, 14.106671333312988, 10.464872360229492, 9.716232299804688, 8.959348678588867, 9.24105167388916, 8.49086856842041, 8.630111694335938], [17.389171600341797, 11.294380187988281, 10.290760040283203, 9.830211639404297, 8.741053581237793, 8.610268592834473, 8.703315734863281, 8.622929573059082], [12.239465713500977, 11.283766746520996, 11.002582550048828, 9.701992988586426, 8.75760269165039, 8.639320373535156, 8.585694313049316, 7.989887237548828], [12.59764575958252, 11.79252815246582, 10.966842651367188, 10.072879791259766, 9.27474594116211, 8.674888610839844, 8.275901794433594, 7.964288234710693]]

loss1 = np.array(LOSS[0])
loss2 = np.array(LOSS[1])
loss3 = np.array(LOSS[2])
loss4 = np.array(LOSS[3])
loss5 = np.array(LOSS[4])

error1 = np.array(STD[0])
error2 = np.array(STD[1])
error3 = np.array(STD[2])
error4 = np.array(STD[3])
error5 = np.array(STD[4])

exact = np.array([1051.104987614517,1009.4996784717939,973.8408186679096,944.3823241807323,920.8489585246118,901.1617063065412,884.3618952526879,869.8418508112793,857.1705412103629,846.0253831110782,836.1570646028667,827.3685472309867,819.5014489849076,812.4267256294704,806.0380467741903,800.2469515985453])

fix = np.array([1597.682970064889,1525.9571863911228,1459.8057676137014,1398.5480483845513,1341.612857520735,1288.5170967249728,1238.8491888829687,1192.2561471669637,1148.4333700194834,1107.1165118352076,1068.0749509785837,1031.1064990650011,996.0330835834103,962.697200232009,930.958978748977,900.6937413401133])

exact = exact[:len(LOSS[0])]
fix = fix[:len(LOSS[0])]

res1 = np.abs(-loss1-exact-fix)/(exact+fix)
res2 = np.abs(-loss2-exact-fix)/(exact+fix)
res3 = np.abs(-loss3-exact-fix)/(exact+fix)
res4 = np.abs(-loss4-exact-fix)/(exact+fix)
#res5 = np.abs(-loss5-exact-fix)/(exact+fix)

#error5 /= (512)**0.5*(exact+fix)
error4 /= (512)**0.5*(exact+fix)
error3 /= (512)**0.5*(exact+fix)
error2 /= (512)**0.5*(exact+fix)
error1 /= (512)**0.5*(exact+fix)


plt.errorbar(T,res1,label="depth = 5",yerr=error1)
plt.errorbar(T,res2,label="depth = 4",yerr=error2)
plt.errorbar(T,res3,label="depth = 3",yerr=error3)
plt.errorbar(T,res4,label="depth = 2",yerr=error4)
#plt.errorbar(T,res5,label="depth = 5",yerr=error5)

plt.legend()
plt.xlabel("Temperature")
plt.ylabel("$\L\ relative error$")

plt.show()


import pdb
pdb.set_trace()