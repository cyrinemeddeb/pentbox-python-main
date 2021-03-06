import pyinputplus as pyip
import pyfiglet

from SymmetricEncryption import SymmetricEncryption
from AsymmetricEncryption import AsymmetricEncryption
from Encoding import Encoding
from Hashing import Hashing

import click

def menu():
    while(True):
        choice = pyip.inputMenu(['Codage','Hachage','Cracker mot de passe','Cryptage/Decryptage symétrique','Cryptage/Decryptage asymétrique','Quitter'])
        if(choice=='Codage'):
            Encoding.menu()
        elif(choice=='Hachage'):
            Hashing.hash_menu()
        elif(choice=='Cracker mot de passe'):
            Hashing.crack_menu()
        elif(choice=='Cryptage/Decryptage symétrique'):
            SymmetricEncryption.menu()
        elif(choice=='Cryptage/Decryptage asymétrique'):
            AsymmetricEncryption.menu()
        
        elif(choice=='Quitter'):
            return



@click.command()
@click.option('-m','--mode','mode', default='rien' , help='choisir la fontion à essayer')
def main(mode):
    """
        -----------------------------------------------------------------------
        --------------------------Security Project-----------------------------
        -----------------------------------------------------------------------
        The first menu does the following : encode and decode a given text to 
          various types of encoding utf8, ascii, base16, base32, base64        
        -----------------------------------------------------------------------

    """
    if(mode=='Cryptage/Decryptage symétrique'):
        SymmetricEncryption.menu()
    if(mode=='Codage'):
        Encoding.menu()
    if(mode=='Hachage'):
        Hashing.hash_menu()
    if(mode=='Cracker mot de passe'):
        Hashing.crack_menu()
    if(mode=='Cryptage/Decryptage asymétrique'):
        AsymmetricEncryption.menu()


    if(mode=='rien'):
        menu()


if __name__ == '__main__':
    main()