import argparse
import string
from password import Password

parser = argparse.ArgumentParser(prog = 'Генератор Паролей')
parser.add_argument('-n','--num', type = int, help = 'Количество создаваемых паролей', default = 1, required = False)
parser.add_argument('-l','--length', type = int, help = 'Длина создаваемых паролей', default = 11, required = False)
parser.add_argument('-a','--alphabet', choices = ['lowercase', 'uppercase', 'digits', 'symb'],
                    help = 'Вывести содержимое алфавита для составления паролей', nargs = '+',
                    default = ['lowercase', 'uppercase', 'digits', 'symb'], required = False)
                    
args = parser.parse_args()

alpha = {'lowercase': string.ascii_lowercase, 'uppercase': string.ascii_uppercase, 'digits': string.digits, 'symb': string.punctuation}
charsets = [alpha[a] for a in args.alphabet]
password_generator = Password(charsets)

for i in range(args.num):
	print('Сгенерированный пароль:', password_generator.generate(args.length))
	if args.length < 11:
		print('Warning! Ваш пароль слишком легкий! Желательно сгенерировать надежный пароль, состоящий минимум из 11 символов!')
		

