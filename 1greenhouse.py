# Cette fonction calcule la température d' équilibre d'une planète gelée soumise au rayonnement solaire,
# en fonction de son albédo et de l'émissivité. En supposant qu'elle soit entièrement recouverte de glace,
# son albédo est autour de 0.9. Sous l'effet du soleil, la planète se réchauffe mais garde une température
# de surface bien en - dessous de 0°C !

# Dans un premier temps, on calcule T sans effet de serre puis avec.
import matplotlib.pyplot as plt
import numpy as np

def greenhouse(alpha=0.3,L=1364):

    eps = 1
    Is = (1 - alpha) * L / 4
    sigma = 5.67 * 10 **(-8)
    timeStep = 100
    Cp = 4000 * 4.2 * 10**6

    Teq1 = (Is / (eps * sigma))**(0.25)
    Teq2 = ( Is / (1 - eps / 2) / sigma)**(1/4)

    time = []
    Ts1 = []
    Ts2 = []

    time.append(0)
    Ts1.append(0)
    Ts2.append(0)

    heatIn = Is

    heatOut1 = 0
    heatOut2 = 0

    heatContent1 = []
    heatContent2 = []

    heatContent1.append(heatIn - heatOut1)
    heatContent2.append(heatIn - heatOut2)

    for it in range(1,100):
        time.append(time[it-1] + timeStep)

        heatOut1 = eps * sigma * Ts1[it - 1] **4
        heatContent1.append(heatContent1[it - 1] + (heatIn - heatOut1) * timeStep * 3.14 * 10**7)
        Ts1.append(heatContent1[it] / Cp)

        heatOut2 = eps * sigma * Ts2[it - 1]** 4 / 2
        heatContent2.append(heatContent2[it - 1] + (heatIn - heatOut2) * timeStep * 3.14 * 10**7)
        Ts2.append(heatContent2[it] / Cp)

    return Teq1, Teq2, Ts1, Ts2, time


## LE PARAMETRAGE
alpha_random = 0.4
L_random = 3000

## L'EXECUTION
Teq1_Earth, Teq2_Earth, Ts1_Earth, Ts2_Earth, time = greenhouse(0.3,1350)
Teq1_Venus, Teq2_Venus, Ts1_Venus, Ts2_Venus, time2 = greenhouse(0.7,2600)
Teq1_Mars, Teq2_Mars, Ts1_Mars, Ts2_Mars, time3 = greenhouse(0.15,600)
Teq1_Random, Teq2_Random, Ts1_Random, Ts2_Random, time4 = greenhouse(alpha_random,L_random)

plt.figure(figsize=(5,5))
plt.scatter(600,Teq1_Mars,color='orange')
plt.scatter(600,Teq2_Mars,marker='*',color='orange')
plt.scatter(600,240,color='darkorange')
plt.text(600,245,'Mars',color='darkorange')

plt.scatter(1350,Teq1_Earth,color='lightblue',label='Terre')
plt.scatter(1350,Teq2_Earth,marker='*',color='lightblue')
plt.scatter(1350,295,color='blue')
plt.text(1350,300,'Terre',color='blue')

plt.scatter(2600,Teq1_Venus,color='pink',label='Vénus')
plt.scatter(2600,Teq2_Venus,marker='*',color='pink')
plt.scatter(2600,700,color='deeppink')
plt.text(2600,705,'Vénus',color='deeppink')

plt.scatter(L_random,Teq1_Random,color='black',label='Ma Planète')
plt.scatter(L_random,Teq2_Random,marker='*',color='black')
plt.text(L_random,Teq2_Random+4,'Ma Planète',color='black')

plt.xlabel('Energie solaire reçue [W/m²]')
plt.ylabel('Température d' "'" 'équilibre planétaire [K]')
#plt.legend(loc='best')
plt.tight_layout()
plt.show()


figure = plt.figure()
plt.title('Terre')
plt.plot(time, Ts1_Earth,color='blue', label='sans effet de serre')
plt.plot(time, Ts2_Earth,color='darkturquoise', label='avec effet de serre')
plt.xlabel('t [annees]')
plt.ylabel('T [K]')
plt.ylim((0,305))
plt.legend(loc=4)
plt.grid(True)
figure.show()

figure = plt.figure()
plt.title('Venus')
plt.plot(time, Ts1_Venus,color='pink',label='sans effet de serre')
plt.plot(time, Ts2_Venus,color='darkorchid',label='avec effet de serre')

plt.xlabel('t [annees]')
plt.ylabel('T [K]')
plt.ylim((0,305))
plt.legend(loc=4)
plt.grid(True)
figure.show()

figure = plt.figure()
plt.title('Mars')
plt.plot(time, Ts1_Mars,color='orange',label='sans effet de serre')
plt.plot(time, Ts2_Mars,color='darkorange', label = 'avec effet de serre')
plt.xlabel('t [annees]')
plt.ylabel('T [K]')
plt.ylim((0,305))
plt.legend(loc=4)
plt.grid(True)
figure.show()