import os
import subprocess

os.system("color a")
def logo():
    os.system("color a")
    os.system("cls")
    print(14*' '+14*'*'+' 4DV4NC3D CMD '+14*'*')
    print(26*' '+' Elisário Carlos (debugger) ')
    print(19*' '+' (https://elisariocarlos.netlify.app) ')
    print()

def hideInAFile():
    logo()
    print('Nome do ficheiro principal')
    main=input('---> ')
    logo()
    print('Nome do ficheiro que queres esconder')
    toHide=input('---> ')
    logo()
    print('Nome do ficheiro final')
    final=input('---> ')
    if main!="" and toHide!="" and final!="":
        output=subprocess.getoutput(f"copy /b {main} + {toHide} {final}")
        result=output.split("\n")
        if result[2]=="        1 file(s) copied.":
            logo()
            print("Feito!")
        else:
            logo()
            print("ocorreu um erro tente novamente!")
    else:
        logo()
        print('Não preencheu todos os campos!\nTente Novamente')

def showHiddenInAFile():
    logo()
    print('Nome do ficheiro gerado')
    gerado=input('---> ')
    logo()
    formato=gerado.split(".")
    formato=formato[1]
    formato=formato.split('"')
    formato=formato[0]
    temp_name=f"random_01.{formato}"
    subprocess.getoutput(f"copy {gerado} {temp_name}")
    print('Nome novo do ficheiro')
    new_name=input('---> ')
    if gerado!="" and new_name!="":
        output=subprocess.getoutput(f"ren {temp_name} {new_name}")
        print("Feito!")
        
    else:
        logo()
        print('Não preencheu todos os campos!\nTente Novamente')

def showHiddenFile():
    logo()
    print('Nome do ficheiro ou pasta que queres mostrar')
    file=input('---> ')
    
    if file!="":
        logo()
        output=subprocess.getoutput(f"attrib -s -r -h {file}")
        print("Feito!")
    else:
        logo()
        print("Não escreveu nada!\nTente Novamente")

def hideFile():
    logo()
    print('Nome da Pasta que queres esconder')
    file=input('---> ')
    
    if file!="":
        logo()
        output=subprocess.getoutput(f"attrib +s +r +h {file}")
        print("Feito!")
    else:
        logo()
        print("Não escreveu nada!\nTente Novamente")
    
def deleteFile():
    logo()
    print('Nome do ficheiro que queres apagar')
    file=input('---> ')
    
    if file!="":
        logo()
        output=subprocess.getoutput(f"del {file}")
        print("Feito!")
    else:
        logo()
        print("Não escreveu nada!\nTente Novamente")

def mkDir():
    logo()
    print('Nome da pasta que queres criar')
    file=input('---> ')
    
    if file!="":
        logo()
        output=subprocess.getoutput(f'mkdir "{file}"')
        if output!="A subdirectory or file a already exists.":
            print("Feito!")
        else:
            print("Já existe pasta com este nome!")
    else:
        logo()
        print("Não escreveu nada!\nTente Novamente")

def wait():
    subprocess.getoutput("timeout 3600")

def _main_():
    logo()
    print('[01] - Ocultar um ficheiro em outro')
    print('[02] - Mostrar ficheiro oculto um ficheiro em outro')
    print('[03] - Ocultar um ficheiro')
    print('[04] - Mostrar um ficheiro oculto')
    print('[05] - Apagar ficheiro')
    print('[06] - Criar Pasta')
    print('[Ctrl+C] - Sair\n')
    try:
        opc=input('---> 0')
        if opc=='1':
            hideInAFile()
        elif opc=='2':
            showHiddenInAFile()
            
        elif opc=="3":
            hideFile()
            
        elif opc=="4":
            showHiddenFile()

        elif opc=="5":
            deleteFile()

        elif opc=="6":
            mkDir()
        else:
            logo()
            print('Opção Inválida\nTente Novamente')
            
    except KeyboardInterrupt:
        os.system("exit")
    
        
while True:
    try:
        _main_()
    
        input('\n\n[Enter] - Para Continuar\n')
    except KeyboardInterrupt:
        break
        os.system("exit")
    
