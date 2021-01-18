n = float(input("N =>"))

n_100 = n // 100
n = n - n_100*100

n_50 = n // 50
n = n - n_50*50

n_20 = n // 20
n = n - n_20*20

n_10 = n // 10
n = n - n_10*10

n_5 = n // 5
n = n - n_5*5

n_2 = n // 2
n = n - n_2*2

n_1 = n // 1
n = n - n_1*1
n_1=float('%.2f'% n_1)
n=float('%.2f'% n)

m_50 = n // 0.5
n = n - m_50*0.5
m_50=float('%.2f'% m_50)
n=float('%.2f'% n)

m_15 = n // 0.25
n = n - m_15*0.25
m_15=float('%.2f'% m_15)
n=float('%.2f'% n)

m_10 = n // 0.10
n = n - m_10*0.10
m_10=float('%.2f'% m_10)
n=float('%.2f'% n)

m_5 = n // 0.05
n = n - m_5*0.05
m_5=float('%.2f'% m_5)
n=float('%.2f'% n)

m_1 = n * 100
m_1=float('%.2f'% m_1)
n=float('%.2f'% n)

print('-------------------------')
print('NOTAS:')
print('{} R$ 100.00'.format(int(n_100)))
print('{} R$ 50.00'.format(int(n_50)))
print('{} R$ 20.00'.format(int(n_20)))
print('{} R$ 10.00'.format(int(n_10)))
print('{} R$ 5.00'.format(int(n_5)))
print('{} R$ 2.00'.format(int(n_2)))
print('-------------------------')
print('MOEDAS:')
print('{} R$ 1.00'.format(int(n_1)))
print('{} R$ 0.50'.format(int(m_50)))
print('{} R$ 0.25'.format(int(m_15)))
print('{} R$ 0.10'.format(int(m_10)))
print('{} R$ 0.05'.format(int(m_5)))
print('{} R$ 0.01'.format(int(m_1)))