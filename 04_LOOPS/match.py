a = int(input('Enter you desired Number'))

match(a):
    case 1 :
        print('you won bike')
    case 3 :
        print('you won nothing')
    case 7 :
        print('you won $5000')
    case _ :
        print('Thank you for participating')