import numpy as np
import matplotlib.pyplot as plt

def P_t(t):
    return np.array([
        [0.6 + 0.4 * t, 0.3 - 0.3 * t, 0.1 - 0.1 * t],
        [0.2 + 0.8 * t, 0.6 - 0.6 * t, 0.2 - 0.2 * t],
        [0.1 + 0.9 * t, 0.2 - 0.2 * t, 0.7 - 0.7 * t]
    ])

tridy = np.array([0, 30000, 100000])
pocet_obyvatel = 5000000


def uhrnny_prijem_simul(t, opakovani=1000):
    P = P_t(t)
    stavy = np.random.choice([0, 1, 2], size=pocet_obyvatel)
    
    for _ in range(opakovani):
        for i in range(pocet_obyvatel):
            pst_prechodu = P[stavy[i]]
            stavy[i] = np.random.choice([0, 1, 2], p=pst_prechodu)
    
    prijmy = tridy[stavy]
    return prijmy.sum()

tvec_simul = np.arange(0, 1.01, 0.05)
prijmy_simul = [uhrnny_prijem_simul(t) for t in tvec_simul]
laffer_simul = prijmy_simul*tvec_simul

plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.plot(tvec_simul, prijmy_simul)
plt.xlabel('Daňová sazba')
plt.ylabel('Úhrnný hrubý příjem')
plt.title('Úhrnný hrubý příjem (simulace)')

plt.subplot(1, 2, 2)
plt.plot(tvec_simul, laffer_simul)
plt.xlabel('Daňová sazba')
plt.ylabel('Úhrnný daňový výnos')
plt.title('Lafferova křivka (simulace)')

plt.tight_layout()
plt.show()


def uhrnny_prijem_anal(t, opakovani=1000):
    P = np.linalg.matrix_power(P_t(t), opakovani)
    stavy = np.random.choice([0, 1, 2], size=pocet_obyvatel)

    for i in range(pocet_obyvatel):
        pst_prechodu = P[stavy[i]]
        stavy[i] = np.random.choice([0, 1, 2], p=pst_prechodu)
    
    prijmy = tridy[stavy]
    return prijmy.sum()

tvec_anal = np.arange(0, 1.01, 0.05)
prijmy_anal = [uhrnny_prijem_anal(t) for t in tvec_anal]
laffer_anal = prijmy_anal * tvec_anal

plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.plot(tvec_anal, prijmy_anal)
plt.xlabel('Daňová sazba')
plt.ylabel('Úhrnný hrubý příjem')
plt.title('Úhrnný hrubý příjem (analyticky)')

plt.subplot(1, 2, 2)
plt.plot(tvec_anal, laffer_anal)
plt.xlabel('Daňová sazba')
plt.ylabel('Úhrnný daňový výnos')
plt.title('Lafferova křivka (analyticky)')

plt.tight_layout()
plt.show()
