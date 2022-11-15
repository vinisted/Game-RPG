from time import sleep
import random
from multiprocessing import TimeoutError
from multiprocessing.pool import ThreadPool

def Inicio():
    
    input('\n~Mestre Yoda: Que a força esteja com você nobre Jedi, iniciada sua jornada está!')
    guerreiro = ''
    cont = 0
    Ato1 = 1
    LadodaForça = 1 #Lado 1 = Luminoso / Lado 2 = Sombrio

    while guerreiro == '' and cont != 4:
        cont += 1

        if cont == 1:
            guerreiro = input('~Mestre Yoda: Começar com o básico nós vamos, pode me dizer seu nome? ')
        
        elif cont == 2:
            guerreiro = input('~Mestre Yoda: O sarlacc comeu sua língua? Me diga seu nome! ')

        elif cont == 3:
            input('~Mestre Yoda: Muito rebelde você é!')
            input('~Mestre Yoda: Desistir de você eu vou!')
            Ato1 = 0
            return Ato1, LadodaForça, guerreiro

    input('~Mestre Yoda: Sinto uma forte relação sua com a força {}.'.format(guerreiro))
    input('~Mestre Yoda: Iniciar protocolo de apredizado iremos.')
    input('~Mestre Yoda: venha, seu potencial eu quero testar\n')
    
    input('Dentro da sala de treinamento...\n')

    input('~Mestre Yoda: {} o sabre de Luz eu quero que você Pegue.'.format(guerreiro))
    obdc = input(
                '\nDigite:\n'
                '(1) Pegar o sabre\n'
                '(2) Desobedecer\n'
                'Qual a sua ação? ')
    cont = 0

    while obdc != '1' and cont != 4:

        cont += 1

        if cont == 1:
            input('\n~Mestre Yoda: Um péssimo Jedi vejo que você é, infelizmente a força se atrai por você.')
            input('~Mestre Yoda: Tentar de novo nós vamos, pegue-o.')
            obdc = input(
                        '\nDigite:\n'
                        '(1) Pegar o sabre\n'
                        '(2) Desobedecer\n'
                        'Qual a sua ação? ')

        elif cont == 2:
            input('\n~Mestre Yoda: Te dar apenas mais essa chance eu vou.')
            obdc = input(
                        '\nDigite:\n'
                        '(1) Pegar o sabre\n'
                        '(2) Desobedecer\n'
                        'Qual a sua ação? ')

        elif cont == 3:
            input('\n~Mestre Yoda: Continuar eu não irei, muito indisciplinado você é!')
            Ato1 = 0
            LadodaForça = 0

    if Ato1 == 0:
        return Ato1, LadodaForça, guerreiro

    if cont == 0:
        input('\n~Mestre Yoda: Jeito para isso você tem!')
    elif cont == 1:
        input('\n~Mestre Yoda: Conseguir te dá um treinamento completo acho que ainda posso.')
    else:
        input('\n~Mestre Yoda: Pegar o sabre de luz mostrou-se ser difícil pra você, pegar leve eu irei')

    if cont == 0 or cont == 1:
        obdc = ''
        input('\n~Mestre Yoda: Muito apto para isso você é.')
        input('~Mestre Yoda: Lembre-se, a força não te torna poderoso...')
        input('~Mestre Yoda: Seu coração, sim!')

        input('\n~Mestre Yoda: Iniciar nosso treinamento nós iremos')
        input('~Mestre Yoda: A pedra pequena quero que levite.')

        obdc = input(
                    '\n'
                    'Digite:\n'
                    '(1) Obedecer a ordem de Mestre Yoda\n'
                    '(2) Obedecer parcialmente\n'
                    'Qual a sua ação? ')

        if obdc == '1':
            input('\n~Mestre Yoda: {} você será um grande Jedi!'.format(guerreiro))

        else:
            print('\n"Mestre Yoda se surpreende"\n')
            input('~Mestre Yoda: Como você fez isso?')
            input('~Mestre Yoda: Levantar a pedra pequena eu pedi e você me levanta a grande!')
            input('~Mestre Yoda: Muito poderoso você é, mas poderosos também são os inimigos!')
            input('~Mestre Yoda: Lembre-se, muito poder com indisciplina perigoso é, tomar cuidado você deve.')

    elif cont == 2:
        obdc = ''
        input('\n~Mestre Yoda: Fechar os olhos você deve. Sinta a força percorrer no seu corpo.')
        input('~Mestre Yoda: A pedra pequena quero que levite.')

        obdc = input(
                    '\n'
                    'Digite:\n'
                    '(1) Obedecer a ordem de Mestre Yoda\n'
                    '(2) Obedecer parcialmente\n'
                    '(3) Questiona-lo\n'
                    'Qual a sua ação? ')

        if obdc == '1':
            input('\n~Mestre Yoda: Começando a gostar de você estou!')
        elif obdc == '2':
            print('\n"Mestre Yoda se surpreende"\n')
            input('~Mestre Yoda: Como você fez isso?')
            input('~Mestre Yoda: Levantar a pedra pequena eu pedi e você me levanta a grande!')
            input('~Mestre Yoda: Muito poderoso você é, mas o Anakin também é.')
            input('~Mestre Yoda: Muito poder com indisciplina perigoso é, tomar cuidado você deve.')
            LadodaForça = 0

        else:
            input('\n~{}: Por que eu te obedeceria? você é só um velho muito feio!\n'.format(guerreiro))
            input('~Mestre Yoda: Muita indisciplina existe em você!')
            input('~Mestre Yoda: Continuar o treinamento você não deve, voltar para sua família você vai...')
            Ato1 = 0
            LadodaForça = 0

    if Ato1 == 0:
        return Ato1, LadodaForça, guerreiro

    if obdc == '1' or obdc == '2':
        input('\n~Mestre Yoda: Com os olhos fechados traga a pedra até você.')
        obdc = input(
                    '\n'
                    'Digite:\n'
                    '(1) Obedecer a ordem de Mestre Yoda\n'
                    '(2) Surpresa...\n'
                    'Qual a sua ação? ')

        

        if obdc == '1':
            input('\n~Mestre Yoda: Muito bom {}!'.format(guerreiro))
            LadodaForça = 1

        else:
            input('\n(respirando ofegante)')
            input('(Semblante começa a cair...)')

            input('\nTentativas depois...\n')
            input('~Mestre Yoda: Te deixando triste alguma coisa está')
            input('~Mestre Yoda: O que houve pequeno Jedi?')
            surp = input(
                        '\n'
                        'Digite:\n'
                        '(1) Não me sinto capaz, mestre\n'
                        '(2) Sinto saudade de minha falecida mãe\n'
                        'Qual a sua ação? ')
            
            if surp == '1':
                input('\n~Mestre Yoda: Jovem {}, Insegurança sentimos sempre.'.format(guerreiro))
                input('~Mestre Yoda: O seu diferencial é como reagir.')
                input('~Mestre Yoda: Erga-se e levante essa pedra!')

            else:
                input('\n~Mestre Yoda: Oh jovem jedi, grandes aprendizados nossas perdas nos trazem!')
                input('~Mestre Yoda: Uma grande guerreira sua mãe foi!')
                input('~Mestre Yoda: Certeza tenho que orgulho ela sentiria de você.')
                input('~Mestre Yoda: Tente novamente!')

            obdc = input('\nDigite "1" para obedecer: ')
            cont = 0

            while obdc != '1' and cont != 4:
                
                cont += 1

                if cont == 1:
                    input('\n~Mestre Yoda: Conseguir eu sei que você vai!')
                    obdc = input('\nDigite "1" para obedecer: ')
                
                elif cont == 2:
                    input('\n~Mestre Yoda: Tentar apenas mais uma vez você deve!')
                    obdc = input('\nDigite "1" para obedecer: ')

                else:
                    input('\n~Mestre Yoda: Forçar você eu não irei, enviar você de volta nós iremos.')
                    Ato1 = 0
                    LadodaForça = 1
                    return Ato1, LadodaForça, guerreiro

        input('\n~Mestre Yoda: Você conseguiu!')
        input('~Mestre Yoda: Continue a confiar na força!')
        input('~Mestre Yoda: Aliada e sua amiga ela é!')
        input('~Mestre Yoda: O proximo passo eu irei dar.')
        input('~Mestre Yoda: Com dois golpes em quatro pedaços parta a pedra.')

        obdc = input('\nDigite "1" para obedecer: ')
        cont = 0

        while obdc != '1' and cont != 4:
            cont += 1

            if cont == 1:
                input('\n~Mestre Yoda: Sei que você consegue!')
                obdc = input('\nDigite "1" para obedecer: ')

            elif cont == 2:
                input('\n~Mestre Yoda: Conseguir você irá!')
                obdc = input('\nDigite "1" para obedecer')
            
            elif cont == 3:
                input('\n~Mestre Yoda: Cansado você está, parar por aqui iremos.')
                return Ato1, LadodaForça, guerreiro

        input('\n~Mestre Yoda: Muito bem {}, suas habilidades em batalha quero ver!'.format(guerreiro))
        input('~Mestre Yoda: O treinamento terminado está!')
        input('~Mestre Yoda: Boa sorte grande Jedi, que a força esteja com você!')

    return Ato1, LadodaForça, guerreiro

def GrandeAto(guerreiro, LadodaForça):
    def Jedi(decisão, guerreiro, LadodaForça):

        def luta(seg):
            def timeout(seconds):
                def decorator(function):
                    def wrapper(*args, **kwargs):
                        pool = ThreadPool(processes=1)
                        result = pool.apply_async(function, args=args, kwds=kwargs)
                        try:
                            return result.get(timeout=seconds)
                        except TimeoutError as e:
                            return e
                    return wrapper
                return decorator

            @timeout(seg)

            def Resposta():
                return input()

            acertos = 10
            Ato2 = 1

            for i in range (10):

                golpe = str(random.randint(1,99))
                print('\nDigite "{}" para acertar o golpe: '.format(golpe), end = '')
                name = Resposta()

                if isinstance(name, TimeoutError):
                    Ato2 = 0
                    return acertos, Ato2
                
                if name == golpe:
                    print('acertou')

                else:
                    print('errou')
                    acertos -= 1

            return acertos, Ato2

        def luta2(seg):
            def timeout(seconds):
                def decorator(function):
                    def wrapper(*args, **kwargs):
                        pool = ThreadPool(processes=1)
                        result = pool.apply_async(function, args=args, kwds=kwargs)
                        try:
                            return result.get(timeout=seconds)
                        except TimeoutError as e:
                            return e
                    return wrapper
                return decorator

            @timeout(seg)

            def Resposta():
                return input()

            acertos = 10
            Ato2 = 1

            for i in range (10):

                num1 = random.randint(1,9)
                num2 = random.randint(1,9)
                print('\nDigite quanto é {} + {} para acertar o golpe: '.format(num1,num2), end = '')
                soma = num1 + num2
                name = Resposta()

                if isinstance(name, TimeoutError):
                    Ato2 = 0
                    return acertos, Ato2
                
                if name == str(soma):
                    print('acertou')

                else:
                    print('errou')
                    acertos -= 1

            return acertos, Ato2

        def luta3(seg):
            def timeout(seconds):
                def decorator(function):
                    def wrapper(*args, **kwargs):
                        pool = ThreadPool(processes=1)
                        result = pool.apply_async(function, args=args, kwds=kwargs)
                        try:
                            return result.get(timeout=seconds)
                        except TimeoutError as e:
                            return e
                    return wrapper
                return decorator

            @timeout(seg)

            def Resposta():
                return input()

            acertos = 15
            Ato2 = 1

            for i in range (15):

                num1 = random.randint(1,10)
                num2 = random.randint(1,5)
                print('\nDigite quanto é {} * {} para acertar o tiro: '.format(num1,num2), end = '')
                mult = num1 * num2
                name = Resposta()

                if isinstance(name, TimeoutError):
                    Ato2 = 0
                    return acertos, Ato2
                
                if name == str(mult):
                    print('acertou')

                else:
                    print('errou')
                    acertos -= 1

            return acertos, Ato2

        Vidas = 5
        Morte = 1

        while Vidas > 0:

            if Morte == 1:
                input('\nVocê tem {} Vidas!'.format(Vidas))

            else:
                print('\nVidas: {}'.format(Vidas))
                input('Tecle "enter" para continuar ')
                Morte = 1

            if Vidas < 5:

                input('\nPor meio de uma mensagem de voz em seu comunicador, a Princesa Leia te passou algumas informações.\n')

                input('~Princesa Leia: O alojamento de Padawans foi atacado, a sua missão é ajudar todos os feridos e combater os droids inimigos enviados para atacar o local')
                input('~Princesa Leia: Nesse momento, você é o Jedi mais capacitado no local para ajudar a todos, mas existe um droid do tipo C-3PO preso em algum lugar')
                input('~Princesa Leia: A sua eficiência não é tão boa na batalha, mas caso encontre-o, terá acesso a senha do Terminal do computador central do alojamento')
                input('~Princesa Leia: Com ele você poderá acessar o complexo com as naves mais facilmente e fujir com todos os socorridos')
                input('~Princesa Leia: TOME CUIDADO, nesse processo não sabemos com certeza')
                input('~Princesa Leia: Identificamos uma nave desconhecida em direção a seu planeta, PODE SER ALGUM INIMIGO!')
                input('~Princesa Leia: Caso consiga sair com os refugiados, voe para o planeta Dagobah, mas tome cuidado com as criaturas aquaticas')
                input('~Princesa Leia: Iremos resgata-los assim que possível, há muita traição e choro por onde andamos!')
                input('~Princesa Leia: Sabemos que você é um grande Jedi e está capacitado para essa missão!')
                input('~Princesa Leia: Boa sorte {}, espero te encontrar em breve, que a força esteja com você!'.format(guerreiro))

                input('\n~{}: Quanta bagunça, por onde eu começo?'.format(guerreiro))

                decisão = input(
                                '\nDigite:\n'
                                '(1) Procurar por refugiados\n'
                                '(2) Procurar o droid C-3PO\n'
                                'Qual a sua ação? ')

            if decisão == '2': #Game over
            
                input('\n~{}: Primeiramente irei resgatar o C-3PO'.format(guerreiro))
                input('~{}: Tenho que descobrir onde ele está!'.format(guerreiro))
                input('\nAo seu redor existem apenas 3 sáidas')
                input('\nA primeira te leva para o complexo das naves, mas a única entrada de fácil acesso está destruída')
                input('A segunda te leva para o alojamento de Padawans, que é onde se encontram a maioria das crianças')
                input('A terceira, te leva para o complexo geral, contendo a sala do terminal do alojamento, o refeitório e a área de lazer')
                input('\nPara onde você vai?')

                decisão = input(
                                '\nDigite:\n'
                                '(1) Ir para o complexo das naves\n'
                                '(2) Ir para o alojamento de Padawans\n'
                                '(3) Ir para o complexo geral\n'
                                '(4) Decidir fugir\n'
                                'Qual a sua ação? ')

                if decisão == '1':
                    input('\nUm droid de reconhecimento avistou você')
                    input('Ele enviou uma mensagem para a nave que a Leia havia mencionado que estava a caminho de seu planeta')
                    input('Era realmente uma nave inimiga...')
                    input('Após vê-lo, facilmente você derrotou o droid, mas...\n')
                    input('A nave estava apenas a alguns quilometros de distância de você')
                    input('Como não sabia, você continuou correndo até a entrada do complexo, mas a nave inimiga atirou e te atingiu')
                    input('\nVocê não resistiu!')
                    Ato2 = 0
                    Vidas -= 1
                    Morte = 0

                elif decisão == '2':
                    input('\n~{}: Acredito que seja melhor salvar as crianças primeiro!'.format(guerreiro))
                    input('\nIndo para o alojamento, um droid B1 te avistou')
                    input('\n~Droid B1: Venham, encontrei um deles aqui!')
                    input('\nOs Droids B1 se reunem e atacam você e os outros 5 padawans')

                    input('\nVocê terá 1,5 segundos para acertar os golpes!')
                    input('Instrução: Aparecerá números para você digitar, cada acerto é um golpe bem executado')
                    input('Caso não digite nada, você será atingido e morrerá!')
                    print('\nContagem regressiva para iniciar...\n')

                    for i in range (5,0,-1):
                        print('Batalha em: {} seg'.format(i))
                        sleep(1)

                    Luta = luta(1.5) #Luta[0] = acertos, Luta[1] = Ato2

                    acertos = Luta[0]
                    Ato2 = Luta[1]

                    if Ato2 == 0 or acertos == 0:
                        if acertos == 0:
                            print('\nVocê foi abatido!\n')
                        else:
                            print('\nDemorou demais!\n')

                    elif acertos < 7:
                        input('\nApós a luta, você conseguiu derrotar os inimigos')
                        input('Mas com um total de apenas {} acertos, você ficou gravemente ferido')
                        input('\nVocê não resistiu...')

                    else:
                        input('\nMesmo acertando vários droids, seu blaster parou de funcionar')
                        input('Como ainda haviam bastante para derrotar, eles te atingiram com vários tiros')
                        input('\nVocê não resistiu...')

                    Vidas -= 1
                    Morte = 0

                elif decisão == '3':
                    input('\nNo caminho para o complexo geral, você ouviu gritos de socorro vindos de uma das salas do complexo')
                    input('Os gritos ecoam sempre de forma diferente')
                    input('A cada grito, como se fosse uma lingua diferente')
                    input('\n~{}: C-3PO!'.format(guerreiro))
                    input('~{}: Só me resta agora descobrir de que sala vem tanto barulho'.format(guerreiro))
                    input(
                        '\nDigite:\n'
                        '(1) Sala do terminal\n'
                        '(2) refeitório\n'
                        '(3) Área de lazer\n'
                        'Qual a sua ação? ')

                    input('\nAo decidir qual sala entrar, um droid de reconhecimento te avistou e atirou em você')
                    input('Você ficou ferido mas não foi abatido')
                    input('O droid do império havia sido informado de uma nave vindo em direção a seu planeta')
                    input('A mesma nave que Leia informou')
                    input('Ele enviou uma mensagem para a nave informando que havia te avistado')
                    input('Mas logo após uma luta, você conseguiu abater o droid')
                    input('Durante esse tempo, a luta te empurrou para dentro da sala do terminal, onde os gritos de socorro se intensificavam')
                    input('Você descobriu onde o droid está, mas...')
                    input('\n"Barulho de droid se movendo!"')
                    input('\nUm dos droids B1, ouve seu barulho dentro da sala')
                    input('O império havia enviado uma escolta para obter informações')
                    input('Os droids prenderam o C-3PO para obte-las')
                    input('Após perceber o movimento na sala, você se esconde, e ao olhar no canto da parede, percebe que a escolta enviada é muito grande')
                    input('Mas parece se ter uma opção')
                    input('A sua frente se encontra uma granada, você pode usa-la, mas se fizer isso vai alertar todos os droids')
                    input('Lembre-se, você está ferido e sua mobilidade não é muito boa')
                    input('A estrátegia a pegar a bomba é correr para fora da sala do terminal, jogar a bomba, e fechar a porta')
                    input('Lembre-se, ao fazer isso o droid com as informações (C-3PO) também será abatido')
                    input('Além disso, você pode tentar combater os droids com com seu sabre de luz')
                    input('Não é uma decisão inteligente, pois existem muitos droids, mas é uma opção')
                    input('E você ainda pode optar por sair da sala.')

                    decisão = input(
                                '\nDigite:\n'
                                '(1) Pegar a bomba\n'
                                '(2) Força bruta\n'
                                '(3) Sair da sala\n'
                                'Qual a sua ação? ')

                    if decisão == '1':
                        input('\nVocê conseguiu pegar a bomba')
                        input('Os droids te viram e um deles conseguiu te atingir enquanto corria')
                        input('Mesmo ferido você resistiu e continuou com o plano')
                        input('Chegou a porta')
                        input('Jogou a granada')
                        input('E fechou...')
                        input('Você se jogou no chão enquanto ouvia o barulho da explosão')
                        input('Enquanto chorava no chão')
                        input('Ouviu barulho de passos correndo até você')
                        input('\n~{}: Deve ser os Padawans\n'.format(guerreiro))
                        input('Enquanto aguardava no chão e ouvia os passos')
                        input('Os passos se itensificavam')
                        input('Ao olhar para cima...')
                        input('\n~{}: Ah, não!!!'.format(guerreiro))
                        input('\n~{}: CLONES!\n'.format(guerreiro))
                        input('Clones que estavam na nave que Leia informou foram contatados pelo droid que você abateu antes de entrar na sala')
                        input('Os clones seguiram o barulho da explosão e te encontrou')
                        input('Você tentou fugir')
                        input('Mas como já estava muito ferido e cansado, não conseguiu ir muito longe')
                        input('Os clones te acertaram com vários tiros')
                        input('Você não resistiu...')
                        Ato2 = 0
                        Vidas -= 1
                        Morte = 0

                    elif decisão == '2':
                        input('\nVocê se levantou e começou a atacar os droids')
                        input('Os droids te viram e começaram a atirar')
                        input('Mesmo ferido você resistiu e continuou com o plano')
                        input('De repente...')
                        input('Tiros vem da parte de trás da sala do terminal')
                        input('Clones que estavam na nave que Leia informou foram contatados pelo droid que você abateu antes de entrar na sala')
                        input('Um dos tiros pegou na granada')
                        input('Você se jogou no chão enquanto ouvia o barulho da explosão')
                        input('Após ser gravemente ferido')
                        input('Ouviu barulho de passos correndo até você')
                        input('Enquanto aguardava no chão ferido, e ouvia os passos')
                        input('Os passos se itensificavam...')
                        input('Ao olhar para cima...')
                        input('Os clones te acertaram com vários tiros')
                        input('Você não resistiu...')
                        Ato2 = 0
                        Vidas -= 1
                        Morte = 0
                        

                    else:
                        input('\nVocê conseguiu de modo furtivo fugir da sala')
                        input('Mesmo ferido você resistiu e continuou com o plano')
                        input('Ao sair da sala')
                        input('Ouviu barulho de passos correndo até você')
                        input('\n~{}: Deve ser os Padawans\n'.format(guerreiro))
                        input('Enquanto corria e ouvia os passos')
                        input('Os passos se itensificavam')
                        input('Ao dobrar o corredor...')
                        input('\n~{}: Ah, não!!!'.format(guerreiro))
                        input('\n~{}: CLONES!\n'.format(guerreiro))
                        input('Clones que estavam na nave que Leia informou foram contatados pelo droid que você abateu antes de entrar na sala')
                        input('Os clones seguiram o sinal que o droid enviou')
                        input('Você tentou fugir')
                        input('Mas como já estava ferido e cansado, não conseguiu ir muito longe')
                        input('Os clones te acertaram com vários tiros')
                        input('Você não resistiu...')
                        Ato2 = 0
                        Vidas -= 1
                        Morte = 0

                else:
                    input('\nApós correr para encontrar a saída do complexo das naves...')
                    input('\nUm droid de reconhecimento avistou você')
                    input('Ele enviou uma mensagem para a nave que a Leia havia mencionado que estava a caminho de seu planeta')
                    input('Era realmente uma nave inimiga...')
                    input('Após vê-lo, facilmente você derrotou o droid, mas...\n')
                    input('A nave estava apenas a alguns quilometros de distância de você')
                    input('Após decidir fugir você conseguiu sair do alojamento, mas a nave te avistou e com alguns tiros')
                    input('\nVocê não resistiu!')
                    Ato2 = 0
                    LadodaForça = 0
                    Vidas -= 1
                    Morte = 0

            elif decisão == '1':
                input('\n~{}: Primeiramente irei resgatar os padawans'.format(guerreiro))
                input('~{}: Tenho que correr para a o alojamento deles!'.format(guerreiro))
                input('~{}: Acredito que a maioria está lá!'.format(guerreiro))
                input('\nIndo para o alojamento dos Padawans')
                input('\nBarulho de droid\n')
                input('~{}: Tenho de ir devagar!'.format(guerreiro))
                input('\nVocê se escorou na parede do corredor e avistou o outro lado\n')
                input('~{}: Droga, um droid de reconhecimento'.format(guerreiro))
                input('~{}: Vou aguardar chegar perto para poder atacar'.format(guerreiro))
                input('\nAguardando...\n')
                input('Após chegar bem perto...\n')
                input('Barulho de sabre("Zoom, zoom, zoomm")\n')
                input('~{}: Boa, vou continuar a seguir!'.format(guerreiro))
                input('~{}: Estou bem perto de chegar'.format(guerreiro))

                input('\nChegando no alojamento...\n')
                input('Padawans se aproximam de surpresa!!!')
                input('\nVocê se asusta!\n')
                input('~{}: Calma crianças, vim ajudar!'.format(guerreiro))
                input('~Padawans: {}!!!'.format(guerreiro))
                input('\nMomento de comemoração e abraços...\n')
                input('~{}: Façam silencio!'.format(guerreiro))
                input('~{}: Acredito que existam muitos droids aqui, estão todos bem?!'.format(guerreiro))
                input('~Padawans: Estamos todos bem!')
                input('~{}: Vamos, precisamos encontrar o C-3PO e sair daqui!'.format(guerreiro))
                input('\nUm dos Padawans chamam sua atenção\n')
                input('~Padawan: {}!'.format(guerreiro))
                input('~{}: Fala pequeno Padawan!'.format(guerreiro))
                input('~Padawan: Vimos uma tropa de B1 levando o C-3PO em direção ao Complexo Geral')
                input('~{}: Pois é para lá que nós iremos!!!'.format(guerreiro))

                input('\nO complexo geral é composto por três salas')
                input('A sala do terminal, a cozinha e a área de lazer')
                input('No caminho')
                input('\nVocês ouvem gritos de socorro vindos de uma das salas do complexo')
                input('Os gritos ecoam sempre de forma diferente')
                input('A cada grito, como se fosse uma lingua diferente')
                input('\n~Todos: C-3PO!\n')
                input('~{}: De onde será que vem esse barulho?'.format(guerreiro))
                input('~{}: Crianças fiquem aqui'.format(guerreiro))
                input('~{}: Vou procurar o C-3PO'.format(guerreiro))
                input('\nPara onde você vai?')

                guardar = ''
                decidir = input(
                                '\nDigite:\n'
                                '(1) Sala do terminal\n'
                                '(2) Refeitório\n'
                                '(3) Área de lazer\n'
                                'Qual a sua ação? ')
                if decidir == '1':
                    guardar = 'a Sala do Terminal'

                elif decidir == '2':
                    guardar = 'o Refeitório'

                else: 
                    guardar = 'a Area de lazer'

                input('\nNo caminho para entrar n{}, um droid de reconhecimento avistou uma das crianças e atirou'.format(guardar))
                input('ela ficou ferida, mas não foi abatida')
                input('O droid do império havia sido informado de uma nave vindo em direção a seu planeta')
                input('A mesma nave que Leia informou')
                input('Ele enviou uma mensagem para a nave informando que havia encontrado você e as crianças')
                input('Mas logo após uma luta, você conseguiu abater o droid')
                input('\n~{}: Você está bem Padawan?'.format(guerreiro))
                input('~Padawan: Vou aguentar, procure o C-3PO')
                input('\nEnquanto isso, saiu um droid B1 da Sala do Terminal ao ouvir o barulho')
                input('\n~Droid B1 (Alerta toda a tropa): Vejam, as crianças estão aqui!')
                input('~{}: Levem o ferido para um abrigo. Os mais velhos, me ajudem a derrota-los!'.format(guerreiro))
                input('\n5 Guerreiros dos 48 que tinham ficaram para te ajudar')
                input('O restante das crianças foram a procura de um abrigo')

                input('\nEnquanto isso na batalha...')

                while Vidas > 0:

                    if Morte == 0:
                        print('\nVidas: {}'.format(Vidas))
                        Morte = 1
                        input('Tecle "enter" para continuar ')

                    input('\nOs Droids B1 se reunem e atacam você e os outros 5 padawans')
                    input('\nVocê terá 2,7 segundos para acertar os golpes!')
                    input('Instrução: Aparecerá números para você digitar, cada acerto é um golpe bem executado')
                    input('Caso não digite nada, você será atingido e morrerá!')
                    print('\nContagem regressiva para iniciar...\n')

                    for i in range (5,0,-1):
                        print('Batalha em: {} seg'.format(i))
                        sleep(1)

                    Luta = luta(2.7) #Luta[0] = acertos, Luta[1] = Ato2

                    acertos = Luta[0]
                    Ato2 = Luta[1]

                    if Ato2 == 0 or acertos == 0:
                        if acertos == 0:
                            print('\nVocê foi abatido!\n')
                        else:
                            print('\nDemorou demais!\n')
                        Vidas -= 1
                        Morte = 0

                    elif acertos < 7:
                        input('\nApós a luta, você conseguiu derrotar os inimigos')
                        input('Mas com um total de apenas {} acertos, 2 dos seus padawans mais experientes, morreram na batalha'.format(acertos))
                        input('A ajuda agora é menor, mas o objetivo continua sendo o mesmo')
                        input('Reuna todos os que ficaram vivos e corra para fugir')

                        decidir = input(
                            '\nDigite:\n'
                                    '(1) Pegar o C-3PO\n'
                                    '(2) Fugir com os padawans\n'
                                    'Qual a sua ação? ')

                        if decidir == '1':
                            input('\nAo entrar na sala que se encontrava o C-3PO')
                            input('Você conseguiu resgatá-lo!')
                            input('\n~C-3PO: Que bom finalmente poder encontrá-los!')
                            input('~{}: Também é bom te ver C-3PO'.format(guerreiro))
                            input('~{}: Estamos com pressa, vamos, precisamos acessar o complexo das naves e fugir!'.format(guerreiro))
                            input('\nEnquanto isso...')

                            input('\nUma tropa de clones enviada pelo imperio (A mesma mencionada por Léia) foi contatada pelos droids B1')
                            input('Eles avistaram você e os outros 3 padawans no corredor e começaram a atacar')

                            input('\nVocê terá 3,5 segundos para acertar os golpes!')
                            input('Instrução: Aparecerá um calculo para resolver, cada acerto é um golpe bem executado')
                            input('Caso não digite nada, você será atingido e morrerá!')
                            print('\nContagem regressiva para iniciar...\n')

                            for i in range (5,0,-1):
                                print('Batalha em: {} seg'.format(i))
                                sleep(1)

                            Luta = luta2(3.5) #Luta[0] = acertos, Luta[1] = Ato2

                            acertos = Luta[0]
                            Ato2 = Luta[1]

                            if Ato2 == 0 or acertos < 8:
                                if acertos < 8:
                                    print('\nVocê foi abatido!\n')
                                else:
                                    print('\nDemorou demais!\n')
                                Vidas -= 1
                                Morte = 0

                            else:
                                input('Mesmo atingindo a quantia de {} acertos, você ficou gravemente ferido e seus padawans não resistiram'.format(acertos))
                                input('Vocês foram abatidos...')
                                Vidas -= 1
                                Morte = 0

                        else:
                            input('\n~{}: Vamos padawans, precisamos nos apressar!'.format(guerreiro))
                            input('~Padawans: Como vamos sem o C-3PO? Será bem mais custoso de abrirmos a porta do complexo!')
                            input('~{}: Infelizmente não há tempo, temos que buscar os outros e ir agora!'.format(guerreiro))
                            input('Enquanto isso...')
                            input('\nUma tropa de clones enviada pelo imperio (A mesma mencionada por Léia) foi contatada pelos droids B1')
                            input('Eles avistaram você e os outros 3 padawans no corredor e começaram a atacar')

                            input('\nVocê terá 3,5 segundos para acertar os golpes!')
                            input('Instrução: Aparecerá um calculo para resolver, cada acerto é um golpe bem executado')
                            input('Caso não digite nada, você será atingido e morrerá!')
                            print('\nContagem regressiva para iniciar...\n')

                            for i in range (5,0,-1):
                                print('Batalha em: {} seg'.format(i))
                                sleep(1)

                            Luta = luta2(3.5) #Luta[0] = acertos, Luta[1] = Ato2

                            acertos = Luta[0]
                            Ato2 = Luta[1]

                            if Ato2 == 0 or acertos < 7:
                                if acertos < 7:
                                    print('\nVocê foi abatido!\n')
                                else:
                                    print('\nDemorou demais!\n')
                                Vidas -= 1
                                Morte = 0

                            else:
                                input('Mesmo atingindo a quantia de {} acertos, você ficou gravemente ferido e seus padawans não resistiram'.format(acertos))
                                input('Vocês foram abatidos...')
                                print('\nVocê foi abatido!\n')
                                Vidas -= 1
                                Morte = 0

                    else:

                        while Vidas > 0:

                            if Morte == 0:
                                print('\nVidas: {}'.format(Vidas))
                                Morte = 1
                                input('Tecle "enter" para continuar ')

                            input('\nToda tropa de B1 foi abatida, aparentemente não há mais nenhum droid inimigo no local')
                            input('\n~{}: Todos estão bem?'.format(guerreiro))
                            input('~Padawans: Sim, senhor!')
                            input('~{}: Vamos, precisamos resgatar o C-3PO e ir embora agora mesmo!'.format(guerreiro))
                            input('\nNa sala que estava o C-3PO...')
                            input('\n~C-3PO: Que bom vê-los, quanta alegria!')
                            input('~{}: Também é bom te ver C-3PO, mas temos que ir, o império está com tudo contra nós, vamos!'.format(guerreiro))
                            input('~C-3PO: Preciso acessar o terminal para liberar o acesso ao complexo!')
                            input('~{}: Rápido!'.format(guerreiro))
                            input('\n~C-3PO: OH, NÃO!')
                            input('~{}: O que houve?'.format(guerreiro))
                            input('\nO C-3PO acessou toda central do refúgio e percebeu duas coisas')
                            input('\n~C-3PO: Precisamos de um plano!')
                            input('~C-3PO: Veja, a entrada principal para o complexo das naves está em ruina')
                            input('~C-3PO: Uma nave do império com uma tropa de clones acaba de chegar pelo portão principal')
                            input('\n~C-3PO: Só temos acesso ao complexo das naves pela entrada da oficina! ')
                            input('~C-3PO: O que faremos?')

                            decidir = input(
                                '\nDigite:\n'
                                        '(1) Atacar os clones e roubar a nave deles\n'
                                        '(2) Acessar o complexo das naves pela oficina de modo furtivo\n'
                                        'Qual a sua ação? ')

                            if decidir == '1':
                                input('\n~{}: Vamos pegar os pequenos padawans e batalhar com os clones'.format(guerreiro))
                                input('~{}: Parece a forma mais arriscada de se conseguir'.format(guerreiro))
                                input('~{}: Mas, assim podemos acessar a sala com as armas que fica no mesmo corredor de acesso a saída'.format(guerreiro))
                                input('~{}: Estão todos de acordo?'.format(guerreiro))
                                input('~Todos: Sim, senhor!')
                                input('\nApós resgatar os pequenos padawans, todos andaram em direção a sala com as armas')
                                input('Cada um dos padawans se armaram de alguma maneira para ajudar no confronte')
                                input('Ao seguir para a saída, todos se escoderam de maneira estratégica e atacaram o máximo de clones de maneira furtiva')
                                input('Mas como é de se esperar...')
                                input('\n~{}: Eles nos viram, ataquem!!!'.format(guerreiro))

                                input('\nVocê terá 3 segundos para acertar os golpes!')
                                input('Instrução: Aparecerá um calculo para resolver, cada acerto é um golpe bem executado')
                                input('Caso não digite nada, você será atingido e morrerá!')
                                input('O exército de clones é bem maior que o seu, então só sobreviverá se acertar pelo menos 8 golpes')
                                print('\nContagem regressiva para iniciar...\n')

                                for i in range (5,0,-1):
                                    print('Batalha em: {} seg'.format(i))
                                    sleep(1)

                                Luta = luta2(3) #Luta[0] = acertos, Luta[1] = Ato2

                                acertos = Luta[0]
                                Ato2 = Luta[1]

                                if Ato2 == 0 or acertos < 8:
                                    if acertos < 8:
                                        print('\nVocê foi abatido!\n')
                                    else:
                                        print('\nDemorou demais!\n')
                                    Vidas -= 1
                                    Morte = 0

                                else:
                                    input('\nApós uma longa luta, todos os clones foram destruídos')
                                    input('A batalha foi árdua e todos os seus guerreiros lutaram muito bem')
                                    input('Os custos da batalha sempre geram grandes sequelas, 5 dos seus melhores guerreiros foram abatidos')
                                    input('A dor, toma de conta de todos os corações, mas a vitória enfim foi alcançada')
                                    input('Algumas das crianças gravemente feridas, outras sem alguns dos membros')
                                    input('\n~{}: Vamos, entrem rápido na nave, precisamos ir logo, precisamos de tratamento urgente!!'.format(guerreiro))
                                    input('\nTodos entraram na nave e fugiram')
                                    input('Das 48 crianças 43 saíram com vida!')

                                    return Ato2, LadodaForça, guerreiro

                            else:
                                input('\n~{}: Vamos pegar os pequenos padawans e ir para o nosso acesso ao complexo!'.format(guerreiro))
                                input('~{}: Estão todos de acordo?'.format(guerreiro))
                                input('~Todos: Sim, senhor!')
                                input('\nApós resgatar os pequenos padawans, todos andaram em direção a entrada da oficina')
                                input('Pois era o melhor acesso ao complexo das naves')
                                input('Cada um dos padawans se protegiam uma direção para que nada de ruim ocorresse')
                                input('Ao seguir para a saída, todos observavam de maneira extremamente cuidadosa')
                                input('Chegando no complexo, perceberam que havia uma nave funcionando')
                                input('As crianças entraram rapidamente')

                                input('Ao tentar ligar o motor, ele falhou e o barulho chamou atenção dos clones')
                                input('Eles começaram a atirar para abrir uma entrada no complexo e os tiros começaram a pegar na nave')
                                input('~{}: Preciso desviar os tiros com golpes de sabre!'.format(guerreiro))

                                input('\nVocê terá 3 segundos para desviar os tiros!!!')
                                input('Instrução: Aparecerá um calculo para resolver, cada acerto é um golpe bem executado')
                                input('Caso não digite nada, a nave será atingida várias vezes e explodirá!')
                                input('Os clones usaram armas poderosas para atingir vocês, cada tiro é fatal')
                                input('Só será possível escapar caso acerte pelo menos 8 golpes')
                                print('\nContagem regressiva para iniciar...\n')

                                for i in range (5,0,-1):
                                    print('Batalha em: {} seg'.format(i))
                                    sleep(1)

                                Luta = luta2(3) #Luta[0] = acertos, Luta[1] = Ato2

                                acertos = Luta[0]
                                Ato2 = Luta[1]

                                if Ato2 == 0 or acertos < 8:
                                    if acertos < 8:
                                        print('\nVocê foi abatido!\n')
                                    else:
                                        print('\nDemorou demais!\n')
                                    Vidas -= 1
                                    Morte = 0

                                else:
                                    input('\nAo sair do complexo, os clones começaram a seguir a sua nave')
                                    input('\n~{}: Eles nos viram, precisamos atacar!!!'.format(guerreiro))
                                    input('~{}: Algum dos padawans, consegue manusear o blaster da nave?'.format(guerreiro))
                                    input('~Padawan: Senhor, consigo pilotar a nave!')
                                    input('~{}: Não temos muitas opções, venha garoto!'.format(guerreiro))

                                    input('\nVocê terá 5 segundos para acertar os tiros!!!')
                                    input('Instrução: Aparecerá um calculo para resolver, cada acerto é um golpe bem executado')
                                    input('Caso não digite nada, vocês serão atingidos e morrerão!')
                                    input('A nave dos clones é bem melhor que o sua, então só sobreviverá se acertar pelo menos 10 tiros!')
                                    print('\nContagem regressiva para iniciar...\n')

                                    for i in range (5,0,-1):
                                        print('Batalha em: {} seg'.format(i))
                                        sleep(1)

                                    Luta = luta3(5) #Luta[0] = acertos, Luta[1] = Ato2

                                    acertos = Luta[0]
                                    Ato2 = Luta[1]

                                    if Ato2 == 0 or acertos < 10:
                                        if acertos < 10:
                                            print('\nVocê foi abatido!\n')
                                        else:
                                            print('\nDemorou demais!\n')
                                        Vidas -= 1
                                        Morte = 0

                                    else:
                                        input('\n"Som de nave explodindo": BOOOOOOOOOOMMMMMM!!!!!')
                                        input('\nTodos comemoram!!!')
                                        input('Você conseguiu, resgatar todos com vida!')

                                    return Ato2, LadodaForça, guerreiro

        return Ato2, LadodaForça, guerreiro

    def Sith(decisão, guerreiro, LadodaForça):

        def sluta(seg):
            def timeout(seconds):
                def decorator(function):
                    def wrapper(*args, **kwargs):
                        pool = ThreadPool(processes=1)
                        result = pool.apply_async(function, args=args, kwds=kwargs)
                        try:
                            return result.get(timeout=seconds)
                        except TimeoutError as e:
                            return e
                    return wrapper
                return decorator

            @timeout(seg)

            def Resposta():
                return input()

            acertos = 10
            Ato2 = 1

            for i in range (20):

                golpe = str(random.randint(1,99))
                print('\nDigite "{}" para acertar o golpe: '.format(golpe), end = '')
                name = Resposta()

                if isinstance(name, TimeoutError):
                    Ato2 = 0
                    return acertos, Ato2
                
                if name == golpe:
                    print('acertou')

                else:
                    print('errou')
                    acertos -= 1

            return acertos, Ato2

        if LadodaForça == 1:
            input('\nUm droid de reconhecimento avistou você')
            input('Ele enviou uma mensagem para a nave que a Leia havia mencionado que estava a caminho de seu planeta')
            input('Era realmente uma nave inimiga...')
            input('Após vê-lo, facilmente você derrotou o droid, mas...\n')
            input('A nave estava apenas a alguns quilometros de distância de você')
            input('Após decidir fugir você conseguiu sair do alojamento, mas a nave te avistou e com alguns tiros')
            input('\nVocê não resistiu!')
            Ato2 = 0
            LadodaForça = 0

            return Ato2, LadodaForça, guerreiro

        else:
            input('\n~{}: Preciso encontrar uma saída para o complexo das naves'. format(guerreiro))
            decisão = input(
                            '\nDigite:\n'
                            '(1) Procurar complexo das naves\n'
                            '(2) Voltar atrás e resgatar os padawans\n'
                            'Qual a sua ação? ')
            
            if decisão == '1':
                input('\nApós um tempo de procura...')
                input('~{}: Estou perto!'.format(guerreiro))
                input('\nBarulho de algo caindo!!!\n')
                input('~{}: Droga, deve ser um droid miserável'.format(guerreiro))
                input('\nO droid de reconhecimento te viu!')
                decisão1 = input(
                    '\nDigite:\n'
                    '(1) Correr\n'
                    '(2) Se esconder\n'
                    'Qual a sua ação? ')
                if decisão1 == '1':
                    input('\nApós uma tentativa de correr, seu pé enganchou em uma ruina do alojamento')
                    input('O droid se aproximou lentamente e com um tiro de seu bláster te atingiu gravemente')
                    input('Você não resistiu...')
                    Ato2 = 0

                    return Ato2, LadodaForça, guerreiro

                if decisão1 == '2':
                    input('\nApós correr um pouco e se esconder, o droid te perdeu de vista')
                    input('Ele se aproxima lentamente para perto do seu local')
                    input('~{}: Devo me preparar para atacar'.format(guerreiro))
                    input('O droid está em sua frente e você o ataca com êxito\n')
                    input('Mas outro droid no mesmo corredor te vê e corre atrás de você')
                    input('Ao sair correndo você encontra uma brecha para entrar no complexo de naves, mas seu pé prende em uma ruína')
                    input('Você usa o sabre de luz mas não consegue retira-lo totalmente')
                    input('Enquanto isso, o droid se aproxima atirando, e atinge sua perna, fazendo que você se solte mas te ferindo na panturrilha')
                    input('Você o atinge com um golpe e consegue abate-lo\n')
                    input('Ao entrar no complexo, você dá de cara com uma nave do império com tripulantes que havia sido enviado para eliminar o restante dos Padawans')
                    input('Você se arma para se defender')
                    input('Mas os Clones declaram honra a você')
                    input('Dizem que receberam ordens para te levar para um lugar de honra, pois você era uma segunda opção depois de Anakin')
                    decisão1(
                        '\nDigite:\n'
                        '(1) Aceitar proposta\n'
                        '(2) Recusar\n'
                        '\nQual a sua ação? ')
                    
                    if decisão1 == '1':
                        input('\nApós entrar na nave, os Clones lançam uma bomba que destroi todo o alojamento junto de todos os padawans')
                        input('Na viagem, você é levado para conhecer o palpatine')
                        input('Leia havia te dito que sabia que havia uma nave desconhecida a caminho do seu planeta')
                        input('Ela enviou um X-Wing próximo para verificar se era você, pois percebeu que a mesma nave havia saído do planeta')
                        input('O x-wing se aproxima e pergunta...')
                        input('~Piloto: {} é você que está pilotando?'.format(guerreiro))
                        decisão1 = input(
                                        '\nDigite:\n'
                                        '(1) Assumir a culpa\n'
                                        '(2) Continuar com o plano e tentar abater o X-Wing\n'
                                        'Qual a sua ação? ')
                        
                        if decisão1 == '1':
                            input('\n~{}: Sou eu sim, mas estou como inimigo!'.format(guerreiro))
                            input('~Piloto: Brincadeira cara, que desgraçado!')
                            input('~Piloto: Leia, encontramos mais um traidor, seu amigo {}'.format(guerreiro))
                            input('~Piloto: Permissão para abater o caça, senhora!')
                            input('~Princesa Leia: Faça!')
                            input('\nApós uma luta entre você e os Clones e o X-Wing, a sua nave foi abatida')
                            Ato2 = 0
                            LadodaForça = 0

                            return Ato2, LadodaForça, guerreiro

                        else:
                            input('\n~{}: Sou eu sim, consegui resgatar uns poucos padawans!'.format(guerreiro))
                            input('~Piloto: Que feliz em te ouvir {}!'.format(guerreiro))
                            input('~Piloto: Estou louco pra ouvir essa história!')
                            input('\nO piloto do X-Wing percebeu que havia um Clones correndo para dentro da nave e notou algo estranho')
                            input('~Piloto: {} cuidado, vi um Clone dentro da sua nave eles são nossos inimigos!')
                            input('Você atira no X-Wing mas não o atinge')
                            input('O piloto percebe o que aconteceu')
                            input('\nApós uma luta entre você o X-Wing, a sua nave foi abatida')
                            Ato2 = 0
                            LadodaForça = 0

                            return Ato2, LadodaForça, guerreiro

                    else:
                        input('\nEu prefiro morrer!')
                        input('Após a luta, você percebe que sua perna está muito machucada')
                        input('Os Stormtoopers venceram essa e conseguiram tirar a sua vida')
                        Ato2 = 0
                        LadodaForça = 0

                        return Ato2, LadodaForça, guerreiro

            else:
                input('\n~{}: Que lixo de Jedi eu me tornei?'.format(guerreiro))
                input('~{}: Preciso voltar logo, existem crianças precisando de mim!'.format(guerreiro))
                input('\n~{}: Acredito que seja melhor salvar as crianças primeiro!'.format(guerreiro))
                input('\nIndo para o alojamento, um droid B1 te avistou')
                input('\n~Droid B1: Venham, encontrei um deles aqui!')
                input('\nOs Droids B1 se reunem e te atacam')

                input('\nVocê terá 1,5 segundos para acertar os golpes!')
                input('Instrução: Aparecerá números para você digitar, cada acerto é um golpe bem executado')
                input('Caso não digite nada, você será atingido e morrerá!')
                print('\nContagem regressiva para iniciar...\n')

                for i in range (5,0,-1):
                    print('Batalha em: {} seg'.format(i))
                    sleep(1)

                Luta = sluta(1.5) #Luta[0] = acertos, Luta[1] = Ato2

                acertos = Luta[0]
                Ato2 = Luta[1]

                if Ato2 == 0 or acertos == 0:
                    if acertos == 0:
                        print('\nVocê foi abatido!\n')
                    else:
                        print('\nDemorou demais!\n')

                elif acertos < 7:
                    input('\nApós a luta, você conseguiu derrotar os inimigos')
                    input('Mas com um total de apenas {} acertos, você ficou gravemente ferido')
                    input('\nVocê não resistiu...')

                else:
                    input('\nMesmo acertando vários droids, seu blaster parou de funcionar')
                    input('Como ainda haviam bastante para derrotar, eles te atingiram com vários tiros')
                    input('\nVocê não resistiu...')

                return Ato2, LadodaForça, guerreiro

        return Ato2, LadodaForça, guerreiro
    
    input(
        '\n'
        ' __________________________________________________________________________________________________ \n'
        '|_________________________________________Algum tempo depos..._____________________________________|\n')
    input('\nApós um longo período de aprendizado')
    input('Houve uma grande traição na República')
    input('Muitas mortes e traições foram registradas')
    input('O Imperador Palpatine assumiu o poder, transformando a grande República no império galáctico')
    input('O lado sombrio toma de conta após descobrirem que dentro do Representante da República havia um grande Viláo...')
    input('\nDarth Sidious!\n')
    print(
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#######!!!########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##########!!!#########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#############!!###########!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##############!!########@#!!#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###############@@@@####@@###!!#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#############@@@@@@@##@@@@#######!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!############@@@@@#@@@#@#@#####!###!!!!!!!!!!!!!!!!!!!!!!::::!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!############@##:::!!#@@@@###########!!!!!!!!!!!!!!!!::::.  .::!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:!#####!####@@@@#::###!#@@#@############!!!!!!!!!!!!:::..    .:::!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!::!!########!###@@#!........:!##@########!!###!!!!!!!::::.     .::::!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:::::::!##########@@#!:!::..:::#!:#@########!!!!!#!!!:::::.     .::::!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:::::!##!!########@@@###!:!!!##!#!:!###########!!!!!!!::.     .::::!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!:!:::::::######@@####@@@@#::::::###:::::!########!!!!!!!:.     .:::::!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!:::::::!#########@@@##@@@@@@#::.:::::::::!########!!!!!:.     .:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!::!::::!!@###########@@@@@@@@@@@@#!....:::##########!!!:.    .::!!!!####!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!:::::!!!#!@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@############!!!:.    .:!!!!!######!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!:!!!!!!!!!:!:::!#@#@@#@@@@@@@@@@@@@@@@@#######@@@@@@@@#########!!:.     :!!!!!!!!#####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!:!!::!::::::!!!!!##!!##@@@##@@@@@@@@@@@@@@#######@@@##########!!:.    .:!!!############!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!::!!!!!:::!##@@@@@@#@@@##@@##@@@@@@@@@@@@@@@###!!#####!#!#!!!:.    .:!!#####!####@@#####@@:!!!!!!!!!!!!!!::!!!:!!!!!!!\n'
        '!!!!:!:::!@@#@@#@##@#@@@#@@@#!##@@@#@@@@@@@@@@@##!!#####!!!:.     .:!!##########@###@@@##@@@#!::!!::!!::!!::::!!:::::!:!\n'
        '!!!!!!!!:::#@@#####@@######@@@###@#@@@@@@@@#######!!!!!!:.    .:!!!#########@@@@@@@@@@@@@@@@@#:::::!!:::::::::::::::::::\n'
        '!:::::::::::#@@@@@@#@@@@####@@@@##@@@@###########!!::..    .:!!!#########@@@@@@@@@@@@@@@@@@@##!:::::::::::::::::::::::::\n'
        '::::::::::!##@@@#@@@@@@@@@@@@#@@@@@@@#######!!!!!:.     .:!!!#########@@@@@@@@@@@@@@@@@@@@@@##!:::::::::::::::::::::::::\n'
        ':::::::::!##@####@@@@@@@@@@@@#@@@#########!!!::.    ..:!!#########@@@@@@@@@@@@@@@@@@@@@@@@#####!::::::::::::::::::::::::\n'
        ':!::::::::!####@##@@@@@@@@@@@##########!!!:.     .:!!!!########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#!#!!:::::::::::::::::::::::\n'
        ':!::::::::!###@@@##@@@@@###########!!!::.     .:!!!!!!######@@@@@@@@@@#!!######@@@@@@@@@@@@@@@#!!:::::::::::::::::::::::\n'
        '::::::::::#@@@@######@@####:.::::!!::.    .::!!!###!#####@@@@@@@@@@@##@@####!#####@@@@@@@@@@@@@#!!::::::::::::::::::::::\n'
        '::::::::::::###@@@@#@@@##!:..:....     .:!!!!#####!###@@@!:::..###@@@@@##############@@@@@@@@#@@@!::::::::::::::::::::::\n'
        ':::::::::::::::!!#@#@@@##:::::.     .:!!!#######!!####@@@@####!::...::###@@@###@@@##!!##@@@@@@@##@!:::::::::::::::::::::\n'
        ':::::::::::::::::::::###!:::.:. ...:!!!!########!!###@@@@@@@@@@#:.::::::###@@@@@@@@@@@@####@@@@@#!!:::::::::::::::::::::\n'
        '::::::::!!!!:::::::::::::::!::::::!:!!!####@@##!#!##@@@@@@@@@@@@##!!::.::#@@@@@@@@@@@@@@@##!!@@@##!!::::::::::::::::::::\n'
        '::::::::!!!!::::::::::::::::!!!!########@@@@####!!@#@@@@@@@@@@@@##::::::!##@@@@@@@@@@########!#@##!!::::::::::::::::::::\n'
        '::::!!!!!!!!!!!!:::::::::::::::::######@@@@#####!###@@@@!::::!#@@#!#######@@@@@@@@@@@@@@###@######!!::::::::::::::::::::\n'
        '!!!!!!!!!!!!!!!!:!!::::::::::::::#@@@@@@@@#######@#@@@@@@@#::....:!!!####@@@@@@@@@@@##@@@###@@@###!:::::::::::::::::::::\n'
        ':!!!!!!!!!!!!!!!!!!:::::::::::::!#@@@@@@@########@##@@@@@@#####!:!####@@@@@@@@@@@@@#!###@@#@@@@@##!!!::::::::!::::::::::\n'
        '!!!!!!!!!!!!!!!!!!!!!!:::::::::!####@@@@@#######@@###@@@@@#!#####@@@@@@@@@@@@@@@@@##!#####@#@@@@@#!!!!!:::!!!!!!!!!:::!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!:::::!!###@@@@@@@@#####@#####@@@@#@@@@@@@@@@@@@@@@@@@@@@@@########@@@@@@#!!!!!!:::!!!::!:!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!::::!####@@###@@@@###@##@####@@@@@@@@@@@@@@@@@@@@@@@####@#@@@@@@@@###!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!############@@@##@@#######@@@@@@@@@@@@@@@@@@@@@@@#####@@@@#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##############@@@@#########@@@@@@@@@@@@@@@@@@@@@@@####@@#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#################@@@@########@@###@@@@@@@@@@@@@@@@@@@@@@@@#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#################@@@@###########@@@@@@@@@@##@@@@@@@@@@@@@@@#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!#################@@@@@###############@@@@######@@#@@@@@@@@@@#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!##################@@@@@######################@@@@@###@@@@@@@@@#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!#################@@@@@@###################@@@@@@@@###@@@@@@@@##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!############@####@@@@@@####################@@@@@@@###@@@@@#######!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')

    input('Juntamente com o Imperador Palpatine, o grande Jedi Anakin foi corrompido.')
    input('Um colápso na galáxia está por vir com o nascimento do grande vilão Darth Vader.')
    print(
        '###################!!!!!!!!!!!!!##!!!!!!!!!!!!!!#!.  ..:::!#.#####:##########!##########@#############@@@@##@@@@@@@@@@@@\n'
        '###################!!!!!!!!!!!!!!!!!!!!!!!!!!!#!!......::!!##################!#!!########@#############@#@@@@@@@@@@@@@@@\n'
        '####################!#!!!!!!!!##!!!!#!!!!!!!!#!!......::!!######@@##############!#########################@@@@@@@@@@@@@@\n'
        '####################!!!!!!!!!!##!#!#!#!!!!!!#!#.:...::!!!#######@@###############:######################@@@@@@@@@@@@@@@@\n'
        '###############################!###!!!!!!!##!#!...::!:..:!#@##@@@@#########@############################@@@@@@@@@@@@@@@@\n'
        '####################!#####!!!!!!!!###!!!###!##.::::::!#####@##@@@@#@@#####!!######:######################@@@@@@@@@@@@@@@\n'
        '#############!#######!###!##!##!!!!!###!###!!!!.:!:!#######@##@@@@@@@@######@@########@#################@@@@@@@@@@@@@@@@\n'
        '###############!##!##!!!!#!!!!!!#!#!##!!!####.::!!#####!###@##@@@@@@@@@@#@@@#@###!!#####################@##@@#@@@@@@@@@@\n'
        '#######!#############!!!!##!!!!!!!!#!!##!!!##.::!!########@@##@@@@@@@@@@#@@@@@######@##################@@####@@@@@@@@@@@\n'
        '#######!###########!!!!!!!####!!#!!!!!!!!!!#!!:!###!!#####@@@#@@@@@@@@@@@@@@@@@####.##################@########@@@@@@@@@\n'
        '#################!!!!!!!#!####!!!!!!!!!!!!!!#!.!###!!#####@@@@@@@@@@@@@@@@@@@@@###!#@################@###########@@@@@@@\n'
        '#####!!##########!!!!!!!###!##!!!!!!!!!!!!!!:!.!###!.!###@@#@@@@@@@@@@@@@@@@@@@###:#@###########################@@@@@@@@\n'
        '#!####!!#########!!!!!!######!##!!!!!!!!!!!!.!:!###!.!###@#@@@@@@@@@@@@@@#!#@@@@#################################@@@####\n'
        '############!#!!#!!!!#######!!!!!!#!!!!!!!!!.!:!###! .###@#@@@@@@@@@@@@@@@#:::#@########################################\n'
        '######!!!#####!!!!!!!!#####!!!!!!!!!!!!!!!!!.:!####!..!##@@@@#@@@@@@@@@@@@#@@!:!###############################@@#@#@@##\n'
        '####!!!#!!!###!!!!!!!!!##!!#!!!!!!!!!!!!!!!!..!!#!###!!#@@@@@@@@@@@@@@@@@@@@@@@#!!##:############################@@#@@##\n'
        '######!!######!!!!!!!#!!####!!!!!!!!!!!!!!!!.:!####@####@@@@@@@@@@@@@@@@@@@@@@@@##!#:##############################@#@@@\n'
        '####!##########!!!!!##!!!#!#!!!!!!!!!!!!!!!!.!!#######@@@@@@@#@@@@@@@@@@@@@@@@@@@@#################################@#@@@\n'
        '#######!##!#########!!!!!!#!#!!!!!!!!!!!!!!!.####!#!#!###@@@@#@@@@@@@###@@@@@@@@####################################@#@@\n'
        '#####!#############!#####!#!#!!!!!!!!!!!!!!.!!!!!.:!:!#####@@#@@@@@@#!######@@@#:####################################@@#\n'
        '###!!!!!!#######!#!!##!#!!!!!!!!!!!!!!!!!!!..!!!:.:!.!!#####@#@@@@@##!#!####@@@@!:###!##################################\n'
        '###!!!!!!#!!#!##!!!######!!!!!!!!!!!!!#!!!!.!!!!:......:####@#@@@@@#!!##!.:!#:##@@@################################@#@##\n'
        '#!!!!!!!!################!!!!!!!!!!!!!!!!!.!!!!#@@@@@@@@@#####@@@@@#:!@@@@@@@@@####@#################################@@#\n'
        '#!!!!!!!#################!!!!!!!!!!##!!!!!.#!#@@@@@@@####@@@######!@@######@@@@@@@:!##!#################################\n'
        '#!!!!!!#!!#!#######!!!!!!!!!!!!!!!!!!!!!!.!#@@@@@@@@@##!!#@@@#####@@###!:!#@@@@@@@@####!#############################@##\n'
        '#!!!!!!!!!#!###!###!!!!!!!!!!!!!!!!!!!!!!.!@@@@@@@@@@@#####@@@@@@#@@@#####!#@@@@@@@@!!###############################@##\n'
        '#!!!#!!!#!####!!!#!!!!!!!!!!!!!!!!!!!!!!.!#@@@@@@@@@@#######!####@@##!!::!#@@@@@@@@@@!##!###################@#@####@####\n'
        '##!!!!!!!##!!!#!!!#!!!!!!!!!!!!!!!!!!!!::#@@@@@@@@@@@###!!####!##@@########@@@@@@@@@@@!#!######################@########\n'
        '#!!!!!!!!##!!!!!!!!!!!!!!!!!!!!!!!!!!!!.!#@@@@@@@@@@@#########!#######@###@@@@@@@@@@@@@!#!##############################\n'
        '#!!!!!!!!!!!!!!!!!!!:::::::!:!!!!!!!!!:!#@@@@@@@@@@@#@@@@@@@@######@@@@@##@@#@@@@@@@@@@#################################\n'
        '###!#!!##!!!!!!!!::!!!!!####!:::::::!!:##@@####@@@@@!@##@@@@#!!!##@#@@@##@@@@@@@@@@@@@@@################################\n'
        '#####!!!#!!!!!!::!!!:!!!!!!####!!###!!:!#########@@@@@@######!####@#######@@@#@@@@@@@@@@#!##############################\n'
        '###!#!!!!!!!!::!#############!########:#########@@@@##@@##!#!#@@@@!#@#######:@@@@@@@###@@!:###############@############@\n'
        '####!!!::!:!###################################@@@@#:.!:!#:!@@@@@@@#@@##@@#@#@@@@@@@@@######################@###########\n'
        '###!!::!!!!!!!!!###############################@@!...##!:!:@@@@@@@@@####!@#!@@@@@@@@@@#@######################@######@##\n'
        '##!::!!!!!!!########################... !######!.:#!#@@#!::@@@@@@@@@@###!#@:@@@@@@@@@@#@@@@##################@#@@###@@@@\n'
        '#!!!#!!############################!.:###!#@@#.:####@@@@#!:@@@@@@@@@@@#####@@@@@@@@@@@@@@##@##############@@@#@#@###@@@@\n'
        '########@@@@###@##@@@@@@@@@@#######.:!@@@##!!!#######@@@@##.@@@@@@@@@@@#!!!@@@@@@@@@@@@@@@@@##############@@@@@@@##@@@@@\n'
        '#########@@@@@@##!#@@@@@@@@@@@@####..#@@@#########!##@@@@@##!###########!::@@@@@@@@@@@@@@@@@@@######@@@@@@@@@##@@@@@@@@@\n'
        '#!##!######@@@!#@#!#@@@@@@@::!!####.#@@@@@!##!!##!::@!!@@@##:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####@@#@#@@@@@@@@@@@@@@\n'
        '####!!###@@@###@@###@##@@# ..:####@:!@@@@#:###:.....!#::@!::.:#@@@@#######@#@@@@###@@@@@@@@@@@@@@#####@@@@@@@@@@@@@@@@@@\n'
        '###########!##@@@@@@###@@ .!!!#!#@@#:@@@@#:##!#:.....##.:    :####!!:!##@@@@@@@@####@@@@@@@@##@@@@@@@@#######@@@@@@@@@@@\n'
        '######@@@@!#@@#!#@@@@@@@@.:!#@@#!@@@#@#!::.!!:::!!::!#@#...  .@@@@#@@@@@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@####@@@@@@@@@\n'
        '#######@@#@#@@@#@@@##@@@@::@@@@!!@@@!#.   .!!:..:::.!#@@#....:@@@@##@@###@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@\n'
        '#######@#####@@@@@@##@#!#!#@@@@!!####:     #!::::..!###@@@@##@@@@@@#########@@@@@@@@#####@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@\n'
        '###@@@#@#@@@@@##@@##@!:@@#@@@@@!!###@!     #!::!:!####!@##@@@@@@@@@@#######!@@@@@@@@#####@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@\n'
        '##@########@###@@@@@!!#@#@@@@@@!###!!#    .#!!#####!!######@@@@@@@@@#######!@@@@@@@@#######@#@@@@@@@@@@####@@@@@@@@@@@@@\n'
        '#####@@#####@##@@#@#:####@@@@@#!#####!:..######!!!!!###!###@@@@@@@@@####!!!#@@@@@@@##########@##@@@@@@@@@@@@#####@@@@@@#\n'
        '####@@#####@@#@@@@@.!####@@@@#!.##!!!!######!!!!!:!!!##:###@@@@@@@@@@###!!!#@@@@@@@##########@@###@@@@@@@@@@@@@@@@@@####\n'
        '#####@#####@@@@@@@!!###!!#@@@#!.!!###!!###!!!!!::::::!#!!###@@@@@@@@@###!!!!@@@@@@@###########@@@@@#@@@@@@@#############\n'
    )

    input('\nEnquanto isso...\n')
    input('\nPor meio de uma mensagem de voz em seu comunicador, a Princesa Leia te passou algumas informações.\n')

    input('~Princesa Leia: O alojamento de Padawans foi atacado, a sua missão é ajudar todos os feridos e combater os droids inimigos enviados para atacar o local')
    input('~Princesa Leia: Nesse momento, você é o Jedi mais capacitado no local para ajudar a todos, mas existe um droid do tipo C-3PO preso em algum lugar')
    input('~Princesa Leia: A sua eficiência não é tão boa na batalha, mas caso encontre-o, terá acesso a senha do Terminal do computador central do alojamento')
    input('~Princesa Leia: Com ele você poderá acessar o complexo com as naves mais facilmente e fujir com todos os socorridos')
    input('~Princesa Leia: TOME CUIDADO, nesse processo não sabemos com certeza')
    input('~Princesa Leia: Identificamos uma nave desconhecida em direção a seu planeta, PODE SER ALGUM INIMIGO!')
    input('~Princesa Leia: Caso consiga sair com os refugiados, voe para o planeta Dagobah, mas tome cuidado com as criaturas aquaticas')
    input('~Princesa Leia: Iremos resgata-los assim que possível, há muita traição e choro por onde andamos!')
    input('~Princesa Leia: Sabemos que você é um grande Jedi e está capacitado para essa missão!')
    input('~Princesa Leia: Boa sorte {}, espero te encontrar em breve, que a força esteja com você!'.format(guerreiro))

    input('\n~{}: Quanta bagunça, por onde eu começo?'.format(guerreiro))

    decisão = input(
                    '\nDigite:\n'
                    '(1) Procurar por refugiados\n'
                    '(2) Procurar o droid C-3PO\n'
                    '(3) Fugir\n'
                    'Qual a sua ação? ')

    if decisão == '1' or decisão == '2':

        LadodaForça = 1
        jedi = Jedi(decisão, guerreiro, LadodaForça)

        Ato2 = jedi[0]
        LadodaForça = jedi[1]
        return Ato2, LadodaForça, guerreiro

    else:
        sith = Sith(decisão, guerreiro, LadodaForça)
        Ato2 = sith[0]
        LadodaForça = sith[1]
        return Ato2, LadodaForça, guerreiro

def Fim(guerreiro):
    input(
        '\n'
        ' __________________________________________________________________________________________________ \n'
        '|________________________________________Chegando em Dagobah...____________________________________|\n')

    input('\n~{}: Finalmente chegamos a Dagobah'.format(guerreiro))
    input('\nApós alguns dias de abrigo')
    input('Leia conseguiu enviar naves para resgatar a todos')
    input('Todos foram contemplados com uma grande festa e comemorações')
    input('Você, foi nomeado por leia como um grande defensor da aliança rebelde')
    input('\n')
    input(
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@::::@@@:::!@@@@@@#:::::@@@@@:::#@@@:::#@@@@@@@@@@@@@@@@!.::@@@@@:::!@@@:::::.:@@@@@:::!@@@@#:::#@@@@!:::@@@@@@@@@\n'
        '@@@@@@@:..:@@@:..!@@@##..:#@::.!#@@...#@@#...#@@@@@@@@@@@@@@@@!...@@@@@:..!@@@@#...#@@@@@@.....##@#...#@@@@!..:@@@@@@@@@\n'
        '@@@@@@@@@.......@@@@@:..:@@@@@...@@...#@@#...#@@@@@@@@@@@@@@@@!...@#.#@:..!@@@@#...#@@@@@@...!@:......#@@@@!..:@@@@@@@@@\n'
        '@@@@@@@@@@#...#@@@@@@##..:#@::.!#@@...#@@#...#@@@@@@@@@@@@@@@@!....:#:....!@@@@#...#@@@@@@...!@@@#!...#@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@:::::::@@@@@@@@#.::::@@@@@::::....::#@@@@@@@@@@@@@@@@!.::@@@@@:::!@@@::..:::@@@@@..:!@@@@#.::#@@@@!..:@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

def GameOver():
    print(
        '\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@!!!@@@@@@@@@@@@@!!!!!!!@@@@@@@!!!!!!!@@@@!!!!!!@@@@!!!!!!!@@@@@@@@@@@@@@!!@@@@@@\n'
        '@@@@@@!@@@@@!!!!!!!!!!!!!!!:@@@@@@@@@!!!!!@@@@@@!!!!@@@@@@!!!!!!@@@@!!!!!!!!!!!!@@@@@@\n'
        '@@@@@@!@@@@!!!!!@@@@@@!!!!:@@@@@:@@@@@!!!@@@@@@@@!!@@@@@@@@!!!!!@@@@@@@@@@@@!!!!@@@@@@\n'
        '@@@@@@!@@@@!!!!!!!@@@@!!!!@@@@@!!!@@@@@!@@@@@!@@@@@@@@!@@@@@!!!!@@@@!!!!!!!!!!!!@@@@@@\n'
        '@@@@@@!!@@@@@!!!!!@@@@!!!@@@@@@@@@@@@@@@@@@@!!!@@@@@@!!!@@@@@!!!@@@@@@@@@@@@@@@!@@@@@@\n'
        '@@@@@@!!!!@@@@@@@@@@@@!!@@@@@!!!!!!!@@@@@@@!!!!!@@@@!!!!!@@@@@!!@@@@@@@@@@@@@@@!@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@!!!!@@@@@@@@@@!!!!!@@@@@!!!!!!!@@@@@!!!@@@@@@@@@@@@@@@!!@@@@@@@@@@@@@@!!!!@@@@@@\n'
        '@@@@@@!@@@@@!!!!!!@@@@!!!!@@@@@!!!!!@@@@@!!!!@@@@!!!!!!!!!!!!!@@@@@@!!!!!@@@@!!!@@@@@@\n'
        '@@@@@@!@@@@!!!!!!!!@@@@!!!!@@@@@!!!@@@@@!!!!!@@@@@@@@@@@@@!!!!@@@@@@!!!!@@@@@!!!@@@@@@\n'
        '@@@@@@!@@@@!!!!!!!!@@@@!!!!!@@@@@!@@@@@!!!!!!@@@@!!!!!!!!!!!!!@@@@@@@@@@@@!!!!!!@@@@@@\n'
        '@@@@@@!!@@@@@@@@@@@@@@!!!!!!!@@@@@@@@@!!!!!!!@@@@@@@@@@@@@@@@!@@@@@@!!!@@@@@@!!!@@@@@@\n'
        '@@@@@@!!!!!@@@@@@@@!!!!!!!!!!!@@@@@@@!!!!!!!!@@@@@@@@@@@@@@@@!@@@@@@!!!!!!@@@@@!@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')

def Menu():

    input(
        '\nIntruções básicas para o jogo:\n'
        '- Sempre que aparecer uma mensagem, digite enter para continuar\n'
        '- Só digite algo caso o jogo peça\n'
        '\nDigite "enter" para continuar ')

    print(
        '\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::#::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@:::::::@@@@@@@@@!::::::@@@::::::::::@::::::@@!::::::@@@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@!::::::::::::::::@::::::#@@::::::::::::#::::::::::::::::@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@!::::::::::::::@:::::::@@::::::@!:::::!!:::::::::::::::@@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@@@::::::::@@!:::::::@!::::::!!:::::::::::::::#:::::::@:::::::!@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@@@@:::::::::::::::::::#@::::::::::::::#@@@:::::::@:::::::@@!:::::::!@@@@@@@@@@@@@@@@@\n'
        '@#@@@@@@@@@@@@@@@@@#!!!!!!!!!!!!!!#@@@!!!!!!!!!!!!!!#@@@@!!!!!!!!@!!!!!!!#@@@!!!!!!!!@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@@@::::::@@@!::::::@@@@:::::::#:::::::::!!:::::::::::::::@:::::::::::::::::#@@@@@@@@@@@@\n'
        '@@@@@@@@@@@@@::::::!@@::::::::@@#::::::!@:::::::::::!!:::::::::::::::::::::::::::::::::::@@@@@@@@@@@\n'
        '@@@@@@@@@@@!::::::@::::::::::!!:::::::@:::::::::::::!!::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@\n'
        '@@@@@@@@@#::::::::::::::::::::::::::@:::::::::::::::!!::::::::::::::::::!:::::::::::::::::::!@@@@@@@\n'
        '@@@@@@@@::::::::::::#:::::::::::::@::::::::!@:::::::!!:::::::::::::::#@@@@@@@@@@@@@!::::::::::#@@@@@\n'
        '@@@@@@::::::::::::@@!:::::::::::@!::::::::::::::::::!!::::::::@::::::::@@@:::::::::@@@::::::::::@@@@\n'
        '@@@@:::::::::::@@@@#::::::::::#:::::::::#@@@@:::::::!!::::::::@@#::::::::!@::::::::::::::::::::::#@@\n'
        '@@#::::::::::@@@@@@:::::::::@#::::::::@@@@@@#:::::::!#::::::::!@@@!:::::::::!:::::::::::::::::::::@@\n'
        '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
        ' __________________________________________________________________________________________________ \n'
        '|_______________________________________Uma história em paralelo___________________________________|')

    game = Inicio()

    Guerreiro = game[2]
    LadodaForça = game[1]
    continuar = game[0]

    while continuar == 0:
        GameOver()
        print('\nDeseja tentar novamente?')
        TryAgain = input(
                        '\nDigite:\n'
                        '(1) Sim\n'
                        '(2) Não\n'
                        'Qual a sua ação? ')

        if TryAgain == '1':
            game = Inicio()

            Guerreiro = game[2]
            LadodaForça = game[1]
            continuar = game[0]

        else:
            break

    if continuar == 1:
        game = GrandeAto(Guerreiro, LadodaForça)

        Guerreiro = game[2]
        LadodaForça = game[1]
        continuar = game[0]

        while continuar == 0:
            GameOver()
            print('\nDeseja tentar novamente?')
            TryAgain = input(
                            '\nDigite:\n'
                            '(1) Sim\n'
                            '(2) Não\n'
                            'Qual a sua ação? ')

            if TryAgain == '1':
                game = GrandeAto(Guerreiro, LadodaForça)

                Guerreiro = game[2]
                LadodaForça = game[1]
                continuar = game[0]

            else:
                break

    if continuar == 1:
        Fim(Guerreiro)

Menu()