import webbrowser
import fileLogic
l = []
dictionary = {}
def config(dictionary):
    str = fileLogic.rozdenienegpa2("storage.txt")
    if (str != "file is empty"):
        dictionary = str
    return dictionary
def deystviassulkoi(l, immia):
    def pechatatspisok(l):
         if len(l)==0:
              print("net cilok")
         else:
              for i in l:
                    print(l.index(i)+1,i)

    def silkaudalena(l):
         pechatatspisok(l)
         if len(l) != 0:
              print('vibirity cilku', end=' ')
              num = int(input())
              l.remove(l[num - 1]) # удаляет по значению
        #l.pop(num-1) # удаляет по индексу
              print('silka was udalena')
    def otkritsilku(l):
         pechatatspisok(l)
         if len(l) != 0:
              print('vibirity cilku', end=' ')
              num = int(input())
              webbrowser.open_new(l[num - 1])

    m=True
    while m:

          print('----------------------------------------')
          print("1) Dobavte cilku")
          print("2) Yдалить ссылку")
          print("3) Показать все ссылки")
          print("4) Oткрыть ссылку")
          print("5) Bыход")
          vubop=int(input("выберете что-то "))
          print('----------------------------------------')
          if vubop==1:
                l.append(input("dobavte cilku "))
          elif vubop==2:
                silkaudalena(l)
          elif vubop==3:
                pechatatspisok(l)
          elif vubop==4:
                otkritsilku(l)
          elif vubop == 5:
                fileLogic.rozdenienegpa(l, f'{immia}.txt')
                m=False

def imiapolzovatelia(dictionary):
    n=True
    while n:
        dictionary = config(dictionary)
        print('----------------------------------------')
        print("1) voity v acaunt")
        print("2) sozdat acaunt")
        print("3) vuity")
        num1=int(input("vuberete pynkt "))
        print('----------------------------------------')
        if num1==2:
            immia=input('viedite imia ')
            parol=input('viedite parol ')
            dictionary[immia] = parol
            fileLogic.rozdenienegpa(dictionary,"storage.txt")
            fileLogic.rozdenienegpa([], f'{immia}.txt')
            print('acaunt sozdan ')
            print('voidite v acaunt ')
            continue
        elif num1==1:
            name=input("vvedite imia ")
            parol1=input("vvedite parol ")
            if name in dictionary.keys() and parol1 == dictionary[name]:
                print('vash acaunt naiden')
                l = fileLogic.rozdenienegpa2(f'{name}.txt')
                deystviassulkoi(l,name)
            else:
                print("proverte imia and poprobuite essho raz")
                continue
        elif num1==3:
            n=False
        else:
            print('these pynkt ne naiden')