import config
import qiwi



number = '79167778899'

payment_id = qiwi.cell_detect(number)
print payment_id

payment = qiwi.Payment(pid=1, recipient=number, amount=0.01).cell_payment(account=number, comment='test')
print "payment: " + str(payment)
