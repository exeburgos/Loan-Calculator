# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:45:39 2020

@author: exebu
"""
import sys
import math
import argparse

def periods(principal, payment, interest):
    interest = interest / 12 / 100
    per = math.ceil(math.log(payment / (payment - interest * principal), (1 + interest)))
    final(per)
    return per

def payment(principal, periods, interest):
    interest = interest / 12 / 100
    pay = principal * interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1)
    print('Your annuity payment = {}!'.format(math.ceil(pay)))
    return math.ceil(pay)

def principal(payment, periods, interest):
    interest = interest / 12 / 100
    prin = payment * ((1 + interest) ** periods - 1) / (interest * ((1 + interest) ** periods))
    print('Your loan principal = {}!'.format(str(math.ceil(prin))))
    return math.ceil(prin)

def overpayment(periods, payment, principal):
    over = periods * payment - principal
    print('Overpayment =' + str(over))

def differentiated_payments(principal, periods, interest):
    over = 0
    interest = interest / 12 / 100
    for monthly in range(1, periods + 1):
        dp = (principal / periods) + interest * (principal - ((principal * (monthly - 1)) / periods))
        print('Month {0}: payment is {1}'.format(monthly, math.ceil(dp)))
        over += math.ceil(dp)
    print('\nOverpayment =' + str(over- args.principal))
        
def final(result):
    if result < 12:
        print('It will take {0} month{1} to repay the loan'.format(result % 12, 's' if result % 12 != 1 else ''))
    elif result % 12 == 0:
        print('It will take {0} year{1} to repay the loan'.format(result // 12, 's' if result // 12 != 1 else ''))
    else:
        print('It will take {0} year{1} and {2} month{3} to repay the loan'.format(result // 12, 's' if result // 12 != 1 else '', result % 12, 's' if result % 12 != 1 else ''))
def input_verifier():
    arguments = sys.argv
    args = [element.split('=') for element in arguments[1:]]

    count = 0
    
    for element in args[1:]:
        if element[0] == '--interest':
            count +=1
            break       
    if count == 0:
        print('Incorrect parameters.')
        sys.exit()
    elif len(args) < 4:
        print('Incorrect parameters.')
        sys.exit()
    elif args[0][1] not in ['diff', 'annuity']:
        print('Incorrect parameters.')
        sys.exit()
    elif args[0][1] not in ['diff', 'annuity'] and '--payment' in args[:][0]:
        print('Incorrect parameters.')
        sys.exit()
    for element in args[1:]:
        if int(element[1]) < 0:
            print('Incorrect parameters.')
            sys.exit()

def check_input():
    global args
    if not args.type:
        print('Incorrect parameters')
    elif args.type == 'diff' and args.payment:
        print('Incorrect parameters')
    elif not args.interest:
        print('Incorrect parameters')
    argu = sys.argv
    arguments = [element.split('=') for element in argu[1:]]
    for element in arguments[1:]:
        if float(element[1]) < 0:
            print('Incorrect parameters.')
            sys.exit()

parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", type=str, help="The type of loan", choices=['diff', 'annuity'])
parser.add_argument("--interest", type=float, help="the annual interest rate without % sign ")
parser.add_argument("--principal", type=int, help="The borowed ammount")
parser.add_argument("--payment", type=int, help="The monthly payment")
parser.add_argument("--periods", type=int, help="The number of months")
args = parser.parse_args()    

if args:
    check_input()
    if args.type == 'annuity':
    
        if args.payment and args.periods and args.interest:
            prin = principal(args.payment, args.periods, args.interest)
            overpayment(args.periods, args.payment, prin)
        
        elif args.payment and args.principal and args.interest:
            per = periods(args.principal, args.payment, args.interest)
            overpayment(per, args.payment, args.principal)
    
        elif args.principal and args.interest and args.periods:
            pay = payment(args.principal, args.periods, args.interest)
            overpayment(args.periods, pay, args.principal)
        
    elif args.type == 'diff':
        if args.interest and args.principal and args.periods:
            differentiated_payments(args.principal, args.periods, args.interest)
else:
    input_verifier()
    selection = input('''What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal,
    type "d" for differentiated loan:''')
    
    if selection == 'n':
        P = int(input('Enter the loan principal:'))
        a = int(input('Enter the monthly payment:'))
        i = float(input('Enter the loan interest:'))
        result = periods(P, a, i)
        final(result)   
        overpayment(result, a, P)
    
    elif selection == 'a':
        P = int(input('Enter the loan principal:'))
        n = int(input('Enter the number of periods:'))
        i = float(input('Enter the loan interest:'))
        result = math.ceil(payment(P, n, i))
        print('Your monthly payment = {0}!'.format(result))
        overpayment(n, result, P)
    elif selection == 'p':
        a = float(input('Enter the annuity payment:'))
        n = int(input('Enter the number of periods:'))
        i = float(input('Enter the loan interest:'))
        result = math.ceil(principal( a, n, i))
        print('Your monthly payment = {0}!'.format(result))
        overpayment(n, a, result)
    else:
        P = int(input('Enter the loan principal:'))
        n = int(input('Enter the number of periods:'))
        i = float(input('Enter the loan interest:'))
        differentiated_payments(P, n, i)