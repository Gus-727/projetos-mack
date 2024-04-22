def valorPagamento(valor_pres, dias_atraso):
   if dias_atraso == 0:
      valor_pres
   elif dias_atraso >= 1:
      c = 0
      valor_acrescimo = valor_pres * 0.03
      valor_pres = valor_pres + valor_acrescimo
      while c <= dias_atraso:
         valor_juros = valor_pres  * 0.001
         valor_pres = valor_pres + valor_juros
         c+=1
   return valor_pres
         

def main():
   valor_pres = float(input('Digite o valor da prestação: '))
   dias_atraso = int(input('Digite o numero de dias em atraso'))
   valor = valorPagamento(valor_pres, dias_atraso)
   print("%.2f" %valor)
main()