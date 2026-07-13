import hashlib
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Passe o argumento!")
    parser.add_argument("--senha", default="senha", help="Senha para criptografar")
    parser.add_argument("--algoritmo", choices=["md5", "sha1", "sha256", "sha512"], default="md5", help="Algoritmo de criptogrfia")
    return parser.parse_args()


def criptografar(senha, algoritmo):
    match algoritmo.strip().lower():
        case "md5":    return hashlib.md5(senha.encode()).hexdigest() # 32 caracteres
        case "sha1":   return hashlib.sha1(senha.encode()).hexdigest() # 40 caracteres
        case "sha256": return hashlib.sha256(senha.encode()).hexdigest() # 64 caracteres
        case "sha512": return hashlib.sha512(senha.encode()).hexdigest() # 128 caracteres
    

def main():
    args = parse_args()

    resultado = criptografar(args.senha, args.algoritmo)
   
    print(f"{args.senha} -> {args.algoritmo} -> {resultado}")

main()